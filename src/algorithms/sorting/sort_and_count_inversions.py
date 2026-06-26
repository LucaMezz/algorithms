from typing import TypeVar

from algorithms.protocols import SupportsLessThan

T = TypeVar("T", bound=SupportsLessThan)


def sort_and_count_inversions(values: list[T]) -> tuple[list[T], int]:
    r"""Sort values into ascending order and count inversions using merge sort.

    ``T`` can be any type that supports ``<`` comparison.
    See [SupportsLessThan][algorithms.protocols.SupportsLessThan].

    Args:
        values: A list of comparable values.

    !!! complexity "Time complexity"
        $O(N log N) worst-case, where N is the number of elements in the ``values`` list.
        We can model the time complexity as a recurrence relation:
        $T(N) = 2T(N/2) + O(1))$. This is because a call to sort_and_count_inversions recursively
        calls itself twice, but each on an input list which is half the size. In addition
        to that, a constant amount of work is done at each call. Solving this recurrence
        relation yields T(N) = O(N log N).

    !!! complexity "Space complexity"
        $O(N)$ auxiliary, where N is the number of elements in the ``values`` list.

    !!! property "Stability"
        Yes - When merging sorted lists, we always take from the left
        list whenever elements are equal. This maintains the relative
        ordering of elements.

    !!! property "Online"
        No
    """
    if len(values) <= 1:
        return values, 0
    mid = len(values) // 2
    left, left_inversions = sort_and_count_inversions(values[:mid])
    right, right_inversions = sort_and_count_inversions(values[mid:])
    result, inversions = merge_and_count_split_inversions(left, right)
    return result, inversions + left_inversions + right_inversions


def merge_and_count_split_inversions(a: list[T], b: list[T]) -> tuple[list[T], int]:
    r"""Merge two sorted lists into a single sorted list, and count inversions."""
    i, j = 0, 0
    inversions = 0
    result = []
    while i < len(a) and j < len(b):
        if b[j] < a[i]:
            result.append(b[j])
            j += 1
            inversions += len(a) - i
        else:
            # Whenever elements are equal, always take from the left
            # to maintain stability / relative ordering of equal elements.
            result.append(a[i])
            i += 1
    result += a[i:]
    result += b[j:]
    return result, inversions
