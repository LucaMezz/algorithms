"""Measurement runner for benchmark cases."""

from __future__ import annotations

import gc
import statistics
import time
import tracemalloc
from collections import defaultdict
from collections.abc import Iterable
from dataclasses import dataclass

from benchmarks.cases import BenchmarkCase, BenchmarkSuite


@dataclass(frozen=True)
class Measurement:
    """One timed and memory-tracked benchmark run."""

    case_name: str
    size: int
    repeat: int
    seconds: float
    peak_bytes: int


@dataclass(frozen=True)
class Summary:
    """Aggregated benchmark result for one case and input size."""

    case_name: str
    size: int
    repeats: int
    min_seconds: float
    mean_seconds: float
    median_seconds: float
    stdev_seconds: float
    min_peak_bytes: int
    mean_peak_bytes: float
    max_peak_bytes: int


def run_suite(suite: BenchmarkSuite) -> list[Measurement]:
    """Run all cases in a benchmark suite."""
    measurements: list[Measurement] = []
    for case in suite.cases:
        measurements.extend(run_case(case))
    return measurements


def run_case(case: BenchmarkCase) -> list[Measurement]:
    """Run a benchmark case for every configured input size."""
    measurements: list[Measurement] = []
    for size in case.sizes:
        _warm_up(case, size)
        for repeat in range(1, case.repeats + 1):
            measurements.append(_measure_once(case, size, repeat))
    return measurements


def summarize(measurements: Iterable[Measurement]) -> list[Summary]:
    """Aggregate raw measurements by benchmark case and input size."""
    grouped: dict[tuple[str, int], list[Measurement]] = defaultdict(list)
    for measurement in measurements:
        grouped[(measurement.case_name, measurement.size)].append(measurement)

    summaries: list[Summary] = []
    for (case_name, size), group in sorted(grouped.items()):
        seconds = [measurement.seconds for measurement in group]
        peak_bytes = [measurement.peak_bytes for measurement in group]
        stdev_seconds = statistics.stdev(seconds) if len(seconds) > 1 else 0.0
        summaries.append(
            Summary(
                case_name=case_name,
                size=size,
                repeats=len(group),
                min_seconds=min(seconds),
                mean_seconds=statistics.fmean(seconds),
                median_seconds=statistics.median(seconds),
                stdev_seconds=stdev_seconds,
                min_peak_bytes=min(peak_bytes),
                mean_peak_bytes=statistics.fmean(peak_bytes),
                max_peak_bytes=max(peak_bytes),
            ),
        )
    return summaries


def _warm_up(case: BenchmarkCase, size: int) -> None:
    for _ in range(case.warmups):
        case.operation(case.input_factory(size))


def _measure_once(case: BenchmarkCase, size: int, repeat: int) -> Measurement:
    gc.collect()
    benchmark_input = case.input_factory(size)

    tracemalloc.start()
    start = time.perf_counter()
    case.operation(benchmark_input)
    seconds = time.perf_counter() - start
    _, peak_bytes = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return Measurement(
        case_name=case.name,
        size=size,
        repeat=repeat,
        seconds=seconds,
        peak_bytes=peak_bytes,
    )
