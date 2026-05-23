<p align="center">
  <h1 align="center">awesome-free-llm-apis</h1>
  <!-- AUTO_STATS -->
  <p align="center"><strong>146+ 免費大模型 API，來自 24 個提供商</strong> — 一站式發現、對比、配置免費模型。</p>
<!-- END_AUTO_STATS -->
</p>

<p align="center">
  <a href="https://freellm.net"><strong>🌐 訪問 freellm.net</strong></a> —
  <a href="https://freellm.net/models/">瀏覽模型</a> ·
  <a href="https://freellm.net/playground/">線上體驗</a> ·
  <a href="https://freellm.net/config/">配置生成器</a> ·
  <a href="https://freellm.net/free-llm-api-keys/">API 金鑰</a>
</p>

  <!-- AUTO_UPDATE_BADGE -->
  <p align="center"><strong>🔄 資料每日從 <a href="https://freellm.net">freellm.net</a> 自動更新</strong> — 最後更新: 2026-05-23</p>
<!-- END_AUTO_UPDATE_BADGE -->

<p align="center">
  🌐 <a href="README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a>
</p>

---

## 為什麼需要這個專案

找一個免費 LLM API，不應該翻十幾個 GitHub README、註冊五個不同平台、或者猜測哪些模型還有免費額度。

這個倉庫是一個**結構化、機器可讀的免費 LLM API 目錄** — 包含速率限制、上下文視窗、一鍵配置程式碼片段和直達 API 金鑰連結。每日更新。

**為什麼選擇這個倉庫 + [freellm.net](https://freellm.net)：**

- ✅ **始終最新** — 資料每日自動化監控更新，不是兩年前的靜態列表
- ✅ **信用卡透明** — 清晰標註哪些提供商需要信用卡、手機驗證，哪些完全無需
- ✅ **一鍵配置** — 即用程式碼片段覆蓋 Claude Code、Cursor、Codex、Aider 等 10+ 工具
- ✅ **並排對比** — 即時對比各提供商的上下文視窗、速率限制和多模態能力

---

## 三步上手

1. **選一個提供商** — 看下方 [Provider Directory](#provider-directory)。推薦從 **Groq** 開始（免信用卡，30 RPM 免費）。
2. **獲取 API Key** — 點下方 [Quick Reference](#quick-reference--base-urls--api-keys) 裡任意一個 [Get Key →] 連結，註冊（大多只需信箱），複製 key。不到 1 分鐘。
3. **填入程式碼** — 複製 base URL + model ID，貼到下邊的 [Quick Start](#quick-start--use-any-free-api-in-30-seconds) 範例。

配置具體工具？[Claude Code](https://freellm.net/config/#claude-code) · [Cursor](https://freellm.net/config/#cursor) · [Codex](https://freellm.net/config/#codex) · [OpenHuman](https://freellm.net/config/#openhuman) · [OpenCode](https://freellm.net/config/#opencode) · [OpenClaw](https://freellm.net/config/#openclaw) — 一鍵配置在 [freellm.net/config/](https://freellm.net/config/)。



## 快速上手 — 30 秒接入免費 API

**沒用過 API？** 最簡單的方式：打開 [console.groq.com/keys](https://console.groq.com/keys)，用信箱註冊（無需信用卡），複製免費 key，貼到下面任意範例。不到一分鐘就能跑起來。

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

- **Claude Code** — 設 `ANTHROPIC_BASE_URL` + `ANTHROPIC_AUTH_TOKEN`。[詳細配置 →](https://freellm.net/config/#claude-code)
- **Cursor** — Settings → Models → Add Model。[詳細配置 →](https://freellm.net/config/#cursor)
- **Codex CLI** — 設 `OPENAI_BASE_URL` + `OPENAI_API_KEY`。[詳細配置 →](https://freellm.net/config/#codex)
- **OpenHuman** — 編輯 `config.toml`。[詳細配置 →](https://freellm.net/config/#openhuman)
- **Aider** — 編輯 `.aider.conf.yml`。[詳細配置 →](https://freellm.net/config/#aider)
- **Cline**（VS Code）— API provider 設定。[詳細配置 →](https://freellm.net/config/#cline)
- **Open WebUI** — Settings → Connections。[詳細配置 →](https://freellm.net/config/#open-webui)

更多即用配置在 **[freellm.net/config/](https://freellm.net/config/)**。

> **所有提供商的 Base URL 和 API Key 連結** 見下方 [Quick Reference](#quick-reference--base-urls--api-keys)。


---

## 提供商目錄 & 熱門免費模型

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

<!-- BEGIN_RENEWABLE -->
| Provider | Free Models | Credit Model | Max Context | Modalities | Get API Key |
|---|---|---|---|---|---|
| OpenRouter | 29 | Free tier + $10 topup → 1K RPD | 1M | audio, code, embeddings, image, reasoning, text | [→](https://openrouter.ai/workspaces/default/keys) |
<!-- END_RENEWABLE -->

## 快速參考 — Base URL 與 API Key

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

## 各提供商最佳免費模型

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



### 热门免费模型

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

## 參與貢獻

歡迎貢獻！

- **補充缺失的免費模型** — 提交 [issue](https://github.com/open-free-llm-api/awesome-free-llm-apis/issues) 或 PR
- **修正不準確的資料** — 速率限制會變、提供商會升級，歡迎 PR
- **添加配置程式碼片段** — 有你常用工具的配置方案？添加到 `code-examples/`

### 收錄標準

模型列入本列表需滿足：
1. 提供商明確提供**免費層**（不僅僅是試用額度）
2. API **公開可訪問**（無需候補、封閉內測、或逆向工程）
3. 試用額度：明確標註且最低 $1 額度

---

## 連結

- 🌐 **線上網站**: [freellm.net](https://freellm.net) — 搜尋、對比、線上體驗、配置產生器
- 🔑 **API 金鑰目錄**: [freellm.net/free-llm-api-keys/](https://freellm.net/free-llm-api-keys/)
- ⚙️ **配置產生器**: [freellm.net/config/](https://freellm.net/config/)
- 🎮 **線上體驗**: [freellm.net/playground/](https://freellm.net/playground/)
- 📊 **模型對比**: [freellm.net/compare/](https://freellm.net/compare/)

## 授權

MIT © [open-free-llm-api](https://github.com/open-free-llm-api)

---

<p align="center">
  <sub>資料每日自動更新 · 最後更新: <!-- AUTO_LAST_UPDATED -->
2026-05-23
<!-- END_AUTO_LAST_UPDATED --></sub>
</p>
