from typing import TypeVar

from algorithms.protocols import SupportsLessThan

T = TypeVar("T", bound=SupportsLessThan)


def insertion_sort(values: list[T]) -> None:
    r"""Sort the list of values into ascending order using insertion sort. Sorting is done inline.

    ``T`` can be any type that supports ``<`` comparison.
    See [SupportsLessThan][algorithms.protocols.SupportsLessThan].

    Args:
        values: A list of integer values.

    !!! complexity "Time complexity"
        $O(N)$ best-case, $O(N^2)$ worst-case, where N is the length of the list of values.
        The best-case occurs when the list of values is already sorted.
        In that case, the inner while loop never runs at all because the second
        condition is never true.
        Worst-case occurs when the list is in descending order.

    !!! complexity "Space complexity"
        $O(1)$ auxiliary space. Sorting is done inline.

    !!! property "Stability"
        Stable - Only adjacent values are ever swapped. Strict inequality is used so equal
        values are never swapped.

    !!! property "Online"
        Yes. Insertion sort can be implemented online: as each new value arrives,
        append it to the end of the list, then move it left until the sorted prefix
        is restored. This implementation is batch-oriented because it receives the
        full list upfront, but the underlying algorithm supports online sorting.
    """
    for i in range(1, len(values)):
        # Loop invariant:
        # values[0:i] is sorted.

        j = i
        while j > 0 and values[j] < values[j - 1]:
            values[j], values[j - 1] = values[j - 1], values[j]
            j -= 1

        # values[0:i+1] is sorted.
