from typing import TypeVar

from algorithms.protocols import SupportsLessThan

T = TypeVar("T", bound=SupportsLessThan)


def bubble_sort(values: list[T]) -> None:
    r"""Sort the list of values into ascending order. Sorting is done inline.

    ``T`` can be any type that supports ``<`` comparison.
    See [SupportsLessThan][algorithms.protocols.SupportsLessThan].

    Args:
        values: A list of comparable values.

    !!! complexity "Time complexity"
        $O(N^2)$, where N is the length of the list of values.
        The algorithm always iterates over the entire list of values N unique times.

    !!! complexity "Space complexity"
        $O(1)$ auxiliary. Sorting is done inline.

    !!! property "Stability"
        Stable - Swaps only occur between adjacent values. Since we use strict
        inequality, two equal values will never be swapped.
    """
    n = len(values)
    for _ in range(1, n):
        for i in range(1, n):
            if values[i - 1] > values[i]:
                values[i - 1], values[i] = values[i], values[i - 1]
