<p align="center">
  <h1 align="center">awesome-free-llm-apis</h1>
  <!-- AUTO_STATS -->
  <p align="center"><strong>146+ free LLM APIs from 24 providers</strong> — find, compare & configure free models in seconds.</p>
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
  <p align="center"><strong>🔄 Data refreshed daily from <a href="https://freellm.net">freellm.net</a></strong> — Last updated: 2026-05-23</p>
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

## How to Use — 3 Steps

1. **Pick a provider** — see [Provider Directory](#provider-directory) below. Start with **Groq** (no credit card, 30 RPM free).
2. **Get your API key** — click any [Get Key →](#quick-reference--base-urls--api-keys) link below, sign up (most need just an email), and copy your key. Takes < 1 minute.
3. **Plug it in** — copy the base URL + model ID, paste into the [Quick Start](#quick-start--use-any-free-api-in-30-seconds) examples below.

Configuring a specific tool? [Claude Code](https://freellm.net/config/#claude-code) · [Cursor](https://freellm.net/config/#cursor) · [Codex](https://freellm.net/config/#codex) · [OpenHuman](https://freellm.net/config/#openhuman) · [OpenCode](https://freellm.net/config/#opencode) · [OpenClaw](https://freellm.net/config/#openclaw) — one-click configs at [freellm.net/config/](https://freellm.net/config/).



## Quick Start — Use Any Free API in 30 Seconds

**Never used an API before?** Here's the simplest path: go to [console.groq.com/keys](https://console.groq.com/keys), sign up with just an email (no credit card), copy your free key, and paste it into any example below. You'll be running in under a minute.

All providers below expose an **OpenAI-compatible endpoint**. Any tool that accepts `baseURL` + `apiKey` works — just swap the base URL and key.

### Python (OpenAI SDK)

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",  # free, no credit card
    api_key="GROQ_API_KEY",                     # get at console.groq.com/keys
)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",            # see Best Models table below
    messages=[{"role": "user", "content": "Hello!"}],
)
print(response.choices[0].message.content)
# Groq free tier: 30 RPM, 14,400 RPD — generous for personal use
```

### Codex CLI

```bash
export OPENAI_BASE_URL="https://api.groq.com/openai/v1"
export OPENAI_API_KEY="your-groq-key"          # get at console.groq.com/keys
codex --model "llama-3.3-70b-versatile"
```

### Cursor

```
Settings → Models → Add Model
  Model name: llama-3.3-70b-versatile
  Base URL: https://api.groq.com/openai/v1
  API key: your-groq-key                       # get at console.groq.com/keys
```

### Claude Code

```bash
# Claude Code needs an Anthropic-compatible API — use OpenRouter
export ANTHROPIC_BASE_URL="https://openrouter.ai/api"
export ANTHROPIC_AUTH_TOKEN="sk-or-v1-your-key"  # openrouter.ai/keys
export ANTHROPIC_API_KEY=""                       # must be empty
# Note: OpenRouter Anthropic models need $10 top-up (one-time)
```

### Using Other Tools?

Most AI dev tools accept custom API endpoints — just point them at any provider above. Grab your free key, then:

- **Claude Code** — set `ANTHROPIC_BASE_URL` + `ANTHROPIC_AUTH_TOKEN`. [Step-by-step →](https://freellm.net/config/#claude-code)
- **Cursor** — Settings → Models → Add Model. [Step-by-step →](https://freellm.net/config/#cursor)
- **Codex CLI** — set `OPENAI_BASE_URL` + `OPENAI_API_KEY`. [Step-by-step →](https://freellm.net/config/#codex)
- **OpenHuman** — edit `config.toml`. [Step-by-step →](https://freellm.net/config/#openhuman)
- **Aider** — edit `.aider.conf.yml`. [Step-by-step →](https://freellm.net/config/#aider)
- **Cline** (VS Code) — API provider settings. [Step-by-step →](https://freellm.net/config/#cline)
- **Open WebUI** — Settings → Connections. [Step-by-step →](https://freellm.net/config/#open-webui)

More ready-to-copy configs at **[freellm.net/config/](https://freellm.net/config/)**.

> **All providers, base URLs, and API key links** are in the [Quick Reference](#quick-reference--base-urls--api-keys) below.


---

## Provider Directory

### ⚡ Permanent Free Tiers

These providers offer a **permanently free tier** — no credit card required for most.

<!-- BEGIN_PERMANENT_FREE -->
| Provider | Free Models | Credit Card? | Max Context | Modalities | Get API Key |
|---|---|---|---|---|---|
| NVIDIA NIM | 16 | Phone verification | 1M | image, text | [→](https://build.nvidia.com/settings/api-keys) |
| GitHub Models | 10 | No | 1M | text | [→](https://github.com/marketplace/models) |
| Cloudflare Workers AI | 8 | No | 10M | image, text | [→](https://dash.cloudflare.com/profile/api-tokens) |
| Groq | 8 | No | 262K | text | [→](https://console.groq.com/keys) |
| Mistral AI | 6 | No | 256K | code, image, text | [→](https://console.mistral.ai/api-keys) |
| Cerebras | 6 | No | 131K | text | [→](https://cloud.cerebras.ai/) |
| Ollama Cloud | 6 | Registration | 262K | code, text | [→](https://ollama.com/settings/keys) |
| Alibaba Cloud Model Studio | 5 | Registration | 1M | code, image, text | [→](https://bailian.console.alibabacloud.com/?apiKey=1) |
| Cohere | 5 | No | 256K | text | [→](https://dashboard.cohere.com/api-keys) |
| Hugging Face | 5 | No | 131K | text | [→](https://huggingface.co/settings/tokens) |
| Kilo Code | 5 | No | 262K | code, text | [→](https://kilo.ai) |
| LLM7.io | 5 | No | 131K | code, text | [→](https://token.llm7.io) |
| Google Gemini | 4 | No | 2M | text | [→](https://aistudio.google.com/app/apikey) |
| OVHcloud AI Endpoints | 4 | Registration | 128K | image, text | [→](https://endpoints.ai.cloud.ovh.net/) |
| Aion Labs | 3 | Registration | 131K | text | [→](https://www.aionlabs.ai) |
| xAI | 3 | Registration | 2M | text | [→](https://console.x.ai) |
| Z AI (Zhipu AI) | 3 | No | 200K | text | [→](https://open.bigmodel.cn/usercenter/apikeys) |
| ModelScope | 3 | Registration | 131K | text | [→](https://modelscope.cn/my/myaccesstoken) |
| Nscale | 3 | Registration | 256K | code, text | [→](https://console.nscale.com/) |
| SiliconFlow | 3 | Registration | 131K | text | [→](https://cloud.siliconflow.cn/account/ak) |
| AI21 Labs | 2 | Registration | 256K | text | [→](https://studio.ai21.com/account/api-key) |
| DeepSeek | 2 | Registration | 128K | text | [→](https://platform.deepseek.com/api_keys) |
| Nebius | 2 | Registration | 128K | text | [→](https://studio.nebius.com/settings/api-keys) |
<!-- END_PERMANENT_FREE -->

### 💰 Renewable Credits

Providers that periodically renew free credits.

<!-- BEGIN_RENEWABLE -->
| Provider | Free Models | Credit Model | Max Context | Modalities | Get API Key |
|---|---|---|---|---|---|
| OpenRouter | 29 | Free tier + $10 topup → 1K RPD | 1M | audio, code, embeddings, image, reasoning, text | [→](https://openrouter.ai/workspaces/default/keys) |
<!-- END_RENEWABLE -->

## Quick Reference — Base URLs & API Keys

<!-- BEGIN_QUICK_REF -->
| Provider | Base URL | Get API Key | Credit Card? |
|---|---|---|---|
| OpenRouter | `https://openrouter.ai/api/v1` | [Get Key →](https://openrouter.ai/workspaces/default/keys) | Registration |
| NVIDIA NIM | `https://integrate.api.nvidia.com/v1` | [Get Key →](https://build.nvidia.com/settings/api-keys) | Phone verification |
| GitHub Models | `https://models.github.ai/inference` | [Get Key →](https://github.com/marketplace/models) | No |
| Cloudflare Workers AI | `https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run` | [Get Key →](https://dash.cloudflare.com/profile/api-tokens) | No |
| Groq | `https://api.groq.com/openai/v1` | [Get Key →](https://console.groq.com/keys) | No |
| Mistral AI | `https://api.mistral.ai/v1` | [Get Key →](https://console.mistral.ai/api-keys) | No |
| Cerebras | `https://api.cerebras.ai/v1` | [Get Key →](https://cloud.cerebras.ai/) | No |
| Ollama Cloud | `https://api.ollama.com` | [Get Key →](https://ollama.com/settings/keys) | Registration |
| Alibaba Cloud Model Studio | `https://dashscope-intl.aliyuncs.com/compatible-mode/v1` | [Get Key →](https://bailian.console.alibabacloud.com/?apiKey=1) | Registration |
| Cohere | `https://api.cohere.com/v2` | [Get Key →](https://dashboard.cohere.com/api-keys) | No |
| Hugging Face | `https://router.huggingface.co/v1` | [Get Key →](https://huggingface.co/settings/tokens) | No |
| Kilo Code | `https://api.kilo.ai/api/gateway` | [Get Key →](https://kilo.ai) | No |
| LLM7.io | `https://api.llm7.io/v1` | [Get Key →](https://token.llm7.io) | No |
| Google Gemini | `https://generativelanguage.googleapis.com/v1beta` | [Get Key →](https://aistudio.google.com/app/apikey) | No |
| OVHcloud AI Endpoints | `https://oai.endpoints.kepler.ai.cloud.ovh.net/v1` | [Get Key →](https://endpoints.ai.cloud.ovh.net/) | Registration |
| Aion Labs | `https://api.aionlabs.ai/v1` | [Get Key →](https://www.aionlabs.ai) | Registration |
| xAI | `https://api.x.ai/v1` | [Get Key →](https://console.x.ai) | Registration |
| Z AI (Zhipu AI) | `https://open.bigmodel.cn/api/paas/v4` | [Get Key →](https://open.bigmodel.cn/usercenter/apikeys) | No |
| ModelScope | `https://api-inference.modelscope.cn/v1` | [Get Key →](https://modelscope.cn/my/myaccesstoken) | Registration |
| Nscale | `https://inference.api.nscale.com/v1` | [Get Key →](https://console.nscale.com/) | Registration |
| SiliconFlow | `https://api.siliconflow.cn/v1` | [Get Key →](https://cloud.siliconflow.cn/account/ak) | Registration |
| AI21 Labs | `https://api.ai21.com/studio/v1` | [Get Key →](https://studio.ai21.com/account/api-key) | Registration |
| DeepSeek | `https://api.deepseek.com/v1` | [Get Key →](https://platform.deepseek.com/api_keys) | Registration |
| Nebius | `https://api.studio.nebius.com/v1` | [Get Key →](https://studio.nebius.com/settings/api-keys) | Registration |
<!-- END_QUICK_REF -->

## Best Free Models by Provider

<!-- BEGIN_BEST_MODELS -->
| Provider | Best Free Model | Model ID | Max Context | Rate Limit |
|---|---|---|---|---|
| OpenRouter | Owl Alpha | `openrouter/owl-alpha` | 1M | See provider |
|  | NVIDIA: Nemotron 3 Super (free) | `nvidia/nemotron-3-super-120b-a12b:free` | 1M | See provider |
|  | Poolside: Laguna M.1 (free) | `poolside/laguna-m.1:free` | 131K | See provider |
| NVIDIA NIM | moonshotai/kimi-k2.6 | `moonshotai/kimi-k2.6` | 262K | Up to 40 RPM |
|  | z-ai/glm-5.1 | `z-ai/glm-5.1` | 202K | Up to 40 RPM |
|  | qwen/qwen3.5-397b-a17b | `qwen/qwen3.5-397b-a17b` | 262K | Up to 40 RPM |
| GitHub Models | gpt-5 | `gpt-5` | 200K | 10 RPM, 50 RPD |
|  | gpt-4.1 | `gpt-4-1` | 1M | 10 RPM, 50 RPD |
|  | gpt-4.1-mini | `gpt-4-1-mini` | 1M | 15 RPM, 150 RPD |
| Cloudflare Workers AI | @cf/meta/llama-3.3-70b-instruct-fp8-fast | `cf-meta-llama-3-3-70b-instruct-fp8-fast` | 131K | 10K neurons/day (shared) |
|  | @cf/meta/llama-3.1-8b-instruct-fp8-fast | `cf-meta-llama-3-1-8b-instruct-fp8-fast` | 131K | 10K neurons/day (shared) |
|  | @cf/meta/llama-3.2-11b-vision-instruct | `cf-meta-llama-3-2-11b-vision-instruct` | 131K | 10K neurons/day (shared) |
| Groq | llama-3.3-70b-versatile | `llama-3-3-70b-versatile` | 131K | 30 RPM, 14,400 RPD |
|  | llama-3.1-8b-instant | `llama-3-1-8b-instant` | 131K | 30 RPM, 14,400 RPD |
|  | llama-4-maverick-17b-128e-instruct | `llama-4-maverick-17b-128e-instruct` | 131K | 15 RPM, 500 RPD |
| Mistral AI | Mistral Small 4 | `mistral-small-4` | 256K | ~1 RPS, 500K TPM |
|  | Mistral Medium 3 | `mistral-medium-3` | 128K | ~1 RPS, 500K TPM |
|  | Mistral Large 3 | `mistral-large-3` | 256K | ~1 RPS, 500K TPM |
| Cerebras | llama-3.3-70b | `llama-3-3-70b` | 128K | 30 RPM, 14,400 RPD, 1M .. |
|  | gpt-oss-120b | `gpt-oss-120b` | 128K | 30 RPM, 14,400 RPD, 1M .. |
|  | qwen-3-235b-a22b-instruct-2507 | `qwen-3-235b-a22b-instruct-2507` | 131K | 30 RPM, 14,400 RPD, 1M .. |
| Ollama Cloud | gpt-oss:120b-cloud | `gpt-oss-120b-cloud` | 128K | Session/weekly limits (.. |
|  | deepseek-v3.1:671b-cloud | `deepseek-v3-1-671b-cloud` | 128K | Session/weekly limits (.. |
|  | qwen3-coder:480b-cloud | `qwen3-coder-480b-cloud` | 128K | Session/weekly limits (.. |
| Alibaba Cloud Model Studio | Qwen3-Max | `qwen3-max` | 128K | Tiered by region |
|  | Qwen3-Plus | `qwen3-plus` | 1M | Tiered by region |
|  | Qwen3-VL-Plus | `qwen3-vl-plus` | 128K | Tiered by region |
| Cohere | Command A (111B) | `command-a-111b` | 256K | 20 RPM |
|  | Command R+ | `command-r` | 128K | 20 RPM |
|  | Command R7B | `command-r7b` | 128K | 20 RPM |
| Hugging Face | Meta-Llama-3.1-8B-Instruct | `meta-llama-3-1-8b-instruct` | 128K | Credit-metered |
|  | Mistral-7B-Instruct-v0.3 | `mistral-7b-instruct-v0-3` | 32K | Credit-metered |
|  | Mixtral-8x7B-Instruct-v0.1 | `mixtral-8x7b-instruct-v0-1` | 32K | Credit-metered |
| Kilo Code | x-ai/grok-code-fast-1:free | `x-ai-grok-code-fast-1-free` | 256K | ~200 req/hr |
|  | minimax/minimax-m2.5:free | `minimax-minimax-m2-5-free` | 196K | ~200 req/hr |
|  | bytedance-seed/dola-seed-2.0-pro:free | `bytedance-seed-dola-seed-2-0-pro-free` | 131K | ~200 req/hr |
| LLM7.io | deepseek-r1-0528 | `deepseek-r1-0528` | 131K | 30 RPM (120 with token) |
|  | deepseek-v3-0324 | `deepseek-v3-0324` | 131K | 30 RPM (120 with token) |
|  | gpt-4o-mini | `gpt-4o-mini` | 131K | 30 RPM (120 with token) |
| Google Gemini | Gemini 2.5 Pro | `gemini-2-5-pro` | 2M | 5 RPM, 100 RPD |
|  | Gemini 2.5 Flash | `gemini-2-5-flash` | 1M | 10 RPM, 250 RPD |
|  | Gemini 2.5 Flash-Lite | `gemini-2-5-flash-lite` | 1M | 15 RPM, 1,000 RPD |
| OVHcloud AI Endpoints | Qwen2.5-VL-72B-Instruct | `qwen2-5-vl-72b-instruct` | 128K | 2 RPM (anonymous) |
|  | Mistral-Nemo-Instruct-2407 | `mistral-nemo-instruct-2407` | 128K | 2 RPM (anonymous) |
|  | Qwen3Guard-Gen-8B | `qwen3guard-gen-8b` | 32K | 2 RPM (anonymous) |
| Aion Labs | aion-2.0 | `aion-2-0` | 131K | Daily token allowance |
|  | aion-1.0 | `aion-1-0` | 131K | Daily token allowance |
|  | aion-1.0-mini | `aion-1-0-mini` | 131K | Daily token allowance |
| xAI | grok-4.3 | `grok-4-3` | 1M | Credit-based |
|  | grok-4.1-fast | `grok-4-1-fast` | 2M | Credit-based |
|  | grok-3-mini | `grok-3-mini` | 131K | Credit-based |
| Z AI (Zhipu AI) | GLM-4.7-Flash | `glm-4-7-flash` | 200K | 1 concurrent request |
|  | GLM-4.5-Flash | `glm-4-5-flash` | 128K | 1 concurrent request |
|  | GLM-4.6V-Flash | `glm-4-6v-flash` | 128K | 1 concurrent request |
| ModelScope | Qwen/Qwen3.5-35B-A3B | `qwen-qwen3-5-35b-a3b` | 131K | 2,000 RPD total; <=500 .. |
|  | Qwen/Qwen3.5-27B | `qwen-qwen3-5-27b` | 131K | 2,000 RPD total; <=500 .. |
|  | Qwen/Qwen-Image | `qwen-qwen-image` | 131K | 2,000 RPD total; model/.. |
| Nscale | Llama-3.3-70B-Instruct | `llama-3-3-70b-instruct` | 128K | Fair-use |
|  | Qwen3-Coder-30B-A3B-Instruct | `qwen3-coder-30b-a3b-instruct` | 256K | Fair-use |
|  | DeepSeek-R1-Distill-Llama-70B | `deepseek-r1-distill-llama-70b` | 128K | Fair-use |
| SiliconFlow | deepseek-ai/DeepSeek-R1-Distill-Qwen-7B | `deepseek-ai-deepseek-r1-distill-qwen-7b` | 131K | 30 RPM, 60K TPM |
|  | deepseek-ai/DeepSeek-OCR | `deepseek-ai-deepseek-ocr` | 131K | 30 RPM, 60K TPM |
|  | Abbreviation | `abbreviation` | 131K | See provider |
| AI21 Labs | Jamba Large 1.7 | `jamba-large-1-7` | 256K | 200 RPM, 10 RPS |
|  | Jamba Mini 2 | `jamba-mini-2` | 256K | 200 RPM, 10 RPS |
| DeepSeek | deepseek-chat (V3.2) | `deepseek-chat-v3-2` | 128K | Dynamic |
|  | deepseek-reasoner (R1) | `deepseek-reasoner-r1` | 128K | Dynamic |
| Nebius | Meta-Llama-3.3-70B-Instruct | `meta-llama-3-3-70b-instruct` | 128K | Tier-based |
|  | Qwen3-235B-A22B | `qwen3-235b-a22b` | 128K | Tier-based |
<!-- END_BEST_MODELS -->



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
| Owl Alpha | OpenRouter | 1M | 1137B tokens |
| moonshotai/kimi-k2.6 | NVIDIA NIM | 262K | 718B tokens |
| NVIDIA: Nemotron 3 Super (free) | OpenRouter | 1M | 612B tokens |
| Poolside: Laguna M.1 (free) | OpenRouter | 131K | 262B tokens |
| OpenAI: gpt-oss-120b (free) | OpenRouter | 131K | 154B tokens |
| z-ai/glm-5.1 | NVIDIA NIM | 202K | 120B tokens |
| qwen/qwen3.5-397b-a17b | NVIDIA NIM | 262K | 98B tokens |
| Z.ai: GLM 4.5 Air (free) | OpenRouter | 131K | 89B tokens |
| DeepSeek: DeepSeek V4 Flash (free) | OpenRouter | 1M | 72B tokens |
| Arcee AI: Trinity Large Thinking (free) | OpenRouter | 262K | 57B tokens |
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
2026-05-23
<!-- END_AUTO_LAST_UPDATED --></sub>
</p>
