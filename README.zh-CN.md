<p align="center">
  <h1 align="center">awesome-free-llm-apis</h1>
  <!-- AUTO_STATS -->
  <p align="center"><strong>144+ 免费大模型 API，来自 24 个提供商</strong> — 一站式发现、对比、配置免费模型。</p>
<!-- END_AUTO_STATS -->
</p>

<p align="center">
  <a href="https://freellm.net" target="_blank" rel="noopener"><strong>🌐 访问 freellm.net</strong></a> —
  <a href="https://freellm.net/models/" target="_blank" rel="noopener">浏览模型</a> ·
  <a href="https://freellm.net/playground/" target="_blank" rel="noopener">在线体验</a> ·
  <a href="https://freellm.net/config/" target="_blank" rel="noopener">配置生成器</a> ·
  <a href="https://freellm.net/free-llm-api-keys/" target="_blank" rel="noopener">API 密钥</a>
</p>

  <!-- AUTO_UPDATE_BADGE -->
  <p align="center"><strong>🔄 数据每日从 <a href="https://freellm.net" target="_blank" rel="noopener">freellm.net</a> 自动更新</strong> — 最后更新: 2026-06-01</p>
<!-- END_AUTO_UPDATE_BADGE -->

<p align="center">
  🌐 <a href="README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a>
</p>

---

## 为什么需要这个项目

找一个免费 LLM API，不应该翻十几个 GitHub README、注册五个不同平台、或者猜测哪些模型还有免费额度。

这个仓库是一个**结构化、机器可读的免费 LLM API 目录** — 包含速率限制、上下文窗口、一键配置代码片段和直达 API 密钥链接。每日更新。

**为什么选择这个仓库 + <a href="https://freellm.net" target="_blank" rel="noopener">freellm.net</a>：**

- ✅ **始终最新** — 数据每日自动化监控更新，不是两年前的静态列表
- ✅ **信用卡透明** — 清晰标注哪些提供商需要信用卡、手机验证，哪些完全无需
- ✅ **一键配置** — 即用代码片段覆盖 Claude Code、Cursor、Codex、Aider 等 10+ 工具
- ✅ **并排对比** — 即时对比各提供商的上下文窗口、速率限制和多模态能力

---

## 三步上手

1. **选一个提供商** — 看下方 [Provider Directory](#provider-directory)。推荐从 **Groq** 开始（免信用卡，30 RPM 免费）。
2. **获取 API Key** — 点下方 [Quick Reference](#quick-reference--base-urls--api-keys) 里任意一个 [Get Key →] 链接，注册（大多只需邮箱），复制 key。不到 1 分钟。
3. **填入代码** — 复制 base URL + model ID，粘贴到下边的 [Quick Start](#quick-start--use-any-free-api-in-30-seconds) 示例。

配置具体工具？<a href="https://freellm.net/config/#claude-code" target="_blank" rel="noopener">Claude Code</a> · <a href="https://freellm.net/config/#cursor" target="_blank" rel="noopener">Cursor</a> · <a href="https://freellm.net/config/#codex" target="_blank" rel="noopener">Codex</a> · <a href="https://freellm.net/config/#openhuman" target="_blank" rel="noopener">OpenHuman</a> · <a href="https://freellm.net/config/#opencode" target="_blank" rel="noopener">OpenCode</a> · <a href="https://freellm.net/config/#openclaw" target="_blank" rel="noopener">OpenClaw</a> — 一键配置在 <a href="https://freellm.net/config/" target="_blank" rel="noopener">freellm.net/config/</a>。



## 快速上手 — 30 秒接入免费 API

**没用过 API？** 最简单的方式：打开 <a href="https://console.groq.com/keys" target="_blank" rel="noopener">console.groq.com/keys</a>，用邮箱注册（无需信用卡），复制免费 key，粘贴到下面任意示例。不到一分钟就能跑起来。

以下所有提供商都暴露了 **OpenAI 兼容接口**。任何接受 `baseURL` + `apiKey` 的工具都能直接用 — 替换 base URL 和 key 即可。

### Python (OpenAI SDK)

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",  # 免费，无需信用卡
    api_key="GROQ_API_KEY",                     # 获取: console.groq.com/keys
)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",            # 模型列表见下方 Best Models 表
    messages=[{"role": "user", "content": "你好！"}],
)
print(response.choices[0].message.content)
# Groq 免费额度: 30 RPM, 14,400 RPD — 个人使用绰绰有余
```

### Codex CLI

```bash
export OPENAI_BASE_URL="https://api.groq.com/openai/v1"
export OPENAI_API_KEY="your-groq-key"          # 获取: console.groq.com/keys
codex --model "llama-3.3-70b-versatile"
```

### Cursor

```
Settings → Models → Add Model
  Model name: llama-3.3-70b-versatile
  Base URL: https://api.groq.com/openai/v1
  API key: your-groq-key                       # 获取: console.groq.com/keys
```

### Claude Code

```bash
# Claude Code 需要 Anthropic 兼容接口 — 使用 OpenRouter
export ANTHROPIC_BASE_URL="https://openrouter.ai/api"
export ANTHROPIC_AUTH_TOKEN="sk-or-v1-your-key"  # openrouter.ai/keys
export ANTHROPIC_API_KEY=""                       # 必须为空
# 注意: OpenRouter 的 Anthropic 模型需充值 $10（一次性）
```

### 其他工具？

大多数 AI 开发工具都接受自定义 API 端点 — 拿到免费 key 后：

- **Claude Code** — 设 `ANTHROPIC_BASE_URL` + `ANTHROPIC_AUTH_TOKEN`。<a href="https://freellm.net/config/#claude-code" target="_blank" rel="noopener">详细配置 →</a>
- **Cursor** — Settings → Models → Add Model。<a href="https://freellm.net/config/#cursor" target="_blank" rel="noopener">详细配置 →</a>
- **Codex CLI** — 设 `OPENAI_BASE_URL` + `OPENAI_API_KEY`。<a href="https://freellm.net/config/#codex" target="_blank" rel="noopener">详细配置 →</a>
- **OpenHuman** — 编辑 `config.toml`。<a href="https://freellm.net/config/#openhuman" target="_blank" rel="noopener">详细配置 →</a>
- **Aider** — 编辑 `.aider.conf.yml`。<a href="https://freellm.net/config/#aider" target="_blank" rel="noopener">详细配置 →</a>
- **Cline**（VS Code）— API provider 设置。<a href="https://freellm.net/config/#cline" target="_blank" rel="noopener">详细配置 →</a>
- **Open WebUI** — Settings → Connections。<a href="https://freellm.net/config/#open-webui" target="_blank" rel="noopener">详细配置 →</a>

更多即用配置在 **<a href="https://freellm.net/config/" target="_blank" rel="noopener">freellm.net/config/</a>**。

> **所有提供商的 Base URL 和 API Key 链接** 见下方 [Quick Reference](#quick-reference--base-urls--api-keys)。


---

## 提供商目录 & 热门免费模型

<!-- BEGIN_PERMANENT_FREE -->
| Provider | Free Models | Credit Card? | Max Context | Modalities | Get API Key |
|---|---|---|---|---|---|
| NVIDIA NIM | 17 | Phone verification | 1M | image, text | <a href="https://build.nvidia.com/settings/api-keys" target="_blank" rel="noopener">→</a> |
| GitHub Models | 10 | No | 1M | text | <a href="https://github.com/marketplace/models" target="_blank" rel="noopener">→</a> |
| Cloudflare Workers AI | 8 | No | 10M | image, text | <a href="https://dash.cloudflare.com/profile/api-tokens" target="_blank" rel="noopener">→</a> |
| Groq | 8 | No | 262K | text | <a href="https://console.groq.com/keys" target="_blank" rel="noopener">→</a> |
| Mistral AI | 6 | No | 256K | code, image, text | <a href="https://console.mistral.ai/api-keys" target="_blank" rel="noopener">→</a> |
| Cerebras | 6 | No | 131K | text | <a href="https://cloud.cerebras.ai/" target="_blank" rel="noopener">→</a> |
| Ollama Cloud | 6 | Registration | 262K | code, text | <a href="https://ollama.com/settings/keys" target="_blank" rel="noopener">→</a> |
| Alibaba Cloud Model Studio | 5 | Registration | 1M | code, image, text | <a href="https://bailian.console.alibabacloud.com/?apiKey=1" target="_blank" rel="noopener">→</a> |
| Cohere | 5 | No | 256K | text | <a href="https://dashboard.cohere.com/api-keys" target="_blank" rel="noopener">→</a> |
| Hugging Face | 5 | No | 131K | text | <a href="https://huggingface.co/settings/tokens" target="_blank" rel="noopener">→</a> |
| Kilo Code | 5 | No | 262K | code, text | <a href="https://kilo.ai" target="_blank" rel="noopener">→</a> |
| LLM7.io | 5 | No | 131K | code, text | <a href="https://token.llm7.io" target="_blank" rel="noopener">→</a> |
| Google Gemini | 4 | No | 2M | text | <a href="https://aistudio.google.com/app/apikey" target="_blank" rel="noopener">→</a> |
| OVHcloud AI Endpoints | 4 | Registration | 128K | image, text | <a href="https://endpoints.ai.cloud.ovh.net/" target="_blank" rel="noopener">→</a> |
| Aion Labs | 3 | Registration | 131K | text | <a href="https://www.aionlabs.ai" target="_blank" rel="noopener">→</a> |
| xAI | 3 | Registration | 2M | text | <a href="https://console.x.ai" target="_blank" rel="noopener">→</a> |
| Z AI (Zhipu AI) | 3 | No | 200K | text | <a href="https://open.bigmodel.cn/usercenter/apikeys" target="_blank" rel="noopener">→</a> |
| ModelScope | 3 | Registration | 131K | text | <a href="https://modelscope.cn/my/myaccesstoken" target="_blank" rel="noopener">→</a> |
| Nscale | 3 | Registration | 256K | code, text | <a href="https://console.nscale.com/" target="_blank" rel="noopener">→</a> |
| SiliconFlow | 3 | Registration | 131K | text | <a href="https://cloud.siliconflow.cn/account/ak" target="_blank" rel="noopener">→</a> |
| AI21 Labs | 2 | Registration | 256K | text | <a href="https://studio.ai21.com/account/api-key" target="_blank" rel="noopener">→</a> |
| DeepSeek | 2 | Registration | 128K | text | <a href="https://platform.deepseek.com/api_keys" target="_blank" rel="noopener">→</a> |
| Nebius | 2 | Registration | 128K | text | <a href="https://studio.nebius.com/settings/api-keys" target="_blank" rel="noopener">→</a> |
<!-- END_PERMANENT_FREE -->

<!-- BEGIN_RENEWABLE -->
| Provider | Free Models | Credit Model | Max Context | Modalities | Get API Key |
|---|---|---|---|---|---|
| OpenRouter | 26 | Free tier + $10 topup → 1K RPD | 1M | audio, code, embeddings, image, reasoning, text | <a href="https://openrouter.ai/workspaces/default/keys" target="_blank" rel="noopener">→</a> |
<!-- END_RENEWABLE -->

## 快速参考 — Base URL 与 API Key

<!-- BEGIN_QUICK_REF -->
| Provider | Base URL | Get API Key | Credit Card? |
|---|---|---|---|
| OpenRouter | `https://openrouter.ai/api/v1` | <a href="https://openrouter.ai/workspaces/default/keys" target="_blank" rel="noopener">Get Key →</a> | Registration |
| NVIDIA NIM | `https://integrate.api.nvidia.com/v1` | <a href="https://build.nvidia.com/settings/api-keys" target="_blank" rel="noopener">Get Key →</a> | Phone verification |
| GitHub Models | `https://models.github.ai/inference` | <a href="https://github.com/marketplace/models" target="_blank" rel="noopener">Get Key →</a> | No |
| Cloudflare Workers AI | `https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run` | <a href="https://dash.cloudflare.com/profile/api-tokens" target="_blank" rel="noopener">Get Key →</a> | No |
| Groq | `https://api.groq.com/openai/v1` | <a href="https://console.groq.com/keys" target="_blank" rel="noopener">Get Key →</a> | No |
| Mistral AI | `https://api.mistral.ai/v1` | <a href="https://console.mistral.ai/api-keys" target="_blank" rel="noopener">Get Key →</a> | No |
| Cerebras | `https://api.cerebras.ai/v1` | <a href="https://cloud.cerebras.ai/" target="_blank" rel="noopener">Get Key →</a> | No |
| Ollama Cloud | `https://api.ollama.com` | <a href="https://ollama.com/settings/keys" target="_blank" rel="noopener">Get Key →</a> | Registration |
| Alibaba Cloud Model Studio | `https://dashscope-intl.aliyuncs.com/compatible-mode/v1` | <a href="https://bailian.console.alibabacloud.com/?apiKey=1" target="_blank" rel="noopener">Get Key →</a> | Registration |
| Cohere | `https://api.cohere.com/v2` | <a href="https://dashboard.cohere.com/api-keys" target="_blank" rel="noopener">Get Key →</a> | No |
| Hugging Face | `https://router.huggingface.co/v1` | <a href="https://huggingface.co/settings/tokens" target="_blank" rel="noopener">Get Key →</a> | No |
| Kilo Code | `https://api.kilo.ai/api/gateway` | <a href="https://kilo.ai" target="_blank" rel="noopener">Get Key →</a> | No |
| LLM7.io | `https://api.llm7.io/v1` | <a href="https://token.llm7.io" target="_blank" rel="noopener">Get Key →</a> | No |
| Google Gemini | `https://generativelanguage.googleapis.com/v1beta` | <a href="https://aistudio.google.com/app/apikey" target="_blank" rel="noopener">Get Key →</a> | No |
| OVHcloud AI Endpoints | `https://oai.endpoints.kepler.ai.cloud.ovh.net/v1` | <a href="https://endpoints.ai.cloud.ovh.net/" target="_blank" rel="noopener">Get Key →</a> | Registration |
| Aion Labs | `https://api.aionlabs.ai/v1` | <a href="https://www.aionlabs.ai" target="_blank" rel="noopener">Get Key →</a> | Registration |
| xAI | `https://api.x.ai/v1` | <a href="https://console.x.ai" target="_blank" rel="noopener">Get Key →</a> | Registration |
| Z AI (Zhipu AI) | `https://open.bigmodel.cn/api/paas/v4` | <a href="https://open.bigmodel.cn/usercenter/apikeys" target="_blank" rel="noopener">Get Key →</a> | No |
| ModelScope | `https://api-inference.modelscope.cn/v1` | <a href="https://modelscope.cn/my/myaccesstoken" target="_blank" rel="noopener">Get Key →</a> | Registration |
| Nscale | `https://inference.api.nscale.com/v1` | <a href="https://console.nscale.com/" target="_blank" rel="noopener">Get Key →</a> | Registration |
| SiliconFlow | `https://api.siliconflow.cn/v1` | <a href="https://cloud.siliconflow.cn/account/ak" target="_blank" rel="noopener">Get Key →</a> | Registration |
| AI21 Labs | `https://api.ai21.com/studio/v1` | <a href="https://studio.ai21.com/account/api-key" target="_blank" rel="noopener">Get Key →</a> | Registration |
| DeepSeek | `https://api.deepseek.com/v1` | <a href="https://platform.deepseek.com/api_keys" target="_blank" rel="noopener">Get Key →</a> | Registration |
| Nebius | `https://api.studio.nebius.com/v1` | <a href="https://studio.nebius.com/settings/api-keys" target="_blank" rel="noopener">Get Key →</a> | Registration |
<!-- END_QUICK_REF -->

## 各提供商最佳免费模型

<!-- BEGIN_BEST_MODELS -->
| Provider | Best Free Model | Model ID | Max Context | Rate Limit |
|---|---|---|---|---|
| OpenRouter | <a href="https://freellm.net/models/openrouter/openrouter-owl-alpha/" target="_blank" rel="noopener">Owl Alpha</a> | `openrouter/owl-alpha` | 1M | See provider |
|  | <a href="https://freellm.net/models/openrouter/nvidia-nemotron-3-super-120b-a12b/" target="_blank" rel="noopener">NVIDIA: Nemotron 3 Super (free)</a> | `nvidia/nemotron-3-super-120b-a12b:free` | 1M | See provider |
|  | <a href="https://freellm.net/models/openrouter/poolside-laguna-m.1/" target="_blank" rel="noopener">Poolside: Laguna M.1 (free)</a> | `poolside/laguna-m.1:free` | 262K | See provider |
| NVIDIA NIM | <a href="https://freellm.net/models/nvidia-nim/z-ai-glm-5-1/" target="_blank" rel="noopener">z-ai/glm-5.1</a> | `z-ai/glm-5.1` | 202K | Up to 40 RPM |
|  | <a href="https://freellm.net/models/nvidia-nim/qwen-qwen3-5-397b-a17b/" target="_blank" rel="noopener">qwen/qwen3.5-397b-a17b</a> | `qwen/qwen3.5-397b-a17b` | 262K | Up to 40 RPM |
|  | <a href="https://freellm.net/models/nvidia-nim/moonshotai-kimi-k2-6/" target="_blank" rel="noopener">moonshotai/kimi-k2.6</a> | `moonshotai/kimi-k2.6` | 262K | Up to 40 RPM |
| GitHub Models | <a href="https://freellm.net/models/github-models/gpt-5/" target="_blank" rel="noopener">gpt-5</a> | `gpt-5` | 200K | 10 RPM, 50 RPD |
|  | <a href="https://freellm.net/models/github-models/gpt-4-1/" target="_blank" rel="noopener">gpt-4.1</a> | `gpt-4-1` | 1M | 10 RPM, 50 RPD |
|  | <a href="https://freellm.net/models/github-models/gpt-4-1-mini/" target="_blank" rel="noopener">gpt-4.1-mini</a> | `gpt-4-1-mini` | 1M | 15 RPM, 150 RPD |
| Cloudflare Workers AI | <a href="https://freellm.net/models/cloudflare-workers-ai/cf-meta-llama-3-3-70b-instruct-fp8-fast/" target="_blank" rel="noopener">`@cf/meta/llama-3.3-70b-instruct-fp8-fast`</a> | `cf-meta-llama-3-3-70b-instruct-fp8-fast` | 131K | 10K neurons/day (shared) |
|  | <a href="https://freellm.net/models/cloudflare-workers-ai/cf-meta-llama-3-1-8b-instruct-fp8-fast/" target="_blank" rel="noopener">`@cf/meta/llama-3.1-8b-instruct-fp8-fast`</a> | `cf-meta-llama-3-1-8b-instruct-fp8-fast` | 131K | 10K neurons/day (shared) |
|  | <a href="https://freellm.net/models/cloudflare-workers-ai/cf-meta-llama-3-2-11b-vision-instruct/" target="_blank" rel="noopener">`@cf/meta/llama-3.2-11b-vision-instruct`</a> | `cf-meta-llama-3-2-11b-vision-instruct` | 131K | 10K neurons/day (shared) |
| Groq | <a href="https://freellm.net/models/groq/llama-3-3-70b-versatile/" target="_blank" rel="noopener">llama-3.3-70b-versatile</a> | `llama-3-3-70b-versatile` | 131K | 30 RPM, 14,400 RPD |
|  | <a href="https://freellm.net/models/groq/llama-3-1-8b-instant/" target="_blank" rel="noopener">llama-3.1-8b-instant</a> | `llama-3-1-8b-instant` | 131K | 30 RPM, 14,400 RPD |
|  | <a href="https://freellm.net/models/groq/llama-4-maverick-17b-128e-instruct/" target="_blank" rel="noopener">llama-4-maverick-17b-128e-instruct</a> | `llama-4-maverick-17b-128e-instruct` | 131K | 15 RPM, 500 RPD |
| Mistral AI | <a href="https://freellm.net/models/mistral-ai/mistral-small-4/" target="_blank" rel="noopener">Mistral Small 4</a> | `mistral-small-4` | 256K | ~1 RPS, 500K TPM |
|  | <a href="https://freellm.net/models/mistral-ai/mistral-medium-3/" target="_blank" rel="noopener">Mistral Medium 3</a> | `mistral-medium-3` | 128K | ~1 RPS, 500K TPM |
|  | <a href="https://freellm.net/models/mistral-ai/mistral-large-3/" target="_blank" rel="noopener">Mistral Large 3</a> | `mistral-large-3` | 256K | ~1 RPS, 500K TPM |
| Cerebras | <a href="https://freellm.net/models/cerebras/llama-3-3-70b/" target="_blank" rel="noopener">llama-3.3-70b</a> | `llama-3-3-70b` | 128K | 30 RPM, 14,400 RPD, 1M .. |
|  | <a href="https://freellm.net/models/cerebras/gpt-oss-120b/" target="_blank" rel="noopener">gpt-oss-120b</a> | `gpt-oss-120b` | 128K | 30 RPM, 14,400 RPD, 1M .. |
|  | <a href="https://freellm.net/models/cerebras/qwen-3-235b-a22b-instruct-2507/" target="_blank" rel="noopener">qwen-3-235b-a22b-instruct-2507</a> | `qwen-3-235b-a22b-instruct-2507` | 131K | 30 RPM, 14,400 RPD, 1M .. |
| Ollama Cloud | <a href="https://freellm.net/models/ollama-cloud/gpt-oss-120b-cloud/" target="_blank" rel="noopener">`gpt-oss:120b-cloud`</a> | `gpt-oss-120b-cloud` | 128K | Session/weekly limits (.. |
|  | <a href="https://freellm.net/models/ollama-cloud/deepseek-v3-1-671b-cloud/" target="_blank" rel="noopener">`deepseek-v3.1:671b-cloud`</a> | `deepseek-v3-1-671b-cloud` | 128K | Session/weekly limits (.. |
|  | <a href="https://freellm.net/models/ollama-cloud/qwen3-coder-480b-cloud/" target="_blank" rel="noopener">`qwen3-coder:480b-cloud`</a> | `qwen3-coder-480b-cloud` | 128K | Session/weekly limits (.. |
| Alibaba Cloud Model Studio | <a href="https://freellm.net/models/alibaba-cloud-model-studio/qwen3-max/" target="_blank" rel="noopener">Qwen3-Max</a> | `qwen3-max` | 128K | Tiered by region |
|  | <a href="https://freellm.net/models/alibaba-cloud-model-studio/qwen3-plus/" target="_blank" rel="noopener">Qwen3-Plus</a> | `qwen3-plus` | 1M | Tiered by region |
|  | <a href="https://freellm.net/models/alibaba-cloud-model-studio/qwen3-vl-plus/" target="_blank" rel="noopener">Qwen3-VL-Plus</a> | `qwen3-vl-plus` | 128K | Tiered by region |
| Cohere | <a href="https://freellm.net/models/cohere/command-a-111b/" target="_blank" rel="noopener">Command A (111B)</a> | `command-a-111b` | 256K | 20 RPM |
|  | <a href="https://freellm.net/models/cohere/command-r/" target="_blank" rel="noopener">Command R+</a> | `command-r` | 128K | 20 RPM |
|  | <a href="https://freellm.net/models/cohere/command-r7b/" target="_blank" rel="noopener">Command R7B</a> | `command-r7b` | 128K | 20 RPM |
| Hugging Face | <a href="https://freellm.net/models/hugging-face/meta-llama-3-1-8b-instruct/" target="_blank" rel="noopener">Meta-Llama-3.1-8B-Instruct</a> | `meta-llama-3-1-8b-instruct` | 128K | Credit-metered |
|  | <a href="https://freellm.net/models/hugging-face/mistral-7b-instruct-v0-3/" target="_blank" rel="noopener">Mistral-7B-Instruct-v0.3</a> | `mistral-7b-instruct-v0-3` | 32K | Credit-metered |
|  | <a href="https://freellm.net/models/hugging-face/mixtral-8x7b-instruct-v0-1/" target="_blank" rel="noopener">Mixtral-8x7B-Instruct-v0.1</a> | `mixtral-8x7b-instruct-v0-1` | 32K | Credit-metered |
| Kilo Code | <a href="https://freellm.net/models/kilo-code/x-ai-grok-code-fast-1-free/" target="_blank" rel="noopener">`x-ai/grok-code-fast-1:free`</a> | `x-ai-grok-code-fast-1-free` | 256K | ~200 req/hr |
|  | <a href="https://freellm.net/models/kilo-code/minimax-minimax-m2-5-free/" target="_blank" rel="noopener">`minimax/minimax-m2.5:free`</a> | `minimax-minimax-m2-5-free` | 196K | ~200 req/hr |
|  | <a href="https://freellm.net/models/kilo-code/bytedance-seed-dola-seed-2-0-pro-free/" target="_blank" rel="noopener">`bytedance-seed/dola-seed-2.0-pro:free`</a> | `bytedance-seed-dola-seed-2-0-pro-free` | 131K | ~200 req/hr |
| LLM7.io | <a href="https://freellm.net/models/llm7-io/deepseek-r1-0528/" target="_blank" rel="noopener">deepseek-r1-0528</a> | `deepseek-r1-0528` | 131K | 30 RPM (120 with token) |
|  | <a href="https://freellm.net/models/llm7-io/deepseek-v3-0324/" target="_blank" rel="noopener">deepseek-v3-0324</a> | `deepseek-v3-0324` | 131K | 30 RPM (120 with token) |
|  | <a href="https://freellm.net/models/llm7-io/gpt-4o-mini/" target="_blank" rel="noopener">gpt-4o-mini</a> | `gpt-4o-mini` | 131K | 30 RPM (120 with token) |
| Google Gemini | <a href="https://freellm.net/models/google-gemini/gemini-2-5-pro/" target="_blank" rel="noopener">Gemini 2.5 Pro</a> | `gemini-2-5-pro` | 2M | 5 RPM, 100 RPD |
|  | <a href="https://freellm.net/models/google-gemini/gemini-2-5-flash/" target="_blank" rel="noopener">Gemini 2.5 Flash</a> | `gemini-2-5-flash` | 1M | 10 RPM, 250 RPD |
|  | <a href="https://freellm.net/models/google-gemini/gemini-2-5-flash-lite/" target="_blank" rel="noopener">Gemini 2.5 Flash-Lite</a> | `gemini-2-5-flash-lite` | 1M | 15 RPM, 1,000 RPD |
| OVHcloud AI Endpoints | <a href="https://freellm.net/models/ovhcloud-ai-endpoints/qwen2-5-vl-72b-instruct/" target="_blank" rel="noopener">Qwen2.5-VL-72B-Instruct</a> | `qwen2-5-vl-72b-instruct` | 128K | 2 RPM (anonymous) |
|  | <a href="https://freellm.net/models/ovhcloud-ai-endpoints/mistral-nemo-instruct-2407/" target="_blank" rel="noopener">Mistral-Nemo-Instruct-2407</a> | `mistral-nemo-instruct-2407` | 128K | 2 RPM (anonymous) |
|  | <a href="https://freellm.net/models/ovhcloud-ai-endpoints/qwen3guard-gen-8b/" target="_blank" rel="noopener">Qwen3Guard-Gen-8B</a> | `qwen3guard-gen-8b` | 32K | 2 RPM (anonymous) |
| Aion Labs | <a href="https://freellm.net/models/aion-labs/aion-2-0/" target="_blank" rel="noopener">aion-2.0</a> | `aion-2-0` | 131K | Daily token allowance |
|  | <a href="https://freellm.net/models/aion-labs/aion-1-0/" target="_blank" rel="noopener">aion-1.0</a> | `aion-1-0` | 131K | Daily token allowance |
|  | <a href="https://freellm.net/models/aion-labs/aion-1-0-mini/" target="_blank" rel="noopener">aion-1.0-mini</a> | `aion-1-0-mini` | 131K | Daily token allowance |
| xAI | <a href="https://freellm.net/models/xai/grok-4-3/" target="_blank" rel="noopener">grok-4.3</a> | `grok-4-3` | 1M | Credit-based |
|  | <a href="https://freellm.net/models/xai/grok-4-1-fast/" target="_blank" rel="noopener">grok-4.1-fast</a> | `grok-4-1-fast` | 2M | Credit-based |
|  | <a href="https://freellm.net/models/xai/grok-3-mini/" target="_blank" rel="noopener">grok-3-mini</a> | `grok-3-mini` | 131K | Credit-based |
| Z AI (Zhipu AI) | <a href="https://freellm.net/models/z-ai-zhipu-ai/glm-4-7-flash/" target="_blank" rel="noopener">GLM-4.7-Flash</a> | `glm-4-7-flash` | 200K | 1 concurrent request |
|  | <a href="https://freellm.net/models/z-ai-zhipu-ai/glm-4-5-flash/" target="_blank" rel="noopener">GLM-4.5-Flash</a> | `glm-4-5-flash` | 128K | 1 concurrent request |
|  | <a href="https://freellm.net/models/z-ai-zhipu-ai/glm-4-6v-flash/" target="_blank" rel="noopener">GLM-4.6V-Flash</a> | `glm-4-6v-flash` | 128K | 1 concurrent request |
| ModelScope | <a href="https://freellm.net/models/modelscope/qwen-qwen3-5-35b-a3b/" target="_blank" rel="noopener">`Qwen/Qwen3.5-35B-A3B`</a> | `qwen-qwen3-5-35b-a3b` | 131K | 2,000 RPD total; <=500 .. |
|  | <a href="https://freellm.net/models/modelscope/qwen-qwen3-5-27b/" target="_blank" rel="noopener">`Qwen/Qwen3.5-27B`</a> | `qwen-qwen3-5-27b` | 131K | 2,000 RPD total; <=500 .. |
|  | <a href="https://freellm.net/models/modelscope/qwen-qwen-image/" target="_blank" rel="noopener">`Qwen/Qwen-Image`</a> | `qwen-qwen-image` | 131K | 2,000 RPD total; model/.. |
| Nscale | <a href="https://freellm.net/models/nscale/llama-3-3-70b-instruct/" target="_blank" rel="noopener">Llama-3.3-70B-Instruct</a> | `llama-3-3-70b-instruct` | 128K | Fair-use |
|  | <a href="https://freellm.net/models/nscale/qwen3-coder-30b-a3b-instruct/" target="_blank" rel="noopener">Qwen3-Coder-30B-A3B-Instruct</a> | `qwen3-coder-30b-a3b-instruct` | 256K | Fair-use |
|  | <a href="https://freellm.net/models/nscale/deepseek-r1-distill-llama-70b/" target="_blank" rel="noopener">DeepSeek-R1-Distill-Llama-70B</a> | `deepseek-r1-distill-llama-70b` | 128K | Fair-use |
| SiliconFlow | <a href="https://freellm.net/models/siliconflow/deepseek-ai-deepseek-r1-distill-qwen-7b/" target="_blank" rel="noopener">`deepseek-ai/DeepSeek-R1-Distill-Qwen-7B`</a> | `deepseek-ai-deepseek-r1-distill-qwen-7b` | 131K | 30 RPM, 60K TPM |
|  | <a href="https://freellm.net/models/siliconflow/deepseek-ai-deepseek-ocr/" target="_blank" rel="noopener">`deepseek-ai/DeepSeek-OCR`</a> | `deepseek-ai-deepseek-ocr` | 131K | 30 RPM, 60K TPM |
|  | <a href="https://freellm.net/models/siliconflow/abbreviation/" target="_blank" rel="noopener">Abbreviation</a> | `abbreviation` | 131K | See provider |
| AI21 Labs | <a href="https://freellm.net/models/ai21-labs/jamba-large-1-7/" target="_blank" rel="noopener">Jamba Large 1.7</a> | `jamba-large-1-7` | 256K | 200 RPM, 10 RPS |
|  | <a href="https://freellm.net/models/ai21-labs/jamba-mini-2/" target="_blank" rel="noopener">Jamba Mini 2</a> | `jamba-mini-2` | 256K | 200 RPM, 10 RPS |
| DeepSeek | <a href="https://freellm.net/models/deepseek/deepseek-chat-v3-2/" target="_blank" rel="noopener">deepseek-chat (V3.2)</a> | `deepseek-chat-v3-2` | 128K | Dynamic |
|  | <a href="https://freellm.net/models/deepseek/deepseek-reasoner-r1/" target="_blank" rel="noopener">deepseek-reasoner (R1)</a> | `deepseek-reasoner-r1` | 128K | Dynamic |
| Nebius | <a href="https://freellm.net/models/nebius/meta-llama-3-3-70b-instruct/" target="_blank" rel="noopener">Meta-Llama-3.3-70B-Instruct</a> | `meta-llama-3-3-70b-instruct` | 128K | Tier-based |
|  | <a href="https://freellm.net/models/nebius/qwen3-235b-a22b/" target="_blank" rel="noopener">Qwen3-235B-A22B</a> | `qwen3-235b-a22b` | 128K | Tier-based |
<!-- END_BEST_MODELS -->



### 热门免费模型

<!-- BEGIN_TOP_MODELS -->
| Model | Provider | Context | Weekly Usage |
|---|---|---|---|
| <a href="https://freellm.net/models/openrouter/openrouter-owl-alpha/" target="_blank" rel="noopener">Owl Alpha</a> | OpenRouter | 1M | 1700B tokens |
| <a href="https://freellm.net/models/openrouter/nvidia-nemotron-3-super-120b-a12b/" target="_blank" rel="noopener">NVIDIA: Nemotron 3 Super (free)</a> | OpenRouter | 1M | 687B tokens |
| <a href="https://freellm.net/models/openrouter/poolside-laguna-m.1/" target="_blank" rel="noopener">Poolside: Laguna M.1 (free)</a> | OpenRouter | 262K | 540B tokens |
| <a href="https://freellm.net/models/openrouter/openai-gpt-oss-120b/" target="_blank" rel="noopener">OpenAI: gpt-oss-120b (free)</a> | OpenRouter | 131K | 211B tokens |
| <a href="https://freellm.net/models/nvidia-nim/z-ai-glm-5-1/" target="_blank" rel="noopener">z-ai/glm-5.1</a> | NVIDIA NIM | 202K | 138B tokens |
| <a href="https://freellm.net/models/openrouter/z-ai-glm-4.5-air/" target="_blank" rel="noopener">Z.ai: GLM 4.5 Air (free)</a> | OpenRouter | 131K | 99B tokens |
| <a href="https://freellm.net/models/openrouter/poolside-laguna-xs.2/" target="_blank" rel="noopener">Poolside: Laguna XS.2 (free)</a> | OpenRouter | 262K | 91B tokens |
| <a href="https://freellm.net/models/nvidia-nim/qwen-qwen3-5-397b-a17b/" target="_blank" rel="noopener">qwen/qwen3.5-397b-a17b</a> | NVIDIA NIM | 262K | 45B tokens |
| <a href="https://freellm.net/models/openrouter/openai-gpt-oss-20b/" target="_blank" rel="noopener">OpenAI: gpt-oss-20b (free)</a> | OpenRouter | 131K | 42B tokens |
| <a href="https://freellm.net/models/openrouter/nvidia-nemotron-3-nano-30b-a3b/" target="_blank" rel="noopener">NVIDIA: Nemotron 3 Nano 30B A3B (free)</a> | OpenRouter | 256K | 36B tokens |
<!-- END_TOP_MODELS -->

---

## 参与贡献

欢迎贡献！

- **补充缺失的免费模型** — 提交 <a href="https://github.com/open-free-llm-api/awesome-free-llm-apis/issues" target="_blank" rel="noopener">issue</a> 或 PR
- **修正不准确的数据** — 速率限制会变、提供商会升级，欢迎 PR
- **添加配置代码片段** — 有你常用工具的配置方案？添加到 `code-examples/`

### 收录标准

模型列入本列表需满足：
1. 提供商明确提供**免费层**（不仅仅是试用额度）
2. API **公开可访问**（无需候补、封闭内测、或逆向工程）
3. 试用额度：明确标注且最低 $1 额度

---

## 链接

- 🌐 **在线网站**: <a href="https://freellm.net" target="_blank" rel="noopener">freellm.net</a> — 搜索、对比、在线体验、配置生成器
- 🔑 **API 密钥目录**: <a href="https://freellm.net/free-llm-api-keys/" target="_blank" rel="noopener">freellm.net/free-llm-api-keys/</a>
- ⚙️ **配置生成器**: <a href="https://freellm.net/config/" target="_blank" rel="noopener">freellm.net/config/</a>
- 🎮 **在线体验**: <a href="https://freellm.net/playground/" target="_blank" rel="noopener">freellm.net/playground/</a>
- 📊 **模型对比**: <a href="https://freellm.net/compare/" target="_blank" rel="noopener">freellm.net/compare/</a>

## 许可证

MIT © <a href="https://github.com/open-free-llm-api" target="_blank" rel="noopener">open-free-llm-api</a>

---

<p align="center">
  <sub>数据每日自动更新 · 最后更新: <!-- AUTO_LAST_UPDATED -->
2026-06-01
<!-- END_AUTO_LAST_UPDATED --></sub>
</p>
