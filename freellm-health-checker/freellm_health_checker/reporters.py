"""Report formatters for Table, JSON, and Markdown outputs."""

from __future__ import annotations

from abc import ABC, abstractmethod
import json
import sys
from typing import Dict, Type

from freellm_health_checker.models import ErrorType, HealthCheckReport, HealthResult, HealthStatus
from freellm_health_checker.utils import format_latency


class BaseReporter(ABC):
    """Abstract base class for report generators."""

    @abstractmethod
    def render(self, report: HealthCheckReport) -> str:
        """Render the given health check report to string.

        Args:
            report: Populated HealthCheckReport.

        Returns:
            Formatted string ready for display or stdout.
        """
        pass


class TableReporter(BaseReporter):
    """Terminal-safe ASCII table formatter."""

    def render(self, report: HealthCheckReport) -> str:
        """Render diagnostic results as a clean, terminal-safe table."""
        # Calculate dynamic column widths based on data
        headers = ["Provider", "Model", "Status", "Latency", "Score"]
        rows = []

        for p in report.providers:
            provider_col = p.provider
            model_col = p.model
            status_col = self._format_status_label(p)
            latency_col = format_latency(p.latency_ms)
            score_col = str(p.health_score)
            rows.append([provider_col, model_col, status_col, latency_col, score_col])

        # Column widths (with sensible minimums)
        col_widths = [
            max(len(headers[0]), max((len(r[0]) for r in rows), default=0), 10),
            max(len(headers[1]), max((len(r[1]) for r in rows), default=0), 16),
            max(len(headers[2]), max((len(r[2]) for r in rows), default=0), 12),
            max(len(headers[3]), max((len(r[3]) for r in rows), default=0), 9),
            max(len(headers[4]), max((len(r[4]) for r in rows), default=0), 5),
        ]

        def row_str(cols: list[str]) -> str:
            # Right align latency and score, left align provider, model, status
            return (
                f"{cols[0].ljust(col_widths[0])}  "
                f"{cols[1].ljust(col_widths[1])}  "
                f"{cols[2].ljust(col_widths[2])}  "
                f"{cols[3].rjust(col_widths[3])}  "
                f"{cols[4].rjust(col_widths[4])}"
            )

        total_width = sum(col_widths) + 8  # 4 * 2 spaces between columns
        sep_char = self._get_sep_char()
        sep_line = sep_char * max(total_width, 60)

        lines = [
            "Free LLM API Health Checker",
            sep_line,
            row_str(headers),
            sep_line,
        ]

        for row in rows:
            lines.append(row_str(row))

        lines.append(sep_line)

        # Summary line
        s = report.summary
        summary_parts = [
            f"Healthy: {s.healthy}",
            f"Degraded: {s.degraded}",
            f"Unhealthy: {s.unhealthy}",
        ]
        if s.configuration_error > 0:
            summary_parts.append(f"Config Errors: {s.configuration_error}")

        lines.append(" | ".join(summary_parts))
        return "\n".join(lines)

    @staticmethod
    def _get_sep_char() -> str:
        """Safely determine table separator character compatible with stdout encoding."""
        enc = getattr(sys.stdout, "encoding", "utf-8") or "utf-8"
        try:
            "─".encode(enc, errors="strict")
            return "─"
        except (UnicodeEncodeError, LookupError, AttributeError):
            return "-"

    @staticmethod
    def _format_status_label(p: HealthResult) -> str:
        """Derive a concise, uppercase display label for table status."""
        if p.status == HealthStatus.HEALTHY:
            return "HEALTHY"
        elif p.status == HealthStatus.DEGRADED:
            return "DEGRADED"
        elif p.status == HealthStatus.CONFIGURATION_ERROR:
            return "CONFIG_ERROR"
        elif p.error_type == ErrorType.RATE_LIMIT or p.rate_limited:
            return "RATE_LIMIT"
        elif p.error_type == ErrorType.TIMEOUT or p.timeout:
            return "TIMEOUT"
        elif p.error_type == ErrorType.AUTHENTICATION_ERROR:
            return "AUTH_ERROR"
        elif p.error_type == ErrorType.SERVER_ERROR:
            return "SERVER_ERROR"
        elif p.error_type == ErrorType.CONNECTION_ERROR:
            return "CONN_ERROR"
        elif p.error_type == ErrorType.INVALID_RESPONSE:
            return "INVALID_RESP"
        return "UNHEALTHY"


class JsonReporter(BaseReporter):
    """Machine-readable JSON formatter ensuring zero secrets leakage."""

    def __init__(self, indent: int = 2) -> None:
        self.indent = indent

    def render(self, report: HealthCheckReport) -> str:
        """Render report as strict JSON."""
        return json.dumps(report.to_dict(), indent=self.indent)


class MarkdownReporter(BaseReporter):
    """GitHub-flavored Markdown table generator for README or CI/CD summaries."""

    def render(self, report: HealthCheckReport) -> str:
        """Render diagnostic results as a GitHub-flavored Markdown table."""
        lines = [
            "## Free LLM API Health",
            "",
            "| Provider | Model | Status | Latency | Score |",
            "|---|---|---|---:|---:|",
        ]

        for p in report.providers:
            status_badge = self._status_badge(p)
            latency_str = self._format_md_latency(p.latency_ms)
            lines.append(
                f"| {p.provider} | {p.model} | {status_badge} | {latency_str} | {p.health_score} |"
            )

        s = report.summary
        lines.append("")
        lines.append(f"**Summary:** Total: {s.total} | 🟢 Healthy: {s.healthy} | 🟡 Degraded: {s.degraded} | 🔴 Unhealthy: {s.unhealthy}")

        return "\n".join(lines)

    @staticmethod
    def _format_md_latency(latency_ms: float | None) -> str:
        """Format latency for Markdown table."""
        if latency_ms is None:
            return "—"
        if latency_ms < 1000:
            return f"{int(round(latency_ms))}ms"
        return f"{latency_ms / 1000:.1f}s"

    @staticmethod
    def _status_badge(p: HealthResult) -> str:
        """Return emoji status badge for Markdown table."""
        if p.status == HealthStatus.HEALTHY:
            return "🟢 Healthy"
        elif p.status == HealthStatus.DEGRADED:
            return "🟡 Degraded"
        elif p.status == HealthStatus.CONFIGURATION_ERROR:
            return "⚪ Config Error"
        elif p.error_type == ErrorType.RATE_LIMIT or p.rate_limited:
            return "🔴 Rate Limited"
        elif p.error_type == ErrorType.TIMEOUT or p.timeout:
            return "🔴 Timeout"
        elif p.error_type == ErrorType.AUTHENTICATION_ERROR:
            return "🔴 Auth Failed"
        elif p.error_type == ErrorType.SERVER_ERROR:
            return "🔴 Server Error"
        elif p.error_type == ErrorType.CONNECTION_ERROR:
            return "🔴 Connection Error"
        elif p.error_type == ErrorType.INVALID_RESPONSE:
            return "🔴 Invalid Response"
        return "🔴 Unhealthy"


_REPORTERS: Dict[str, Type[BaseReporter]] = {
    "table": TableReporter,
    "json": JsonReporter,
    "markdown": MarkdownReporter,
    "md": MarkdownReporter,
}


def get_reporter(format_name: str) -> BaseReporter:
    """Retrieve reporter instance by format name ('table', 'json', 'markdown').

    Args:
        format_name: Name of the format.

    Returns:
        Configured BaseReporter instance.

    Raises:
        ValueError: If the format is unknown.
    """
    key = format_name.strip().lower()
    if key not in _REPORTERS:
        raise ValueError(f"Unknown format: '{format_name}'. Supported formats: {list(_REPORTERS.keys())}")
    return _REPORTERS[key]()
