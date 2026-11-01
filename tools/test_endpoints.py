#!/usr/bin/env python3
"""Ping free OpenAI-compatible LLM endpoints with your own keys.

Set keys as env vars (only providers with a key set are tested):
  GROQ_API_KEY NVIDIA_API_KEY OPENROUTER_API_KEY CEREBRAS_API_KEY MISTRAL_API_KEY
  GEMINI_API_KEY SAMBANOVA_API_KEY LLM7_API_KEY HF_TOKEN
Usage: python3 tools/test_endpoints.py [--list]   (stdlib only)
Model IDs change often; edit PROVIDERS if one returns 404.
"""
import json, os, sys, time, urllib.request, urllib.error

PROVIDERS = {  # name: (base_url, env_key, model)
    "groq":       ("https://api.groq.com/openai/v1", "GROQ_API_KEY", "llama-3.3-70b-versatile"),
    "nvidia":     ("https://integrate.api.nvidia.com/v1", "NVIDIA_API_KEY", "meta/llama-3.3-70b-instruct"),
    "openrouter": ("https://openrouter.ai/api/v1", "OPENROUTER_API_KEY", "openai/gpt-oss-120b:free"),
    "cerebras":   ("https://api.cerebras.ai/v1", "CEREBRAS_API_KEY", "llama3.1-8b"),
    "mistral":    ("https://api.mistral.ai/v1", "MISTRAL_API_KEY", "mistral-small-latest"),
    "gemini":     ("https://generativelanguage.googleapis.com/v1beta/openai", "GEMINI_API_KEY", "gemini-2.0-flash"),
    "sambanova":  ("https://api.sambanova.ai/v1", "SAMBANOVA_API_KEY", "Meta-Llama-3.3-70B-Instruct"),
    "llm7":       ("https://api.llm7.io/v1", "LLM7_API_KEY", "gpt-oss-20b"),
    "huggingface":("https://router.huggingface.co/v1", "HF_TOKEN", "meta-llama/Llama-3.1-8B-Instruct"),
}

def ping(base, key, model):
    body = json.dumps({"model": model, "max_tokens": 8,
                       "messages": [{"role": "user", "content": "Say hi"}]}).encode()
    req = urllib.request.Request(base + "/chat/completions", body, {
        "Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    t = time.time()
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            d = json.load(r)
        return "OK", f"{time.time()-t:.1f}s", d["choices"][0]["message"]["content"].strip()[:30]
    except urllib.error.HTTPError as e:
        return f"HTTP {e.code}", f"{time.time()-t:.1f}s", e.read().decode()[:80].replace("\n", " ")
    except Exception as e:
        return "ERR", "-", str(e)[:80]

if "--list" in sys.argv:
    for n, (b, k, m) in PROVIDERS.items():
        print(f"{n:12} {k:20} {'set' if os.getenv(k) else 'missing'}")
    sys.exit()
tested = 0
for n, (b, k, m) in PROVIDERS.items():
    if os.getenv(k):
        tested += 1
        s, t, note = ping(b, os.environ[k], m)
        print(f"{n:12} {s:9} {t:6} {m}  {note}")
if not tested:
    print("No keys found in environment. Run with --list to see variable names.")
