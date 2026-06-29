from collections.abc import Sequence
from typing import Self, TypeVar

from algorithms.adts.heap import Heap
from algorithms.protocols import SupportsLessThan

T = TypeVar("T", bound=SupportsLessThan)


def _parent(child: int) -> int:
    return (child - 1) // 2


class MaxHeap(Heap[T]):
    """A max heap."""

    def __init__(self) -> None:
        self._values: list[T] = []

    def insert(self, value: T) -> None:
        r"""Insert a value into the heap.

        Inserts the value at the end of the internal array, furthest from
        the root. Then bubbles it upwards towards the root until it reaches
        a position where it no longer violates the heap property.

        Args:
            value: The value to insert.

        !!! complexity "Time complexity"
            $O(\log N)$ where $N$ is the number of elements in the list.
            A heap is a *complete* binary tree. With $N$ nodes, its height is $O(\log N)$.
            Since the inserted value starts at a leaf, it can move upward by at most the
            height of the tree. So the number of swaps/comparisons is at most $O(\log N)$.

        !!! complexity "Space complexity"
            $O(1)$ auxiliary.
        """
        self._values.append(value)
        self._bubble_up(len(self._values) - 1)

    def extract(self) -> T:
        r"""Extract the largest value from the heap.

        !!! complexity "Time complexity"
            $O(\log N)$ where $N$ is the number of elements in the list.
            A heap is a *complete* binary tree. With $N$ nodes, its height is $O(\log N)$.
            Since the root is swapped to a leaf before removal, the new root may need to
            travel down by at most the height of the tree.

        !!! complexity "Space complexity"
            $O(1)$ auxiliary.
        """
        self._swap(0, len(self._values) - 1)
        value = self._values.pop()
        self._bubble_down(0)
        return value

    def peek(self) -> T:
        """Peek at the largest value within the heap.

        Returns the value at index 0 within the internal values list, i.e. the root.
        By the heap property, this must always be the largest value within the heap.

        !!! complexity "Time complexity"
            $O(1)$ worst-case.

        !!! complexity "Space complexity"
            $O(1)$ auxiliary.
        """
        return self._values[0]

    def size(self) -> int:
        """Get the number of elements within the heap.

        !!! complexity "Time complexity"
            $O(1)$ worst-case.

        !!! complexity "Space complexity"
            $O(1)$ auxiliary.
        """
        return len(self._values)

    def is_empty(self) -> bool:
        """Check if the heap is empty."""
        return len(self._values) == 0

    def _bubble_up(self, index: int) -> None:
        r"""Continuously swap node with its parent node until the node no longer violates the max heap property.

        !!! complexity "Time complexity"
            $O(\log N)$ worst-case, where $N$ is the number of values in the heap.

        !!! complexity "Space Complexity"
            $O(1)$ auxiliary.
        """
        curr = index

        while curr > 0 and self._values[_parent(curr)] < self._values[curr]:
            self._swap(_parent(curr), curr)
            curr = _parent(curr)

    def _bubble_down(self, index: int = 0) -> None:
        r"""Continuously swap node with its child node of largest value until the node no longer violates the max heap property.

        !!! complexity "Time complexity"
            $O(\log N)$ worst-case, where $N$ is the number of values in the heap.

        !!! complexity "Space Complexity"
            $O(1)$ auxiliary.
        """
        curr = index

        while True:
            left, right = 2 * curr + 1, 2 * curr + 2
            largest = curr

            if left < len(self._values) and self._values[left] > self._values[largest]:
                largest = left
            if (
                right < len(self._values)
                and self._values[right] > self._values[largest]
            ):
                largest = right

            if largest == curr:
                break

            self._swap(largest, curr)
            curr = largest

    def _swap(self, a: int, b: int) -> None:
        self._values[a], self._values[b] = self._values[b], self._values[a]

    @classmethod
    def build_from(cls, values: Sequence[T]) -> Self:
        """Build a new heap from an existing sequence of values using the heapify algorithm.

        !!! complexity "Time complexity"
            $O(N)$ worst-case, where $N$ is the number of values.

        !!! complexity "Space complexity"
            $O(1)$ auxiliary.
        """
        heap = cls()
        heap._values = list(values)
        end = len(values) - 1
        last = _parent(end)
        for i in range(last, -1, -1):
            heap._bubble_down(i)

        return heap
