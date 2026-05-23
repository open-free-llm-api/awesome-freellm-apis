<p align="center">
  <h1 align="center">awesome-free-llm-apis</h1>
  <!-- AUTO_STATS -->
  <p align="center"><strong>24プロバイダー、146+の無料LLM API</strong> — 無料モデルを検索・比較・設定。</p>
<!-- END_AUTO_STATS -->
</p>

<p align="center">
  <a href="https://freellm.net"><strong>🌐 freellm.net を見る</strong></a> —
  <a href="https://freellm.net/models/">モデル一覧</a> ·
  <a href="https://freellm.net/playground/">プレイグラウンド</a> ·
  <a href="https://freellm.net/config/">設定生成</a> ·
  <a href="https://freellm.net/free-llm-api-keys/">APIキー</a>
</p>

  <!-- AUTO_UPDATE_BADGE -->
  <p align="center"><strong>🔄 <a href="https://freellm.net">freellm.net</a> から毎日自動更新</strong> — 最終更新: 2026-05-23</p>
<!-- END_AUTO_UPDATE_BADGE -->

<p align="center">
  🌐 <a href="README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a>
</p>

---

## このプロジェクトの目的

無料のLLM APIを探すために、複数のGitHub READMEを読み漁ったり、いくつものプラットフォームに登録したり、どのモデルがまだ無料枠を提供しているか推測したりするのは非効率です。

このリポジトリは**構造化された機械可読な無料LLM APIディレクトリ**です — レート制限、コンテキストウィンドウ、ワンクリック設定スニペット、APIキー入手リンクをまとめ、毎日更新しています。

**このリポジトリ + [freellm.net](https://freellm.net) を選ぶ理由：**

- ✅ **常に最新** — 毎日の自動モニタリングで更新、2年前の静的リストではありません
- ✅ **クレカ条件が明確** — クレジットカード要・電話認証要・完全無料が一目で分かります
- ✅ **ワンクリック設定** — Claude Code、Cursor、Codex、Aiderなど10以上のツールに対応
- ✅ **横並び比較** — コンテキストウィンドウ、レート制限、マルチモーダル対応を瞬時に比較

---

## クイックスタート — 30秒で無料APIを使う

以下の全プロバイダーが**OpenAI互換エンドポイント**を提供しています（Geminiは簡単なラッパーで対応）。つまり、`baseURL` + `apiKey` を受け付けるツールならすべて動作します。

### Claude Code (cc)

```bash
export ANTHROPIC_BASE_URL="https://api.openai.com/v1"  # または Groq, OpenRouter, NVIDIA NIM
export ANTHROPIC_AUTH_TOKEN="your-api-key-here"
# Claude Codeが無料バックエンド経由で動作
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
    base_url="https://api.openai.com/v1",  # 以下の任意のプロバイダーに変更可
    api_key="YOUR_FREE_API_KEY",
)

response = client.chat.completions.create(
    model="gpt-oss-120b",
    messages=[{"role": "user", "content": "こんにちは！"}],
)
print(response.choices[0].message.content)
```

> Aider、Cline、OpenCode、Continue、Open WebUI、Gemini CLI の設定は [freellm.net/config/](https://freellm.net/config/) からコピーできます。

---

## プロバイダーディレクトリ & 人気の無料モデル

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

## クイックリファレンス — Base URL と APIキー

<!-- BEGIN_QUICK_REF -->
| Provider | Base URL | Get API Key | Credit Card? |
|---|---|---|---|
| AI21 Labs | `https://api.ai21.com/studio/v1` | [Get Key →](https://studio.ai21.com/account/api-key) | Registration |
| Aion Labs | `https://api.aionlabs.ai/v1` | [Get Key →](https://www.aionlabs.ai) | Registration |
| Alibaba Cloud Model Studio | `https://dashscope-intl.aliyuncs.com/compatible-mode/v1` | [Get Key →](https://bailian.console.alibabacloud.com/?apiKey=1) | Registration |
| Cerebras | `https://api.cerebras.ai/v1` | [Get Key →](https://cloud.cerebras.ai/) | No |
| Cloudflare Workers AI | `https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run` | [Get Key →](https://dash.cloudflare.com/profile/api-tokens) | No |
| Cohere | `https://api.cohere.com/v2` | [Get Key →](https://dashboard.cohere.com/api-keys) | No |
| DeepSeek | `https://api.deepseek.com/v1` | [Get Key →](https://platform.deepseek.com/api_keys) | Registration |
| GitHub Models | `https://models.github.ai/inference` | [Get Key →](https://github.com/marketplace/models) | No |
| Google Gemini | `https://generativelanguage.googleapis.com/v1beta` | [Get Key →](https://aistudio.google.com/app/apikey) | No |
| Groq | `https://api.groq.com/openai/v1` | [Get Key →](https://console.groq.com/keys) | No |
| Hugging Face | `https://router.huggingface.co/v1` | [Get Key →](https://huggingface.co/settings/tokens) | No |
| Kilo Code | `https://api.kilo.ai/api/gateway` | [Get Key →](https://kilo.ai) | No |
| LLM7.io | `https://api.llm7.io/v1` | [Get Key →](https://token.llm7.io) | No |
| Mistral AI | `https://api.mistral.ai/v1` | [Get Key →](https://console.mistral.ai/api-keys) | No |
| ModelScope | `https://api-inference.modelscope.cn/v1` | [Get Key →](https://modelscope.cn/my/myaccesstoken) | Registration |
| Nebius | `https://api.studio.nebius.com/v1` | [Get Key →](https://studio.nebius.com/settings/api-keys) | Registration |
| Nscale | `https://inference.api.nscale.com/v1` | [Get Key →](https://console.nscale.com/) | Registration |
| NVIDIA NIM | `https://integrate.api.nvidia.com/v1` | [Get Key →](https://build.nvidia.com/settings/api-keys) | Phone verification |
| Ollama Cloud | `https://api.ollama.com` | [Get Key →](https://ollama.com/settings/keys) | Registration |
| OpenRouter | `https://openrouter.ai/api/v1` | [Get Key →](https://openrouter.ai/workspaces/default/keys) | Registration |
| OVHcloud AI Endpoints | `https://oai.endpoints.kepler.ai.cloud.ovh.net/v1` | [Get Key →](https://endpoints.ai.cloud.ovh.net/) | Registration |
| SiliconFlow | `https://api.siliconflow.cn/v1` | [Get Key →](https://cloud.siliconflow.cn/account/ak) | Registration |
| xAI | `https://api.x.ai/v1` | [Get Key →](https://console.x.ai) | Registration |
| Z AI (Zhipu AI) | `https://open.bigmodel.cn/api/paas/v4` | [Get Key →](https://open.bigmodel.cn/usercenter/apikeys) | No |
<!-- END_QUICK_REF -->

## プロバイダー別ベスト無料モデル

<!-- BEGIN_BEST_MODELS -->
| Provider | Best Free Model | Max Context | Best For |
|---|---|---|---|
| AI21 Labs | Jamba Large 1.7 | 256K | chat |
|  | Jamba Mini 2 | 256K | chat |
| Aion Labs | aion-2.0 | 131K | chat |
|  | aion-1.0 | 131K | chat |
|  | aion-1.0-mini | 131K | chat |
| Alibaba Cloud Model Studio | Qwen3-Max | 128K | chat |
|  | Qwen3-Plus | 1M | chat |
|  | Qwen3-VL-Plus | 128K | chat |
| Cerebras | llama-3.3-70b | 128K | chat |
|  | gpt-oss-120b | 128K | chat, coding |
|  | qwen-3-235b-a22b-instruct-2507 | 131K | chat |
| Cloudflare Workers AI | @cf/meta/llama-3.3-70b-instruct-fp8-fast | 131K | chat |
|  | @cf/meta/llama-3.1-8b-instruct-fp8-fast | 131K | chat |
|  | @cf/meta/llama-3.2-11b-vision-instruct | 131K | chat, vision |
| Cohere | Command A (111B) | 256K | chat |
|  | Command R+ | 128K | chat |
|  | Command R7B | 128K | chat |
| DeepSeek | deepseek-chat (V3.2) | 128K | chat |
|  | deepseek-reasoner (R1) | 128K | chat, reasoning |
| GitHub Models | gpt-5 | 200K | chat |
|  | gpt-4.1 | 1M | chat |
|  | gpt-4.1-mini | 1M | chat |
| Google Gemini | Gemini 2.5 Pro | 2M | chat |
|  | Gemini 2.5 Flash | 1M | chat |
|  | Gemini 2.5 Flash-Lite | 1M | chat |
| Groq | llama-3.3-70b-versatile | 131K | chat |
|  | llama-3.1-8b-instant | 131K | chat |
|  | llama-4-maverick-17b-128e-instruct | 131K | chat |
| Hugging Face | Meta-Llama-3.1-8B-Instruct | 128K | chat |
|  | Mistral-7B-Instruct-v0.3 | 32K | chat |
|  | Mixtral-8x7B-Instruct-v0.1 | 32K | chat |
| Kilo Code | x-ai/grok-code-fast-1:free | 256K | chat, coding |
|  | minimax/minimax-m2.5:free | 196K | chat |
|  | bytedance-seed/dola-seed-2.0-pro:free | 131K | chat |
| LLM7.io | deepseek-r1-0528 | 131K | chat, reasoning |
|  | deepseek-v3-0324 | 131K | chat |
|  | gpt-4o-mini | 131K | chat |
| Mistral AI | Mistral Small 4 | 256K | chat |
|  | Mistral Medium 3 | 128K | chat |
|  | Mistral Large 3 | 256K | chat |
| ModelScope | Qwen/Qwen3.5-35B-A3B | 131K | chat |
|  | Qwen/Qwen3.5-27B | 131K | chat |
|  | Qwen/Qwen-Image | 131K | chat |
| Nebius | Meta-Llama-3.3-70B-Instruct | 128K | chat |
|  | Qwen3-235B-A22B | 128K | chat |
| Nscale | Llama-3.3-70B-Instruct | 128K | chat |
|  | Qwen3-Coder-30B-A3B-Instruct | 256K | chat, coding |
|  | DeepSeek-R1-Distill-Llama-70B | 128K | chat, reasoning |
| NVIDIA NIM | moonshotai/kimi-k2.6 | 262K | chat |
|  | z-ai/glm-5.1 | 202K | chat |
|  | qwen/qwen3.5-397b-a17b | 262K | chat |
| Ollama Cloud | gpt-oss:120b-cloud | 128K | chat, coding |
|  | deepseek-v3.1:671b-cloud | 128K | chat |
|  | qwen3-coder:480b-cloud | 128K | chat, coding |
| OpenRouter | Owl Alpha | 1M | chat |
|  | NVIDIA: Nemotron 3 Super (free) | 1M | chat, reasoning |
|  | Poolside: Laguna M.1 (free) | 131K | chat |
| OVHcloud AI Endpoints | Qwen2.5-VL-72B-Instruct | 128K | chat |
|  | Mistral-Nemo-Instruct-2407 | 128K | chat |
|  | Qwen3Guard-Gen-8B | 32K | chat |
| SiliconFlow | deepseek-ai/DeepSeek-R1-Distill-Qwen-7B | 131K | chat, reasoning |
|  | deepseek-ai/DeepSeek-OCR | 131K | chat |
|  | Abbreviation | 131K | chat |
| xAI | grok-4.3 | 1M | chat |
|  | grok-4.1-fast | 2M | chat |
|  | grok-3-mini | 131K | chat |
| Z AI (Zhipu AI) | GLM-4.7-Flash | 200K | chat |
|  | GLM-4.5-Flash | 128K | chat |
|  | GLM-4.6V-Flash | 128K | chat |
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

## コントリビューション

貢献を歓迎します！

- **不足している無料モデルの追加** — [issue](https://github.com/open-free-llm-api/awesome-free-llm-apis/issues) または PR を提出
- **不正確なデータの修正** — レート制限は変更され、プロバイダーも進化します。PR歓迎
- **設定スニペットの追加** — お使いのツールの設定方法があれば `code-examples/` に追加

### 収録基準

以下の条件を満たすモデルが対象です：
1. プロバイダーが明示的に**無料枠**を提供している（単なるトライアルクレジットではない）
2. APIが**公開アクセス可能**（待機リスト、クローズドベータ、リバースエンジニアリングではない）
3. トライアルクレジット：明示的に表示され、最低$1相当

---

## リンク

- 🌐 **ライブサイト**: [freellm.net](https://freellm.net) — 検索、比較、プレイグラウンド、設定生成
- 🔑 **APIキーディレクトリ**: [freellm.net/free-llm-api-keys/](https://freellm.net/free-llm-api-keys/)
- ⚙️ **設定ジェネレーター**: [freellm.net/config/](https://freellm.net/config/)
- 🎮 **プレイグラウンド**: [freellm.net/playground/](https://freellm.net/playground/)
- 📊 **モデル比較**: [freellm.net/compare/](https://freellm.net/compare/)

## ライセンス

MIT © [open-free-llm-api](https://github.com/open-free-llm-api)

---

<p align="center">
  <sub>毎日自動更新 · 最終更新: <!-- AUTO_LAST_UPDATED -->
2026-05-23
<!-- END_AUTO_LAST_UPDATED --></sub>
</p>
