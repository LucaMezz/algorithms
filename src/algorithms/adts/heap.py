from abc import ABC, abstractmethod
from collections.abc import Sequence
from typing import Generic, Self, TypeVar

from algorithms.protocols import SupportsLessThan

T = TypeVar("T", bound=SupportsLessThan)


class Heap(ABC, Generic[T]):
    """A heap ADT."""

    def __init__(self) -> None:
        self.values: list[T] = []

    @abstractmethod
    def insert(self, value: T) -> None:
        r"""Insert a value into the heap.

        Args:
            value: The value to insert.

        """
        ...

    @abstractmethod
    def extract(self) -> T:
        r"""Extract the next value from the heap."""
        ...

    @abstractmethod
    def peek(self) -> T:
        """Peek at the next value within the heap."""
        ...

    @abstractmethod
    def size(self) -> int:
        """Get the number of elements within the heap."""
        ...

    @abstractmethod
    def is_empty(self) -> bool:
        """Check if the heap is empty."""
        ...

    @classmethod
    @abstractmethod
    def build_from(cls, values: Sequence[T]) -> Self:
        """Build a new heap from an existing sequence of values."""
        ...
