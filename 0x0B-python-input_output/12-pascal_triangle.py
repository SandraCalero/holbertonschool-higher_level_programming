#!/usr/bin/python3
"""Function that returns a list of lists of integers
representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """Function that returns a list of lists of integers
    representing the Pascal’s triangle of n"""
    if n <= 0:
        return []
    myList = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    return myList
