"""
This is the code for interpolation search. This also only works with a sorted array.
"""


def interpolation_search(arr, low, high, x):
    if low <= high and arr[low] <= x <= arr[high]:

        pos = low + ((high - low) // (arr[high] - arr[low]) *
                     (x - arr[low]))

        if arr[pos] == x:
            return pos

        if arr[pos] < x:
            return interpolation_search(arr, pos + 1,
                                        high, x)

        if arr[pos] > x:
            return interpolation_search(arr, low,
                                        pos - 1, x)
    return -1
