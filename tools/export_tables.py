#!/usr/bin/env python3
"""Export README provider tables to CSV files and one XLSX workbook.

Usage: python3 tools/export_tables.py [README.md] [out_dir]
"""
import csv, re, sys
from pathlib import Path

readme = Path(sys.argv[1] if len(sys.argv) > 1 else "README.md")
out = Path(sys.argv[2] if len(sys.argv) > 2 else "export")
out.mkdir(parents=True, exist_ok=True)
text = readme.read_text(encoding="utf-8")

SECTIONS = {
    "permanent_free": "PERMANENT_FREE",
    "renewable_credits": "RENEWABLE",
    "quick_reference": "QUICK_REF",
    "best_models": "BEST_MODELS",
}

def clean(cell):
    m = re.search(r'href="([^"]+)"', cell)
    if m and "<a" in cell:
        label = re.sub(r"<[^>]+>", "", cell).strip()
        # keep the URL for "Get key" arrows, the label for model names
        return m.group(1) if label in ("→", "Get Key →") else label
    return re.sub(r"<[^>]+>", "", cell).strip().strip("`")

def parse(block):
    rows = [l for l in block.splitlines() if l.startswith("|")]
    rows = [[clean(c) for c in l.strip().strip("|").split("|")] for l in rows]
    return [r for r in rows if not all(set(c) <= set("-: ") for c in r)]

tables = {}
for name, marker in SECTIONS.items():
    m = re.search(rf"<!-- BEGIN_{marker} -->(.*?)<!-- END_{marker} -->", text, re.S)
    if m:
        tables[name] = parse(m.group(1))
# fill blank provider cells in best_models (grouped rows)
bm = tables.get("best_models")
if bm:
    last = ""
    for r in bm[1:]:
        last = r[0] or last
        r[0] = last

for name, rows in tables.items():
    with open(out / f"{name}.csv", "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(rows)

try:
    from openpyxl import Workbook
    from openpyxl.styles import Font
    wb = Workbook(); wb.remove(wb.active)
    for name, rows in tables.items():
        ws = wb.create_sheet(name[:31])
        for r in rows:
            ws.append(r)
        for c in ws[1]:
            c.font = Font(bold=True)
        ws.freeze_panes = "A2"; ws.auto_filter.ref = ws.dimensions
        for col in ws.columns:
            ws.column_dimensions[col[0].column_letter].width = min(60, max(len(str(c.value or "")) for c in col) + 2)
    wb.save(out / "free_llm_apis.xlsx")
except ImportError:
    print("openpyxl missing; CSV only")
print({k: len(v) - 1 for k, v in tables.items()}, "->", out)
