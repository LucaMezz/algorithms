"""Benchmarks for sorting algorithms.

Add one BenchmarkCase per implementation and operation. Keep input factories
separate from operations so each repeat receives a fresh, unmodified input.
"""

from __future__ import annotations

from random import Random

from benchmarks.cases import BenchmarkCase, BenchmarkSuite, powers_of_two
from benchmarks.complexity import LINEAR, LINEARITHMIC, QUADRATIC

SORTING_SIZES = powers_of_two(32, 4096)


def random_ints(size: int) -> list[int]:
    """Return deterministic pseudo-random integers for sorting benchmarks."""
    random = Random(2026 + size)
    return [random.randrange(size * 10) for _ in range(size)]


SUITE = BenchmarkSuite(
    name="sorting",
    cases=(
        BenchmarkCase(
            name="python sorted baseline random integers",
            input_factory=random_ints,
            operation=sorted,
            sizes=SORTING_SIZES,
            expected_time=LINEARITHMIC,
            expected_space=LINEAR,
        ),
        # Example for future use:
        # BenchmarkCase(
        #     name="merge_sort random integers",
        #     input_factory=random_ints,
        #     operation=lambda values: merge_sort(values),
        #     sizes=SORTING_SIZES,
        #     expected_time=LINEARITHMIC,
        #     expected_space=LINEAR,
        # ),
        # BenchmarkCase(
        #     name="selection_sort random integers",
        #     input_factory=random_ints,
        #     operation=lambda values: selection_sort(values),
        #     sizes=powers_of_two(16, 1024),
        #     expected_time=QUADRATIC,
        #     expected_space=CONSTANT,
        # ),
    ),
)

__all__ = [
    "LINEAR",
    "LINEARITHMIC",
    "QUADRATIC",
    "SORTING_SIZES",
    "SUITE",
    "BenchmarkCase",
    "BenchmarkSuite",
    "random_ints",
]
