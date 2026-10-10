"""Data models for Free LLM API Health Checker."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional


class HealthStatus(str, Enum):
    """Overall health state of an LLM API provider."""

    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNHEALTHY = "unhealthy"
    CONFIGURATION_ERROR = "configuration_error"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return self.value


class ErrorType(str, Enum):
    """Categorized error types for health check failures."""

    AUTHENTICATION_ERROR = "authentication_error"
    RATE_LIMIT = "rate_limit"
    TIMEOUT = "timeout"
    CONNECTION_ERROR = "connection_error"
    SERVER_ERROR = "server_error"
    INVALID_RESPONSE = "invalid_response"
    CONFIGURATION_ERROR = "configuration_error"
    UNKNOWN_ERROR = "unknown_error"

    def __str__(self) -> str:
        return self.value


@dataclass
class RateLimitInfo:
    """Captured rate limit telemetry from HTTP response headers."""

    limit: Optional[int] = None
    remaining: Optional[int] = None
    reset: Optional[str] = None
    retry_after: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert rate limit information to a dictionary."""
        return {
            "limit": self.limit,
            "remaining": self.remaining,
            "reset": self.reset,
            "retry_after": self.retry_after,
        }


@dataclass
class HealthScoreBreakdown:
    """Granular points breakdown for the composite 0-100 health score."""

    availability: int = 0
    response_validity: int = 0
    latency: int = 0
    rate_limit_health: int = 0
    configuration: int = 0
    total: int = 0

    def to_dict(self) -> Dict[str, int]:
        """Convert score breakdown to a dictionary."""
        return asdict(self)


@dataclass
class HealthResult:
    """Complete diagnostic result for a single provider/model health check."""

    provider: str
    model: str
    status: HealthStatus
    latency_ms: Optional[float] = None
    http_status: Optional[int] = None
    response_valid: bool = False
    rate_limited: bool = False
    timeout: bool = False
    error_type: Optional[ErrorType] = None
    error_message: Optional[str] = None
    health_score: int = 0
    score_breakdown: Optional[HealthScoreBreakdown] = None
    rate_limit: Optional[RateLimitInfo] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert the health result to a dictionary safe for serialization.

        Guarantees that no sensitive tokens, headers, or keys are present.
        """
        data: Dict[str, Any] = {
            "provider": self.provider,
            "model": self.model,
            "status": str(self.status),
            "latency_ms": round(self.latency_ms, 2) if self.latency_ms is not None else None,
            "health_score": self.health_score,
            "http_status": self.http_status,
            "response_valid": self.response_valid,
            "rate_limited": self.rate_limited,
            "timeout": self.timeout,
            "error_type": str(self.error_type) if self.error_type else None,
        }

        if self.error_message:
            data["error_message"] = self.error_message

        if self.rate_limit:
            data["rate_limit"] = self.rate_limit.to_dict()
        else:
            data["rate_limit"] = {
                "limit": None,
                "remaining": None,
                "reset": None,
                "retry_after": None,
            }

        if self.score_breakdown:
            data["score_breakdown"] = self.score_breakdown.to_dict()

        return data


@dataclass
class HealthSummary:
    """Summary counts across all monitored providers."""

    total: int = 0
    healthy: int = 0
    degraded: int = 0
    unhealthy: int = 0
    configuration_error: int = 0

    def to_dict(self) -> Dict[str, int]:
        """Convert summary counts to a dictionary."""
        return {
            "total": self.total,
            "healthy": self.healthy,
            "degraded": self.degraded,
            "unhealthy": self.unhealthy,
        }


@dataclass
class HealthCheckReport:
    """Composite health check report containing results for all providers."""

    timestamp: str
    summary: HealthSummary
    providers: List[HealthResult] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        """Convert full report to a clean dictionary structure."""
        return {
            "timestamp": self.timestamp,
            "summary": self.summary.to_dict(),
            "providers": [p.to_dict() for p in self.providers],
        }
