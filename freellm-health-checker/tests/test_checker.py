"""Comprehensive unit tests for provider execution and health checking with mock transports."""

import httpx
import pytest

from freellm_health_checker.checker import HealthChecker
from freellm_health_checker.config import AppConfig, ProviderConfig, SettingsConfig
from freellm_health_checker.models import ErrorType, HealthStatus
from freellm_health_checker.providers.openai_compatible import OpenAICompatibleProvider


@pytest.fixture
def provider_cfg(monkeypatch):
    """Fixture providing a configured provider with a valid env var key."""
    monkeypatch.setenv("TEST_KEY", "sk-mock-valid-secret-key")
    return ProviderConfig(
        name="test-provider",
        model="mock-model-v1",
        base_url="https://api.testprovider.com/v1",
        api_key_env="TEST_KEY",
        timeout=5.0,
    )


@pytest.mark.asyncio
async def test_check_200_valid_response(provider_cfg):
    """Test successful 200 response with valid chat completion JSON."""
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.headers["authorization"] == "Bearer sk-mock-valid-secret-key"
        return httpx.Response(
            200,
            json={
                "choices": [
                    {"message": {"role": "assistant", "content": "HEALTH_OK"}}
                ]
            },
        )

    async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as client:
        provider = OpenAICompatibleProvider(provider_cfg)
        result = await provider.health_check(client)

    assert result.status == HealthStatus.HEALTHY
    assert result.response_valid is True
    assert result.http_status == 200
    assert result.error_type is None
    assert result.latency_ms is not None
    assert result.latency_ms >= 0
    assert result.health_score >= 85


@pytest.mark.asyncio
async def test_check_200_invalid_json(provider_cfg):
    """Test 200 response with non-JSON body."""
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, text="<html><body>Gateway HTML</body></html>")

    async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as client:
        provider = OpenAICompatibleProvider(provider_cfg)
        result = await provider.health_check(client)

    assert result.status == HealthStatus.UNHEALTHY
    assert result.response_valid is False
    assert result.error_type == ErrorType.INVALID_RESPONSE
    assert "JSON" in result.error_message


@pytest.mark.asyncio
async def test_check_200_empty_choices(provider_cfg):
    """Test 200 response with empty choices list."""
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"choices": []})

    async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as client:
        provider = OpenAICompatibleProvider(provider_cfg)
        result = await provider.health_check(client)

    assert result.status == HealthStatus.UNHEALTHY
    assert result.response_valid is False
    assert result.error_type == ErrorType.INVALID_RESPONSE


@pytest.mark.asyncio
async def test_check_200_empty_content(provider_cfg):
    """Test 200 response with blank message content."""
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"choices": [{"message": {"content": "   "}}]})

    async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as client:
        provider = OpenAICompatibleProvider(provider_cfg)
        result = await provider.health_check(client)

    assert result.status == HealthStatus.UNHEALTHY
    assert result.response_valid is False
    assert result.error_type == ErrorType.INVALID_RESPONSE


@pytest.mark.asyncio
async def test_check_401_authentication_error(provider_cfg):
    """Test 401 Unauthorized handling."""
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(401, text="Invalid API key provided")

    async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as client:
        provider = OpenAICompatibleProvider(provider_cfg)
        result = await provider.health_check(client)

    assert result.status == HealthStatus.UNHEALTHY
    assert result.http_status == 401
    assert result.error_type == ErrorType.AUTHENTICATION_ERROR


@pytest.mark.asyncio
async def test_check_403_forbidden_error(provider_cfg):
    """Test 403 Forbidden handling."""
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(403, text="Access denied to requested model")

    async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as client:
        provider = OpenAICompatibleProvider(provider_cfg)
        result = await provider.health_check(client)

    assert result.status == HealthStatus.UNHEALTHY
    assert result.http_status == 403
    assert result.error_type == ErrorType.AUTHENTICATION_ERROR


@pytest.mark.asyncio
async def test_check_408_provider_timeout(provider_cfg):
    """Test 408 Request Timeout handling."""
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(408, text="Request Timeout")

    async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as client:
        provider = OpenAICompatibleProvider(provider_cfg)
        result = await provider.health_check(client)

    assert result.status == HealthStatus.UNHEALTHY
    assert result.http_status == 408
    assert result.timeout is True
    assert result.error_type == ErrorType.TIMEOUT


@pytest.mark.asyncio
async def test_check_429_rate_limit_with_telemetry(provider_cfg):
    """Test 429 Rate Limit and header extraction."""
    def handler(request: httpx.Request) -> httpx.Response:
        headers = {
            "Retry-After": "30",
            "X-RateLimit-Limit": "100",
            "X-RateLimit-Remaining": "0",
            "X-RateLimit-Reset": "2026-10-08T12:00:00Z",
        }
        return httpx.Response(429, headers=headers, text="Rate limit exceeded")

    async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as client:
        provider = OpenAICompatibleProvider(provider_cfg)
        result = await provider.health_check(client)

    assert result.status == HealthStatus.UNHEALTHY
    assert result.http_status == 429
    assert result.rate_limited is True
    assert result.error_type == ErrorType.RATE_LIMIT
    assert result.rate_limit is not None
    assert result.rate_limit.retry_after == "30"
    assert result.rate_limit.limit == 100
    assert result.rate_limit.remaining == 0
    assert result.rate_limit.reset == "2026-10-08T12:00:00Z"


@pytest.mark.asyncio
@pytest.mark.parametrize("status_code", [500, 502, 503])
async def test_check_server_errors(provider_cfg, status_code):
    """Test 500, 502, and 503 provider server errors."""
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(status_code, text="Internal Server Error")

    async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as client:
        provider = OpenAICompatibleProvider(provider_cfg)
        result = await provider.health_check(client)

    assert result.status == HealthStatus.UNHEALTHY
    assert result.http_status == status_code
    assert result.error_type == ErrorType.SERVER_ERROR


@pytest.mark.asyncio
async def test_check_connection_exception(provider_cfg):
    """Test network connection failure (e.g. DNS or refused connection)."""
    def handler(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("Connection refused by peer")

    async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as client:
        provider = OpenAICompatibleProvider(provider_cfg)
        result = await provider.health_check(client)

    assert result.status == HealthStatus.UNHEALTHY
    assert result.error_type == ErrorType.CONNECTION_ERROR
    assert "ConnectError" in result.error_message


@pytest.mark.asyncio
async def test_check_timeout_exception(provider_cfg):
    """Test HTTP client timeout exception."""
    def handler(request: httpx.Request) -> httpx.Response:
        raise httpx.ReadTimeout("Read timed out")

    async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as client:
        provider = OpenAICompatibleProvider(provider_cfg)
        result = await provider.health_check(client)

    assert result.status == HealthStatus.UNHEALTHY
    assert result.timeout is True
    assert result.error_type == ErrorType.TIMEOUT


@pytest.mark.asyncio
async def test_check_missing_api_key_configuration_error(monkeypatch):
    """Test configuration error when API key environment variable is missing."""
    monkeypatch.delenv("MISSING_KEY", raising=False)
    cfg = ProviderConfig(
        name="no-key-provider",
        model="mock-model",
        base_url="https://api.test.com/v1",
        api_key_env="MISSING_KEY",
    )

    provider = OpenAICompatibleProvider(cfg)
    async with httpx.AsyncClient() as client:
        result = await provider.health_check(client)

    assert result.status == HealthStatus.CONFIGURATION_ERROR
    assert result.error_type == ErrorType.CONFIGURATION_ERROR
    assert "AUTH_CONFIG_ERROR" in result.error_message
    assert result.health_score == 0


@pytest.mark.asyncio
async def test_orchestrator_parallel_check_all(monkeypatch):
    """Test HealthChecker concurrent execution across multiple providers."""
    monkeypatch.setenv("P1_KEY", "key1")
    monkeypatch.setenv("P2_KEY", "key2")
    monkeypatch.delenv("P3_KEY", raising=False)

    p1 = ProviderConfig(name="p1-healthy", model="m1", base_url="https://p1.com/v1", api_key_env="P1_KEY")
    p2 = ProviderConfig(name="p2-rate-limit", model="m2", base_url="https://p2.com/v1", api_key_env="P2_KEY")
    p3 = ProviderConfig(name="p3-missing-key", model="m3", base_url="https://p3.com/v1", api_key_env="P3_KEY")

    app_config = AppConfig(
        settings=SettingsConfig(concurrency=3, retries=0, timeout=5.0),
        providers=[p1, p2, p3],
    )

    def handler(request: httpx.Request) -> httpx.Response:
        if "p1.com" in str(request.url):
            return httpx.Response(200, json={"choices": [{"message": {"content": "HEALTH_OK"}}]})
        elif "p2.com" in str(request.url):
            return httpx.Response(429, headers={"Retry-After": "10"}, text="Too Many Requests")
        return httpx.Response(404)

    checker = HealthChecker(app_config)
    async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as client:
        report = await checker.check_all(client=client)

    assert report.summary.total == 3
    assert report.summary.healthy == 1
    assert report.summary.unhealthy == 1
    assert report.summary.configuration_error == 1

    assert report.providers[0].provider == "p1-healthy"
    assert report.providers[0].status == HealthStatus.HEALTHY

    assert report.providers[1].provider == "p2-rate-limit"
    assert report.providers[1].status == HealthStatus.UNHEALTHY
    assert report.providers[1].rate_limited is True

    assert report.providers[2].provider == "p3-missing-key"
    assert report.providers[2].status == HealthStatus.CONFIGURATION_ERROR
