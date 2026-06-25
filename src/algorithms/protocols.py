"""Protocols defining structural contracts used across the algorithms package."""

from typing import Protocol, Self


class SupportsLessThan(Protocol):
    """Protocol for types that support the less-than (``<``) comparison operator.

    Any type that implements ``__lt__`` satisfies this protocol — built-in types
    such as ``int``, ``float``, and ``str`` all qualify.
    """

    def __lt__(self, other: Self, /) -> bool: ...
