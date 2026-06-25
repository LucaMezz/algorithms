from collections.abc import Sequence
from typing import TypeVar

from algorithms.protocols import SupportsLessThan

T = TypeVar("T", bound=SupportsLessThan)


def binary_search(
    values: Sequence[T],
    key: T,
) -> int | None:
    r"""Search the given sorted sequence for the key.

    ``T`` can be any type that supports ``<`` comparison.
    See [SupportsLessThan][algorithms.protocols.SupportsLessThan].

    Args:
        values: A **sorted** sequence of comparable values. Passing an
            unsorted sequence produces undefined behaviour.
        key: The key to search for. If the sequence contains duplicates,
            the index of an arbitrary match is returned.

    Returns:
        The index of the key in the sequence, or ``None`` if not found.

    !!! complexity "Time complexity"
        $O(\log N)$ worst case, where $N$ is the length of the ``values`` sequence.

    !!! complexity "Space complexity"
        $O(1)$ auxiliary space.

    """
    lo = 0
    hi = len(values) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        x = values[mid]
        if key < x:
            hi = mid - 1
        elif x < key:
            lo = mid + 1
        else:
            return mid

    return None
