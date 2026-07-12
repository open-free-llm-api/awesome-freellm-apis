<p align="center">
  <h1 align="center">awesome-free-llm-apis</h1>
  <!-- AUTO_STATS -->
  <p align="center"><strong>30개 제공업체, 377+개의 무료 LLM API</strong> — 무료 모델을 검색, 비교, 설정하세요.</p>
<!-- END_AUTO_STATS -->
</p>

<p align="center">
  <a href="https://freellm.net" target="_blank" rel="noopener"><strong>🌐 freellm.net 방문</strong></a> —
  <a href="https://freellm.net/models/" target="_blank" rel="noopener">모델 찾기</a> ·
  <a href="https://freellm.net/playground/" target="_blank" rel="noopener">플레이그라운드</a> ·
  <a href="https://freellm.net/config/" target="_blank" rel="noopener">설정 생성</a> ·
  <a href="https://freellm.net/free-llm-api-keys/" target="_blank" rel="noopener">API 키</a>
</p>

<p align="center">
  <img alt="Provider Logos" src="assets/provider-logos-marquee.svg" width="100%" />
</p>

  <!-- AUTO_UPDATE_BADGE -->
  <p align="center"><strong>🔄 <a href="https://freellm.net" target="_blank" rel="noopener">freellm.net</a>에서 매일 자동 업데이트</strong> — 마지막 업데이트: 2026-07-12</p>
<!-- END_AUTO_UPDATE_BADGE -->

<p align="center">
  🌐 <a href="README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a>
</p>

---

## 이 프로젝트가 필요한 이유

무료 LLM API를 찾기 위해 여러 GitHub README를 뒤지고, 여러 플랫폼에 가입하고, 어떤 모델이 아직 무료 티어를 제공하는지 추측해서는 안 됩니다.

이 저장소는 **구조화된 기계 판독 가능 무료 LLM API 디렉토리**입니다 — 속도 제한, 컨텍스트 윈도우, 원클릭 설정 스니펫, API 키 링크를 매일 업데이트합니다.

**이 저장소 + <a href="https://freellm.net" target="_blank" rel="noopener">freellm.net</a>을 선택하는 이유:**

- ✅ **항상 최신** — 매일 자동 모니터링으로 업데이트, 2년 된 정적 목록이 아닙니다
- ✅ **신용카드 투명성** — 신용카드 필요, 전화 인증 필요, 완전 무료 제공업체를 명확히 표시
- ✅ **원클릭 설정** — Claude Code, Cursor, Codex, Aider 등 10개 이상 도구 지원
- ✅ **나란히 비교** — 컨텍스트 윈도우, 속도 제한, 멀티모달 지원을 즉시 비교

---

## 3단계로 시작하기

1. **제공업체 선택** — 아래 [Provider Directory](#provider-directory)를 보세요. **Groq**부터 시작하는 것을 추천（신용카드 불필요, 30 RPM 무료).
2. **API 키 발급** — 아래 [Quick Reference](#quick-reference--base-urls--api-keys)의 [Get Key →] 링크를 클릭해서 가입（대부분 이메일만 필요), 키를 복사. 1분도 안 걸립니다.
3. **코드에 붙여넣기** — base URL + model ID를 복사해서 아래 [빠른 시작](#빠른-시작--30초-만에-무료-api-사용하기) 예제에 붙여넣으세요.

도구 설정이 필요하세요? <a href="https://freellm.net/config/#claude-code" target="_blank" rel="noopener">Claude Code</a> · <a href="https://freellm.net/config/#cursor" target="_blank" rel="noopener">Cursor</a> · <a href="https://freellm.net/config/#codex" target="_blank" rel="noopener">Codex</a> · <a href="https://freellm.net/config/#openhuman" target="_blank" rel="noopener">OpenHuman</a> · <a href="https://freellm.net/config/#opencode" target="_blank" rel="noopener">OpenCode</a> · <a href="https://freellm.net/config/#openclaw" target="_blank" rel="noopener">OpenClaw</a> — <a href="https://freellm.net/config/" target="_blank" rel="noopener">freellm.net/config/</a>에서 원클릭 설정.



## 빠른 시작 — 30초 만에 무료 API 사용하기

**API를 처음 써보세요?** 가장 간단한 방법: <a href="https://console.groq.com/keys" target="_blank" rel="noopener">console.groq.com/keys</a>에 접속, 이메일만으로 가입（신용카드 불필요), 무료 키를 복사해서 아래 예제에 붙여넣으세요. 1분도 안 걸려 실행할 수 있습니다.

아래 모든 제공업체는 **OpenAI 호환 엔드포인트**를 제공합니다. `baseURL` + `apiKey`를 지원하는 모든 도구에서 작동합니다 — base URL과 키만 바꾸면 됩니다.

### Python (OpenAI SDK)

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",  # 무료, 신용카드 불필요
    api_key="GROQ_API_KEY",                     # 발급: console.groq.com/keys
)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",            # 모델 목록은 아래 Best Models 표 참조
    messages=[{"role": "user", "content": "안녕하세요!"}],
)
print(response.choices[0].message.content)
# Groq 무료 한도: 30 RPM, 14,400 RPD — 개인 사용에 충분
```

### Codex CLI

```bash
export OPENAI_BASE_URL="https://api.groq.com/openai/v1"
export OPENAI_API_KEY="your-groq-key"          # 발급: console.groq.com/keys
codex --model "llama-3.3-70b-versatile"
```

### Cursor

```
Settings → Models → Add Model
  Model name: llama-3.3-70b-versatile
  Base URL: https://api.groq.com/openai/v1
  API key: your-groq-key                       # 발급: console.groq.com/keys
```

### Claude Code

```bash
# Claude Code 는 Anthropic 호환 API 필요 — OpenRouter 사용
export ANTHROPIC_BASE_URL="https://openrouter.ai/api"
export ANTHROPIC_AUTH_TOKEN="sk-or-v1-your-key"  # openrouter.ai/keys
export ANTHROPIC_API_KEY=""                       # 빈 값 필수
# 참고: OpenRouter Anthropic 모델은 $10 충전 필요 (1회)
```

### 다른 도구 사용하기

대부분의 AI 개발 도구는 커스텀 API 엔드포인트를 지원합니다. 무료 키를 받은 후:

- **Claude Code** — `ANTHROPIC_BASE_URL` + `ANTHROPIC_AUTH_TOKEN` 설정.<a href="https://freellm.net/config/#claude-code" target="_blank" rel="noopener">단계별 가이드 →</a>
- **Cursor** — Settings → Models → Add Model.<a href="https://freellm.net/config/#cursor" target="_blank" rel="noopener">단계별 가이드 →</a>
- **Codex CLI** — `OPENAI_BASE_URL` + `OPENAI_API_KEY` 설정.<a href="https://freellm.net/config/#codex" target="_blank" rel="noopener">단계별 가이드 →</a>
- **OpenHuman** — `config.toml` 편집.<a href="https://freellm.net/config/#openhuman" target="_blank" rel="noopener">단계별 가이드 →</a>
- **Aider** — `.aider.conf.yml` 편집.<a href="https://freellm.net/config/#aider" target="_blank" rel="noopener">단계별 가이드 →</a>
- **Cline**（VS Code）— API provider 설정.<a href="https://freellm.net/config/#cline" target="_blank" rel="noopener">단계별 가이드 →</a>
- **Open WebUI** — Settings → Connections.<a href="https://freellm.net/config/#open-webui" target="_blank" rel="noopener">단계별 가이드 →</a>

더 많은 즉시 사용 가능한 설정은 **<a href="https://freellm.net/config/" target="_blank" rel="noopener">freellm.net/config/</a>** 에서.

> **모든 제공업체의 Base URL 및 API 키 링크**는 아래 [Quick Reference](#quick-reference--base-urls--api-keys) 참조.


---

## 제공업체 디렉토리 & 인기 무료 모델

<!-- BEGIN_PERMANENT_FREE -->
| Provider | Free Models | Credit Card? | Max Context | Modalities | Get API Key |
|---|---|---|---|---|---|
| NVIDIA NIM | 115 | Phone verification | 1M | audio, embedding, image, reasoning, rerank, text, video, vision | <a href="https://build.nvidia.com/settings/api-keys" target="_blank" rel="noopener">→</a> |
| ModelScope | 54 | Registration | 1M | audio, image, reasoning, text, video, vision | <a href="https://modelscope.cn/my/myaccesstoken" target="_blank" rel="noopener">→</a> |
| Cloudflare Workers AI | 39 | No | 10M | code, image, reasoning, text, video | <a href="https://dash.cloudflare.com/profile/api-tokens" target="_blank" rel="noopener">→</a> |
| GitHub Models | 13 | No | 1M | audio, image, pdf, reasoning, text | <a href="https://github.com/marketplace/models" target="_blank" rel="noopener">→</a> |
| Google Gemini | 12 | No | 1M | audio, image, pdf, reasoning, text, video, vision | <a href="https://aistudio.google.com/app/apikey" target="_blank" rel="noopener">→</a> |
| OVHcloud AI Endpoints | 12 | Registration | 262K | audio, code, image, reasoning, text, video | <a href="https://www.ovhcloud.com/en/public-cloud/ai-endpoints/catalog/" target="_blank" rel="noopener">→</a> |
| Groq | 10 | No | 262K | text | <a href="https://console.groq.com/keys" target="_blank" rel="noopener">→</a> |
| Mistral AI | 9 | No | 256K | code, image, text | <a href="https://console.mistral.ai/api-keys" target="_blank" rel="noopener">→</a> |
| LLM7.io | 8 | No | 256K | audio, code, image, pdf, reasoning, text, video | <a href="https://token.llm7.io" target="_blank" rel="noopener">→</a> |
| Cerebras | 7 | No | 262K | reasoning, text, vision | <a href="https://cloud.cerebras.ai/" target="_blank" rel="noopener">→</a> |
| Cohere | 6 | No | 256K | text | <a href="https://dashboard.cohere.com/api-keys" target="_blank" rel="noopener">→</a> |
| Ollama Cloud | 6 | Registration | 262K | code, reasoning, text | <a href="https://ollama.com/settings/keys" target="_blank" rel="noopener">→</a> |
| OpenCode Zen | 6 | Registration | 1M | audio, reasoning, vision | <a href="https://opencode.ai/auth" target="_blank" rel="noopener">→</a> |
| Agnes AI | 5 | Registration | 256K | image, text, video, vision | <a href="https://platform.agnes-ai.com/settings/apiKeys" target="_blank" rel="noopener">→</a> |
| Aion Labs | 5 | Registration | 131K | text | <a href="https://www.aionlabs.ai" target="_blank" rel="noopener">→</a> |
| Hugging Face | 5 | No | 131K | text | <a href="https://huggingface.co/settings/tokens" target="_blank" rel="noopener">→</a> |
| Kilo Code | 5 | No | 262K | code, reasoning, text | <a href="https://kilo.ai" target="_blank" rel="noopener">→</a> |
| Alibaba Cloud Model Studio | 5 | Registration | 1M | code, image, text | <a href="https://bailian.console.alibabacloud.com/?apiKey=1" target="_blank" rel="noopener">→</a> |
| Z AI (Zhipu AI) | 4 | No | 200K | image, reasoning, text, video | <a href="https://open.bigmodel.cn/usercenter/apikeys" target="_blank" rel="noopener">→</a> |
| SambaNova | 4 | Registration | 128K | image, reasoning, text | <a href="https://cloud.sambanova.ai/apis" target="_blank" rel="noopener">→</a> |
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
| OpenRouter | 28 | Free tier + $10 topup → 1K RPD | 1M | audio, code, embeddings, image, reasoning, rerank, text, video, vision | <a href="https://openrouter.ai/workspaces/default/keys" target="_blank" rel="noopener">→</a> |
<!-- END_RENEWABLE -->

## 빠른 참조 — Base URL 및 API 키

<!-- BEGIN_QUICK_REF -->
| Provider | Base URL | Get API Key | Credit Card? |
|---|---|---|---|
| NVIDIA NIM | `https://integrate.api.nvidia.com/v1` | <a href="https://build.nvidia.com/settings/api-keys" target="_blank" rel="noopener">Get Key →</a> | Phone verification |
| ModelScope | `https://api-inference.modelscope.cn/v1` | <a href="https://modelscope.cn/my/myaccesstoken" target="_blank" rel="noopener">Get Key →</a> | Registration |
| Cloudflare Workers AI | `https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run` | <a href="https://dash.cloudflare.com/profile/api-tokens" target="_blank" rel="noopener">Get Key →</a> | No |
| OpenRouter | `https://openrouter.ai/api/v1` | <a href="https://openrouter.ai/workspaces/default/keys" target="_blank" rel="noopener">Get Key →</a> | Registration |
| GitHub Models | `https://models.github.ai/inference` | <a href="https://github.com/marketplace/models" target="_blank" rel="noopener">Get Key →</a> | No |
| Google Gemini | `https://generativelanguage.googleapis.com/v1beta` | <a href="https://aistudio.google.com/app/apikey" target="_blank" rel="noopener">Get Key →</a> | No |
| OVHcloud AI Endpoints | `https://oai.endpoints.kepler.ai.cloud.ovh.net/v1` | <a href="https://www.ovhcloud.com/en/public-cloud/ai-endpoints/catalog/" target="_blank" rel="noopener">Get Key →</a> | Registration |
| Groq | `https://api.groq.com/openai/v1` | <a href="https://console.groq.com/keys" target="_blank" rel="noopener">Get Key →</a> | No |
| Mistral AI | `https://api.mistral.ai/v1` | <a href="https://console.mistral.ai/api-keys" target="_blank" rel="noopener">Get Key →</a> | No |
| LLM7.io | `https://api.llm7.io/v1` | <a href="https://token.llm7.io" target="_blank" rel="noopener">Get Key →</a> | No |
| Cerebras | `https://api.cerebras.ai/v1` | <a href="https://cloud.cerebras.ai/" target="_blank" rel="noopener">Get Key →</a> | No |
| Cohere | `https://api.cohere.com/v2` | <a href="https://dashboard.cohere.com/api-keys" target="_blank" rel="noopener">Get Key →</a> | No |
| Ollama Cloud | `https://api.ollama.com` | <a href="https://ollama.com/settings/keys" target="_blank" rel="noopener">Get Key →</a> | Registration |
| OpenCode Zen | `https://opencode.ai/zen/v1` | <a href="https://opencode.ai/auth" target="_blank" rel="noopener">Get Key →</a> | Registration |
| Agnes AI | `https://apihub.agnes-ai.com/v1` | <a href="https://platform.agnes-ai.com/settings/apiKeys" target="_blank" rel="noopener">Get Key →</a> | Registration |
| Aion Labs | `https://api.aionlabs.ai/v1` | <a href="https://www.aionlabs.ai" target="_blank" rel="noopener">Get Key →</a> | Registration |
| Hugging Face | `https://router.huggingface.co/v1` | <a href="https://huggingface.co/settings/tokens" target="_blank" rel="noopener">Get Key →</a> | No |
| Kilo Code | `https://api.kilo.ai/api/gateway` | <a href="https://kilo.ai" target="_blank" rel="noopener">Get Key →</a> | No |
| Alibaba Cloud Model Studio | `https://dashscope-intl.aliyuncs.com/compatible-mode/v1` | <a href="https://bailian.console.alibabacloud.com/?apiKey=1" target="_blank" rel="noopener">Get Key →</a> | Registration |
| Z AI (Zhipu AI) | `https://open.bigmodel.cn/api/paas/v4` | <a href="https://open.bigmodel.cn/usercenter/apikeys" target="_blank" rel="noopener">Get Key →</a> | No |
| SambaNova | `https://api.sambanova.ai/v1` | <a href="https://cloud.sambanova.ai/apis" target="_blank" rel="noopener">Get Key →</a> | Registration |
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

## 제공업체별 최고의 무료 모델

<!-- BEGIN_BEST_MODELS -->
| Provider | Best Free Model | Model ID | Max Context | Rate Limit |
|---|---|---|---|---|
| NVIDIA NIM | <a href="https://freellm.net/models/nvidia-nim/moonshotai-kimi-k2-6/" target="_blank" rel="noopener">moonshotai/kimi-k2.6</a> | `moonshotai/kimi-k2.6` | 262K | Up to 40 RPM |
|  | <a href="https://freellm.net/models/nvidia-nim/z-ai-glm-5-2/" target="_blank" rel="noopener">z-ai/glm-5.2</a> | `z-ai/glm-5.2` | 1M | Up to 40 RPM |
|  | <a href="https://freellm.net/models/nvidia-nim/z-ai-glm-5-1/" target="_blank" rel="noopener">z-ai/glm-5.1</a> | `z-ai/glm-5.1` | 202K | Up to 40 RPM |
| ModelScope | <a href="https://freellm.net/models/modelscope/minimax-minimax-m2-5/" target="_blank" rel="noopener">MiniMax-M2.5-highspeed</a> | `MiniMax/MiniMax-M2.5` | 204K | See provider |
|  | <a href="https://freellm.net/models/modelscope/qwen-qwen3-5-35b-a3b/" target="_blank" rel="noopener">Qwen/Qwen3.5-35B-A3B</a> | `Qwen/Qwen3.5-35B-A3B` | 131K | 2,000 RPD total; <=500 .. |
|  | <a href="https://freellm.net/models/modelscope/qwen-qwen3-5-27b/" target="_blank" rel="noopener">Qwen/Qwen3.5-27B</a> | `Qwen/Qwen3.5-27B` | 131K | 2,000 RPD total; <=500 .. |
| Cloudflare Workers AI | <a href="https://freellm.net/models/cloudflare-workers-ai/mistral-mistral-7b-instruct-v0-1/" target="_blank" rel="noopener">Mistral 7B</a> | `@cf/mistral/mistral-7b-instruct-v0.1` | 32K | See provider |
|  | <a href="https://freellm.net/models/cloudflare-workers-ai/qwen-qwen1-5-7b-chat/" target="_blank" rel="noopener">Qwen 1.5 7B</a> | `@cf/qwen/qwen1.5-7b-chat` | 32K | See provider |
|  | <a href="https://freellm.net/models/cloudflare-workers-ai/cf-meta-llama-3-3-70b-instruct-fp8-fast/" target="_blank" rel="noopener">@cf/meta/llama-3.3-70b-instruct-fp8-fast</a> | `@cf/meta/llama-3.3-70b-instruct-fp8-fast` | 131K | 10K neurons/day (shared) |
| OpenRouter | <a href="https://freellm.net/models/openrouter/tencent-hy3/" target="_blank" rel="noopener">Tencent: Hy3 (free)</a> | `tencent/hy3:free` | 262K | See provider |
|  | <a href="https://freellm.net/models/openrouter/nvidia-nemotron-3-ultra-550b-a55b/" target="_blank" rel="noopener">NVIDIA: Nemotron 3 Ultra (free)</a> | `nvidia/nemotron-3-ultra-550b-a55b:free` | 1M | See provider |
|  | <a href="https://freellm.net/models/openrouter/poolside-laguna-m-1/" target="_blank" rel="noopener">Poolside: Laguna M.1 (free)</a> | `poolside/laguna-m.1:free` | 262K | See provider |
| GitHub Models | <a href="https://freellm.net/models/github-models/phi-4/" target="_blank" rel="noopener">Phi-4</a> | `Phi-4` | 131K | See provider |
|  | <a href="https://freellm.net/models/github-models/mistral-large-2411/" target="_blank" rel="noopener">Mistral Large (24.11)</a> | `Mistral-large-2411` | 131K | See provider |
|  | <a href="https://freellm.net/models/github-models/ai21-jamba-1-5-large/" target="_blank" rel="noopener">AI21 Jamba 1.5 Large</a> | `AI21-Jamba-1.5-Large` | 256K | See provider |
| Google Gemini | <a href="https://freellm.net/models/google-gemini/gemini-3-5-flash/" target="_blank" rel="noopener">Gemini 3.5 Flash</a> | `gemini-3.5-flash` | 1M | 15 RPM, 1,500 RPD |
|  | <a href="https://freellm.net/models/google-gemini/gemini-3-1-flash-lite/" target="_blank" rel="noopener">Gemini 3.1 Flash-Lite</a> | `gemini-3.1-flash-lite` | 1M | 30 RPM, 1,500 RPD |
|  | <a href="https://freellm.net/models/google-gemini/gemini-2-5-flash/" target="_blank" rel="noopener">Gemini 2.5 Flash</a> | `gemini-2.5-flash` | 1M | 15 RPM, 1,500 RPD |
| OVHcloud AI Endpoints | <a href="https://freellm.net/models/ovhcloud-ai-endpoints/qwen3-5-397b-a17b/" target="_blank" rel="noopener">Qwen3.5-397B-A17B</a> | `qwen3.5-397b-a17b` | 131K | 2 RPM (anonymous) |
|  | <a href="https://freellm.net/models/ovhcloud-ai-endpoints/gpt-oss-20b/" target="_blank" rel="noopener">gpt-oss-20b</a> | `gpt-oss-20b` | 128K | 2 RPM (anonymous) |
|  | <a href="https://freellm.net/models/ovhcloud-ai-endpoints/meta-llama-3-3-70b-instruct/" target="_blank" rel="noopener">Meta-Llama-3_3-70B-Instruct</a> | `meta-llama-3_3-70b-instruct` | 131K | 2 RPM (anonymous) |
| Groq | <a href="https://freellm.net/models/groq/moonshotai-kimi-k2-instruct/" target="_blank" rel="noopener">Moonshot Kimi K2</a> | `moonshotai/kimi-k2-instruct` | 131K | See provider |
|  | <a href="https://freellm.net/models/groq/moonshotai-kimi-k2-instruct-0905/" target="_blank" rel="noopener">Moonshot Kimi K2 0905</a> | `moonshotai/kimi-k2-instruct-0905` | 131K | See provider |
|  | <a href="https://freellm.net/models/groq/llama-4-maverick-17b-128e-instruct/" target="_blank" rel="noopener">llama-4-maverick-17b-128e-instruct</a> | `llama-4-maverick-17b-128e-instruct` | 131K | 15 RPM, 500 RPD |
| Mistral AI | <a href="https://freellm.net/models/mistral-ai/open-mistral-7b/" target="_blank" rel="noopener">Mistral 7B</a> | `open-mistral-7b` | 32K | See provider |
|  | <a href="https://freellm.net/models/mistral-ai/open-mixtral-8x7b/" target="_blank" rel="noopener">Mixtral 8x7B</a> | `open-mixtral-8x7b` | 32K | See provider |
|  | <a href="https://freellm.net/models/mistral-ai/mistral-medium-3-5-128b/" target="_blank" rel="noopener">Mistral Medium 3.5 (128B)</a> | `mistral-medium-3-5-128b` | 256K | ~1 RPS, 500K TPM |
| LLM7.io | <a href="https://freellm.net/models/llm7-io/deepseek-r1-0528/" target="_blank" rel="noopener">deepseek-r1-0528</a> | `deepseek-r1-0528` | 131K | 30 RPM (120 with token) |
|  | <a href="https://freellm.net/models/llm7-io/deepseek-v3-0324/" target="_blank" rel="noopener">deepseek-v3-0324</a> | `deepseek-v3-0324` | 131K | 30 RPM (120 with token) |
|  | <a href="https://freellm.net/models/llm7-io/gemini-2-5-flash-lite/" target="_blank" rel="noopener">gemini-2.5-flash-lite</a> | `gemini-2-5-flash-lite` | 131K | 30 RPM (120 with token) |
| Cerebras | <a href="https://freellm.net/models/cerebras/llama3-1-70b/" target="_blank" rel="noopener">Llama 3.1 70B</a> | `llama3.1-70b` | 131K | See provider |
|  | <a href="https://freellm.net/models/cerebras/gpt-oss-120b/" target="_blank" rel="noopener">gpt-oss-120b</a> | `gpt-oss-120b` | 128K | 30 RPM, 14,400 RPD, 1M .. |
|  | <a href="https://freellm.net/models/cerebras/zai-glm-4-7/" target="_blank" rel="noopener">zai-glm-4.7</a> | `zai-glm-4.7` | 128K | 10 RPM, 100 RPD, 1M TPD |
| Cohere | <a href="https://freellm.net/models/cohere/command-a-218b/" target="_blank" rel="noopener">Command A+ (218B)</a> | `command-a-218b` | 128K | 20 RPM |
|  | <a href="https://freellm.net/models/cohere/command-a-111b/" target="_blank" rel="noopener">Command A (111B)</a> | `command-a-111b` | 256K | 20 RPM |
|  | <a href="https://freellm.net/models/cohere/command-r/" target="_blank" rel="noopener">Command R+</a> | `command-r` | 128K | 20 RPM |
| Ollama Cloud | <a href="https://freellm.net/models/ollama-cloud/gpt-oss-120b-cloud/" target="_blank" rel="noopener">gpt-oss:120b-cloud</a> | `gpt-oss-120b-cloud` | 128K | Session/weekly limits (.. |
|  | <a href="https://freellm.net/models/ollama-cloud/deepseek-v3-1-671b-cloud/" target="_blank" rel="noopener">deepseek-v3.1:671b-cloud</a> | `deepseek-v3-1-671b-cloud` | 128K | Session/weekly limits (.. |
|  | <a href="https://freellm.net/models/ollama-cloud/qwen3-coder-480b-cloud/" target="_blank" rel="noopener">qwen3-coder:480b-cloud</a> | `qwen3-coder-480b-cloud` | 128K | Session/weekly limits (.. |
| OpenCode Zen | <a href="https://freellm.net/models/opencode/big-pickle/" target="_blank" rel="noopener">big-pickle</a> | `big-pickle` | 0 |  |
|  | <a href="https://freellm.net/models/opencode/deepseek-v4-flash-free/" target="_blank" rel="noopener">DeepSeek V4 Flash</a> | `deepseek-v4-flash-free` | 1M |  |
|  | <a href="https://freellm.net/models/opencode/mimo-v2-5-free/" target="_blank" rel="noopener">MiMo-V2.5</a> | `mimo-v2.5-free` | 1M |  |
| Agnes AI | <a href="https://freellm.net/models/agnes-ai/agnes-1-5-flash/" target="_blank" rel="noopener">agnes-1.5-flash</a> | `agnes-1.5-flash` | 256K | 30 RPM |
|  | <a href="https://freellm.net/models/agnes-ai/agnes-2-0-flash/" target="_blank" rel="noopener">agnes-2.0-flash</a> | `agnes-2.0-flash` | 256K | 30 RPM |
|  | <a href="https://freellm.net/models/agnes-ai/agnes-image-2-0-flash/" target="_blank" rel="noopener">agnes-image-2.0-flash</a> | `agnes-image-2.0-flash` | 4K | 30 RPM (1K) |
| Aion Labs | <a href="https://freellm.net/models/aion-labs/aion-2-5/" target="_blank" rel="noopener">Aion 2.5</a> | `aion-2-5` | 128K | 15 RPM, 20K TPD |
|  | <a href="https://freellm.net/models/aion-labs/aion-2-0/" target="_blank" rel="noopener">Aion 2.0</a> | `aion-2-0` | 128K | 15 RPM, 20K TPD |
|  | <a href="https://freellm.net/models/aion-labs/aion-rp-1-0-8b/" target="_blank" rel="noopener">Aion-RP 1.0 (8B)</a> | `aion-rp-1-0-8b` | 32K | 15 RPM, 20K TPD |
| Hugging Face | <a href="https://freellm.net/models/hugging-face/meta-llama-3-1-8b-instruct/" target="_blank" rel="noopener">Meta-Llama-3.1-8B-Instruct</a> | `meta-llama-3-1-8b-instruct` | 128K | Credit-metered |
|  | <a href="https://freellm.net/models/hugging-face/mistral-7b-instruct-v0-3/" target="_blank" rel="noopener">Mistral-7B-Instruct-v0.3</a> | `mistral-7b-instruct-v0-3` | 32K | Credit-metered |
|  | <a href="https://freellm.net/models/hugging-face/mixtral-8x7b-instruct-v0-1/" target="_blank" rel="noopener">Mixtral-8x7B-Instruct-v0.1</a> | `mixtral-8x7b-instruct-v0-1` | 32K | Credit-metered |
| Kilo Code | <a href="https://freellm.net/models/kilo-code/x-ai-grok-code-fast-1-free/" target="_blank" rel="noopener">x-ai/grok-code-fast-1:free</a> | `x-ai-grok-code-fast-1-free` | 256K | ~200 req/hr |
|  | <a href="https://freellm.net/models/kilo-code/minimax-minimax-m2-5-free/" target="_blank" rel="noopener">minimax/minimax-m2.5:free</a> | `minimax/minimax-m2.5` | 196K | ~200 req/hr |
|  | <a href="https://freellm.net/models/kilo-code/bytedance-seed-dola-seed-2-0-pro-free/" target="_blank" rel="noopener">bytedance-seed/dola-seed-2.0-pro:free</a> | `bytedance-seed-dola-seed-2-0-pro-free` | 131K | ~200 req/hr |
| Alibaba Cloud Model Studio | <a href="https://freellm.net/models/alibaba-cloud-model-studio/qwen3-max/" target="_blank" rel="noopener">Qwen3-Max</a> | `qwen3-max` | 128K | Tiered by region |
|  | <a href="https://freellm.net/models/alibaba-cloud-model-studio/qwen3-plus/" target="_blank" rel="noopener">Qwen3-Plus</a> | `qwen3-plus` | 1M | Tiered by region |
|  | <a href="https://freellm.net/models/alibaba-cloud-model-studio/qwen3-vl-plus/" target="_blank" rel="noopener">Qwen3-VL-Plus</a> | `qwen3-vl-plus` | 128K | Tiered by region |
| Z AI (Zhipu AI) | <a href="https://freellm.net/models/z-ai-zhipu-ai/glm-4-7-flash/" target="_blank" rel="noopener">GLM-4.7-Flash</a> | `glm-4.7` | 200K | 1 concurrent request |
|  | <a href="https://freellm.net/models/z-ai-zhipu-ai/glm-4-6v-flash/" target="_blank" rel="noopener">GLM-4.6V-Flash</a> | `glm-4.6` | 128K | 1 concurrent request |
|  | <a href="https://freellm.net/models/z-ai-zhipu-ai/glm-4-5-flash/" target="_blank" rel="noopener">GLM-4.5-Flash</a> | `glm-4.5` | 128K | 1 concurrent request |
| SambaNova | <a href="https://freellm.net/models/sambanova/deepseek-v3-1/" target="_blank" rel="noopener">DeepSeek-V3.1</a> | `deepseek-v3-1` | 128K | 20 RPM, 20 RPD, 200K TPD |
|  | <a href="https://freellm.net/models/sambanova/deepseek-v3-2-preview/" target="_blank" rel="noopener">DeepSeek-V3.2 (Preview)</a> | `deepseek-v3-2-preview` | 128K | 20 RPM, 20 RPD, 200K TPD |
|  | <a href="https://freellm.net/models/sambanova/minimax-m2-7/" target="_blank" rel="noopener">MiniMax-M2.7</a> | `minimax-m2-7` | 128K | 20 RPM, 20 RPD, 200K TPD |
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
| <a href="https://freellm.net/models/openrouter/tencent-hy3/" target="_blank" rel="noopener">Tencent: Hy3 (free)</a> | OpenRouter | 262K | 4997B tokens |
| <a href="https://freellm.net/models/openrouter/nvidia-nemotron-3-ultra-550b-a55b/" target="_blank" rel="noopener">NVIDIA: Nemotron 3 Ultra (free)</a> | OpenRouter | 1M | 1683B tokens |
| <a href="https://freellm.net/models/openrouter/poolside-laguna-m-1/" target="_blank" rel="noopener">Poolside: Laguna M.1 (free)</a> | OpenRouter | 262K | 768B tokens |
| <a href="https://freellm.net/models/nvidia-nim/moonshotai-kimi-k2-6/" target="_blank" rel="noopener">moonshotai/kimi-k2.6</a> | NVIDIA NIM | 262K | 416B tokens |
| <a href="https://freellm.net/models/openrouter/nvidia-nemotron-3-super-120b-a12b/" target="_blank" rel="noopener">NVIDIA: Nemotron 3 Super (free)</a> | OpenRouter | 1M | 376B tokens |
| <a href="https://freellm.net/models/nvidia-nim/z-ai-glm-5-2/" target="_blank" rel="noopener">z-ai/glm-5.2</a> | NVIDIA NIM | 1M | 314B tokens |
| <a href="https://freellm.net/models/nvidia-nim/z-ai-glm-5-1/" target="_blank" rel="noopener">z-ai/glm-5.1</a> | NVIDIA NIM | 202K | 158B tokens |
| <a href="https://freellm.net/models/openrouter/cohere-north-mini-code/" target="_blank" rel="noopener">Cohere: North Mini Code (free)</a> | OpenRouter | 256K | 113B tokens |
| <a href="https://freellm.net/models/openrouter/poolside-laguna-xs-2-1/" target="_blank" rel="noopener">Poolside: Laguna XS 2.1 (free)</a> | OpenRouter | 262K | 81B tokens |
| <a href="https://freellm.net/models/openrouter/nvidia-nemotron-3-nano-30b-a3b/" target="_blank" rel="noopener">NVIDIA: Nemotron 3 Nano 30B A3B (free)</a> | OpenRouter | 256K | 41B tokens |
<!-- END_TOP_MODELS -->

---

## 기여하기

기여를 환영합니다!

- **누락된 무료 모델 추가** — <a href="https://github.com/open-free-llm-api/awesome-free-llm-apis/issues" target="_blank" rel="noopener">이슈</a> 또는 PR 제출
- **부정확한 데이터 수정** — 속도 제한은 변경되고 제공업체도 발전합니다. PR 환영
- **설정 스니펫 추가** — 사용 중인 도구의 설정 방법이 있다면 `code-examples/`에 추가

### 포함 기준

다음 조건을 충족하는 모델이 대상입니다:
1. 제공업체가 명시적으로 **무료 티어**를 제공 (단순 체험 크레딧이 아님)
2. API가 **공개적으로 접근 가능** (대기자 명단, 비공개 베타, 리버스 엔지니어링이 아님)
3. 체험 크레딧: 명확히 표시되고 최소 $1 상당

---

## 링크

- 🌐 **라이브 사이트**: <a href="https://freellm.net" target="_blank" rel="noopener">freellm.net</a> — 검색, 비교, 플레이그라운드, 설정 생성
- 🔑 **API 키 디렉토리**: <a href="https://freellm.net/free-llm-api-keys/" target="_blank" rel="noopener">freellm.net/free-llm-api-keys/</a>
- ⚙️ **설정 생성기**: <a href="https://freellm.net/config/" target="_blank" rel="noopener">freellm.net/config/</a>
- 🎮 **플레이그라운드**: <a href="https://freellm.net/playground/" target="_blank" rel="noopener">freellm.net/playground/</a>
- 📊 **모델 비교**: <a href="https://freellm.net/compare/" target="_blank" rel="noopener">freellm.net/compare/</a>

## 라이선스

MIT © <a href="https://github.com/open-free-llm-api" target="_blank" rel="noopener">open-free-llm-api</a>

---

<p align="center">
  <sub>매일 자동 업데이트 · 마지막 업데이트: <!-- AUTO_LAST_UPDATED -->
2026-07-12
<!-- END_AUTO_LAST_UPDATED --></sub>
</p>
