# Free LLM API Health Checker

[![Tests](https://github.com/open-free-llm-api/awesome-freellm-apis/actions/workflows/tests.yml/badge.svg)](https://github.com/open-free-llm-api/awesome-freellm-apis/actions)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A modular, high-performance CLI tool and Python framework that checks whether free LLM APIs are actually usable in real time. It monitors availability, latency, rate limits, network timeouts, response structure, and computes a composite 0–100 health score.

Designed as an independent, extensible module ready for integration with [awesome-freellm-apis](https://github.com/open-free-llm-api/awesome-freellm-apis).

---

## Features

- ⚡ **Real-Time API Availability Monitoring**: Probes endpoints with minimal token overhead.
- ⏱️ **Accurate Latency Measurement**: High-precision monotonic timer measuring network roundtrip.
- 🚦 **Rate-Limit Telemetry**: Automatically parses `Retry-After`, `X-RateLimit-Limit`, `X-RateLimit-Remaining`, and `X-RateLimit-Reset` headers.
- 🛡️ **Zero Secret Leakage Guarantee**: API keys and authorization headers are never logged, printed, or exposed in output.
- 🔍 **Strict Response Validation**: Verifies that responses are valid JSON, match expected schema structures, and deliver non-empty generated content (HTTP 200 alone does not mean healthy).
- 📊 **Composite Health Scoring (0–100)**: Evaluates availability, response validity, latency tiers, rate-limit health, and configuration.
- 📄 **Multiple Output Formats**: Human-friendly terminal tables, machine-readable JSON, and GitHub-ready Markdown.
- 🚀 **High-Throughput Asynchronous Checks**: Built on `asyncio` and `httpx` with configurable concurrency limits.
- 🤖 **CI/CD Integration**: Returns predictable exit codes (0 = healthy, 1 = degraded/unhealthy, 2 = config error, 3 = runtime error).
- 🧩 **Modular Architecture**: Clean separation between configuration, provider abstractions, scoring, and report formatters.

---

## Architecture

The system is structured as a pipeline with strict separation of concerns:

```
┌─────────────────┐
│  Configuration  │  (YAML parser, env var resolver, schema validation)
└────────┬────────┘
         ▼
┌─────────────────┐
│ Provider Engine │  (OpenAICompatibleProvider, Anthropic, Gemini...)
└────────┬────────┘
         ▼
┌─────────────────┐
│  Health Checker │  (Async orchestrator, semaphore concurrency, retries)
└────────┬────────┘
         ▼
┌─────────────────┐
│ Response Valid. │  (JSON schema verification, non-empty text check)
└────────┬────────┘
         ▼
┌─────────────────┐
│ Scoring Engine  │  (Availability, response, latency, rate-limit scoring)
└────────┬────────┘
         ▼
┌─────────────────┐
│ Report Renderers│  (Terminal Table, JSON, GitHub Markdown)
└─────────────────┘
```

### Module Breakdown

| Module | Responsibility |
|---|---|
| `freellm_health_checker/config.py` | Loads and validates YAML configurations; resolves environment variable keys. |
| `freellm_health_checker/models.py` | Strongly typed dataclasses and Enums (`HealthStatus`, `ErrorType`, `HealthResult`). |
| `freellm_health_checker/providers/` | Pluggable provider adapter interface and `ProviderRegistry`. |
| `freellm_health_checker/checker.py` | Asynchronous orchestrator with concurrency throttling and transient retries. |
| `freellm_health_checker/scoring.py` | Modular 0–100 composite scoring formula and latency tier classifications. |
| `freellm_health_checker/reporters.py` | Formatters for Terminal Table, JSON, and Markdown. |
| `freellm_health_checker/utils.py` | Security redaction, secret masking, and rate-limit header parsing. |
| `freellm_health_checker/cli.py` | Command-line interface with standard exit codes and format flags. |

---

## Installation

### Prerequisites
- Python 3.11 or higher
- Git

```bash
# Clone the repository
git clone https://github.com/open-free-llm-api/awesome-freellm-apis.git
cd awesome-freellm-apis/freellm-health-checker

# Install in editable mode
pip install -e .

# Or install with developer dependencies (for testing)
pip install -e ".[dev]"
```

Verify the installation:
```bash
freellm-health --help
```

---

## Configuration

Configuration is defined via a YAML file. **API keys must NEVER be placed in the configuration file.** Instead, reference the environment variable name via `api_key_env`.

Create a file named `config.yml`:

```yaml
settings:
  concurrency: 5     # Maximum concurrent requests
  retries: 0         # Retries for transient failures (default: 0)
  timeout: 15        # Default timeout in seconds

providers:
  - name: groq
    model: llama-3.3-70b-versatile
    base_url: https://api.groq.com/openai/v1
    api_key_env: GROQ_API_KEY
    timeout: 15

  - name: cerebras
    model: llama3.1-8b
    base_url: https://api.cerebras.ai/v1
    api_key_env: CEREBRAS_API_KEY
    timeout: 15

  - name: mistral
    model: mistral-small-latest
    base_url: https://api.mistral.ai/v1
    api_key_env: MISTRAL_API_KEY
    timeout: 15

  - name: openrouter
    model: meta-llama/llama-3.2-3b-instruct:free
    base_url: https://openrouter.ai/api/v1
    api_key_env: OPENROUTER_API_KEY
    timeout: 15
```

### Supplying API Keys

Export your provider API keys into your local shell environment:

```bash
# Linux / macOS
export GROQ_API_KEY="your-groq-api-key-here"
export CEREBRAS_API_KEY="your-cerebras-key-here"

# Windows (PowerShell)
$env:GROQ_API_KEY="your-groq-api-key-here"
$env:CEREBRAS_API_KEY="your-cerebras-key-here"
```

If an environment variable is missing, the tool reports `AUTH_CONFIG_ERROR` and status `configuration_error` without failing the entire run or leaking secret details.

---

## Usage

### 1. Default Terminal Table

```bash
freellm-health config.yml
# or
freellm-health --config config.yml
```

**Example Output:**
```
Free LLM API Health Checker
─────────────────────────────────────────────────────────────────────────────────
Provider    Model                    Status     Latency  Score
─────────────────────────────────────────────────────────────────────────────────
groq        llama-3.3-70b-versatile  HEALTHY     320 ms     96
cerebras    llama3.1-8b              HEALTHY     450 ms     96
provider-b  model-x                  DEGRADED     1.8 s     78
provider-c  model-y                  RATE_LIMIT      --     10
provider-d  model-z                  TIMEOUT         --     20
─────────────────────────────────────────────────────────────────────────────────
Healthy: 2 | Degraded: 1 | Unhealthy: 2
```

### 2. Machine-Readable JSON Output

Ideal for ingestion by dashboards, monitoring agents, and metrics aggregators:

```bash
freellm-health config.yml --format json
```

**Example Output:**
```json
{
  "timestamp": "2026-10-08T10:00:00Z",
  "summary": {
    "total": 4,
    "healthy": 1,
    "degraded": 1,
    "unhealthy": 2
  },
  "providers": [
    {
      "provider": "groq",
      "model": "llama-3.3-70b-versatile",
      "status": "healthy",
      "latency_ms": 320.0,
      "health_score": 96,
      "http_status": 200,
      "response_valid": true,
      "rate_limited": false,
      "timeout": false,
      "error_type": null,
      "rate_limit": {
        "limit": 30,
        "remaining": 28,
        "reset": null,
        "retry_after": null
      }
    }
  ]
}
```

### 3. GitHub Markdown Output

Ideal for GitHub Actions workflow summaries or automated README updates:

```bash
freellm-health config.yml --format markdown
```

**Example Output:**

## Free LLM API Health

| Provider | Model | Status | Latency | Score |
|---|---|---|---:|---:|
| Groq | llama-3.3-70b-versatile | 🟢 Healthy | 320ms | 96 |
| Provider B | model-x | 🟡 Degraded | 1.8s | 78 |
| Provider C | model-y | 🔴 Rate Limited | — | 10 |

### 4. Verbose Logging Mode

```bash
freellm-health config.yml --verbose
```

---

## Health Scoring Formula

The health score is a composite index ranging from 0 to 100:

| Component | Points | Criteria |
|---|---|---|
| **Availability** | 40 | HTTP 200–299 = 40 pts; 0 pts on connection failure, timeout, 4xx/5xx |
| **Response Validity** | 20 | Parsed JSON with valid model completion = 20 pts; 0 pts if invalid |
| **Latency** | 20 | < 500 ms = 20 pts (excellent)<br>500–1000 ms = 16 pts (good)<br>1000–2000 ms = 12 pts (acceptable)<br>2000–5000 ms = 6 pts (degraded)<br>> 5000 ms = 2 pts (poor) |
| **Rate-Limit Health** | 10 | 10 pts if not rate-limited; 0 pts on HTTP 429 |
| **Configuration** | 10 | 10 pts if configuration and API key are present; 0 pts on missing key |
| **Total** | **100** | Sum of all components |

---

## CLI Exit Codes

The tool produces deterministic exit codes suitable for CI/CD automation:

- `0`: All configured providers are healthy.
- `1`: One or more providers are degraded or unhealthy.
- `2`: Configuration error (missing config file, invalid YAML syntax, or malformed schema).
- `3`: Unexpected runtime / CLI execution error.

---

## Security

Security is an explicit priority:
1. **No Keys in Config**: Configurations only store the names of environment variables.
2. **Sanitized Output**: Error messages and stack traces pass through `sanitize_error_message()` which masks authorization headers, bearer tokens, and credentials.
3. **Ignored Secret Files**: `.gitignore` contains standard rules for `.env`, `*.secret`, and `secrets/`.
4. **Mocked Unit Tests**: No live network requests or real API keys are ever used in unit tests.

---

## Testing

The project includes unit tests covering configuration parsing, error classification, scoring tiers, mock HTTP responses, and CLI operations:

```bash
pytest -v
```

All tests execute fully offline using mock HTTP transports.

---

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for instructions on setting up your environment, running tests, and adding new provider adapters.

---

## Roadmap

- [ ] More provider adapters (Anthropic Messages API, Google Gemini native, Mistral native)
- [ ] Historical health telemetry tracking (SQLite / JSONL)
- [ ] Web health dashboard
- [ ] Dynamic GitHub README badges
- [ ] API reliability leaderboard
- [ ] Automatic provider discovery from community registries
- [ ] Direct integration with [awesome-freellm-apis](https://github.com/open-free-llm-api/awesome-freellm-apis)
- [ ] Scheduled GitHub Actions monitoring workflow with status badge publishing
