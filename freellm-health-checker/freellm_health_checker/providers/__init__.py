"""Provider abstraction layer and registry for Free LLM API Health Checker."""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, List, Type

import httpx

from freellm_health_checker.config import ProviderConfig, load_config
from freellm_health_checker.models import HealthResult


class LLMProvider(ABC):
    """Abstract base class for all LLM provider health check implementations."""

    def __init__(self, config: ProviderConfig) -> None:
        self.config = config

    @abstractmethod
    async def health_check(self, client: httpx.AsyncClient) -> HealthResult:
        """Execute a health check against the provider endpoint.

        Args:
            client: Shared asynchronous HTTP client.

        Returns:
            A populated HealthResult.
        """
        pass


class ProviderRegistry:
    """Registry managing available provider adapter implementations.

    Designed for clean extensibility without modifying the core checker.
    """

    _registry: Dict[str, Type[LLMProvider]] = {}

    @classmethod
    def register(cls, provider_type: str, provider_cls: Type[LLMProvider]) -> None:
        """Register a new provider class under a key.

        Args:
            provider_type: Identifying string (e.g. 'openai_compatible', 'anthropic').
            provider_cls: The LLMProvider subclass to register.
        """
        cls._registry[provider_type.lower()] = provider_cls

    @classmethod
    def create_provider(cls, config: ProviderConfig) -> LLMProvider:
        """Instantiate the appropriate LLMProvider for the given config.

        Args:
            config: Target provider configuration.

        Returns:
            Instantiated LLMProvider subclass.
        """
        p_type = config.provider_type.lower()
        if p_type not in cls._registry:
            # Default to openai_compatible if available, else raise
            if "openai_compatible" in cls._registry:
                return cls._registry["openai_compatible"](config)
            raise ValueError(f"Unknown provider type: '{config.provider_type}'")
        return cls._registry[p_type](config)

    @classmethod
    def load_from_yaml(cls, config_path: str | Path) -> List[LLMProvider]:
        """Load and instantiate providers from a YAML configuration file.

        Args:
            config_path: Path to configuration YAML.

        Returns:
            List of instantiated LLMProvider objects.
        """
        app_config = load_config(config_path)
        return [cls.create_provider(p_cfg) for p_cfg in app_config.providers]

    @classmethod
    def load_from_repository(cls, repo_path_or_url: str) -> List[LLMProvider]:
        """Future integration hook to dynamically load provider metadata

        from open-free-llm-api/awesome-freellm-apis repository.

        Args:
            repo_path_or_url: Local path or remote URL to the repository.

        Raises:
            NotImplementedError: Scheduled for future integration phase.
        """
        raise NotImplementedError(
            "Repository adapter for 'awesome-freellm-apis' is planned for a future release. "
            "Use load_from_yaml() for current configurations."
        )


# Import providers to trigger registration
from freellm_health_checker.providers.openai_compatible import OpenAICompatibleProvider  # noqa: E402

ProviderRegistry.register("openai_compatible", OpenAICompatibleProvider)
ProviderRegistry.register("openai", OpenAICompatibleProvider)

__all__ = [
    "LLMProvider",
    "ProviderRegistry",
    "OpenAICompatibleProvider",
]
