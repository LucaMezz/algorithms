from collections.abc import Callable
from typing import Any

import pytest
from hypothesis import given
from hypothesis import strategies as st

from algorithms.sorting import bubble_sort, selection_sort
from algorithms.sorting.heap_sort import heap_sort
from algorithms.sorting.insertion_sort import insertion_sort
from algorithms.sorting.merge_sort import merge_sort
from algorithms.sorting.quick_sort import quick_sort
from algorithms.sorting.sort_and_count_inversions import sort_and_count_inversions


def _as_inplace(fn: Callable[[list[Any]], list[Any]]) -> Callable[[list[Any]], None]:
    def wrapper(values: list[Any]) -> None:
        values[:] = fn(values)

    wrapper.__name__ = fn.__name__
    return wrapper


def _sort_and_count_inplace(values: list[Any]) -> None:
    values[:] = sort_and_count_inversions(values)[0]


_sort_and_count_inplace.__name__ = "sort_and_count_inversions"

SORTING_ALGORITHMS: list[Callable[[list[Any]], None]] = [
    bubble_sort,
    selection_sort,
    insertion_sort,
    _as_inplace(merge_sort),
    quick_sort,
    _as_inplace(heap_sort),
    _sort_and_count_inplace,
]


@pytest.mark.parametrize("sort", SORTING_ALGORITHMS, ids=lambda f: f.__name__)
class TestSorted:
    @pytest.mark.parametrize(
        "values",
        [
            [],
            [0],
            [1, 1, 1],
            [3, 2, 1],
            [1, 2, 3],
            [-3, -1, -2],
            [8, 2, 19, 5, 8, 9, 2, 35, 62, 5],
            [""],
            ["a"],
            ["a", "a"],
            ["a", "b", "c"],
            ["apple", "ape", "banana", "ban", "cow"],
            [-0.1, -0.3, 1, 3.4, 2.2, 0],
            [0.1],
            [0.1, -0.1],
            [0.1, 0.1, 0.1],
        ],
    )
    def test_sorts(self, sort: Callable[[list[Any]], None], values: list[Any]) -> None:
        actual = sorted(values)
        sort(values)
        assert values == actual


@pytest.mark.parametrize("sort", SORTING_ALGORITHMS, ids=lambda f: f.__name__)
class TestProperties:
    @given(st.lists(st.integers()))
    def test_result_is_correct(
        self, sort: Callable[[list[Any]], None], values: list[int]
    ) -> None:
        actual = sorted(values)
        sort(values)
        assert values == actual


class TestSortAndCountInversions:
    @pytest.mark.parametrize(
        ("values", "expected_inversions"),
        [
            ([], 0),
            ([0], 0),
            ([1, 1, 1], 0),
            ([3, 2, 1], 3),
            ([1, 2, 3], 0),
            ([-3, -1, -2], 1),
            ([8, 2, 19, 5, 8, 9, 2, 35, 62, 5], 16),
            ([""], 0),
            (["a"], 0),
            (["a", "a"], 0),
            (["a", "b", "c"], 0),
            (["apple", "ape", "banana", "ban", "cow"], 2),
            ([-0.1, -0.3, 1, 3.4, 2.2, 0], 5),
            ([0.1], 0),
            ([0.1, -0.1], 1),
            ([0.1, 0.1, 0.1], 0),
        ],
    )
    def test_inversion_count(self, values: list[Any], expected_inversions: int) -> None:
        _, inversions = sort_and_count_inversions(values)
        assert inversions == expected_inversions

    @given(st.lists(st.integers()))
    def test_inversion_count_matches_brute_force(self, values: list[int]) -> None:
        n = len(values)
        expected = sum(
            1 for i in range(n) for j in range(i + 1, n) if values[i] > values[j]
        )
        _, inversions = sort_and_count_inversions(values)
        assert inversions == expected
