# Contributing to Free LLM API Health Checker

Thank you for your interest in contributing! This project is maintained as an open-source tool to monitor and evaluate free LLM API availability and performance.

---

## Contribution Workflow

1. **Fork the Repository**  
   Click the **Fork** button on GitHub to create a personal copy of the repository.

2. **Clone the Repository**  
   ```bash
   git clone https://github.com/<your-username>/awesome-freellm-apis.git
   cd awesome-freellm-apis/freellm-health-checker
   ```

3. **Create a Topic Branch**  
   ```bash
   git checkout -b feature/add-new-provider
   ```

4. **Install Dependencies**  
   Ensure you have Python 3.11+ installed. Create a virtual environment and install in editable mode with development dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -e ".[dev]"
   ```

5. **Implement Your Change**  
   - Follow [PEP 8](https://peps.python.org/pep-0008/) style guidelines.
   - Use Python type annotations throughout.
   - Keep functions concise with single responsibilities.
   - Ensure sensitive headers and keys are never printed or stored.

6. **Add Unit Tests**  
   - Add unit tests in the `tests/` directory.
   - Never write tests that require live external network requests or real API credentials.
   - Use mock transports (`httpx.MockTransport`) to simulate API behaviors.

7. **Run the Test Suite**  
   Ensure all tests pass and code compiles cleanly:
   ```bash
   python -m compileall freellm_health_checker
   pytest -v
   ```

8. **Submit a Pull Request (PR)**  
   Push your branch to GitHub and open a Pull Request against the `main` branch. Provide a clear description of the problem solved and the tests added.

---

## How to Add a New Provider Adapter

If a provider does not use the standard OpenAI-compatible `/chat/completions` API (e.g. Anthropic, Google Gemini, or custom endpoints), you can easily add a dedicated adapter:

### 1. Create the Provider Module
Create a new file in `freellm_health_checker/providers/`, for example `freellm_health_checker/providers/anthropic.py`:

```python
import time
import httpx
from freellm_health_checker.config import ProviderConfig
from freellm_health_checker.models import ErrorType, HealthResult, HealthStatus, RateLimitInfo
from freellm_health_checker.providers import LLMProvider
from freellm_health_checker.scoring import calculate_health_score, determine_health_status
from freellm_health_checker.utils import extract_rate_limit_headers, sanitize_error_message

class AnthropicProvider(LLMProvider):
    """Adapter for Anthropic Claude /v1/messages endpoint."""

    async def health_check(self, client: httpx.AsyncClient) -> HealthResult:
        api_key = self.config.resolve_api_key()
        if not api_key:
            score, breakdown = calculate_health_score(None, False, None, False, False)
            return HealthResult(
                provider=self.config.name,
                model=self.config.model,
                status=HealthStatus.CONFIGURATION_ERROR,
                error_type=ErrorType.CONFIGURATION_ERROR,
                error_message=f"AUTH_CONFIG_ERROR: Environment variable '{self.config.api_key_env}' is missing",
                health_score=score,
                score_breakdown=breakdown,
            )

        headers = {
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        }
        payload = {
            "model": self.config.model,
            "max_tokens": 10,
            "messages": [{"role": "user", "content": "Reply with exactly: HEALTH_OK"}],
        }

        # Measure roundtrip and handle response...
        ...
```

### 2. Register with ProviderRegistry
In `freellm_health_checker/providers/__init__.py`, import and register the new class:

```python
from freellm_health_checker.providers.anthropic import AnthropicProvider

ProviderRegistry.register("anthropic", AnthropicProvider)
```

### 3. Add Mock Unit Tests
Add offline mock tests in `tests/test_checker.py` simulating 200 responses, rate limits, and network errors for the new provider.

---

## Code Quality Standards

- **Zero Secrets**: Never print, log, or store API keys or authorization headers.
- **Type Annotations**: All public methods and functions should include type hints.
- **Docstrings**: Include clear docstrings for all modules, classes, and public functions.
- **Error Handling**: Catch specific exceptions and sanitize any error message before returning it to the user.
