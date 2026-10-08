"""Unit tests for scoring engine and latency classification."""

import pytest

from freellm_health_checker.models import ErrorType, HealthStatus
from freellm_health_checker.scoring import (
    DEFAULT_LATENCY_THRESHOLDS,
    calculate_health_score,
    calculate_latency_points,
    determine_health_status,
)


def test_calculate_latency_points_tiers():
    """Verify latency tier scoring according to thresholds."""
    # < 500 ms: 20 points
    assert calculate_latency_points(150.0) == 20
    assert calculate_latency_points(499.0) == 20

    # 500 - 1000 ms: 16 points
    assert calculate_latency_points(500.0) == 16
    assert calculate_latency_points(850.0) == 16

    # 1000 - 2000 ms: 12 points
    assert calculate_latency_points(1000.0) == 12
    assert calculate_latency_points(1800.0) == 12

    # 2000 - 5000 ms: 6 points
    assert calculate_latency_points(2000.1) == 6
    assert calculate_latency_points(4500.0) == 6

    # > 5000 ms: 2 points
    assert calculate_latency_points(5001.0) == 2
    assert calculate_latency_points(12000.0) == 2

    # None or invalid: 0 points
    assert calculate_latency_points(None) == 0
    assert calculate_latency_points(-10.0) == 0


def test_healthy_score_perfect():
    """Verify maximum 100 score for fast, successful, valid request."""
    score, breakdown = calculate_health_score(
        http_status=200,
        response_valid=True,
        latency_ms=250.0,
        rate_limited=False,
        config_valid=True,
    )

    assert breakdown.availability == 40
    assert breakdown.response_validity == 20
    assert breakdown.latency == 20
    assert breakdown.rate_limit_health == 10
    assert breakdown.configuration == 10
    assert score == 100
    assert breakdown.total == 100

    status = determine_health_status(
        score=score,
        config_valid=True,
        error_type=None,
        latency_ms=250.0,
    )
    assert status == HealthStatus.HEALTHY


def test_degraded_due_to_latency():
    """Verify degraded status when latency exceeds acceptable threshold."""
    score, breakdown = calculate_health_score(
        http_status=200,
        response_valid=True,
        latency_ms=2800.0,  # 2.8s
        rate_limited=False,
        config_valid=True,
    )

    # 40 (avail) + 20 (resp) + 6 (latency) + 10 (rate limit) + 10 (config) = 86
    assert breakdown.latency == 6
    assert score == 86

    status = determine_health_status(
        score=score,
        config_valid=True,
        error_type=None,
        latency_ms=2800.0,
    )
    assert status == HealthStatus.DEGRADED


def test_rate_limited_scoring():
    """Verify scoring and status when 429 rate limit is encountered."""
    score, breakdown = calculate_health_score(
        http_status=429,
        response_valid=False,
        latency_ms=100.0,
        rate_limited=True,
        config_valid=True,
    )

    # Avail: 0, Resp: 0, Lat: 0, Rate limit: 0, Config: 10
    assert breakdown.availability == 0
    assert breakdown.rate_limit_health == 0
    assert breakdown.configuration == 10
    assert score == 10

    status = determine_health_status(
        score=score,
        config_valid=True,
        error_type=ErrorType.RATE_LIMIT,
        latency_ms=100.0,
    )
    assert status == HealthStatus.UNHEALTHY


def test_timeout_scoring():
    """Verify score and status on request timeout."""
    score, breakdown = calculate_health_score(
        http_status=None,
        response_valid=False,
        latency_ms=None,
        rate_limited=False,
        config_valid=True,
    )

    assert score == 20  # Rate limit health (10) + Config (10)
    status = determine_health_status(
        score=score,
        config_valid=True,
        error_type=ErrorType.TIMEOUT,
        latency_ms=None,
    )
    assert status == HealthStatus.UNHEALTHY


def test_invalid_response_scoring():
    """Verify score when HTTP is 200 but payload is unparseable or empty."""
    score, breakdown = calculate_health_score(
        http_status=200,
        response_valid=False,
        latency_ms=300.0,
        rate_limited=False,
        config_valid=True,
    )

    # Avail: 40, Resp: 0, Lat: 0 (no lat pts if invalid), Rate limit: 10, Config: 10 = 60
    assert breakdown.availability == 40
    assert breakdown.response_validity == 0
    assert breakdown.latency == 0
    assert score == 60

    status = determine_health_status(
        score=score,
        config_valid=True,
        error_type=ErrorType.INVALID_RESPONSE,
        latency_ms=300.0,
    )
    assert status == HealthStatus.UNHEALTHY


def test_configuration_error_scoring():
    """Verify score is 0 and status is CONFIGURATION_ERROR on config issue."""
    score, breakdown = calculate_health_score(
        http_status=None,
        response_valid=False,
        latency_ms=None,
        rate_limited=False,
        config_valid=False,
    )

    assert score == 0
    assert breakdown.total == 0
    assert breakdown.configuration == 0

    status = determine_health_status(
        score=score,
        config_valid=False,
        error_type=ErrorType.CONFIGURATION_ERROR,
        latency_ms=None,
    )
    assert status == HealthStatus.CONFIGURATION_ERROR
