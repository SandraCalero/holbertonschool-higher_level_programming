#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    if isinstance(list_of_integers, list) and len(list_of_integers) > 0:
        list_of_integers.sort()
        return list_of_integers[-1]
    return None
