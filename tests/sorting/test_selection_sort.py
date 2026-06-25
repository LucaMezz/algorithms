import pytest
from hypothesis import given
from hypothesis import strategies as st

from algorithms.sorting import selection_sort


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
    def test_sorts(self, values: list[int]) -> None:
        actual = sorted(values)
        selection_sort(values)
        assert values == actual


class TestProperties:
    @given(st.lists(st.integers()))
    def test_result_is_correct(self, values: list[int]) -> None:
        actual = sorted(values)
        selection_sort(values)
        assert values == actual
