#!/usr/bin/python3
"""
matrix_divided: divides all elements of a matrix.
matrix must be a list of lists of integers or floats, otherwise raise a
TypeError exception with the message matrix must be a matrix (list of lists)
of integers/floats
Each row of the matrix must be of the same size, otherwise raise a TypeError
exception with the message Each row of the matrix must have the same size
div must be a number (integer or float), otherwise raise a TypeError exception
with the message div must be a number
div can’t be equal to 0, otherwise raise a ZeroDivisionError exception with
the message division by zero
All elements of the matrix should be divided by div, rounded to 2 decimal
places
Return: a new matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix
    Return: a new matrix
    """
    err_message = 'matrix must be a matrix (list of lists) of integers/floats'
    if type(matrix) is not list:
        raise TypeError(err_message)
    for row in matrix:
        if type(row) is not list:
            raise TypeError(err_message)
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(err_message)
    length = len(matrix[0])
    for row in matrix:
        if len(row) != length:
            raise TypeError('Each row of the matrix must have the same size')
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    return [[round(element / div, 2)for element in row]for row in matrix]
