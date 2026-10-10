"""Free LLM API Health Checker.

A modular, real-time health, latency, and reliability monitoring tool
for free and open LLM API endpoints.
"""

__version__ = "0.1.0"

from freellm_health_checker.config import AppConfig, ProviderConfig, load_config
from freellm_health_checker.models import (
    ErrorType,
    HealthCheckReport,
    HealthResult,
    HealthStatus,
    HealthSummary,
    RateLimitInfo,
)
from freellm_health_checker.checker import HealthChecker
from freellm_health_checker.scoring import calculate_health_score

__all__ = [
    "__version__",
    "AppConfig",
    "ProviderConfig",
    "load_config",
    "HealthStatus",
    "ErrorType",
    "RateLimitInfo",
    "HealthResult",
    "HealthSummary",
    "HealthCheckReport",
    "HealthChecker",
    "calculate_health_score",
]
