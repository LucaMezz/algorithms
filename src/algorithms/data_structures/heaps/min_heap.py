from collections.abc import Sequence
from typing import Self, TypeVar

from algorithms.adts.heap import Heap
from algorithms.protocols import SupportsLessThan

T = TypeVar("T", bound=SupportsLessThan)


class MinHeap(Heap[T]):
    """A min heap."""

    def __init__(self) -> None:
        self.values: list[T] = []

    def insert(self, value: T) -> None:
        r"""Insert a value into the heap.

        Inserts the value at the end of the internal array, furthest from
        the root. Then bubbles it upwards towards the root until it reaches
        a position where it no longer violates the heap property.

        Args:
            value: The value to insert.

        !!! compelxity "Time complexity"
            $O(\log N)$ where $N$ is the number of elements in the list.
            A heap is a *complete* binary tree. With $N$ nodes, its height is $O(\log N)$.
            Since the inserted value starts at a leaf, it can move upward by at most the
            height of the tree. So the number of swaps/comparisons is at most $O(\log N)$.

        !!! complexity "Space complexity"
            $O(1) auxiliary.
        """
        self.values.append(value)
        self._bubble_up(len(self.values) - 1)

    def extract(self) -> T:
        r"""Extract the smallest value from the heap.

        !!! compelxity "Time complexity"
            $O(\log N)$ where $N$ is the number of elements in the list.
            A heap is a *complete* binary tree. With $N$ nodes, its height is $O(\log N)$.
            Since the inserted value starts at a leaf, it can move upward by at most the
            height of the tree. So the number of swaps/comparisons is at most $O(\log N)$.

        !!! complexity "Space complexity"
            $O(1) auxiliary.
        """
        self._swap(0, len(self.values) - 1)
        value = self.values.pop()
        self._bubble_down(0)
        return value

    def peek(self) -> T:
        """Peek at the smallest value within the heap.

        Returns the value at index 0 within the internal values list, i.e. the root.
        By the heap property, this must always be the smallest value within the heap.

        !!! complexity "Time complexity"
            $O(1)$ worst-case.

        !!! complexity "Space complexity"
            $O(1)$ auxiliary.
        """
        return self.values[0]

    def size(self) -> int:
        """Get the number of elements within the heap.

        !!! complexity "Time complexity"
            $O(1)$ worst-case.

        !!! complexity "Space complexity"
            $O(1)$ auxiliary.
        """
        return len(self.values)

    def is_empty(self) -> bool:
        """Check if the heap is empty."""
        return len(self.values) == 0

    def _bubble_up(self, index: int) -> None:
        r"""Continuously swap node with its parent node until the node no longer violates the min heap property.

        !!! complexity "Time complexity"
            $O(\log N)$ worst-case, where $N$ is the number of values in the heap.

        !!! complexity "Space Complexity"
            $O(1)$ auxiliary.
        """
        curr = index

        while curr > 0 and self.values[self._parent(curr)] > self.values[curr]:
            self._swap(self._parent(curr), curr)
            curr = self._parent(curr)

    def _bubble_down(self, index: int = 0) -> None:
        r"""Continuously swap node with its child node of smallest value until the node no longer violates the min heap property.

        !!! complexity "Time complexity"
            $O(\log N)$ worst-case, where $N$ is the number of values in the heap.

        !!! complexity "Space Complexity"
            $O(1)$ auxiliary.
        """
        curr = index

        while True:
            left, right = 2 * curr + 1, 2 * curr + 2
            smallest = curr

            if left < len(self.values) and self.values[left] < self.values[smallest]:
                smallest = left
            if right < len(self.values) and self.values[right] < self.values[smallest]:
                smallest = right

            if smallest == curr:
                break

            self._swap(smallest, curr)
            curr = smallest

    def _swap(self, a: int, b: int) -> None:
        self.values[a], self.values[b] = self.values[b], self.values[a]

    @classmethod
    def build_from(cls, values: Sequence[T]) -> Self:
        """Build a new heap from an existing sequence of values."""
        raise NotImplementedError

    @classmethod
    def _parent(cls, child: int) -> int:
        return (child - 1) // 2
