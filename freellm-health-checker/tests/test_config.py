"""Unit tests for configuration loading and validation."""

import os
from pathlib import Path
import pytest

from freellm_health_checker.config import ConfigError, ProviderConfig, load_config


def test_valid_config(tmp_path: Path):
    """Test loading a fully specified valid configuration."""
    config_file = tmp_path / "valid.yml"
    config_file.write_text(
        """
settings:
  concurrency: 3
  retries: 1
  timeout: 10

providers:
  - name: groq
    model: llama-3.3-70b-versatile
    base_url: https://api.groq.com/openai/v1
    api_key_env: GROQ_API_KEY
    timeout: 12
    extra_headers:
      X-Custom: test-val

  - name: cerebras
    model: llama3.1-8b
    base_url: https://api.cerebras.ai/v1
    api_key_env: CEREBRAS_API_KEY
""",
        encoding="utf-8",
    )

    app_config = load_config(config_file)
    assert app_config.settings.concurrency == 3
    assert app_config.settings.retries == 1
    assert app_config.settings.timeout == 10.0

    assert len(app_config.providers) == 2
    p1 = app_config.providers[0]
    assert p1.name == "groq"
    assert p1.model == "llama-3.3-70b-versatile"
    assert p1.base_url == "https://api.groq.com/openai/v1"
    assert p1.api_key_env == "GROQ_API_KEY"
    assert p1.timeout == 12.0
    assert p1.extra_headers == {"X-Custom": "test-val"}

    p2 = app_config.providers[1]
    assert p2.name == "cerebras"
    # Fallback to default settings timeout
    assert p2.timeout == 10.0


def test_missing_config_file(tmp_path: Path):
    """Test loading a non-existent configuration file raises ConfigError."""
    missing = tmp_path / "non_existent.yml"
    with pytest.raises(ConfigError, match="Configuration file not found"):
        load_config(missing)


def test_invalid_yaml_syntax(tmp_path: Path):
    """Test loading malformed YAML raises ConfigError."""
    bad_yaml = tmp_path / "bad.yml"
    bad_yaml.write_text("providers: [unclosed list", encoding="utf-8")
    with pytest.raises(ConfigError, match="Invalid YAML syntax"):
        load_config(bad_yaml)


def test_root_not_dict(tmp_path: Path):
    """Test YAML with list root raises ConfigError."""
    bad_yaml = tmp_path / "list_root.yml"
    bad_yaml.write_text("- item1\n- item2", encoding="utf-8")
    with pytest.raises(ConfigError, match="root structure must be a YAML mapping"):
        load_config(bad_yaml)


def test_missing_providers_key(tmp_path: Path):
    """Test configuration missing 'providers' list raises ConfigError."""
    bad_yaml = tmp_path / "no_providers.yml"
    bad_yaml.write_text("settings:\n  concurrency: 5", encoding="utf-8")
    with pytest.raises(ConfigError, match="missing required 'providers' list"):
        load_config(bad_yaml)


def test_empty_providers_list(tmp_path: Path):
    """Test empty 'providers' list raises ConfigError."""
    bad_yaml = tmp_path / "empty_providers.yml"
    bad_yaml.write_text("providers: []", encoding="utf-8")
    with pytest.raises(ConfigError, match="must be a non-empty list"):
        load_config(bad_yaml)


@pytest.mark.parametrize("missing_field", ["name", "model", "base_url", "api_key_env"])
def test_missing_provider_required_fields(tmp_path: Path, missing_field: str):
    """Test provider missing essential fields raises ConfigError."""
    fields = {
        "name": "groq",
        "model": "llama-3",
        "base_url": "https://api.groq.com/openai/v1",
        "api_key_env": "GROQ_API_KEY",
    }
    del fields[missing_field]

    yaml_content = "providers:\n  - " + "\n    ".join(f"{k}: {v}" for k, v in fields.items())
    config_file = tmp_path / f"missing_{missing_field}.yml"
    config_file.write_text(yaml_content, encoding="utf-8")

    with pytest.raises(ConfigError, match=f"missing required field: '{missing_field}'"):
        load_config(config_file)


def test_invalid_base_url(tmp_path: Path):
    """Test provider with invalid base_url protocol raises ConfigError."""
    bad_yaml = tmp_path / "bad_url.yml"
    bad_yaml.write_text(
        """
providers:
  - name: test
    model: test-model
    base_url: ftp://invalid.host/v1
    api_key_env: TEST_KEY
""",
        encoding="utf-8",
    )
    with pytest.raises(ConfigError, match="invalid base_url"):
        load_config(bad_yaml)


def test_invalid_timeout(tmp_path: Path):
    """Test invalid timeout raises ConfigError."""
    bad_yaml = tmp_path / "bad_timeout.yml"
    bad_yaml.write_text(
        """
providers:
  - name: test
    model: test-model
    base_url: https://example.com/v1
    api_key_env: TEST_KEY
    timeout: -5
""",
        encoding="utf-8",
    )
    with pytest.raises(ConfigError, match="invalid timeout"):
        load_config(bad_yaml)


def test_api_key_env_resolution(monkeypatch):
    """Test secure resolution of environment variable for API keys."""
    cfg = ProviderConfig(
        name="test",
        model="m",
        base_url="https://api.test.com",
        api_key_env="TEST_LLM_KEY",
    )

    # Missing env var
    monkeypatch.delenv("TEST_LLM_KEY", raising=False)
    assert cfg.resolve_api_key() is None

    # Empty env var
    monkeypatch.setenv("TEST_LLM_KEY", "   ")
    assert cfg.resolve_api_key() is None

    # Present env var
    monkeypatch.setenv("TEST_LLM_KEY", "sk-secret-key-12345")
    assert cfg.resolve_api_key() == "sk-secret-key-12345"
