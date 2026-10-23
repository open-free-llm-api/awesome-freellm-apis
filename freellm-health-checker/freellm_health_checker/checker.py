"""Core health check orchestrator with async concurrency and retry management."""

from __future__ import annotations

import asyncio
from datetime import datetime, timezone
import logging
from pathlib import Path
from typing import List, Optional

import httpx

from freellm_health_checker.config import AppConfig, ProviderConfig, load_config
from freellm_health_checker.models import (
    ErrorType,
    HealthCheckReport,
    HealthResult,
    HealthStatus,
    HealthSummary,
)
from freellm_health_checker.providers import ProviderRegistry

logger = logging.getLogger("freellm_health_checker.checker")


class HealthChecker:
    """Asynchronous orchestrator for concurrent LLM provider health checks."""

    def __init__(self, config: AppConfig) -> None:
        self.config = config

    @classmethod
    def from_config_file(cls, config_path: str | Path) -> HealthChecker:
        """Create a HealthChecker instance from a YAML configuration file path."""
        app_config = load_config(config_path)
        return cls(app_config)

    async def _check_provider_with_retry(
        self,
        provider_config: ProviderConfig,
        client: httpx.AsyncClient,
        semaphore: asyncio.Semaphore,
    ) -> HealthResult:
        """Run health check for a single provider guarded by semaphore and retry rules."""
        async with semaphore:
            provider = ProviderRegistry.create_provider(provider_config)
            max_retries = self.config.settings.retries
            attempt = 0

            while True:
                attempt += 1
                result = await provider.health_check(client)

                # Never retry authentication, configuration, or invalid response errors
                if result.error_type in (
                    ErrorType.AUTHENTICATION_ERROR,
                    ErrorType.CONFIGURATION_ERROR,
                    ErrorType.INVALID_RESPONSE,
                ):
                    return result

                # If result is healthy or degraded, or no more retries remaining, return
                if result.status in (HealthStatus.HEALTHY, HealthStatus.DEGRADED) or attempt > max_retries:
                    return result

                # Transient failure (connection error, timeout, server error): retry if attempts remain
                logger.debug(
                    "Retrying '%s' (attempt %d/%d) after error: %s",
                    provider_config.name,
                    attempt,
                    max_retries,
                    result.error_message,
                )
                await asyncio.sleep(0.5)

    async def check_all(self, client: Optional[httpx.AsyncClient] = None) -> HealthCheckReport:
        """Execute health checks concurrently across all configured providers.

        Args:
            client: Optional pre-configured httpx.AsyncClient (e.g. for testing).

        Returns:
            Aggregated HealthCheckReport containing all results and summary counts.
        """
        semaphore = asyncio.Semaphore(self.config.settings.concurrency)
        tasks = []

        # Use passed client or manage our own
        close_client = False
        if client is None:
            client = httpx.AsyncClient(
                timeout=httpx.Timeout(self.config.settings.timeout),
                follow_redirects=True,
            )
            close_client = True

        try:
            for provider_cfg in self.config.providers:
                tasks.append(self._check_provider_with_retry(provider_cfg, client, semaphore))

            results: List[HealthResult] = await asyncio.gather(*tasks)
        finally:
            if close_client:
                await client.aclose()

        # Build summary metrics
        total = len(results)
        healthy_count = sum(1 for r in results if r.status == HealthStatus.HEALTHY)
        degraded_count = sum(1 for r in results if r.status == HealthStatus.DEGRADED)
        unhealthy_count = sum(1 for r in results if r.status == HealthStatus.UNHEALTHY)
        config_err_count = sum(1 for r in results if r.status == HealthStatus.CONFIGURATION_ERROR)

        summary = HealthSummary(
            total=total,
            healthy=healthy_count,
            degraded=degraded_count,
            unhealthy=unhealthy_count,
            configuration_error=config_err_count,
        )

        utc_now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

        return HealthCheckReport(
            timestamp=utc_now,
            summary=summary,
            providers=results,
        )

    def run(self) -> HealthCheckReport:
        """Synchronously execute the full asynchronous health check suite."""
        return asyncio.run(self.check_all())
