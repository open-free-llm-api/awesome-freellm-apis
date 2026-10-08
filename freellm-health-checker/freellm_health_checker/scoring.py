"""Health scoring engine and latency classification for Free LLM API Health Checker."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Tuple

from freellm_health_checker.models import ErrorType, HealthScoreBreakdown, HealthStatus


@dataclass
class LatencyThresholds:
    """Configurable latency score thresholds in milliseconds.

    Note: These thresholds are default heuristics for conversational API monitoring
    and are not universal or guaranteed network benchmarks.
    """

    excellent_max: float = 500.0   # < 500 ms: 20 points
    good_max: float = 1000.0       # 500 - 1000 ms: 16 points
    acceptable_max: float = 2000.0 # 1000 - 2000 ms: 12 points
    degraded_max: float = 5000.0   # 2000 - 5000 ms: 6 points
    # > 5000 ms: 2 points


DEFAULT_LATENCY_THRESHOLDS = LatencyThresholds()


def calculate_latency_points(
    latency_ms: Optional[float],
    thresholds: LatencyThresholds = DEFAULT_LATENCY_THRESHOLDS,
) -> int:
    """Calculate the latency component (0-20 points) of the health score.

    Args:
        latency_ms: Measured latency in milliseconds, or None if failed.
        thresholds: Configurable LatencyThresholds.

    Returns:
        Integer score between 0 and 20.
    """
    if latency_ms is None or latency_ms < 0:
        return 0

    if latency_ms < thresholds.excellent_max:
        return 20
    elif latency_ms < thresholds.good_max:
        return 16
    elif latency_ms < thresholds.acceptable_max:
        return 12
    elif latency_ms <= thresholds.degraded_max:
        return 6
    else:
        return 2


def calculate_health_score(
    http_status: Optional[int],
    response_valid: bool,
    latency_ms: Optional[float],
    rate_limited: bool,
    config_valid: bool,
    thresholds: LatencyThresholds = DEFAULT_LATENCY_THRESHOLDS,
) -> Tuple[int, HealthScoreBreakdown]:
    """Calculate the composite 0-100 health score and detailed breakdown.

    Scoring formula:
        - Availability: 40 points (HTTP 200-299)
        - Response validity: 20 points (valid non-empty model completion)
        - Latency: 20 points (based on configurable latency tiers)
        - Rate-limit health: 10 points (not rate limited)
        - Configuration: 10 points (configuration valid & API key present)

    Args:
        http_status: HTTP status code, if any.
        response_valid: Whether response body structure and content are valid.
        latency_ms: Measured latency in milliseconds.
        rate_limited: Whether rate limiting was detected.
        config_valid: Whether configuration was valid and API key existed.
        thresholds: LatencyThresholds instance.

    Returns:
        Tuple of (total_score, HealthScoreBreakdown).
    """
    # 1. Availability (40 pts)
    availability_pts = 40 if (http_status is not None and 200 <= http_status < 300) else 0

    # 2. Response validity (20 pts)
    response_pts = 20 if (availability_pts > 0 and response_valid) else 0

    # 3. Latency (20 pts)
    latency_pts = calculate_latency_points(latency_ms, thresholds) if response_pts > 0 else 0

    # 4. Rate-limit health (10 pts)
    rate_limit_pts = 0 if rate_limited or (http_status == 429) else 10

    # 5. Configuration (10 pts)
    config_pts = 10 if config_valid else 0

    # If configuration is invalid, total score is 0
    if not config_valid:
        breakdown = HealthScoreBreakdown(
            availability=0,
            response_validity=0,
            latency=0,
            rate_limit_health=0,
            configuration=0,
            total=0,
        )
        return 0, breakdown

    total = availability_pts + response_pts + latency_pts + rate_limit_pts + config_pts

    breakdown = HealthScoreBreakdown(
        availability=availability_pts,
        response_validity=response_pts,
        latency=latency_pts,
        rate_limit_health=rate_limit_pts,
        configuration=config_pts,
        total=total,
    )
    return total, breakdown


def determine_health_status(
    score: int,
    config_valid: bool,
    error_type: Optional[ErrorType],
    latency_ms: Optional[float],
    thresholds: LatencyThresholds = DEFAULT_LATENCY_THRESHOLDS,
) -> HealthStatus:
    """Determine the high-level HealthStatus enum from diagnostic factors.

    Args:
        score: Total computed health score (0-100).
        config_valid: Whether configuration is valid.
        error_type: Categorized error type, if any.
        latency_ms: Measured latency in milliseconds.
        thresholds: Configurable LatencyThresholds.

    Returns:
        HealthStatus enum value.
    """
    if not config_valid or error_type == ErrorType.CONFIGURATION_ERROR:
        return HealthStatus.CONFIGURATION_ERROR

    if error_type in (
        ErrorType.AUTHENTICATION_ERROR,
        ErrorType.SERVER_ERROR,
        ErrorType.CONNECTION_ERROR,
        ErrorType.TIMEOUT,
        ErrorType.INVALID_RESPONSE,
        ErrorType.RATE_LIMIT,
    ):
        return HealthStatus.UNHEALTHY

    # For successful requests (no fatal error_type):
    # If latency falls in degraded or poor category, mark as degraded
    if latency_ms is not None and latency_ms > thresholds.acceptable_max:
        return HealthStatus.DEGRADED

    if score >= 85:
        return HealthStatus.HEALTHY
    elif score >= 60:
        return HealthStatus.DEGRADED
    else:
        return HealthStatus.UNHEALTHY
