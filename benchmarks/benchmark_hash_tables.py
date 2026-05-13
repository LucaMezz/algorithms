"""Benchmarks for hash table implementations and operations."""

from __future__ import annotations

from benchmarks.cases import BenchmarkCase, BenchmarkSuite, powers_of_two
from benchmarks.complexity import CONSTANT, LINEAR

HASH_TABLE_SIZES = powers_of_two(32, 16384)


def sequential_items(size: int) -> list[tuple[int, str]]:
    """Return deterministic key-value pairs for hash table benchmarks."""
    return [(index, str(index)) for index in range(size)]


SUITE = BenchmarkSuite(
    name="hash-tables",
    cases=(
        # Example for future use:
        # BenchmarkCase(
        #     name="chained_hash_table insert",
        #     input_factory=sequential_items,
        #     operation=lambda items: build_chained_hash_table(items),
        #     sizes=HASH_TABLE_SIZES,
        #     expected_time=LINEAR,
        #     expected_space=LINEAR,
        # ),
        # BenchmarkCase(
        #     name="chained_hash_table lookup",
        #     input_factory=existing_table_and_keys,
        #     operation=lambda payload: lookup_all(payload),
        #     sizes=HASH_TABLE_SIZES,
        #     expected_time=LINEAR,  # n lookups at expected O(1) each
        #     expected_space=CONSTANT,
        # ),
    ),
)

__all__ = [
    "CONSTANT",
    "HASH_TABLE_SIZES",
    "LINEAR",
    "SUITE",
    "BenchmarkCase",
    "BenchmarkSuite",
    "sequential_items",
]
