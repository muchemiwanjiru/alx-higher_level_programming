#!/usr/bin/python3
"""module containing function find_peak"""


def find_peak(list_of_integers):
    """function finds a peak in a list of unsorted integers"""
    if not list_of_integers or list_of_integers == []:
        return None

    l = 0
    r = len(list_of_integers) - 1

    while l < r:
        mid = int((l + r) / 2)
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            r = mid
        else:
            l = mid + 1

    return list_of_integers[l]
