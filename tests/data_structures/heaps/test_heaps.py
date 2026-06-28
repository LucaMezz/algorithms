from dataclasses import dataclass

import pytest
from hypothesis import given
from hypothesis import strategies as st

from algorithms.data_structures.heaps.min_heap import MinHeap


@dataclass
class HeapSpec:
    """Pairs a heap class with the sort order its extract() produces."""

    cls: type
    reverse: bool  # True for max-heap (extracts largest first)


HEAP_IMPLEMENTATIONS: list[HeapSpec] = [
    HeapSpec(cls=MinHeap, reverse=False),
    # HeapSpec(cls=MaxHeap, reverse=True),  # uncomment when implemented
]


@pytest.mark.parametrize("spec", HEAP_IMPLEMENTATIONS, ids=lambda s: s.cls.__name__)
class TestHeapBehaviour:
    def test_extract_order(self, spec: HeapSpec) -> None:
        values = [5, 1, 3, 2, 4]
        h = spec.cls()
        for v in values:
            h.insert(v)

        extracted = [h.extract() for _ in range(len(values))]
        assert extracted == sorted(values, reverse=spec.reverse)

    def test_peek_returns_next_without_removing(self, spec: HeapSpec) -> None:
        h = spec.cls()
        for v in [3, 1, 2]:
            h.insert(v)

        expected = sorted([3, 1, 2], reverse=spec.reverse)[0]
        assert h.peek() == expected
        assert h.size() == 3

    def test_size_tracks_inserts_and_extracts(self, spec: HeapSpec) -> None:
        h = spec.cls()
        assert h.size() == 0
        h.insert(1)
        assert h.size() == 1
        h.insert(2)
        assert h.size() == 2
        h.extract()
        assert h.size() == 1
        h.extract()
        assert h.size() == 0

    def test_is_empty(self, spec: HeapSpec) -> None:
        h = spec.cls()
        assert h.is_empty()
        h.insert(42)
        assert not h.is_empty()
        h.extract()
        assert h.is_empty()

    def test_single_element(self, spec: HeapSpec) -> None:
        h = spec.cls()
        h.insert(99)
        assert h.peek() == 99
        assert h.extract() == 99
        assert h.is_empty()

    def test_duplicate_values(self, spec: HeapSpec) -> None:
        values = [2, 2, 2, 1, 1]
        h = spec.cls()
        for v in values:
            h.insert(v)

        extracted = [h.extract() for _ in range(len(values))]
        assert extracted == sorted(values, reverse=spec.reverse)

    @given(st.lists(st.integers(), min_size=1))
    def test_sequential_extracts_are_sorted(
        self, spec: HeapSpec, values: list[int]
    ) -> None:
        h = spec.cls()
        for v in values:
            h.insert(v)

        extracted = [h.extract() for _ in range(len(values))]
        assert extracted == sorted(values, reverse=spec.reverse)

    @given(st.lists(st.integers(), min_size=1))
    def test_peek_matches_first_extract(
        self, spec: HeapSpec, values: list[int]
    ) -> None:
        h = spec.cls()
        for v in values:
            h.insert(v)

        assert h.peek() == h.extract()
