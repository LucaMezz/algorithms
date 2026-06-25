import pytest
from hypothesis import given
from hypothesis import strategies as st

from algorithms.searching import binary_search


class TestFound:
    @pytest.mark.parametrize(
        ("values", "key", "expected"),
        [
            ([1, 2, 3], 1, 0),
            ([1, 2, 3], 2, 1),
            ([1, 2, 3], 3, 2),
            ([42], 42, 0),
            (list(range(10_000)), 8000, 8000),
        ],
    )
    def test_returns_index(self, values: list[int], key: int, expected: int) -> None:
        assert binary_search(values, key) == expected


class TestNotFound:
    @pytest.mark.parametrize(
        ("values", "key"),
        [
            ([], 1),
            ([3], 5),
            ([1, 2, 3], 0),
            ([1, 2, 3], 4),
            ([1, 3, 5], 2),
        ],
    )
    def test_returns_none(self, values: list[int], key: int) -> None:
        assert binary_search(values, key) is None


class TestTypes:
    def test_strings(self) -> None:
        assert binary_search(["apple", "banana", "cherry"], "banana") == 1

    def test_floats(self) -> None:
        assert binary_search([1.0, 2.5, 3.7], 2.5) == 1
        assert binary_search([1.0, 2.5, 3.7], 3) is None


class TestProperties:
    @given(st.lists(st.integers()).map(sorted), st.integers())
    def test_result_is_correct(self, values: list[int], key: int) -> None:
        idx = binary_search(values, key)
        if idx is None:
            assert key not in values
        else:
            assert values[idx] == key
