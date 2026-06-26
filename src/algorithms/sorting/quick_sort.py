from random import randrange
from typing import TypeVar

from algorithms.protocols import SupportsLessThan

T = TypeVar("T", bound=SupportsLessThan)


def quick_sort(values: list[T]) -> None:
    r"""Sort the list of values into ascending order using quick sort.

    ``T`` can be any type that supports ``<`` comparison.
    See [SupportsLessThan][algorithms.protocols.SupportsLessThan].

    Args:
        values: A list of comparable values.

    !!! complexity "Time complexity"

    !!! complexity "Space complexity"
        $O(1)$ auxiliary. Sorting is done inline.

    !!! property "Stability"
        No - this implementation is not stable because sorting is done
        inline. However, the algorithm can be implemented to be stable
        when not implemented inline by partitioning into three lists,
        less than the pivot, equal to the pivot, and greater than the
        pivot.

    !!! property "Online"
        No
    """
    _quick_sort_aux(values, 0, len(values))


def _quick_sort_aux(values: list[T], start: int, end: int) -> None:
    if end - start <= 1:
        return
    pivot = randrange(start, end)

    values[pivot], values[start] = values[start], values[pivot]

    i = start + 1
    for j in range(start + 1, end):
        if values[j] < values[start]:
            values[i], values[j] = values[j], values[i]
            i += 1

    values[start], values[i - 1] = values[i - 1], values[start]

    _quick_sort_aux(values, start, i - 1)
    _quick_sort_aux(values, i, end)
