"""Benchmark case definitions shared by benchmark suites."""

from __future__ import annotations

from collections.abc import Callable, Sequence
from dataclasses import dataclass
from typing import TypeAlias

from benchmarks.complexity import ComplexityModel

BenchmarkInput: TypeAlias = object
InputFactory: TypeAlias = Callable[[int], BenchmarkInput]
Operation: TypeAlias = Callable[[BenchmarkInput], object]


@dataclass(frozen=True)
class BenchmarkCase:
    """A single operation to measure across a range of input sizes."""

    name: str
    input_factory: InputFactory
    operation: Operation
    sizes: Sequence[int]
    expected_time: ComplexityModel
    expected_space: ComplexityModel | None = None
    repeats: int = 7
    warmups: int = 1

    def __post_init__(self) -> None:
        """Validate the case configuration."""
        if not self.name:
            msg = "benchmark case name must not be empty"
            raise ValueError(msg)
        if not self.sizes:
            msg = "benchmark case sizes must not be empty"
            raise ValueError(msg)
        if any(size <= 0 for size in self.sizes):
            msg = "benchmark case sizes must all be positive"
            raise ValueError(msg)
        if self.repeats <= 0:
            msg = "benchmark case repeats must be positive"
            raise ValueError(msg)
        if self.warmups < 0:
            msg = "benchmark case warmups must not be negative"
            raise ValueError(msg)


@dataclass(frozen=True)
class BenchmarkSuite:
    """A named group of benchmark cases."""

    name: str
    cases: Sequence[BenchmarkCase]

    def __post_init__(self) -> None:
        """Validate the suite configuration."""
        if not self.name:
            msg = "benchmark suite name must not be empty"
            raise ValueError(msg)


def powers_of_two(start: int, stop: int) -> tuple[int, ...]:
    """Return powers of two from start through stop, inclusive."""
    if start <= 0 or stop < start:
        msg = "expected 0 < start <= stop"
        raise ValueError(msg)

    sizes: list[int] = []
    value = start
    while value <= stop:
        sizes.append(value)
        value *= 2
    return tuple(sizes)
