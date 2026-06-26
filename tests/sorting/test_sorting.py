from collections.abc import Callable
from typing import Any

import pytest
from hypothesis import given
from hypothesis import strategies as st

from algorithms.sorting import bubble_sort, selection_sort
from algorithms.sorting.insertion_sort import insertion_sort
from algorithms.sorting.quick_sort import quick_sort

SORTING_ALGORITHMS: list[Callable[[list[Any]], None]] = [
    bubble_sort,
    selection_sort,
    insertion_sort,
    quick_sort,
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
