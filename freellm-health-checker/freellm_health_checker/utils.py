"""Utility functions for error sanitization, header parsing, and formatting."""

from __future__ import annotations

import re
from typing import Any, Iterable, Mapping, Optional

from freellm_health_checker.models import RateLimitInfo

# Regex patterns matching authorization headers and sensitive bearer tokens
_BEARER_REGEX = re.compile(r"(?i)\b(bearer\s+)([A-Za-z0-9_\-\.\~]{6,})")
_AUTH_HEADER_REGEX = re.compile(r"(?i)(authorization|api[-_]?key|x-api-key)\s*[:=]\s*['\"]?([A-Za-z0-9_\-\.\~]{6,})['\"]?")


def sanitize_error_message(message: str, secrets_to_mask: Optional[Iterable[str]] = None) -> str:
    """Sanitize error messages to guarantee no API keys or credentials leak.

    Args:
        message: The raw error message string.
        secrets_to_mask: Optional iterable of known secret strings to mask.

    Returns:
        A sanitized string with sensitive tokens replaced by '[REDACTED]'.
    """
    if not message:
        return ""

    sanitized = message

    # 1. Mask known active secrets if provided
    if secrets_to_mask:
        for secret in secrets_to_mask:
            if secret and len(secret) >= 4:
                sanitized = sanitized.replace(secret, "[REDACTED]")

    # 2. Mask regex bearer patterns
    sanitized = _BEARER_REGEX.sub(r"\1[REDACTED]", sanitized)

    # 3. Mask authorization / key header patterns
    sanitized = _AUTH_HEADER_REGEX.sub(r"\1: [REDACTED]", sanitized)

    return sanitized


def extract_rate_limit_headers(headers: Mapping[str, str]) -> RateLimitInfo:
    """Extract standard and provider-specific rate-limit telemetry from headers.

    Captures:
    - Retry-After
    - X-RateLimit-Limit / RateLimit-Limit
    - X-RateLimit-Remaining / RateLimit-Remaining
    - X-RateLimit-Reset / RateLimit-Reset

    Args:
        headers: Mapping of HTTP response headers.

    Returns:
        RateLimitInfo with parsed or None values. Never fabricates headers.
    """
    # Normalize headers for case-insensitive lookup
    norm_headers = {k.lower(): v for k, v in headers.items()}

    # Limit
    limit_val: Optional[int] = None
    for key in ("x-ratelimit-limit", "ratelimit-limit", "x-ratelimit-limit-requests"):
        if key in norm_headers:
            try:
                limit_val = int(norm_headers[key])
                break
            except (ValueError, TypeError):
                pass

    # Remaining
    remaining_val: Optional[int] = None
    for key in ("x-ratelimit-remaining", "ratelimit-remaining", "x-ratelimit-remaining-requests"):
        if key in norm_headers:
            try:
                remaining_val = int(norm_headers[key])
                break
            except (ValueError, TypeError):
                pass

    # Reset
    reset_val: Optional[str] = None
    for key in ("x-ratelimit-reset", "ratelimit-reset", "x-ratelimit-reset-requests"):
        if key in norm_headers:
            reset_val = norm_headers[key]
            break

    # Retry-After
    retry_after_val: Optional[str] = None
    if "retry-after" in norm_headers:
        retry_after_val = norm_headers["retry-after"]

    return RateLimitInfo(
        limit=limit_val,
        remaining=remaining_val,
        reset=reset_val,
        retry_after=retry_after_val,
    )


def format_latency(latency_ms: Optional[float]) -> str:
    """Format latency in milliseconds or seconds for human-readable display.

    Example:
        320.0 -> "320 ms"
        1850.0 -> "1.8 s"
        None -> "--"
    """
    if latency_ms is None:
        return "--"
    if latency_ms < 1000:
        return f"{int(round(latency_ms))} ms"
    return f"{latency_ms / 1000:.1f} s"
