"""
this algorithm is for linear searching in Python
"""


def search(lst, x):
    for i in range(len(lst)):
        if x == lst[i]:
            return i
    return -1
