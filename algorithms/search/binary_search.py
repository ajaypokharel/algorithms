"""
This algorithm is for binary search. This only works for sorted arrays or lists.
"""


def search(lst, x):
    if len(lst) == 1:
        return 0
    first = 0
    last = len(lst) - 1
    mid = (first + last) // 2
    i = 0
    while i < len(lst) - 1:
        if lst[mid] == x:
            return mid
        elif lst[mid] > x:
            mid = mid - 1
        elif lst[mid] < x:
            mid = mid + 1
        i += 1
    return -1


# binary search with recursion
def search_recursive(lst, first, last, x):
    if first > last:
        mid = (first + last) // 2
        if lst[mid] == x:
            return mid
        elif lst[mid] > x:
            return search_recursive(lst, first, mid - 1, x)
        elif lst[mid] < x:
            return search_recursive(lst, mid + 1, last, x)
    else:
        return -1


def search_2(lst, x):
    first = 0
    last = len(lst) - 1
    return search_recursive(lst, first, last, x)

