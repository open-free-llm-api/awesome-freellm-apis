# Claude Code (cc) — Free LLM API Config

Point Claude Code at any free OpenAI-compatible backend in 30 seconds.

## How It Works

Claude Code reads `ANTHROPIC_BASE_URL` and `ANTHROPIC_AUTH_TOKEN` from the environment. When you set them to a free provider, cc routes API calls through that backend instead of Anthropic's paid API.

## Quick Config

### Groq (fastest inference, no credit card)

```bash
export ANTHROPIC_BASE_URL="https://api.groq.com/openai/v1"
export ANTHROPIC_AUTH_TOKEN="gsk_your_groq_api_key"
```

Get your key at [console.groq.com/keys](https://console.groq.com/keys). Recommended model: `llama-3.3-70b-versatile`, `qwen-3-32b`.

### NVIDIA NIM (no daily token cap)

```bash
export ANTHROPIC_BASE_URL="https://integrate.api.nvidia.com/v1"
export ANTHROPIC_AUTH_TOKEN="nvapi-your_nvidia_key"
```

Get your key at [build.nvidia.com](https://build.nvidia.com/settings/api-keys). Recommended model: `meta/llama-3.3-70b-instruct`, `deepseek-ai/deepseek-r1`.

### OpenRouter (35+ free models, single key)

```bash
export ANTHROPIC_BASE_URL="https://openrouter.ai/api/v1"
export ANTHROPIC_AUTH_TOKEN="sk-or-v1-your_openrouter_key"
```

Get your key at [openrouter.ai/keys](https://openrouter.ai/workspaces/default/keys). Recommended model: `openai/gpt-oss-120b:free`, `google/gemini-2.5-flash:free`.

### Cloudflare Workers AI (10K requests/day free)

```bash
export ANTHROPIC_BASE_URL="https://api.cloudflare.com/client/v4/accounts/YOUR_ACCOUNT_ID/ai/v1"
export ANTHROPIC_AUTH_TOKEN="your_cloudflare_api_token"
```

### SiliconFlow (best latency for China-based users)

```bash
export ANTHROPIC_BASE_URL="https://api.siliconflow.cn/v1"
export ANTHROPIC_AUTH_TOKEN="sk-your_siliconflow_key"
```

Get your key at [cloud.siliconflow.cn](https://cloud.siliconflow.cn/account/ak). Recommended model: `Qwen/Qwen3-Coder-480B-A35B-Instruct`.

### onomeo (native Anthropic format, one key for 23 providers)

onomeo answers on `/v1/messages` in the Anthropic wire format — streaming events and `count_tokens` included — so Claude Code talks to it without a shim.

```bash
export ANTHROPIC_BASE_URL="https://onomeo.com"
export ANTHROPIC_AUTH_TOKEN="sk-onomeo-your_key"
export ANTHROPIC_MODEL="my/gemini/gemini-3-flash-preview"
```

Get your key at [onomeo.com/dashboard](https://onomeo.com/dashboard). The Anthropic endpoint serves models from a provider you connect with your own key — 23 are supported (OpenRouter, Gemini, Groq, Mistral, NVIDIA, Cloudflare, DeepSeek, Qwen and more) — addressed as `my/<provider>/<model>`. A free key you already hold becomes usable inside Claude Code. onomeo's own 36 free models (daily check-in credits, no card, no phone) are on the OpenAI-compatible endpoint at `https://onomeo.com/v1`.

Verified 2026-09-19 with the Claude Code CLI against a connected Gemini key.

## Persistent Config

Add to your shell profile (`~/.zshrc` or `~/.bashrc`):

```bash
# Free LLM API backend for Claude Code
export ANTHROPIC_BASE_URL="https://api.groq.com/openai/v1"
export ANTHROPIC_AUTH_TOKEN="gsk_your_key_here"
```

## Caveats

- Claude Code expects tools/capabilities that not all free backends support. If you hit errors, try a more capable model (Llama 3.3 70B+ or DeepSeek R1).
- The "Claude" model name shown in cc is cosmetic — you're actually using whichever model you configure.
- Free tiers have rate limits. Groq: 14,400 RPD. NVIDIA NIM: 40 RPM. OpenRouter: 50 RPD (free tier).

## More Configs

Visit [freellm.net/config/claude-code/](https://freellm.net/config/claude-code/) for the interactive config generator with all 128+ free models.
