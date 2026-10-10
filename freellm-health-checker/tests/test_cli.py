"""Unit tests for the CLI interface, report formatting, exit codes, and secret security."""

import json
from pathlib import Path
from unittest.mock import patch
import pytest

from freellm_health_checker.cli import parse_args, run_cli
from freellm_health_checker.models import (
    HealthCheckReport,
    HealthResult,
    HealthStatus,
    HealthSummary,
    RateLimitInfo,
)


@pytest.fixture
def sample_config_path(tmp_path: Path, monkeypatch) -> Path:
    """Create a temporary valid YAML config file."""
    monkeypatch.setenv("DUMMY_SECRET_KEY_12345", "DUMMY_SECRET_KEY_12345_VALUE")
    cfg_file = tmp_path / "test_config.yml"
    cfg_file.write_text(
        """
settings:
  concurrency: 2
  retries: 0
  timeout: 5

providers:
  - name: groq
    model: llama-3.3-70b-versatile
    base_url: https://api.groq.com/openai/v1
    api_key_env: DUMMY_SECRET_KEY_12345
""",
        encoding="utf-8",
    )
    return cfg_file


def test_cli_help(capsys):
    """Test --help exits cleanly."""
    with pytest.raises(SystemExit) as exc:
        parse_args(["--help"])
    assert exc.value.code == 0


def test_cli_missing_config_returns_exit_code_2(tmp_path: Path):
    """Test missing configuration file returns exit code 2."""
    missing = str(tmp_path / "does_not_exist.yml")
    code = run_cli([missing])
    assert code == 2


def test_cli_positional_and_named_config_parsing(tmp_path: Path):
    """Test parsing config positional argument vs --config flag."""
    c1 = parse_args(["my_config.yml"])
    assert c1.config_pos == "my_config.yml"
    assert c1.config_flag is None

    c2 = parse_args(["--config", "my_config.yml"])
    assert c2.config_flag == "my_config.yml"


def test_cli_healthy_run_exit_code_0(sample_config_path: Path, capsys):
    """Test healthy check run returns exit code 0 and renders table."""
    mock_report = HealthCheckReport(
        timestamp="2026-10-08T10:00:00Z",
        summary=HealthSummary(total=1, healthy=1, degraded=0, unhealthy=0),
        providers=[
            HealthResult(
                provider="groq",
                model="llama-3.3-70b-versatile",
                status=HealthStatus.HEALTHY,
                latency_ms=320.0,
                http_status=200,
                response_valid=True,
                health_score=96,
            )
        ],
    )

    with patch("freellm_health_checker.cli.HealthChecker.run", return_value=mock_report):
        code = run_cli([str(sample_config_path), "--format", "table"])

    assert code == 0
    captured = capsys.readouterr()
    assert "Free LLM API Health Checker" in captured.out
    assert "groq" in captured.out
    assert "HEALTHY" in captured.out
    assert "320 ms" in captured.out
    assert "Healthy: 1" in captured.out


def test_cli_unhealthy_run_exit_code_1(sample_config_path: Path, capsys):
    """Test degraded or unhealthy check run returns exit code 1."""
    mock_report = HealthCheckReport(
        timestamp="2026-10-08T10:00:00Z",
        summary=HealthSummary(total=1, healthy=0, degraded=0, unhealthy=1),
        providers=[
            HealthResult(
                provider="groq",
                model="llama-3.3-70b-versatile",
                status=HealthStatus.UNHEALTHY,
                latency_ms=None,
                http_status=429,
                rate_limited=True,
                health_score=10,
            )
        ],
    )

    with patch("freellm_health_checker.cli.HealthChecker.run", return_value=mock_report):
        code = run_cli([str(sample_config_path)])

    assert code == 1
    captured = capsys.readouterr()
    assert "RATE_LIMIT" in captured.out or "UNHEALTHY" in captured.out
    assert "Unhealthy: 1" in captured.out


def test_cli_json_output(sample_config_path: Path, capsys):
    """Test json format generates valid JSON containing expected keys."""
    mock_report = HealthCheckReport(
        timestamp="2026-10-08T10:00:00Z",
        summary=HealthSummary(total=1, healthy=1, degraded=0, unhealthy=0),
        providers=[
            HealthResult(
                provider="groq",
                model="llama-3.3-70b-versatile",
                status=HealthStatus.HEALTHY,
                latency_ms=320.0,
                http_status=200,
                response_valid=True,
                health_score=96,
                rate_limit=RateLimitInfo(limit=30, remaining=28),
            )
        ],
    )

    with patch("freellm_health_checker.cli.HealthChecker.run", return_value=mock_report):
        code = run_cli([str(sample_config_path), "--format", "json"])

    assert code == 0
    captured = capsys.readouterr()
    data = json.loads(captured.out)

    assert data["timestamp"] == "2026-10-08T10:00:00Z"
    assert data["summary"]["healthy"] == 1
    assert data["summary"]["total"] == 1
    assert len(data["providers"]) == 1
    p = data["providers"][0]
    assert p["provider"] == "groq"
    assert p["status"] == "healthy"
    assert p["latency_ms"] == 320.0
    assert p["health_score"] == 96
    assert p["rate_limit"]["limit"] == 30


def test_cli_markdown_output(sample_config_path: Path, capsys):
    """Test markdown format generates valid markdown table."""
    mock_report = HealthCheckReport(
        timestamp="2026-10-08T10:00:00Z",
        summary=HealthSummary(total=1, healthy=1, degraded=0, unhealthy=0),
        providers=[
            HealthResult(
                provider="groq",
                model="llama-3.3-70b-versatile",
                status=HealthStatus.HEALTHY,
                latency_ms=320.0,
                http_status=200,
                response_valid=True,
                health_score=96,
            )
        ],
    )

    with patch("freellm_health_checker.cli.HealthChecker.run", return_value=mock_report):
        code = run_cli([str(sample_config_path), "--format", "markdown"])

    assert code == 0
    captured = capsys.readouterr()
    assert "## Free LLM API Health" in captured.out
    assert "| Provider | Model | Status | Latency | Score |" in captured.out
    assert "🟢 Healthy" in captured.out
    assert "320ms" in captured.out


def test_security_never_exposes_api_key_or_secrets(sample_config_path: Path, capsys):
    """Verify that active secret keys never appear in stdout, stderr, or JSON reports."""
    secret_value = "DUMMY_SECRET_KEY_12345_VALUE"

    mock_report = HealthCheckReport(
        timestamp="2026-10-08T10:00:00Z",
        summary=HealthSummary(total=1, healthy=0, degraded=0, unhealthy=1),
        providers=[
            HealthResult(
                provider="groq",
                model="llama-3.3-70b-versatile",
                status=HealthStatus.UNHEALTHY,
                latency_ms=None,
                http_status=401,
                error_message="Unauthorized access token error",
                health_score=0,
            )
        ],
    )

    for fmt in ["table", "json", "markdown"]:
        with patch("freellm_health_checker.cli.HealthChecker.run", return_value=mock_report):
            run_cli([str(sample_config_path), "--format", fmt])
        captured = capsys.readouterr()
        assert secret_value not in captured.out
        assert secret_value not in captured.err
        assert "Bearer" not in captured.out
