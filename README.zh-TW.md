<p align="center">
  <h1 align="center">awesome-free-llm-apis</h1>
  <!-- AUTO_STATS -->
  <p align="center"><strong>146+ 免費大模型 API，來自 20 個提供商</strong> — 一站式發現、對比、配置免費模型。</p>
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

## 快速開始 — 30 秒接入任意免費 API

以下所有提供商都暴露了 **OpenAI 相容介面**（Gemini 需要簡單包裝）。這表示任何接受 `baseURL` + `apiKey` 的工具都能直接使用。

### Claude Code (cc)

```bash
export ANTHROPIC_BASE_URL="https://api.openai.com/v1"  # 或 Groq, OpenRouter, NVIDIA NIM
export ANTHROPIC_AUTH_TOKEN="your-api-key-here"
# Claude Code 現在透過免費後端路由
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
    base_url="https://api.openai.com/v1",  # 換成以下任意提供商
    api_key="YOUR_FREE_API_KEY",
)

response = client.chat.completions.create(
    model="gpt-oss-120b",
    messages=[{"role": "user", "content": "你好！"}],
)
print(response.choices[0].message.content)
```

> 訪問 [freellm.net/config/](https://freellm.net/config/) 獲取 Aider、Cline、OpenCode、Continue、Open WebUI 和 Gemini CLI 的即用配置。

---

## 提供商目錄 & 熱門免費模型

<!-- BEGIN_PERMANENT_FREE -->
| Provider | Free Models | Credit Card? | Max Context | Modalities | Get API Key |
|---|---|---|---|---|---|
| NVIDIA NIM | 16 | Phone verification | 1M | image, text | [→](https://build.nvidia.com/settings/api-keys) |
| Groq | 14 | No | 262K | text | [→](https://console.groq.com/keys) |
| GitHub Models | 13 | No | 1M | text | [→](https://github.com/marketplace/models) |
| Cloudflare Workers AI | 10 | No | 10M | image, text | [→](https://dash.cloudflare.com/profile/api-tokens) |
| Mistral AI | 8 | No | 256K | code, image, text | [→](https://console.mistral.ai/api-keys) |
| OVHcloud AI Endpoints | 7 | Registration | 262K | code, image, text | [→](https://endpoints.ai.cloud.ovh.net/) |
| SiliconFlow | 6 | Registration | 131K | text | [→](https://cloud.siliconflow.cn/account/ak) |
| Cohere | 5 | No | 256K | text | [→](https://dashboard.cohere.com/api-keys) |
| Cerebras | 5 | No | 131K | text | [→](https://cloud.cerebras.ai/) |
| Hugging Face | 5 | No | 131K | text | [→](https://huggingface.co/settings/tokens) |
| LLM7.io | 5 | No | 131K | code, text | [→](https://token.llm7.io) |
| Ollama Cloud | 5 | Registration | 128K | text | [→](https://ollama.com/settings/keys) |
| Kilo Code | 4 | No | 262K | code, text | [→](https://kilo.ai) |
| Z AI (Zhipu AI) | 3 | No | 200K | text | [→](https://open.bigmodel.cn/usercenter/apikeys) |
| ModelScope | 3 | Registration | 131K | text | [→](https://modelscope.cn/my/myaccesstoken) |
| Google Gemini | 2 | No | 1M | text | [→](https://aistudio.google.com/app/apikey) |
| Chutes.ai | 2 | Registration | 131K | text | [→](https://chutes.ai/) |
| Glhf.chat | 2 | Registration | 131K | text | [→](https://glhf.chat/) |
| Grok (xAI) | 2 | Registration | 131K | text | [→](https://console.x.ai/) |
<!-- END_PERMANENT_FREE -->

<!-- BEGIN_RENEWABLE -->
| Provider | Free Models | Credit Model | Max Context | Modalities | Get API Key |
|---|---|---|---|---|---|
| OpenRouter | 29 | Free tier + $10 topup → 1K RPD | 1M | audio, code, embeddings, image, reasoning, text | [→](https://openrouter.ai/workspaces/default/keys) |
<!-- END_RENEWABLE -->

### 热门免费模型

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
