from collections.abc import Sequence
from typing import Protocol, Self, TypeVar


class _SupportsLessThan(Protocol):
    def __lt__(self, other: Self, /) -> bool: ...


T = TypeVar("T", bound=_SupportsLessThan)


def binary_search(
    values: Sequence[T],
    key: T,
) -> int | None:
    r"""Search the given sorted sequence for the key.

    Args:
        values: A **sorted** sequence of comparable values. Passing an
            unsorted sequence produces undefined behaviour.
        key: The key to search for. If the sequence contains duplicates,
            the index of an arbitrary match is returned.

    Returns:
        The index of the key in the sequence, or ``None`` if not found.

    Time complexity:
        $O(\log N)$ worst case, where $N$ is the length of the ``values`` sequence.

    Space complexity:
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
