# Cursor — Free LLM API Config

Configure Cursor with any free OpenAI-compatible API in under a minute.

## How It Works

Cursor supports custom API providers via Settings → Models → Add Model. You enter a model name, base URL, and API key — Cursor routes completions through that provider.

## Step-by-Step

1. **Get a free API key** from one of the providers below
2. **Open Cursor Settings** → Models → scroll to "OpenAI API Key" section
3. **Override the API key** — paste your free provider's key into the "OpenAI API Key" field
4. **Override the base URL** — paste the provider's base URL into "OpenAI Base URL"
5. **Add the model name** — under "Custom Models", add the model ID (e.g., `gpt-oss-120b`)

## Recommended Backends

### Groq

```
Base URL:  https://api.groq.com/openai/v1
API Key:   gsk_your_groq_api_key
Model:     openai/gpt-oss-120b  # check current availability and limits with Groq
```

Get key: [console.groq.com/keys](https://console.groq.com/keys) — no credit card, instant.

### OpenRouter

```
Base URL:  https://openrouter.ai/api/v1
API Key:   sk-or-v1-your_openrouter_key
Models:    openai/gpt-oss-120b:free, google/gemini-2.5-flash:free, qwen/qwen3-coder:free
```

Get key: [openrouter.ai/keys](https://openrouter.ai/workspaces/default/keys) — 35+ free models.

### NVIDIA NIM

```
Base URL:  https://integrate.api.nvidia.com/v1
API Key:   nvapi-your_nvidia_key
Models:    meta/llama-3.3-70b-instruct, deepseek-ai/deepseek-r1
```

Get key: [build.nvidia.com](https://build.nvidia.com/settings/api-keys) — phone verification required, no credit card.

### Cloudflare Workers AI

```
Base URL:  https://api.cloudflare.com/client/v4/{account_id}/ai/v1
API Key:   your_cloudflare_token
Models:    @cf/meta/llama-3.1-8b-instruct, @cf/deepseek-ai/deepseek-r1-distill-qwen-32b
```

Get key: [dash.cloudflare.com](https://dash.cloudflare.com/profile/api-tokens) — 10K req/day free.

## Caveats

- Cursor's agent mode (multi-step tool use) works best with models that support tool calling. Check tool-calling support for the specific provider and model.
- Some providers throttle free-tier requests — if you see "rate limit" errors, try a different provider.
- The model name in Cursor must match the provider's model ID exactly.

## More Configs

Visit [freellm.net/config/cursor/](https://freellm.net/config/cursor/) for the interactive config generator.
