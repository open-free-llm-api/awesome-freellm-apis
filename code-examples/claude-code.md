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

Get your key at [console.groq.com/keys](https://console.groq.com/keys). Model to check: `openai/gpt-oss-120b`. The Claude Code route requires separate compatibility verification.

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

## Persistent Config

Add to your shell profile (`~/.zshrc` or `~/.bashrc`):

```bash
# Free LLM API backend for Claude Code
export ANTHROPIC_BASE_URL="https://api.groq.com/openai/v1"
export ANTHROPIC_AUTH_TOKEN="gsk_your_key_here"
```

## Caveats

- Claude Code expects tools/capabilities that not all free backends support. Check the provider endpoint and model capabilities for your client.
- The "Claude" model name shown in cc is cosmetic — you're actually using whichever model you configure.
- Free tiers have rate limits. Check the current per-model limits on each provider’s site.

## More Configs

Visit [freellm.net/config/claude-code/](https://freellm.net/config/claude-code/) for the interactive config generator with all 128+ free models.
