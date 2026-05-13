"""Plot benchmark summaries against expected complexity curves."""

from __future__ import annotations

import importlib
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path

from benchmarks.cases import BenchmarkCase
from benchmarks.complexity import normalized_curve
from benchmarks.runner import Summary


@dataclass(frozen=True)
class _PlotConfig:
    metric_name: str
    ylabel: str
    expected_label: str
    filename_suffix: str


def plot_case(case: BenchmarkCase, summaries: Sequence[Summary], output_dir: Path) -> list[Path]:
    """Create time and space plots for a benchmark case."""
    case_summaries = [
        summary for summary in summaries if summary.case_name == case.name
    ]
    if not case_summaries:
        return []

    paths = [
        _plot_metric(
            case=case,
            summaries=case_summaries,
            output_dir=output_dir,
            config=_PlotConfig(
                metric_name="mean_seconds",
                ylabel="Mean time (seconds)",
                expected_label=case.expected_time.name,
                filename_suffix="time",
            ),
        ),
    ]

    if case.expected_space is not None:
        paths.append(
            _plot_metric(
                case=case,
                summaries=case_summaries,
                output_dir=output_dir,
                config=_PlotConfig(
                    metric_name="mean_peak_bytes",
                    ylabel="Mean peak memory (bytes)",
                    expected_label=case.expected_space.name,
                    filename_suffix="space",
                ),
            ),
        )

    return paths


def _plot_metric(
    *,
    case: BenchmarkCase,
    summaries: Sequence[Summary],
    output_dir: Path,
    config: _PlotConfig,
) -> Path:
    try:
        plt = importlib.import_module("matplotlib.pyplot")
    except ImportError as error:
        msg = 'Install benchmark dependencies with: python -m pip install -e ".[bench]"'
        raise RuntimeError(msg) from error

    ordered = sorted(summaries, key=lambda summary: summary.size)
    sizes = [summary.size for summary in ordered]
    observed = [float(getattr(summary, config.metric_name)) for summary in ordered]
    model = case.expected_space if config.filename_suffix == "space" else case.expected_time
    expected = normalized_curve(model, sizes, observed)

    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / f"{_slug(case.name)}-{config.filename_suffix}.png"

    figure, axis = plt.subplots(figsize=(8, 5))
    axis.plot(sizes, observed, marker="o", label="observed")
    axis.plot(sizes, expected, linestyle="--", label=f"expected {config.expected_label}")
    axis.set_title(case.name)
    axis.set_xlabel("Input size (n)")
    axis.set_ylabel(config.ylabel)
    axis.grid(visible=True, alpha=0.25)
    axis.legend()
    figure.tight_layout()
    figure.savefig(path, dpi=150)
    plt.close(figure)

    return path


def _slug(value: str) -> str:
    return (
        value.lower()
        .replace(" ", "-")
        .replace("/", "-")
        .replace("\\", "-")
        .replace(":", "-")
    )
