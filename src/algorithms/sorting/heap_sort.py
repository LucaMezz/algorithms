from typing import TypeVar

from algorithms.data_structures.heaps import MinHeap
from algorithms.protocols import SupportsLessThan

T = TypeVar("T", bound=SupportsLessThan)


def heap_sort(values: list[T]) -> list[T]:
    r"""Sort the list of values into ascending order using heap sort.

    ``T`` can be any type that supports ``<`` comparison.
    See [SupportsLessThan][algorithms.protocols.SupportsLessThan].

    Args:
        values: A list of comparable values.

    !!! complexity "Time complexity"
        $O(N \log N)$ worst-case, where $N$ is the number of values in the list.
        The algorithm performs $N$ extract operations on the heap
        data structure, each of which is $O(\log N)$. Hence, in total we get a
        time complexity of $O(N \log N)$.

    !!! complexity "Space complexity"
        $O(N)$ space complexity. This could be $O(1)$, just need to ensure that
        Heap.build_from does not clone the input list.

    !!! property "Stability"
        Unstable.

    !!! property "Online"
        No - It needs the entire input upfront to build the heap before it can
        produce any output.
    """
    heap = MinHeap.build_from(values)
    return [heap.extract() for _ in range(len(values))]
