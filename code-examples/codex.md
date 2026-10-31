# Codex CLI — Free LLM API Config

Use OpenAI's Codex CLI with any free LLM backend — no paid OpenAI tier needed.

## How It Works

Codex CLI reads `OPENAI_BASE_URL` and `OPENAI_API_KEY` from environment variables. For a custom backend, Codex requires a compatible Responses API, including streaming, tool calls, and conversation continuation. Chat Completions compatibility alone is not enough. See the [Codex gateway compatibility guide](https://learn.chatgpt.com/docs/enterprise/gateway-compatibility).

## Quick Config

### Groq (fastest, no credit card)

```bash
export OPENAI_BASE_URL="https://api.groq.com/openai/v1"
export OPENAI_API_KEY="gsk_your_groq_api_key"
```

Get key: [console.groq.com/keys](https://console.groq.com/keys). Model to check: `openai/gpt-oss-120b`. Groq provides a [beta Responses API](https://console.groq.com/docs/responses-api); verify the complete Codex workflow with your account and CLI version.

### NVIDIA NIM (no daily token cap)

```bash
export OPENAI_BASE_URL="https://integrate.api.nvidia.com/v1"
export OPENAI_API_KEY="nvapi-your_nvidia_key"
```

Get key: [build.nvidia.com](https://build.nvidia.com/settings/api-keys). Model: `meta/llama-3.3-70b-instruct`.

### OpenRouter (one key, 35+ models)

```bash
export OPENAI_BASE_URL="https://openrouter.ai/api/v1"
export OPENAI_API_KEY="sk-or-v1-your_openrouter_key"
```

Get key: [openrouter.ai/keys](https://openrouter.ai/workspaces/default/keys). Model: `openai/gpt-oss-120b:free`.

### Cerebras (gpt-oss with no credit card)

```bash
export OPENAI_BASE_URL="https://api.cerebras.ai/v1"
export OPENAI_API_KEY="your_cerebras_key"
```

Get key: [cloud.cerebras.ai](https://cloud.cerebras.ai/). Model: `llama3.1-70b`.

## Persistent Config

```bash
# ~/.zshrc or ~/.bashrc
export OPENAI_BASE_URL="https://api.groq.com/openai/v1"
export OPENAI_API_KEY="gsk_your_key_here"
```

## Codex-Specific Model Recommendations

Codex CLI works best with models that support:

| Capability | Recommended Free Models |
|---|---|
| Fast completions | Check your provider’s current model catalog and limits |
| Complex reasoning | DeepSeek R1 (OpenRouter, NVIDIA NIM) |
| Long context | Gemini 2.5 Flash (Google AI Studio, 1M ctx) |
| Tool calling | Check model and endpoint support with your client |
| Code generation | Qwen3 Coder, DeepSeek R1, GPT-OSS 120B |

## Caveats

- Check Responses API streaming, tool calls, and continuation with the chosen provider and model; compatibility and limits differ.
- Set a model name in your Codex config that matches the provider's model ID exactly.
- Rate limits apply to all free tiers.

## More Configs

Visit [freellm.net/config/codex/](https://freellm.net/config/codex/) for the interactive config generator.
