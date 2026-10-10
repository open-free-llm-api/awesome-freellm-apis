"""Configuration loader and schema validation for Free LLM API Health Checker."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml


class ConfigError(Exception):
    """Raised when configuration file is missing, unreadable, or invalid."""


@dataclass
class SettingsConfig:
    """Global execution settings."""

    concurrency: int = 5
    retries: int = 0
    timeout: float = 15.0


@dataclass
class ProviderConfig:
    """Configuration for an individual LLM provider target."""

    name: str
    model: str
    base_url: str
    api_key_env: str
    timeout: float = 15.0
    provider_type: str = "openai_compatible"
    extra_headers: Dict[str, str] = field(default_factory=dict)

    def resolve_api_key(self) -> Optional[str]:
        """Resolve the API key securely from environment variables.

        Returns:
            The secret key string if set and non-empty, otherwise None.
        """
        if not self.api_key_env:
            return None
        val = os.getenv(self.api_key_env)
        if val is None or not val.strip():
            return None
        return val.strip()


@dataclass
class AppConfig:
    """Root configuration holding settings and provider targets."""

    settings: SettingsConfig
    providers: List[ProviderConfig]


def _validate_provider_dict(raw: Any, index: int) -> ProviderConfig:
    """Validate a raw provider dictionary from YAML."""
    if not isinstance(raw, dict):
        raise ConfigError(f"Provider entry #{index + 1} must be a dictionary, got {type(raw).__name__}")

    required_keys = ["name", "model", "base_url", "api_key_env"]
    for key in required_keys:
        if key not in raw or not str(raw[key]).strip():
            raise ConfigError(f"Provider entry #{index + 1} is missing required field: '{key}'")

    name = str(raw["name"]).strip()
    model = str(raw["model"]).strip()
    base_url = str(raw["base_url"]).strip()
    api_key_env = str(raw["api_key_env"]).strip()

    # Validate base_url format
    if not (base_url.startswith("http://") or base_url.startswith("https://")):
        raise ConfigError(
            f"Provider '{name}' has invalid base_url '{base_url}'. Must begin with http:// or https://"
        )

    # Optional timeout
    timeout = 15.0
    if "timeout" in raw:
        try:
            timeout = float(raw["timeout"])
            if timeout <= 0:
                raise ValueError()
        except (ValueError, TypeError):
            raise ConfigError(f"Provider '{name}' has invalid timeout '{raw['timeout']}'. Must be a positive number.")

    provider_type = str(raw.get("provider_type", "openai_compatible")).strip()
    extra_headers = raw.get("extra_headers", {})
    if not isinstance(extra_headers, dict):
        raise ConfigError(f"Provider '{name}' extra_headers must be a dictionary if provided.")

    return ProviderConfig(
        name=name,
        model=model,
        base_url=base_url,
        api_key_env=api_key_env,
        timeout=timeout,
        provider_type=provider_type,
        extra_headers={str(k): str(v) for k, v in extra_headers.items()},
    )


def load_config(config_path: str | Path) -> AppConfig:
    """Load, parse, and validate an AppConfig from a YAML file path.

    Args:
        config_path: Path to the YAML configuration file.

    Returns:
        Validated AppConfig instance.

    Raises:
        ConfigError: If the file does not exist, contains invalid YAML,
                     or fails schema validation.
    """
    path = Path(config_path)
    if not path.exists():
        raise ConfigError(f"Configuration file not found: {path}")
    if not path.is_file():
        raise ConfigError(f"Configuration path is not a file: {path}")

    try:
        content = path.read_text(encoding="utf-8")
    except Exception as exc:
        raise ConfigError(f"Failed to read configuration file: {exc}") from exc

    try:
        data = yaml.safe_load(content)
    except yaml.YAMLError as exc:
        raise ConfigError(f"Invalid YAML syntax in configuration file: {exc}") from exc

    if not isinstance(data, dict):
        raise ConfigError("Invalid configuration: root structure must be a YAML mapping (dictionary).")

    # Parse settings
    raw_settings = data.get("settings", {})
    if not isinstance(raw_settings, dict):
        raise ConfigError("'settings' section must be a dictionary if defined.")

    concurrency = 5
    if "concurrency" in raw_settings:
        try:
            concurrency = int(raw_settings["concurrency"])
            if concurrency < 1:
                raise ValueError()
        except (ValueError, TypeError):
            raise ConfigError("settings.concurrency must be a positive integer.")

    retries = 0
    if "retries" in raw_settings:
        try:
            retries = int(raw_settings["retries"])
            if retries < 0:
                raise ValueError()
        except (ValueError, TypeError):
            raise ConfigError("settings.retries must be a non-negative integer.")

    default_timeout = 15.0
    if "timeout" in raw_settings:
        try:
            default_timeout = float(raw_settings["timeout"])
            if default_timeout <= 0:
                raise ValueError()
        except (ValueError, TypeError):
            raise ConfigError("settings.timeout must be a positive number.")

    settings = SettingsConfig(
        concurrency=concurrency,
        retries=retries,
        timeout=default_timeout,
    )

    # Parse providers
    raw_providers = data.get("providers")
    if raw_providers is None:
        raise ConfigError("Configuration file missing required 'providers' list.")
    if not isinstance(raw_providers, list) or len(raw_providers) == 0:
        raise ConfigError("'providers' must be a non-empty list of provider configurations.")

    providers: List[ProviderConfig] = []
    for i, item in enumerate(raw_providers):
        provider_cfg = _validate_provider_dict(item, i)
        # Inherit default timeout if not explicitly set in provider
        if "timeout" not in item:
            provider_cfg.timeout = default_timeout
        providers.append(provider_cfg)

    return AppConfig(settings=settings, providers=providers)
