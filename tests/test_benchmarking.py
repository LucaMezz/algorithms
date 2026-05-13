"""Tests for the local benchmark harness."""

from benchmarks.cases import BenchmarkCase, BenchmarkSuite, powers_of_two
from benchmarks.complexity import LINEAR, normalized_curve
from benchmarks.runner import run_suite, summarize


def test_powers_of_two_includes_stop() -> None:
    """Power-of-two helper should include the upper bound when exact."""
    assert powers_of_two(2, 16) == (2, 4, 8, 16)


def test_normalized_curve_scales_to_final_observation() -> None:
    """Expected curves should be scaled to the final observed value."""
    assert normalized_curve(LINEAR, [10, 20], [0.5, 2.0]) == [1.0, 2.0]


def test_run_suite_summarizes_case() -> None:
    """A tiny benchmark case should produce one summary per input size."""
    suite = BenchmarkSuite(
        name="smoke",
        cases=(
            BenchmarkCase(
                name="sum list",
                input_factory=lambda size: list(range(size)),
                operation=sum,
                sizes=(4, 8),
                expected_time=LINEAR,
                repeats=1,
                warmups=0,
            ),
        ),
    )

    measurements = run_suite(suite)
    summaries = summarize(measurements)

    assert len(measurements) == 2
    assert [summary.size for summary in summaries] == [4, 8]
