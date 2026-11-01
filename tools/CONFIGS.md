# Tool configs (corrected quick-start)

## Claude Code
Claude Code speaks the **Anthropic Messages API**, so the endpoint must be Anthropic-compatible.
Plain OpenAI-style URLs (Groq `/openai/v1`, NVIDIA `/v1`) will NOT work — `code-examples/claude-code.md`
in this repo suggests them, which is wrong. Use OpenRouter (per the main README), or put an
OpenAI->Anthropic proxy (e.g. LiteLLM) in front of any other provider.

```bash
export ANTHROPIC_BASE_URL="https://openrouter.ai/api"
export ANTHROPIC_AUTH_TOKEN="$OPENROUTER_API_KEY"
export ANTHROPIC_API_KEY=""            # must be empty
export ANTHROPIC_MODEL="nvidia/nemotron-3-ultra-550b-a55b:free"   # any :free model id
claude
```
Some vendors also publish native Anthropic-compatible endpoints (e.g. DeepSeek, Z.AI) — check their docs.

## Codex CLI (~/.codex/config.toml)
```toml
model = "llama-3.3-70b-versatile"
model_provider = "groq"

[model_providers.groq]
name = "Groq"
base_url = "https://api.groq.com/openai/v1"
env_key = "GROQ_API_KEY"
wire_api = "chat"
```
Or the env-var form: `export OPENAI_BASE_URL=https://api.groq.com/openai/v1 OPENAI_API_KEY=$GROQ_API_KEY`.
Needs a model with tool calling (Llama 3.3 70B+, Qwen3 Coder, GPT-OSS).

## Cursor
Settings -> Models -> OpenAI API Key: paste key, enable "Override OpenAI Base URL" with
`https://api.groq.com/openai/v1`, add custom model `llama-3.3-70b-versatile`.
(Cursor routes custom endpoints via its servers, so `localhost` URLs won't work.)

## Verify
```bash
set -a; source tools/.env; set +a
python3 tools/test_endpoints.py
```
