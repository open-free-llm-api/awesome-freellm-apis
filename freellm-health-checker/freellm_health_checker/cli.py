"""Command-line interface (CLI) for Free LLM API Health Checker."""

from __future__ import annotations

import argparse
import logging
from pathlib import Path
import sys
from typing import List, Optional

from freellm_health_checker import __version__
from freellm_health_checker.checker import HealthChecker
from freellm_health_checker.config import ConfigError, load_config
from freellm_health_checker.reporters import get_reporter


def setup_logging(verbose: bool) -> None:
    """Configure python logging according to verbosity flag."""
    level = logging.DEBUG if verbose else logging.WARNING
    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(
        logging.Formatter("%(levelname)s: %(message)s")
    )
    root_logger = logging.getLogger("freellm_health_checker")
    root_logger.setLevel(level)
    root_logger.handlers = [handler]


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        prog="freellm-health",
        description="Free LLM API Health Checker - Real-time health, latency, and reliability monitor.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "config_pos",
        nargs="?",
        metavar="CONFIG_FILE",
        help="Path to YAML configuration file (positional argument).",
    )

    parser.add_argument(
        "-c",
        "--config",
        dest="config_flag",
        metavar="FILE",
        help="Path to YAML configuration file (named flag).",
    )

    parser.add_argument(
        "-f",
        "--format",
        choices=["table", "json", "markdown"],
        default="table",
        help="Output format: 'table', 'json', or 'markdown'.",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable detailed diagnostic logging to stderr.",
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"freellm-health {__version__}",
        help="Show program version and exit.",
    )

    return parser.parse_args(argv)


def run_cli(argv: Optional[List[str]] = None) -> int:
    """Execute the CLI application with predictable exit codes.

    Exit codes:
        0 = All configured providers are healthy
        1 = One or more providers are degraded or unhealthy
        2 = Configuration error (missing file, bad YAML, invalid schema)
        3 = CLI / runtime error
    """
    try:
        args = parse_args(argv)
    except SystemExit as exc:
        return exc.code if isinstance(exc.code, int) else 3

    # Ensure UTF-8 output encoding for cross-platform emojis and unicode box-drawing
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            try:
                stream.reconfigure(encoding="utf-8", errors="replace")
            except Exception:
                pass

    setup_logging(args.verbose)
    logger = logging.getLogger("freellm_health_checker.cli")

    # Resolve config file path
    config_path = args.config_flag or args.config_pos
    if not config_path:
        for candidate in ("config.yml", "config.yaml"):
            if Path(candidate).is_file():
                config_path = candidate
                break

    if not config_path:
        sys.stderr.write(
            "Error: No configuration file specified.\n"
            "Usage: freellm-health <config.yml> or freellm-health --config <config.yml>\n"
        )
        return 2

    # Load and validate configuration
    try:
        app_config = load_config(config_path)
    except ConfigError as exc:
        sys.stderr.write(f"Configuration Error: {exc}\n")
        return 2
    except Exception as exc:
        sys.stderr.write(f"Unexpected configuration failure: {exc}\n")
        return 2

    # Execute health checks
    try:
        checker = HealthChecker(app_config)
        report = checker.run()
    except Exception as exc:
        logger.error("Execution failed: %s", exc, exc_info=args.verbose)
        sys.stderr.write(f"Runtime Error: {exc}\n")
        return 3

    # Format and print report
    try:
        reporter = get_reporter(args.format)
        rendered = reporter.render(report)
        print(rendered)
    except Exception as exc:
        sys.stderr.write(f"Reporter Error: {exc}\n")
        return 3

    # Check summary health to set exit code
    summary = report.summary
    if summary.degraded > 0 or summary.unhealthy > 0 or summary.configuration_error > 0:
        return 1

    return 0


def main() -> None:
    """Console script entrypoint."""
    sys.exit(run_cli())


if __name__ == "__main__":
    main()
