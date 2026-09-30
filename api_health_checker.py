#!/usr/bin/env python3
"""
api_health_checker.py
=====================================================================
Standalone health-checker for the awesome-free-llm-apis repository.

What it does
------------
1. Parses README.md (English) and extracts, per provider:
     - Provider name
     - Base endpoint  (OpenAI-compatible API base URL)
     - "Get API Key" URL  (provider's key/signup page)
     - Model IDs  (from the "Best Free Models by Provider" table)
     - Provider directory URL (freellm.net link)
2. Probes every endpoint over HTTP (concurrently) and classifies it:
     - ACTIVE    -> server answered (any 2xx/3xx/4xx incl. 401/403/404)
     - DEGRADED  -> 5xx, HTTP 429, or very slow (>5s), or API down but
                    provider key-page still up
     - OFFLINE   -> DNS / connection / timeout failure on BOTH the API
                    and the provider key page
3. Writes a JSON report (active_free_llm_apis_report.json) and prints a
   clean table of verified-active providers.

Design notes
------------
* Standard library only (urllib) so it re-runs anywhere with no pip.
* Re-runnable: `python3 api_health_checker.py` writes report next to it.
* The README sections are delimited by stable HTML comment markers
  (BEGIN_QUICK_REF / END_QUICK_REF, BEGIN_BEST_MODELS / END_BEST_MODELS,
  BEGIN_PERMANENT_FREE / END_PERMANENT_FREE, BEGIN_RENEWABLE / END_RENEWABLE)
  so parsing is robust to row re-ordering.

Usage
-----
    python3 api_health_checker.py            # full run, writes report
    python3 api_health_checker.py --quiet    # no table, just JSON
    python3 api_health_checker.py --timeout 8
"""

import argparse
import concurrent.futures as cf
import json
import os
import re
import socket
import ssl
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

# --------------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------------
HERE = os.path.dirname(os.path.abspath(__file__))
README_PATH = os.path.join(HERE, "README.md")
REPORT_PATH = os.path.join(HERE, "active_free_llm_apis_report.json")

# A response slower than this (seconds) is flagged DEGRADED even if 2xx.
SLOW_THRESHOLD = 5.0
HTTP_TIMEOUT = 20.0
CONCURRENCY = 12
USER_AGENT = "Mozilla/5.0 (compatible; FreeLLMHealthCheck/1.0)"


# --------------------------------------------------------------------------
# README parsing
# --------------------------------------------------------------------------
def _read_section(text: str, begin: str, end: str) -> str:
    """Extract the markdown table that sits between two comment markers."""
    pat = re.compile(r"<!--\s*BEGIN_%s\s*-->(.*?)<!--\s*END_%s\s*-->" % (begin, end),
                     re.DOTALL)
    m = pat.search(text)
    return m.group(1) if m else ""


def _table_rows(section: str):
    """Yield parsed cells for each markdown table row (skips the header)."""
    rows = []
    for line in section.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        if re.match(r"^\|[\s:|-]+\|$", line):  # separator row
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        rows.append(cells)
    return rows


def _first_link(text: str):
    """Return (url, label) of the first markdown/html link in a cell."""
    m = re.search(r'<a\s+href="([^"]+)"[^>]*>(.*?)</a>', text, re.IGNORECASE | re.DOTALL)
    if m:
        return m.group(1).strip(), re.sub(r"<[^>]+>", "", m.group(2)).strip()
    m = re.search(r"\[([^\]]+)\]\(([^)]+)\)", text)
    if m:
        return m.group(2).strip(), m.group(1).strip()
    return None, None


def _backtick(text: str):
    """Pull the first `backtick` content from a cell (base URL / model id)."""
    m = re.search(r"`([^`]+)`", text)
    return m.group(1).strip() if m else ""


def parse_readme(path: str):
    """Return a dict: provider_name -> provider record."""
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()

    providers = {}

    # ---- Quick Reference: Provider | Base URL | Get Key | Credit Card? ----
    qr = _table_rows(_read_section(text, "QUICK_REF", "QUICK_REF"))
    for cells in qr:
        if len(cells) < 4:
            continue
        name = re.sub(r"<[^>]+>", "", cells[0]).strip()
        if not name or name.lower() == "provider":
            continue
        base_url = _backtick(cells[1])
        key_url, _ = _first_link(cells[2])
        cc = re.sub(r"<[^>]+>", "", cells[3]).strip()
        providers.setdefault(name, {
            "provider": name,
            "base_url": base_url,
            "get_key_url": key_url or "",
            "credit_card": cc,
            "model_ids": [],
        })

    # ---- Best Free Models: Provider | Model | Model ID | Context | Rate ----
    bm = _table_rows(_read_section(text, "BEST_MODELS", "BEST_MODELS"))
    current = None
    for cells in bm:
        if len(cells) < 5:
            continue
        pname = re.sub(r"<[^>]+>", "", cells[0]).strip()
        if pname.lower() == "provider":
            continue
        if pname:
            current = pname
        model_id = _backtick(cells[2])
        if current and model_id:
            rec = providers.get(current)
            if rec and model_id not in rec["model_ids"]:
                rec["model_ids"].append(model_id)

    # ---- Provider directory: name | ... | Get Key (for provider URLs) ----
    for marker in ("PERMANENT_FREE", "RENEWABLE"):
        pd = _table_rows(_read_section(text, marker, marker))
        for cells in pd:
            if len(cells) < 6:
                continue
            name = re.sub(r"<[^>]+>", "", cells[0]).strip()
            rec = providers.get(name)
            if not rec:
                continue
            key_url, _ = _first_link(cells[-1])
            if key_url and not rec["get_key_url"]:
                rec["get_key_url"] = key_url
            rec.setdefault("free_models_count",
                           _to_int(re.sub(r"<[^>]+>", "", cells[1])))

    return providers


def _to_int(s: str):
    m = re.search(r"\d+", s)
    return int(m.group(0)) if m else None


# --------------------------------------------------------------------------
# HTTP probing
# --------------------------------------------------------------------------
def _normalize(url: str):
    """Handle placeholder paths like Cloudflare's {account_id}."""
    if not url:
        return None
    if "{" in url:
        url = url.split("{")[0].rstrip("/")
    return url or None


def probe(url: str, timeout: float = HTTP_TIMEOUT):
    """GET a URL (no auth). Returns dict with status/elapsed/error."""
    url = _normalize(url)
    result = {"url": url, "status": None, "elapsed": None,
              "error": None, "ok": False}
    if not url:
        result["error"] = "no-url"
        return result
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, method="GET",
                                 headers={"User-Agent": USER_AGENT,
                                          "Accept": "*/*"})
    t0 = time.time()
    try:
        resp = urllib.request.urlopen(req, timeout=timeout, context=ctx)
        result["status"] = resp.status
        result["ok"] = True
    except urllib.error.HTTPError as e:
        result["status"] = e.code
        result["ok"] = True  # server answered -> reachable
    except (urllib.error.URLError, socket.timeout, ssl.SSLError,
            ConnectionError, TimeoutError) as e:
        result["error"] = _short_err(e)
    finally:
        result["elapsed"] = round(time.time() - t0, 2)
    return result


def _short_err(e):
    msg = str(getattr(e, "reason", e)) or type(e).__name__
    msg = re.sub(r"\[.*?\]", "", msg).strip()
    return msg[:80]


def classify(api_probe, key_probe):
    """Return (status, reason) from the two probes."""
    api_ok = api_probe.get("ok")
    if api_ok:
        code = api_probe.get("status")
        if code and 500 <= code < 600:
            return "Degraded", f"API returned HTTP {code}"
        if code == 429:
            return "Degraded", "API returned HTTP 429 (rate limited)"
        if api_probe.get("elapsed", 0) and api_probe["elapsed"] > SLOW_THRESHOLD:
            return "Degraded", f"slow response ({api_probe['elapsed']}s)"
        return "Active", f"API reachable (HTTP {code})"

    # API unreachable -> check provider key page
    if key_probe.get("ok"):
        return "Degraded", "API unreachable but provider site is up"
    return "Offline", f"API unreachable ({api_probe.get('error')})"


# --------------------------------------------------------------------------
# Orchestration
# --------------------------------------------------------------------------
def run(timeout: float = HTTP_TIMEOUT):
    providers = parse_readme(README_PATH)
    urls = []
    for rec in providers.values():
        api = _normalize(rec.get("base_url"))
        key = _normalize(rec.get("get_key_url"))
        if api:
            urls.append(("api", rec["provider"], api))
        if key and key != api:
            urls.append(("key", rec["provider"], key))

    probes = {}
    with cf.ThreadPoolExecutor(max_workers=CONCURRENCY) as ex:
        futs = {ex.submit(probe, u, timeout): (kind, name, u)
                for kind, name, u in urls}
        for fut in cf.as_completed(futs):
            kind, name, u = futs[fut]
            probes[(kind, name)] = fut.result()

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": "README.md",
        "summary": {},
        "providers": [],
    }
    status_counts = {"Active": 0, "Degraded": 0, "Offline": 0, "Unknown": 0}

    for name, rec in providers.items():
        api_p = probes.get(("api", name), {"url": rec.get("base_url"),
                                           "status": None, "elapsed": None,
                                           "error": "not-probed", "ok": False})
        key_p = probes.get(("key", name), {"url": rec.get("get_key_url"),
                                           "status": None, "elapsed": None,
                                           "error": "n/a", "ok": False})
        if not rec.get("base_url"):
            status, reason = "Unknown", "no base URL in README"
            status_counts["Unknown"] += 1
        else:
            status, reason = classify(api_p, key_p)
            status_counts[status] = status_counts.get(status, 0) + 1

        report["providers"].append({
            "provider": name,
            "status": status,
            "reason": reason,
            "base_url": rec.get("base_url", ""),
            "get_key_url": rec.get("get_key_url", ""),
            "credit_card": rec.get("credit_card", ""),
            "free_models_count": rec.get("free_models_count"),
            "model_ids": rec.get("model_ids", []),
            "api_probe": _trim(api_p),
            "key_probe": _trim(key_p),
        })

    report["summary"] = {
        "total_providers": len(providers),
        "active": status_counts.get("Active", 0),
        "degraded": status_counts.get("Degraded", 0),
        "offline": status_counts.get("Offline", 0),
        "unknown": status_counts.get("Unknown", 0),
        "total_model_ids": sum(len(r["model_ids"]) for r in providers.values()),
    }
    return report


def _trim(p):
    return {"url": p.get("url"), "status": p.get("status"),
            "elapsed": p.get("elapsed"), "error": p.get("error"),
            "ok": p.get("ok")}


def print_table(report):
    provs = report["providers"]
    active = [p for p in provs if p["status"] == "Active"]
    degraded = [p for p in provs if p["status"] == "Degraded"]
    offline = [p for p in provs if p["status"] == "Offline"]
    unknown = [p for p in provs if p["status"] == "Unknown"]

    print("\n" + "=" * 78)
    print("  VERIFIED ACTIVE FREE LLM API PROVIDERS")
    print("=" * 78)
    hdr = f"{'#':>2}  {'Provider':<26} {'Base URL':<48}"
    print(hdr)
    print("-" * 78)
    for i, p in enumerate(active, 1):
        base = (p["base_url"] or "-")[:48]
        print(f"{i:>2}  {p['provider']:<26} {base:<48}")
    print("-" * 78)
    print(f"ACTIVE: {len(active)}   DEGRADED: {len(degraded)}   "
          f"OFFLINE: {len(offline)}   UNKNOWN: {len(unknown)}")
    print(f"Total providers parsed: {report['summary']['total_providers']}   "
          f"Model IDs indexed: {report['summary']['total_model_ids']}")

    if degraded:
        print("\n  DEGRADED (reachable but unhealthy / API down, site up):")
        for p in degraded:
            print(f"    - {p['provider']:<26} {p['reason']}")
    if offline:
        print("\n  OFFLINE (no response from API or site):")
        for p in offline:
            print(f"    - {p['provider']:<26} {p['reason']}")
    if unknown:
        print("\n  UNKNOWN (no base URL to test):")
        for p in unknown:
            print(f"    - {p['provider']:<26} {p['reason']}")
    print("=" * 78 + "\n")


def main():
    global README_PATH, REPORT_PATH
    ap = argparse.ArgumentParser(description="Free LLM API health checker")
    ap.add_argument("--quiet", action="store_true", help="skip table print")
    ap.add_argument("--timeout", type=float, default=HTTP_TIMEOUT)
    ap.add_argument("--readme", default=README_PATH)
    ap.add_argument("--out", default=REPORT_PATH)
    args = ap.parse_args()

    README_PATH = args.readme
    REPORT_PATH = args.out

    if not os.path.exists(README_PATH):
        print(f"ERROR: README not found at {README_PATH}", file=sys.stderr)
        sys.exit(1)

    print(f"[*] Parsing {README_PATH} ...")
    report = run(args.timeout)

    with open(REPORT_PATH, "w", encoding="utf-8") as fh:
        json.dump(report, fh, indent=2, ensure_ascii=False)
    print(f"[*] Wrote report -> {REPORT_PATH}")

    if not args.quiet:
        print_table(report)


if __name__ == "__main__":
    main()
