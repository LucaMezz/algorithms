"""Command-line runner for benchmark suites."""

from __future__ import annotations

import argparse
import importlib
from pathlib import Path

from benchmarks.cases import BenchmarkSuite
from benchmarks.plotting import plot_case
from benchmarks.reports import (
    write_measurements_csv,
    write_summaries_csv,
    write_summaries_json,
)
from benchmarks.runner import run_suite, summarize


def main() -> None:
    """Run a benchmark suite module and write reports."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("suite_module", help="Module containing a SUITE object")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("benchmark-results"),
        help="Directory for CSV, JSON, and plot files",
    )
    parser.add_argument(
        "--no-plots",
        action="store_true",
        help="Skip matplotlib plot generation",
    )
    args = parser.parse_args()

    suite = _load_suite(args.suite_module)
    if not suite.cases:
        msg = (
            f"{args.suite_module} has no active benchmark cases. "
            "Add a BenchmarkCase to its SUITE before running it."
        )
        raise SystemExit(msg)

    measurements = run_suite(suite)
    summaries = summarize(measurements)

    output_dir = args.output / suite.name
    write_measurements_csv(output_dir / "measurements.csv", measurements)
    write_summaries_csv(output_dir / "summary.csv", summaries)
    write_summaries_json(output_dir / "summary.json", summaries)

    plot_paths: list[Path] = []
    if not args.no_plots:
        for case in suite.cases:
            plot_paths.extend(plot_case(case, summaries, output_dir / "plots"))

    print(f"Wrote benchmark results to {output_dir}")
    for path in plot_paths:
        print(f"Wrote plot {path}")


def _load_suite(module_name: str) -> BenchmarkSuite:
    module = importlib.import_module(module_name)
    suite = getattr(module, "SUITE", None)
    if not isinstance(suite, BenchmarkSuite):
        msg = f"{module_name} must define SUITE as a BenchmarkSuite"
        raise TypeError(msg)
    return suite


if __name__ == "__main__":
    main()
