<p align="center">
  <h1 align="center">awesome-free-llm-apis</h1>
  <!-- AUTO_STATS -->
  <p align="center"><strong>127+ free LLM APIs from 17 providers</strong> — find, compare & configure free models in seconds.</p>
<!-- END_AUTO_STATS -->
</p>

<p align="center">
  <a href="https://freellm.net"><strong>🌐 Live at freellm.net</strong></a> —
  <a href="https://freellm.net/models/">Browse models</a> ·
  <a href="https://freellm.net/playground/">Playground</a> ·
  <a href="https://freellm.net/config/">Config generator</a> ·
  <a href="https://freellm.net/free-llm-api-keys/">API keys</a>
</p>

<!-- AUTO_UPDATE_BADGE -->
<p align="center"><strong>🔄 Data refreshed daily from <a href="https://freellm.net">freellm.net</a></strong> — Last updated: 2026-05-22</p>
<!-- END_AUTO_UPDATE_BADGE -->

<p align="center">
  🌐 <a href="README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a>
</p>

---

## Why This Exists

Finding a free LLM API shouldn't mean hunting through a dozen GitHub READMEs, signing up for five different platforms, or guessing which models still have a free tier.

This repo is a **structured, machine-readable directory** of every free LLM API — rate limits, context windows, one-click config snippets, and direct API key links. Updated daily.

**Why this repo + [freellm.net](https://freellm.net):**

- ✅ **Always up-to-date** — data refreshed daily via automated monitoring, not a 2-year-old static list
- ✅ **Credit card transparency** — clearly shows which providers require a card, phone verification, or nothing at all
- ✅ **One-click configs** — ready-to-copy snippets for Claude Code, Cursor, Codex, Aider, and 10+ more tools
- ✅ **Side-by-side comparison** — compare context windows, rate limits, and modalities across providers instantly

---

## Quick Start — Use Any Free API in 30 Seconds

All providers below expose an **OpenAI-compatible endpoint** (or, for Gemini, a trivial wrapper). That means any tool that accepts `baseURL` + `apiKey` works.

### Claude Code (cc)

```bash
export ANTHROPIC_BASE_URL="https://api.openai.com/v1"  # or Groq, OpenRouter, NVIDIA NIM
export ANTHROPIC_AUTH_TOKEN="your-api-key-here"
# Claude Code now routes through the free backend
```

### Cursor

```
Settings → Models → Add Model
  Model name: gpt-oss-120b
  Base URL: https://api.openai.com/v1
  API key: your-free-api-key
```

### Codex CLI

```bash
export OPENAI_BASE_URL="https://api.openai.com/v1"
export OPENAI_API_KEY="your-api-key-here"
```

### OpenAI SDK (Python)

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.openai.com/v1",  # swap to any provider below
    api_key="YOUR_FREE_API_KEY",
)

response = client.chat.completions.create(
    model="gpt-oss-120b",
    messages=[{"role": "user", "content": "Hello!"}],
)
print(response.choices[0].message.content)
```

> See [freellm.net/config/](https://freellm.net/config/) for ready-to-copy configs for Aider, Cline, OpenCode, Continue, Open WebUI, and Gemini CLI.

---

## Provider Directory

### ⚡ Permanent Free Tiers

These providers offer a **permanently free tier** — no credit card required for most.

<!-- BEGIN_PERMANENT_FREE -->
| Provider | Free Models | Credit Card? | Max Context | Modalities | Get API Key |
|---|---|---|---|---|---|
| NVIDIA NIM | 16 | Phone verification | 1M | image, text | [→](https://build.nvidia.com/settings/api-keys) |
| GitHub Models | 10 | No | 1M | text | [→](https://github.com/marketplace/models) |
| Groq | 9 | No | 262K | text | [→](https://console.groq.com/keys) |
| Cloudflare Workers AI | 8 | No | 10M | image, text | [→](https://dash.cloudflare.com/profile/api-tokens) |
| OVHcloud AI Endpoints | 7 | Registration | 262K | code, image, text | [→](https://endpoints.ai.cloud.ovh.net/) |
| Mistral AI | 6 | No | 256K | code, image, text | [→](https://console.mistral.ai/api-keys) |
| SiliconFlow | 6 | Registration | 131K | text | [→](https://cloud.siliconflow.cn/account/ak) |
| Cohere | 5 | No | 256K | text | [→](https://dashboard.cohere.com/api-keys) |
| Hugging Face | 5 | No | 131K | text | [→](https://huggingface.co/settings/tokens) |
| LLM7.io | 5 | No | 131K | code, text | [→](https://token.llm7.io) |
| Ollama Cloud | 5 | Registration | 128K | text | [→](https://ollama.com/settings/keys) |
| Cerebras | 4 | No | 131K | text | [→](https://cloud.cerebras.ai/) |
| Kilo Code | 4 | No | 262K | code, text | [→](https://kilo.ai) |
| Z AI (Zhipu AI) | 3 | No | 200K | text | [→](https://open.bigmodel.cn/usercenter/apikeys) |
| ModelScope | 3 | Registration | 131K | text | [→](https://modelscope.cn/my/myaccesstoken) |
| Google Gemini | 2 | No | 1M | text | [→](https://aistudio.google.com/app/apikey) |
<!-- END_PERMANENT_FREE -->

### 💰 Renewable Credits

Providers that periodically renew free credits.

<!-- BEGIN_RENEWABLE -->
| Provider | Free Models | Credit Model | Max Context | Modalities | Get API Key |
|---|---|---|---|---|---|
| OpenRouter | 29 | Free tier + $10 topup → 1K RPD | 1M | audio, code, embeddings, image, reasoning, text | [→](https://openrouter.ai/workspaces/default/keys) |
<!-- END_RENEWABLE -->

### 🖥️ Local / Self-Hosted (Unlimited, Private, Free Forever)

| Tool | Type | Highlights |
|---|---|---|
| [Ollama](https://ollama.com) | CLI + API | 100+ models, GPU acceleration, OpenAI-compatible endpoint |
| [LM Studio](https://lmstudio.ai) | Desktop GUI | Any GGUF model, built-in model browser, offline |
| [llama.cpp](https://github.com/ggerganov/llama.cpp) | C/C++ engine | Runs any GGUF, minimal dependencies |
| [GPT4All](https://gpt4all.io) | Desktop app | CPU-only, no GPU required, open source |
| [Jan.ai](https://jan.ai) | Desktop app | Privacy-focused, 100% offline ChatGPT alternative |
| [KoboldCpp](https://github.com/LostRuins/koboldcpp) | Single executable | Optimized for creative writing, GGUF |

---

## Top Free Models (by Weekly Usage)

Data from freellm.net, updated daily via API monitoring.

<!-- BEGIN_TOP_MODELS -->
| Model | Provider | Context | Weekly Usage |
|---|---|---|---|
| Owl Alpha | OpenRouter | 1M | 1196B tokens |
| moonshotai/kimi-k2.6 | NVIDIA NIM | 262K | 758B tokens |
| NVIDIA: Nemotron 3 Super (free) | OpenRouter | 1M | 617B tokens |
| z-ai/glm-5.1 | NVIDIA NIM | 202K | 403B tokens |
| Poolside: Laguna M.1 (free) | OpenRouter | 131K | 259B tokens |
| OpenAI: gpt-oss-120b (free) | OpenRouter | 131K | 153B tokens |
| qwen/qwen3.5-397b-a17b | NVIDIA NIM | 262K | 110B tokens |
| Z.ai: GLM 4.5 Air (free) | OpenRouter | 131K | 88B tokens |
| DeepSeek: DeepSeek V4 Flash (free) | OpenRouter | 1M | 80B tokens |
| Arcee AI: Trinity Large Thinking (free) | OpenRouter | 262K | 54B tokens |
<!-- END_TOP_MODELS -->

---

## Repository Structure

```
awesome-free-llm-apis/
├── README.md              ← Complete provider directory & code examples
├── code-examples/          ← Ready-to-use config snippets
│   ├── claude-code.md
│   ├── cursor.md
│   └── codex.md
└── LICENSE                 ← MIT
```

> For the full structured dataset with 453 models and daily updates, visit **[freellm.net](https://freellm.net)**.

---

## Contributing

We welcome contributions!

- **Add a missing free model** — Open an [issue](https://github.com/open-free-llm-api/awesome-free-llm-apis/issues) or submit a PR
- **Fix inaccurate data** — Rate limits change, providers graduate. PRs welcome
- **Add a config snippet** — Have a working config for a tool we don't cover? Add it to `code-examples/`

### Criteria for inclusion

A model belongs in this list if:
1. The provider explicitly offers a **free tier** (not just a trial credit)
2. The API is **publicly accessible** (no waitlist, closed beta, or reverse-engineering)
3. For trial credits: clearly labeled and minimum $1 credit value

---

## Links

- 🌐 **Live site**: [freellm.net](https://freellm.net) — search, compare, playground, config generator
- 🔑 **API key directory**: [freellm.net/free-llm-api-keys/](https://freellm.net/free-llm-api-keys/)
- ⚙️ **Config generator**: [freellm.net/config/](https://freellm.net/config/)
- 🎮 **Playground**: [freellm.net/playground/](https://freellm.net/playground/)
- 📊 **Compare models**: [freellm.net/compare/](https://freellm.net/compare/)

## License

MIT © [open-free-llm-api](https://github.com/open-free-llm-api)

---

<p align="center">
  <sub>Last updated: <!-- AUTO_LAST_UPDATED -->
2026-05-22
<!-- END_AUTO_LAST_UPDATED --></sub>
</p>
