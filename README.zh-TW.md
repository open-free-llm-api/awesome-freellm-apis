<p align="center">
  <h1 align="center">awesome-free-llm-apis</h1>
  <!-- AUTO_STATS -->
  <p align="center"><strong>454+ 免費大模型 API，來自 31 個提供商</strong> — 一站式發現、對比、配置免費模型。</p>
<!-- END_AUTO_STATS -->
</p>

<p align="center">
  <a href="https://freellm.net" target="_blank" rel="noopener"><strong>🌐 訪問 freellm.net</strong></a> —
  <a href="https://freellm.net/models/" target="_blank" rel="noopener">瀏覽模型</a> ·
  <a href="https://freellm.net/playground/" target="_blank" rel="noopener">線上體驗</a> ·
  <a href="https://freellm.net/config/" target="_blank" rel="noopener">配置生成器</a> ·
  <a href="https://freellm.net/free-llm-api-keys/" target="_blank" rel="noopener">API 金鑰</a>
</p>

<p align="center">
  <img alt="Provider Logos" src="assets/provider-logos-marquee.svg" width="100%" />
</p>

  <!-- AUTO_UPDATE_BADGE -->
  <p align="center"><strong>🔄 資料每日從 <a href="https://freellm.net" target="_blank" rel="noopener">freellm.net</a> 自動更新</strong> — 最後更新: 2026-09-05</p>
<!-- END_AUTO_UPDATE_BADGE -->

<p align="center">
  🌐 <a href="README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a>
</p>

---

## 為什麼需要這個專案

找一個免費 LLM API，不應該翻十幾個 GitHub README、註冊五個不同平台、或者猜測哪些模型還有免費額度。

這個倉庫是一個**結構化、機器可讀的免費 LLM API 目錄** — 包含速率限制、上下文視窗、一鍵配置程式碼片段和直達 API 金鑰連結。每日更新。

**為什麼選擇這個倉庫 + <a href="https://freellm.net" target="_blank" rel="noopener">freellm.net</a>：**

- ✅ **始終最新** — 資料每日自動化監控更新，不是兩年前的靜態列表
- ✅ **信用卡透明** — 清晰標註哪些提供商需要信用卡、手機驗證，哪些完全無需
- ✅ **一鍵配置** — 即用程式碼片段覆蓋 Claude Code、Cursor、Codex、Aider 等 10+ 工具
- ✅ **並排對比** — 即時對比各提供商的上下文視窗、速率限制和多模態能力

---

## 三步上手

1. **選一個提供商** — 看下方 [Provider Directory](#provider-directory)。推薦從 **Groq** 開始（免信用卡，30 RPM 免費）。
2. **獲取 API Key** — 點下方 [Quick Reference](#quick-reference--base-urls--api-keys) 裡任意一個 [Get Key →] 連結，註冊（大多只需信箱），複製 key。不到 1 分鐘。
3. **填入程式碼** — 複製 base URL + model ID，貼到下邊的 [Quick Start](#quick-start--use-any-free-api-in-30-seconds) 範例。

配置具體工具？<a href="https://freellm.net/config/#claude-code" target="_blank" rel="noopener">Claude Code</a> · <a href="https://freellm.net/config/#cursor" target="_blank" rel="noopener">Cursor</a> · <a href="https://freellm.net/config/#codex" target="_blank" rel="noopener">Codex</a> · <a href="https://freellm.net/config/#openhuman" target="_blank" rel="noopener">OpenHuman</a> · <a href="https://freellm.net/config/#opencode" target="_blank" rel="noopener">OpenCode</a> · <a href="https://freellm.net/config/#openclaw" target="_blank" rel="noopener">OpenClaw</a> — 一鍵配置在 <a href="https://freellm.net/config/" target="_blank" rel="noopener">freellm.net/config/</a>。



## 快速上手 — 30 秒接入免費 API

**沒用過 API？** 最簡單的方式：打開 <a href="https://console.groq.com/keys" target="_blank" rel="noopener">console.groq.com/keys</a>，用信箱註冊（無需信用卡），複製免費 key，貼到下面任意範例。不到一分鐘就能跑起來。

以下所有提供商都暴露了 **OpenAI 相容介面**。任何接受 `baseURL` + `apiKey` 的工具都能直接用 — 替換 base URL 和 key 即可。

### Python (OpenAI SDK)

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",  # 免費，無需信用卡
    api_key="GROQ_API_KEY",                     # 獲取: console.groq.com/keys
)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",            # 模型列表見下方 Best Models 表
    messages=[{"role": "user", "content": "你好！"}],
)
print(response.choices[0].message.content)
# Groq 免費額度: 30 RPM, 14,400 RPD — 個人使用綽綽有餘
```

### Codex CLI

```bash
export OPENAI_BASE_URL="https://api.groq.com/openai/v1"
export OPENAI_API_KEY="your-groq-key"          # 獲取: console.groq.com/keys
codex --model "llama-3.3-70b-versatile"
```

### Cursor

```
Settings → Models → Add Model
  Model name: llama-3.3-70b-versatile
  Base URL: https://api.groq.com/openai/v1
  API key: your-groq-key                       # 獲取: console.groq.com/keys
```

### Claude Code

```bash
# Claude Code 需要 Anthropic 相容介面 — 使用 OpenRouter
export ANTHROPIC_BASE_URL="https://openrouter.ai/api"
export ANTHROPIC_AUTH_TOKEN="sk-or-v1-your-key"  # openrouter.ai/keys
export ANTHROPIC_API_KEY=""                       # 必須為空
# 注意: OpenRouter 的 Anthropic 模型需儲值 $10（一次性）
```

### 其他工具？

大多數 AI 開發工具都接受自訂 API 端點 — 拿到免費 key 後：

- **Claude Code** — 設 `ANTHROPIC_BASE_URL` + `ANTHROPIC_AUTH_TOKEN`。<a href="https://freellm.net/config/#claude-code" target="_blank" rel="noopener">詳細配置 →</a>
- **Cursor** — Settings → Models → Add Model。<a href="https://freellm.net/config/#cursor" target="_blank" rel="noopener">詳細配置 →</a>
- **Codex CLI** — 設 `OPENAI_BASE_URL` + `OPENAI_API_KEY`。<a href="https://freellm.net/config/#codex" target="_blank" rel="noopener">詳細配置 →</a>
- **OpenHuman** — 編輯 `config.toml`。<a href="https://freellm.net/config/#openhuman" target="_blank" rel="noopener">詳細配置 →</a>
- **Aider** — 編輯 `.aider.conf.yml`。<a href="https://freellm.net/config/#aider" target="_blank" rel="noopener">詳細配置 →</a>
- **Cline**（VS Code）— API provider 設定。<a href="https://freellm.net/config/#cline" target="_blank" rel="noopener">詳細配置 →</a>
- **Open WebUI** — Settings → Connections。<a href="https://freellm.net/config/#open-webui" target="_blank" rel="noopener">詳細配置 →</a>

更多即用配置在 **<a href="https://freellm.net/config/" target="_blank" rel="noopener">freellm.net/config/</a>**。

> **所有提供商的 Base URL 和 API Key 連結** 見下方 [Quick Reference](#quick-reference--base-urls--api-keys)。


---

## 提供商目錄 & 熱門免費模型

<!-- BEGIN_PERMANENT_FREE -->
| Provider | Free Models | Credit Card? | Max Context | Modalities | Get API Key |
|---|---|---|---|---|---|
| NVIDIA NIM | 126 | Phone verification | 1M | audio, embedding, image, reasoning, rerank, text, video, vision | <a href="https://build.nvidia.com/settings/api-keys" target="_blank" rel="noopener">→</a> |
| ModelScope | 59 | Registration | 1M | audio, image, reasoning, text, video, vision | <a href="https://modelscope.cn/my/myaccesstoken" target="_blank" rel="noopener">→</a> |
| Cloudflare Workers AI | 40 | No | 10M | code, image, reasoning, text, video | <a href="https://dash.cloudflare.com/profile/api-tokens" target="_blank" rel="noopener">→</a> |
| Google Gemini | 18 | No | 1M | audio, image, pdf, reasoning, text, video, vision | <a href="https://aistudio.google.com/app/apikey" target="_blank" rel="noopener">→</a> |
| GitHub Models | 16 | No | 1M | image, pdf, reasoning, text | <a href="https://github.com/marketplace/models" target="_blank" rel="noopener">→</a> |
| LLM7.io | 16 | No | 1M | audio, code, image, pdf, reasoning, text, video, vision | <a href="https://token.llm7.io" target="_blank" rel="noopener">→</a> |
| OVHcloud AI Endpoints | 14 | Registration | 262K | audio, code, image, reasoning, text, video | <a href="https://www.ovhcloud.com/en/public-cloud/ai-endpoints/catalog/" target="_blank" rel="noopener">→</a> |
| Ollama Cloud | 13 | Registration | 1M | code, image, reasoning, text, video, vision | <a href="https://ollama.com/settings/keys" target="_blank" rel="noopener">→</a> |
| OpenCode Zen | 13 | Registration | 1M | audio, reasoning, vision | <a href="https://opencode.ai/auth" target="_blank" rel="noopener">→</a> |
| Groq | 12 | No | 262K | image, reasoning, text | <a href="https://console.groq.com/keys" target="_blank" rel="noopener">→</a> |
| Mistral AI | 12 | No | 256K | code, image, text | <a href="https://console.mistral.ai/api-keys" target="_blank" rel="noopener">→</a> |
| Cohere | 12 | No | 436K | image, text | <a href="https://dashboard.cohere.com/api-keys" target="_blank" rel="noopener">→</a> |
| Kilo Code | 12 | No | 1M | audio, code, image, reasoning, text, video | <a href="https://kilo.ai" target="_blank" rel="noopener">→</a> |
| Aion Labs | 7 | Registration | 131K | text | <a href="https://www.aionlabs.ai" target="_blank" rel="noopener">→</a> |
| Hugging Face | 7 | No | 131K | code, text | <a href="https://huggingface.co/settings/tokens" target="_blank" rel="noopener">→</a> |
| Cerebras | 6 | No | 131K | reasoning, text | <a href="https://cloud.cerebras.ai/" target="_blank" rel="noopener">→</a> |
| Agnes AI | 5 | Registration | 256K | image, text, video, vision | <a href="https://platform.agnes-ai.com/settings/apiKeys" target="_blank" rel="noopener">→</a> |
| Alibaba Cloud Model Studio | 5 | Registration | 1M | code, image, text | <a href="https://bailian.console.alibabacloud.com/?apiKey=1" target="_blank" rel="noopener">→</a> |
| Z AI (Zhipu AI) | 4 | No | 200K | image, reasoning, text, video | <a href="https://open.bigmodel.cn/usercenter/apikeys" target="_blank" rel="noopener">→</a> |
| SambaNova | 4 | Registration | 128K | image, reasoning, text | <a href="https://cloud.sambanova.ai/apis" target="_blank" rel="noopener">→</a> |
| Cline | 4 | Registration | 0 | text | <a href="" target="_blank" rel="noopener">→</a> |
| SiliconFlow | 3 | Registration | 131K | text | <a href="https://cloud.siliconflow.cn/account/ak" target="_blank" rel="noopener">→</a> |
| xAI | 3 | Registration | 2M | text | <a href="https://console.x.ai" target="_blank" rel="noopener">→</a> |
| Chutes.ai | 2 | Registration | 131K | reasoning, text | <a href="https://chutes.ai/" target="_blank" rel="noopener">→</a> |
| Glhf.chat | 2 | Registration | 131K | text | <a href="https://glhf.chat/" target="_blank" rel="noopener">→</a> |
| Grok (xAI) | 2 | Registration | 131K | text | <a href="https://console.x.ai/" target="_blank" rel="noopener">→</a> |
| AI21 Labs | 2 | Registration | 256K | text | <a href="https://studio.ai21.com/account/api-key" target="_blank" rel="noopener">→</a> |
| DeepSeek | 2 | Registration | 128K | text | <a href="https://platform.deepseek.com/api_keys" target="_blank" rel="noopener">→</a> |
| Nscale | 2 | Registration | 128K | text | <a href="https://console.nscale.com/" target="_blank" rel="noopener">→</a> |
| Nebius | 1 | Registration | 128K | text | <a href="https://studio.nebius.com/settings/api-keys" target="_blank" rel="noopener">→</a> |
<!-- END_PERMANENT_FREE -->

<!-- BEGIN_RENEWABLE -->
| Provider | Free Models | Credit Model | Max Context | Modalities | Get API Key |
|---|---|---|---|---|---|
| OpenRouter | 30 | Free tier + $10 topup → 1K RPD | 1M | audio, code, embeddings, image, reasoning, rerank, speech, text, video | <a href="https://openrouter.ai/workspaces/default/keys" target="_blank" rel="noopener">→</a> |
<!-- END_RENEWABLE -->

## 快速參考 — Base URL 與 API Key

<!-- BEGIN_QUICK_REF -->
| Provider | Base URL | Get API Key | Credit Card? |
|---|---|---|---|
| NVIDIA NIM | `https://integrate.api.nvidia.com/v1` | <a href="https://build.nvidia.com/settings/api-keys" target="_blank" rel="noopener">Get Key →</a> | Phone verification |
| ModelScope | `https://api-inference.modelscope.cn/v1` | <a href="https://modelscope.cn/my/myaccesstoken" target="_blank" rel="noopener">Get Key →</a> | Registration |
| Cloudflare Workers AI | `https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run` | <a href="https://dash.cloudflare.com/profile/api-tokens" target="_blank" rel="noopener">Get Key →</a> | No |
| OpenRouter | `https://openrouter.ai/api/v1` | <a href="https://openrouter.ai/workspaces/default/keys" target="_blank" rel="noopener">Get Key →</a> | Registration |
| Google Gemini | `https://generativelanguage.googleapis.com/v1beta` | <a href="https://aistudio.google.com/app/apikey" target="_blank" rel="noopener">Get Key →</a> | No |
| GitHub Models | `https://models.github.ai/inference` | <a href="https://github.com/marketplace/models" target="_blank" rel="noopener">Get Key →</a> | No |
| LLM7.io | `https://api.llm7.io/v1` | <a href="https://token.llm7.io" target="_blank" rel="noopener">Get Key →</a> | No |
| OVHcloud AI Endpoints | `https://oai.endpoints.kepler.ai.cloud.ovh.net/v1` | <a href="https://www.ovhcloud.com/en/public-cloud/ai-endpoints/catalog/" target="_blank" rel="noopener">Get Key →</a> | Registration |
| Ollama Cloud | `https://api.ollama.com` | <a href="https://ollama.com/settings/keys" target="_blank" rel="noopener">Get Key →</a> | Registration |
| OpenCode Zen | `https://opencode.ai/zen/v1` | <a href="https://opencode.ai/auth" target="_blank" rel="noopener">Get Key →</a> | Registration |
| Groq | `https://api.groq.com/openai/v1` | <a href="https://console.groq.com/keys" target="_blank" rel="noopener">Get Key →</a> | No |
| Mistral AI | `https://api.mistral.ai/v1` | <a href="https://console.mistral.ai/api-keys" target="_blank" rel="noopener">Get Key →</a> | No |
| Cohere | `https://api.cohere.com/v2` | <a href="https://dashboard.cohere.com/api-keys" target="_blank" rel="noopener">Get Key →</a> | No |
| Kilo Code | `https://api.kilo.ai/api/gateway` | <a href="https://kilo.ai" target="_blank" rel="noopener">Get Key →</a> | No |
| Aion Labs | `https://api.aionlabs.ai/v1` | <a href="https://www.aionlabs.ai" target="_blank" rel="noopener">Get Key →</a> | Registration |
| Hugging Face | `https://router.huggingface.co/v1` | <a href="https://huggingface.co/settings/tokens" target="_blank" rel="noopener">Get Key →</a> | No |
| Cerebras | `https://api.cerebras.ai/v1` | <a href="https://cloud.cerebras.ai/" target="_blank" rel="noopener">Get Key →</a> | No |
| Agnes AI | `https://apihub.agnes-ai.com/v1` | <a href="https://platform.agnes-ai.com/settings/apiKeys" target="_blank" rel="noopener">Get Key →</a> | Registration |
| Alibaba Cloud Model Studio | `https://dashscope-intl.aliyuncs.com/compatible-mode/v1` | <a href="https://bailian.console.alibabacloud.com/?apiKey=1" target="_blank" rel="noopener">Get Key →</a> | Registration |
| Z AI (Zhipu AI) | `https://open.bigmodel.cn/api/paas/v4` | <a href="https://open.bigmodel.cn/usercenter/apikeys" target="_blank" rel="noopener">Get Key →</a> | No |
| SambaNova | `https://api.sambanova.ai/v1` | <a href="https://cloud.sambanova.ai/apis" target="_blank" rel="noopener">Get Key →</a> | Registration |
| Cline | `` | <a href="" target="_blank" rel="noopener">Get Key →</a> | Registration |
| SiliconFlow | `https://api.siliconflow.cn/v1` | <a href="https://cloud.siliconflow.cn/account/ak" target="_blank" rel="noopener">Get Key →</a> | Registration |
| xAI | `https://api.x.ai/v1` | <a href="https://console.x.ai" target="_blank" rel="noopener">Get Key →</a> | Registration |
| Chutes.ai | `https://api.chutes.ai/v1` | <a href="https://chutes.ai/" target="_blank" rel="noopener">Get Key →</a> | Registration |
| Glhf.chat | `https://glhf.chat/api/openai/v1` | <a href="https://glhf.chat/" target="_blank" rel="noopener">Get Key →</a> | Registration |
| Grok (xAI) | `https://api.x.ai/v1` | <a href="https://console.x.ai/" target="_blank" rel="noopener">Get Key →</a> | Registration |
| AI21 Labs | `https://api.ai21.com/studio/v1` | <a href="https://studio.ai21.com/account/api-key" target="_blank" rel="noopener">Get Key →</a> | Registration |
| DeepSeek | `https://api.deepseek.com/v1` | <a href="https://platform.deepseek.com/api_keys" target="_blank" rel="noopener">Get Key →</a> | Registration |
| Nscale | `https://inference.api.nscale.com/v1` | <a href="https://console.nscale.com/" target="_blank" rel="noopener">Get Key →</a> | Registration |
| Nebius | `https://api.studio.nebius.com/v1` | <a href="https://studio.nebius.com/settings/api-keys" target="_blank" rel="noopener">Get Key →</a> | Registration |
<!-- END_QUICK_REF -->

## 各提供商最佳免費模型

<!-- BEGIN_BEST_MODELS -->
| Provider | Best Free Model | Model ID | Max Context | Rate Limit |
|---|---|---|---|---|
| NVIDIA NIM | <a href="https://freellm.net/models/nvidia-nim/z-ai-glm-5-2/" target="_blank" rel="noopener">z-ai/glm-5.2</a> | `z-ai/glm-5.2` | 1M | Up to 40 RPM |
|  | <a href="https://freellm.net/models/nvidia-nim/poolside-laguna-xs-2-1/" target="_blank" rel="noopener">poolside/laguna-xs-2.1</a> | `poolside/laguna-xs-2.1` | 262K | Up to 40 RPM |
|  | <a href="https://freellm.net/models/nvidia-nim/z-ai-glm-5-1/" target="_blank" rel="noopener">z-ai/glm-5.1</a> | `z-ai/glm-5.1` | 202K | Up to 40 RPM |
| ModelScope | <a href="https://freellm.net/models/modelscope/minimax-minimax-m2-5/" target="_blank" rel="noopener">MiniMax-M2.5-highspeed</a> | `MiniMax/MiniMax-M2.5` | 204K | See provider |
|  | <a href="https://freellm.net/models/modelscope/qwen-qwen3-5-35b-a3b/" target="_blank" rel="noopener">Qwen/Qwen3.5-35B-A3B</a> | `qwen-qwen3-5-35b-a3b` | 131K | 2,000 RPD total; <=500 .. |
|  | <a href="https://freellm.net/models/modelscope/qwen-qwen3-5-27b/" target="_blank" rel="noopener">Qwen/Qwen3.5-27B</a> | `qwen-qwen3-5-27b` | 131K | 2,000 RPD total; <=500 .. |
| Cloudflare Workers AI | <a href="https://freellm.net/models/cloudflare-workers-ai/mistral-mistral-7b-instruct-v0-1/" target="_blank" rel="noopener">Mistral 7B</a> | `@cf/mistral/mistral-7b-instruct-v0.1` | 32K | See provider |
|  | <a href="https://freellm.net/models/cloudflare-workers-ai/qwen-qwen1-5-7b-chat/" target="_blank" rel="noopener">Qwen 1.5 7B</a> | `@cf/qwen/qwen1.5-7b-chat` | 32K | See provider |
|  | <a href="https://freellm.net/models/cloudflare-workers-ai/cf-meta-llama-3-3-70b-instruct-fp8-fast/" target="_blank" rel="noopener">@cf/meta/llama-3.3-70b-instruct-fp8-fast</a> | `@cf/meta/llama-3.3-70b-instruct-fp8-fast` | 131K | 10K neurons/day (shared) |
| OpenRouter | <a href="https://freellm.net/models/openrouter/nvidia-nemotron-3-ultra-550b-a55b/" target="_blank" rel="noopener">NVIDIA: Nemotron 3 Ultra (free)</a> | `nvidia/nemotron-3-ultra-550b-a55b:free` | 1M | See provider |
|  | <a href="https://freellm.net/models/openrouter/poolside-laguna-m-1/" target="_blank" rel="noopener">Poolside: Laguna M.1 (free)</a> | `poolside/laguna-m.1:free` | 262K | See provider |
|  | <a href="https://freellm.net/models/openrouter/nvidia-nemotron-3-super-120b-a12b/" target="_blank" rel="noopener">NVIDIA: Nemotron 3 Super (free)</a> | `nvidia/nemotron-3-super-120b-a12b:free` | 262K | See provider |
| Google Gemini | <a href="https://freellm.net/models/google-gemini/gemini-3-6-flash/" target="_blank" rel="noopener">Gemini 3.6 Flash</a> | `gemini-3.6-flash` | 1M | 15 RPM, 1,500 RPD |
|  | <a href="https://freellm.net/models/google-gemini/gemini-3-5-flash/" target="_blank" rel="noopener">Gemini 3.5 Flash</a> | `gemini-3.5-flash` | 1M | 15 RPM, 1,500 RPD |
|  | <a href="https://freellm.net/models/google-gemini/gemini-3-5-flash-lite/" target="_blank" rel="noopener">Gemini 3.5 Flash-Lite</a> | `gemini-3.5-flash-lite` | 1M | 30 RPM, 1,500 RPD |
| GitHub Models | <a href="https://freellm.net/models/github-models/phi-4/" target="_blank" rel="noopener">Phi-4</a> | `Phi-4` | 131K | See provider |
|  | <a href="https://freellm.net/models/github-models/mistral-large-2411/" target="_blank" rel="noopener">Mistral Large (24.11)</a> | `Mistral-large-2411` | 131K | See provider |
|  | <a href="https://freellm.net/models/github-models/ai21-jamba-1-5-large/" target="_blank" rel="noopener">AI21 Jamba 1.5 Large</a> | `AI21-Jamba-1.5-Large` | 256K | See provider |
| LLM7.io | <a href="https://freellm.net/models/llm7-io/deepseek-r1-0528/" target="_blank" rel="noopener">deepseek-r1-0528</a> | `deepseek-r1-0528` | 131K | 30 RPM (120 with token) |
|  | <a href="https://freellm.net/models/llm7-io/deepseek-v3-0324/" target="_blank" rel="noopener">deepseek-v3-0324</a> | `deepseek-v3.2` | 131K | 30 RPM (120 with token) |
|  | <a href="https://freellm.net/models/llm7-io/gpt-4o-mini/" target="_blank" rel="noopener">gpt-4o-mini</a> | `gpt-4o-mini` | 131K | 30 RPM (120 with token) |
| OVHcloud AI Endpoints | <a href="https://freellm.net/models/ovhcloud-ai-endpoints/qwen3-5-397b-a17b/" target="_blank" rel="noopener">Qwen3.5-397B-A17B</a> | `qwen3.5-397b-a17b` | 131K | 2 RPM (anonymous) |
|  | <a href="https://freellm.net/models/ovhcloud-ai-endpoints/meta-llama-3-3-70b-instruct/" target="_blank" rel="noopener">Meta-Llama-3_3-70B-Instruct</a> | `meta-llama-3_3-70b-instruct` | 131K | 2 RPM (anonymous) |
|  | <a href="https://freellm.net/models/ovhcloud-ai-endpoints/qwen3-6-27b/" target="_blank" rel="noopener">Qwen3.6-27B</a> | `qwen3.6-27b` | 131K | 2 RPM (anonymous) |
| Ollama Cloud | <a href="https://freellm.net/models/ollama-cloud/minimax-m3/" target="_blank" rel="noopener">minimax-m3</a> | `minimax-m3` | 1M | Session/weekly limits (.. |
|  | <a href="https://freellm.net/models/ollama-cloud/gpt-oss-20b/" target="_blank" rel="noopener">gpt-oss:20b</a> | `gpt-oss:20b` | 131K | Session/weekly limits (.. |
|  | <a href="https://freellm.net/models/ollama-cloud/nemotron-3-ultra/" target="_blank" rel="noopener">nemotron-3-ultra</a> | `nemotron-3-ultra` | 262K | Session/weekly limits (.. |
| OpenCode Zen | <a href="https://freellm.net/models/opencode/big-pickle/" target="_blank" rel="noopener">big-pickle</a> | `big-pickle` | 0 |  |
|  | <a href="https://freellm.net/models/opencode/deepseek-v4-flash-free/" target="_blank" rel="noopener">DeepSeek V4 Flash</a> | `deepseek-v4-flash-free` | 1M |  |
|  | <a href="https://freellm.net/models/opencode/mimo-v2-5-free/" target="_blank" rel="noopener">MiMo-V2.5</a> | `mimo-v2.5-free` | 1M |  |
| Groq | <a href="https://freellm.net/models/groq/moonshotai-kimi-k2-instruct/" target="_blank" rel="noopener">Moonshot Kimi K2</a> | `moonshotai/kimi-k2-instruct` | 131K | See provider |
|  | <a href="https://freellm.net/models/groq/moonshotai-kimi-k2-instruct-0905/" target="_blank" rel="noopener">Moonshot Kimi K2 0905</a> | `moonshotai/kimi-k2-instruct-0905` | 131K | See provider |
|  | <a href="https://freellm.net/models/groq/groq-compound/" target="_blank" rel="noopener">groq/compound</a> | `groq/compound` | 131K | 30 RPM, 250 RPD |
| Mistral AI | <a href="https://freellm.net/models/mistral-ai/open-mistral-7b/" target="_blank" rel="noopener">Mistral 7B</a> | `open-mistral-7b` | 32K | See provider |
|  | <a href="https://freellm.net/models/mistral-ai/open-mixtral-8x7b/" target="_blank" rel="noopener">Mixtral 8x7B</a> | `open-mixtral-8x7b` | 32K | See provider |
|  | <a href="https://freellm.net/models/mistral-ai/mistral-medium-3-5-128b/" target="_blank" rel="noopener">Mistral Medium 3.5 (128B)</a> | `mistral-medium-3-5-128b` | 256K | ~1 RPS, 500K TPM |
| Cohere | <a href="https://freellm.net/models/cohere/command-a-218b/" target="_blank" rel="noopener">Command A+ (218B)</a> | `command-a-218b` | 436K | 20 RPM |
|  | <a href="https://freellm.net/models/cohere/command-a-111b/" target="_blank" rel="noopener">Command A (111B)</a> | `command-a-111b` | 288K | 20 RPM |
|  | <a href="https://freellm.net/models/cohere/command-r/" target="_blank" rel="noopener">Command R+</a> | `command-r` | 128K | 20 RPM |
| Kilo Code | <a href="https://freellm.net/models/kilo-code/nvidia-nemotron-3-ultra-550b-a55b-free/" target="_blank" rel="noopener">nvidia/nemotron-3-ultra-550b-a55b:free</a> | `nvidia/nemotron-3-ultra-550b-a55b:free` | 1M | ~200 req/hr |
|  | <a href="https://freellm.net/models/kilo-code/stepfun-step-3-7-flash-free/" target="_blank" rel="noopener">stepfun/step-3.7-flash:free</a> | `stepfun/step-3.7-flash:free` | 262K | ~200 req/hr |
|  | <a href="https://freellm.net/models/kilo-code/nvidia-nemotron-3-super-120b-a12b-free/" target="_blank" rel="noopener">nvidia/nemotron-3-super-120b-a12b:free</a> | `nvidia/nemotron-3-super-120b-a12b:free` | 262K | ~200 req/hr |
| Aion Labs | <a href="https://freellm.net/models/aion-labs/aion-2-5/" target="_blank" rel="noopener">Aion 2.5</a> | `aion-2-5` | 128K | 15 RPM, 20K TPD |
|  | <a href="https://freellm.net/models/aion-labs/aion-2-0/" target="_blank" rel="noopener">Aion 2.0</a> | `aion-2-0` | 128K | 15 RPM, 20K TPD |
|  | <a href="https://freellm.net/models/aion-labs/aion-rp-1-0-8b/" target="_blank" rel="noopener">Aion-RP 1.0 (8B)</a> | `aion-rp-1-0-8b` | 32K | 15 RPM, 20K TPD |
| Hugging Face | <a href="https://freellm.net/models/hugging-face/meta-llama-3-1-8b-instruct/" target="_blank" rel="noopener">Meta-Llama-3.1-8B-Instruct</a> | `meta-llama-3-1-8b-instruct` | 128K | Credit-metered |
|  | <a href="https://freellm.net/models/hugging-face/gemma-3-4b-it/" target="_blank" rel="noopener">gemma-3-4b-it</a> | `gemma-3-4b-it` | 131K | Credit-metered |
|  | <a href="https://freellm.net/models/hugging-face/qwen2-5-coder-7b-instruct/" target="_blank" rel="noopener">Qwen2.5-Coder-7B-Instruct</a> | `qwen2-5-coder-7b-instruct` | 131K | Credit-metered |
| Cerebras | <a href="https://freellm.net/models/cerebras/llama3-1-70b/" target="_blank" rel="noopener">Llama 3.1 70B</a> | `llama3.1-70b` | 131K | See provider |
|  | <a href="https://freellm.net/models/cerebras/zai-glm-4-7-deprecated-aug-2026/" target="_blank" rel="noopener">zai-glm-4.7 (deprecated Aug 2026)</a> | `zai-glm-4.7` | 131K | 5 RPM, 30K TPM, 1M TPD |
|  | <a href="https://freellm.net/models/cerebras/zai-glm-4-7/" target="_blank" rel="noopener">zai-glm-4.7</a> | `zai-glm-4.7` | 128K | 10 RPM, 100 RPD, 1M TPD |
| Agnes AI | <a href="https://freellm.net/models/agnes-ai/agnes-1-5-flash/" target="_blank" rel="noopener">agnes-1.5-flash</a> | `agnes-1.5-flash` | 256K | 30 RPM |
|  | <a href="https://freellm.net/models/agnes-ai/agnes-2-0-flash/" target="_blank" rel="noopener">agnes-2.0-flash</a> | `agnes-2.0-flash` | 256K | 30 RPM |
|  | <a href="https://freellm.net/models/agnes-ai/agnes-image-2-0-flash/" target="_blank" rel="noopener">agnes-image-2.0-flash</a> | `agnes-image-2.0-flash` | 4K | 30 RPM (1K) |
| Alibaba Cloud Model Studio | <a href="https://freellm.net/models/alibaba-cloud-model-studio/qwen3-max/" target="_blank" rel="noopener">Qwen3-Max</a> | `qwen3-max` | 128K | Tiered by region |
|  | <a href="https://freellm.net/models/alibaba-cloud-model-studio/qwen3-plus/" target="_blank" rel="noopener">Qwen3-Plus</a> | `qwen3-plus` | 1M | Tiered by region |
|  | <a href="https://freellm.net/models/alibaba-cloud-model-studio/qwen3-vl-plus/" target="_blank" rel="noopener">Qwen3-VL-Plus</a> | `qwen3-vl-plus` | 128K | Tiered by region |
| Z AI (Zhipu AI) | <a href="https://freellm.net/models/z-ai-zhipu-ai/glm-4-7-flash/" target="_blank" rel="noopener">GLM-4.7-Flash</a> | `glm-4.7` | 200K | 1 concurrent request |
|  | <a href="https://freellm.net/models/z-ai-zhipu-ai/glm-4-5-flash/" target="_blank" rel="noopener">GLM-4.5-Flash</a> | `glm-4.5` | 128K | 1 concurrent request |
|  | <a href="https://freellm.net/models/z-ai-zhipu-ai/glm-4-6v-flash/" target="_blank" rel="noopener">GLM-4.6V-Flash</a> | `glm-4.6` | 128K | 1 concurrent request |
| SambaNova | <a href="https://freellm.net/models/sambanova/deepseek-v3-1/" target="_blank" rel="noopener">DeepSeek-V3.1</a> | `deepseek-v3-1` | 128K | 20 RPM, 20 RPD, 200K TPD |
|  | <a href="https://freellm.net/models/sambanova/deepseek-v3-2-preview/" target="_blank" rel="noopener">DeepSeek-V3.2 (Preview)</a> | `deepseek-v3-2-preview` | 128K | 20 RPM, 20 RPD, 200K TPD |
|  | <a href="https://freellm.net/models/sambanova/minimax-m2-7/" target="_blank" rel="noopener">MiniMax-M2.7</a> | `minimax-m2-7` | 128K | 20 RPM, 20 RPD, 200K TPD |
| Cline | <a href="https://freellm.net/models/cline/deepseek-deepseek-v4-flash/" target="_blank" rel="noopener">deepseek-v4-flash</a> | `deepseek/deepseek-v4-flash` | 0 | See provider |
|  | <a href="https://freellm.net/models/cline/poolside-laguna-s-2-1/" target="_blank" rel="noopener">laguna-s-2.1:free</a> | `poolside/laguna-s-2.1:free` | 0 | See provider |
|  | <a href="https://freellm.net/models/cline/z-ai-glm-5-3-flash/" target="_blank" rel="noopener">glm-5.3-flash</a> | `z-ai/glm-5.3-flash` | 0 | See provider |
| SiliconFlow | <a href="https://freellm.net/models/siliconflow/deepseek-ai-deepseek-r1-distill-qwen-7b/" target="_blank" rel="noopener">deepseek-ai/DeepSeek-R1-Distill-Qwen-7B</a> | `deepseek-ai-deepseek-r1-distill-qwen-7b` | 131K | 30 RPM, 60K TPM |
|  | <a href="https://freellm.net/models/siliconflow/abbreviation/" target="_blank" rel="noopener">Abbreviation</a> | `abbreviation` | 131K | See provider |
|  | <a href="https://freellm.net/models/siliconflow/deepseek-ai-deepseek-ocr/" target="_blank" rel="noopener">deepseek-ai/DeepSeek-OCR</a> | `deepseek-ai-deepseek-ocr` | 131K | 30 RPM, 60K TPM |
| xAI | <a href="https://freellm.net/models/xai/grok-4-3/" target="_blank" rel="noopener">grok-4.3</a> | `grok-4-3` | 1M | Credit-based |
|  | <a href="https://freellm.net/models/xai/grok-4-1-fast/" target="_blank" rel="noopener">grok-4.1-fast</a> | `grok-4-1-fast` | 2M | Credit-based |
|  | <a href="https://freellm.net/models/xai/grok-3-mini/" target="_blank" rel="noopener">grok-3-mini</a> | `grok-3-mini` | 131K | Credit-based |
| Chutes.ai | <a href="https://freellm.net/models/chutes-ai/deepseek-ai-deepseek-r1/" target="_blank" rel="noopener">DeepSeek-R1</a> | `deepseek-ai/DeepSeek-R1` | 131K | Community-powered, no h.. |
|  | <a href="https://freellm.net/models/chutes-ai/meta-llama-meta-llama-3-1-70b-instruct/" target="_blank" rel="noopener">Llama 3.1 70B</a> | `meta-llama/Meta-Llama-3.1-70B-Instruct` | 131K | Community-powered, no h.. |
| Glhf.chat | <a href="https://freellm.net/models/glhf-chat/meta-llama-meta-llama-3-1-70b-instruct-2/" target="_blank" rel="noopener">Llama 3.1 70B</a> | `meta-llama/Meta-Llama-3.1-70B-Instruct` | 131K | Unlimited for free models |
|  | <a href="https://freellm.net/models/glhf-chat/mistralai-mixtral-8x7b-instruct-v0-1/" target="_blank" rel="noopener">Mixtral 8x7B</a> | `mistralai/Mixtral-8x7B-Instruct-v0.1` | 32K | Unlimited for free models |
| Grok (xAI) | <a href="https://freellm.net/models/grok-(xai)/grok-2/" target="_blank" rel="noopener">Grok-2</a> | `grok-2` | 131K | $25/month free credits,.. |
|  | <a href="https://freellm.net/models/grok-(xai)/grok-2-mini/" target="_blank" rel="noopener">Grok-2 Mini</a> | `grok-2-mini` | 131K | $25/month free credits,.. |
| AI21 Labs | <a href="https://freellm.net/models/ai21-labs/jamba-large-1-7/" target="_blank" rel="noopener">Jamba Large 1.7</a> | `jamba-large-1-7` | 256K | 200 RPM, 10 RPS |
|  | <a href="https://freellm.net/models/ai21-labs/jamba-mini-2/" target="_blank" rel="noopener">Jamba Mini 2</a> | `jamba-mini-2` | 256K | 200 RPM, 10 RPS |
| DeepSeek | <a href="https://freellm.net/models/deepseek/deepseek-chat-v3-2/" target="_blank" rel="noopener">deepseek-chat (V3.2)</a> | `deepseek-chat-v3-2` | 128K | Dynamic |
|  | <a href="https://freellm.net/models/deepseek/deepseek-reasoner-r1/" target="_blank" rel="noopener">deepseek-reasoner (R1)</a> | `deepseek-reasoner-r1` | 128K | Dynamic |
| Nscale | <a href="https://freellm.net/models/nscale/llama-3-3-70b-instruct/" target="_blank" rel="noopener">Llama-3.3-70B-Instruct</a> | `llama-3-3-70b-instruct` | 128K | Fair-use |
|  | <a href="https://freellm.net/models/nscale/deepseek-r1-distill-llama-70b/" target="_blank" rel="noopener">DeepSeek-R1-Distill-Llama-70B</a> | `deepseek-r1-distill-llama-70b` | 128K | Fair-use |
| Nebius | <a href="https://freellm.net/models/nebius/qwen3-235b-a22b/" target="_blank" rel="noopener">Qwen3-235B-A22B</a> | `qwen3-235b-a22b` | 128K | Tier-based |
<!-- END_BEST_MODELS -->



### 热门免费模型

<!-- BEGIN_TOP_MODELS -->
| Model | Provider | Context | Weekly Usage |
|---|---|---|---|
| <a href="https://freellm.net/models/nvidia-nim/z-ai-glm-5-2/" target="_blank" rel="noopener">z-ai/glm-5.2</a> | NVIDIA NIM | 1M | 2998B tokens |
| <a href="https://freellm.net/models/openrouter/nvidia-nemotron-3-ultra-550b-a55b/" target="_blank" rel="noopener">NVIDIA: Nemotron 3 Ultra (free)</a> | OpenRouter | 1M | 2326B tokens |
| <a href="https://freellm.net/models/openrouter/poolside-laguna-m-1/" target="_blank" rel="noopener">Poolside: Laguna M.1 (free)</a> | OpenRouter | 262K | 768B tokens |
| <a href="https://freellm.net/models/openrouter/nvidia-nemotron-3-super-120b-a12b/" target="_blank" rel="noopener">NVIDIA: Nemotron 3 Super (free)</a> | OpenRouter | 262K | 315B tokens |
| <a href="https://freellm.net/models/openrouter/cohere-north-mini-code/" target="_blank" rel="noopener">Cohere: North Mini Code (free)</a> | OpenRouter | 256K | 255B tokens |
| <a href="https://freellm.net/models/nvidia-nim/poolside-laguna-xs-2-1/" target="_blank" rel="noopener">poolside/laguna-xs-2.1</a> | NVIDIA NIM | 262K | 171B tokens |
| <a href="https://freellm.net/models/nvidia-nim/z-ai-glm-5-1/" target="_blank" rel="noopener">z-ai/glm-5.1</a> | NVIDIA NIM | 202K | 158B tokens |
| <a href="https://freellm.net/models/openrouter/poolside-laguna-s-2-1/" target="_blank" rel="noopener">Poolside: Laguna S 2.1 (free)</a> | OpenRouter | 262K | 83B tokens |
| <a href="https://freellm.net/models/openrouter/poolside-laguna-xs-2-1/" target="_blank" rel="noopener">Poolside: Laguna XS 2.1 (free)</a> | OpenRouter | 262K | 81B tokens |
| <a href="https://freellm.net/models/nvidia-nim/qwen-qwen3-5-397b-a17b/" target="_blank" rel="noopener">qwen/qwen3.5-397b-a17b</a> | NVIDIA NIM | 262K | 35B tokens |
<!-- END_TOP_MODELS -->

---

## 參與貢獻

歡迎貢獻！

- **補充缺失的免費模型** — 提交 <a href="https://github.com/open-free-llm-api/awesome-free-llm-apis/issues" target="_blank" rel="noopener">issue</a> 或 PR
- **修正不準確的資料** — 速率限制會變、提供商會升級，歡迎 PR
- **添加配置程式碼片段** — 有你常用工具的配置方案？添加到 `code-examples/`

### 收錄標準

模型列入本列表需滿足：
1. 提供商明確提供**免費層**（不僅僅是試用額度）
2. API **公開可訪問**（無需候補、封閉內測、或逆向工程）
3. 試用額度：明確標註且最低 $1 額度

---

## 連結

- 🌐 **線上網站**: <a href="https://freellm.net" target="_blank" rel="noopener">freellm.net</a> — 搜尋、對比、線上體驗、配置產生器
- 🔑 **API 金鑰目錄**: <a href="https://freellm.net/free-llm-api-keys/" target="_blank" rel="noopener">freellm.net/free-llm-api-keys/</a>
- ⚙️ **配置產生器**: <a href="https://freellm.net/config/" target="_blank" rel="noopener">freellm.net/config/</a>
- 🎮 **線上體驗**: <a href="https://freellm.net/playground/" target="_blank" rel="noopener">freellm.net/playground/</a>
- 📊 **模型對比**: <a href="https://freellm.net/compare/" target="_blank" rel="noopener">freellm.net/compare/</a>

## 授權

MIT © <a href="https://github.com/open-free-llm-api" target="_blank" rel="noopener">open-free-llm-api</a>

---

<p align="center">
  <sub>資料每日自動更新 · 最後更新: <!-- AUTO_LAST_UPDATED -->
2026-09-05
<!-- END_AUTO_LAST_UPDATED --></sub>
</p>
