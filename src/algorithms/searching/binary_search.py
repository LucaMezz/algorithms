from collections.abc import Sequence
from typing import Literal


def binary_search(
    values: Sequence[int],
    key: int,
    *,
    missing: Literal["raise", "negative", "insertion_index"] = "raise",
) -> int:
    """Search the given values for for the key.

    Args:
        values: A sorted list of values.
        key: The key to search for.
        missing: What to do if the key is not found within the values.

    Returns:
        The index of the key in the sequence, if found. Otherwise -1 if
        missing is "negative". Otherwise the index where the key would
        be located at if it were in the sorted values if missing is
        "insertion_index".

    Raises:
        KeyError if the key was not found and missing is set to "raise".

    Time complexity:
        O(log N) where N is the length of the values sequence.

    Space complexity:
        O(1) auxiliary space.

    """
    lo = 0
    hi = len(values) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        x = values[mid]
        if x < key:
            lo = mid + 1
        elif x > key:
            hi = mid - 1
        else:
            return mid

    if missing == "raise":
        raise KeyError(f"Key {key} was not found.")

    if missing == "negative":
        return -1

    return lo
