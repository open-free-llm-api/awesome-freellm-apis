"""OpenAI-compatible LLM provider health check implementation."""

from __future__ import annotations

import logging
import time
from typing import Any, Dict, Optional

import httpx

from freellm_health_checker.config import ProviderConfig
from freellm_health_checker.models import (
    ErrorType,
    HealthResult,
    HealthStatus,
    RateLimitInfo,
)
from freellm_health_checker.providers import LLMProvider
from freellm_health_checker.scoring import (
    calculate_health_score,
    determine_health_status,
)
from freellm_health_checker.utils import (
    extract_rate_limit_headers,
    sanitize_error_message,
)

logger = logging.getLogger("freellm_health_checker.providers.openai_compatible")


class OpenAICompatibleProvider(LLMProvider):
    """Health check adapter for OpenAI-compatible Chat Completion API endpoints.

    Tests reachability and validity via POST /chat/completions using a minimal token prompt.
    """

    def __init__(self, config: ProviderConfig) -> None:
        super().__init__(config)
        self.endpoint_url = self._build_endpoint_url(config.base_url)

    @staticmethod
    def _build_endpoint_url(base_url: str) -> str:
        """Construct the full chat completions endpoint URL."""
        cleaned = base_url.rstrip("/")
        if cleaned.endswith("/chat/completions"):
            return cleaned
        return f"{cleaned}/chat/completions"

    async def health_check(self, client: httpx.AsyncClient) -> HealthResult:
        """Execute diagnostic health check against provider chat endpoint."""
        api_key = self.config.resolve_api_key()

        # Check for missing API key without exposing secret
        if api_key is None:
            logger.warning(
                "API key for '%s' not found in environment variable '%s'",
                self.config.name,
                self.config.api_key_env,
            )
            score, breakdown = calculate_health_score(
                http_status=None,
                response_valid=False,
                latency_ms=None,
                rate_limited=False,
                config_valid=False,
            )
            return HealthResult(
                provider=self.config.name,
                model=self.config.model,
                status=HealthStatus.CONFIGURATION_ERROR,
                latency_ms=None,
                http_status=None,
                response_valid=False,
                rate_limited=False,
                timeout=False,
                error_type=ErrorType.CONFIGURATION_ERROR,
                error_message=f"AUTH_CONFIG_ERROR: Environment variable '{self.config.api_key_env}' is missing or empty",
                health_score=score,
                score_breakdown=breakdown,
                rate_limit=RateLimitInfo(),
            )

        headers: Dict[str, str] = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "User-Agent": "freellm-health-checker/0.1.0",
        }
        if self.config.extra_headers:
            headers.update(self.config.extra_headers)

        payload: Dict[str, Any] = {
            "model": self.config.model,
            "messages": [
                {"role": "user", "content": "Reply with exactly: HEALTH_OK"}
            ],
            "max_tokens": 10,
        }

        latency_ms: Optional[float] = None
        http_status: Optional[int] = None
        response_valid = False
        rate_limited = False
        timed_out = False
        error_type: Optional[ErrorType] = None
        error_message: Optional[str] = None
        rate_limit_info = RateLimitInfo()

        start_time = time.perf_counter()
        logger.debug("Checking provider '%s' (model: '%s') at %s...", self.config.name, self.config.model, self.endpoint_url)

        try:
            response = await client.post(
                self.endpoint_url,
                json=payload,
                headers=headers,
                timeout=self.config.timeout,
            )
            end_time = time.perf_counter()
            latency_ms = (end_time - start_time) * 1000.0
            http_status = response.status_code

            logger.debug(
                "Response from '%s': status=%s latency=%.1fms",
                self.config.name,
                http_status,
                latency_ms,
            )

            # Extract rate limit telemetry
            rate_limit_info = extract_rate_limit_headers(response.headers)

            if 200 <= http_status < 300:
                # Validate response body structure and non-empty content
                try:
                    data = response.json()
                    choices = data.get("choices")
                    if isinstance(choices, list) and len(choices) > 0:
                        first_choice = choices[0]
                        if isinstance(first_choice, dict):
                            msg = first_choice.get("message")
                            if isinstance(msg, dict):
                                content = msg.get("content")
                                if isinstance(content, str) and content.strip():
                                    response_valid = True
                                else:
                                    error_type = ErrorType.INVALID_RESPONSE
                                    error_message = "Empty content received in response choices message"
                            else:
                                error_type = ErrorType.INVALID_RESPONSE
                                error_message = "Missing 'message' dictionary in choices[0]"
                        else:
                            error_type = ErrorType.INVALID_RESPONSE
                            error_message = "Expected dictionary for choices[0]"
                    else:
                        error_type = ErrorType.INVALID_RESPONSE
                        error_message = "Missing or empty 'choices' list in response"
                except Exception as parse_err:
                    response_valid = False
                    error_type = ErrorType.INVALID_RESPONSE
                    error_message = f"Failed to parse JSON response: {type(parse_err).__name__}"

            elif http_status in (401, 403):
                error_type = ErrorType.AUTHENTICATION_ERROR
                error_message = f"HTTP {http_status}: Authentication failed (invalid credentials or access denied)"

            elif http_status == 408:
                timed_out = True
                error_type = ErrorType.TIMEOUT
                error_message = "HTTP 408: Provider returned request timeout"

            elif http_status == 429:
                rate_limited = True
                error_type = ErrorType.RATE_LIMIT
                retry_str = f" (Retry-After: {rate_limit_info.retry_after})" if rate_limit_info.retry_after else ""
                error_message = f"HTTP 429: Rate limit exceeded{retry_str}"

            elif 500 <= http_status < 600:
                error_type = ErrorType.SERVER_ERROR
                error_message = f"HTTP {http_status}: Provider server error"

            else:
                error_type = ErrorType.UNKNOWN_ERROR
                error_message = f"HTTP {http_status}: Unexpected HTTP status"

        except httpx.TimeoutException:
            timed_out = True
            error_type = ErrorType.TIMEOUT
            error_message = f"Connection/Read timeout after {self.config.timeout:.1f}s"
            logger.debug("Provider '%s' timed out after %.1fs", self.config.name, self.config.timeout)

        except (httpx.ConnectError, httpx.NetworkError) as net_err:
            error_type = ErrorType.CONNECTION_ERROR
            error_message = sanitize_error_message(
                f"Connection failure: {type(net_err).__name__}",
                secrets_to_mask=[api_key],
            )
            logger.debug("Provider '%s' connection failed: %s", self.config.name, error_message)

        except httpx.HTTPError as http_err:
            error_type = ErrorType.UNKNOWN_ERROR
            error_message = sanitize_error_message(
                f"HTTP transport error: {type(http_err).__name__}",
                secrets_to_mask=[api_key],
            )
            logger.debug("Provider '%s' transport error: %s", self.config.name, error_message)

        except Exception as unexpected_err:
            error_type = ErrorType.UNKNOWN_ERROR
            error_message = sanitize_error_message(
                f"Unexpected error: {type(unexpected_err).__name__}",
                secrets_to_mask=[api_key],
            )
            logger.error("Provider '%s' unexpected error: %s", self.config.name, error_message)

        # Compute composite health score
        score, breakdown = calculate_health_score(
            http_status=http_status,
            response_valid=response_valid,
            latency_ms=latency_ms,
            rate_limited=rate_limited,
            config_valid=True,
        )

        status = determine_health_status(
            score=score,
            config_valid=True,
            error_type=error_type,
            latency_ms=latency_ms,
        )

        return HealthResult(
            provider=self.config.name,
            model=self.config.model,
            status=status,
            latency_ms=latency_ms,
            http_status=http_status,
            response_valid=response_valid,
            rate_limited=rate_limited,
            timeout=timed_out,
            error_type=error_type,
            error_message=error_message,
            health_score=score,
            score_breakdown=breakdown,
            rate_limit=rate_limit_info,
        )
