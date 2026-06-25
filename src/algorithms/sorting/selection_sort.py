def selection_sort(values: list[int]) -> None:
    r"""Sort the list of values into ascending order. Sorting is done inline.

    Args:
        values: A list of integer values.

    !!! complexity "Time complexity"
        $O(N^2)$ worst case, where $N$ is the length of the list of values.

    !!! complexity "Space complexity"
        $O(1) auxiliary. Sorting is done inline.
    """
    n = len(values)

    for k in range(n):
        # Loop invariant:
        # values[0:k] is sorted
        min_value = values[k]
        min_index = k
        for i in range(k + 1, n):
            if values[i] < min_value:
                min_value = values[i]
                min_index = i
        values[k], values[min_index] = values[min_index], values[k]
        # values[0:k+1] is sorted


if __name__ == "__main__":
    values = [7, 2, 8, 2, 4, 8, 2, 10, 37, 1, 45, 23]
    selection_sort(values)
    print(values)
