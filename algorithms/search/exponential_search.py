"""
This is the code for exponential_search.
"""


def binary_search(arr, left, right, x):

    if right >= left:
        mid = left + (right - left) / 2

        if arr[mid] == x:
            return mid

        if arr[mid] > x:
            return binary_search(arr, left,
                                 mid - 1, x)

        return binary_search(arr, mid + 1, right, x)

    return -1


def exponential_search(arr, n, x):
    if arr[0] == x:
        return 0

    i = 1
    while i < n and arr[i] <= x:
        i = i * 2

    return binary_search(arr, i / 2,
                         min(i, n - 1), x)
