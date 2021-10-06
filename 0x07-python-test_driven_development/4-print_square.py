#!/usr/bin/python3
"""
print_square: prints a square with the character #.
size is the size length of the square
size must be an integer, otherwise raise a TypeError exception with the
message: size must be an integer
if size is less than 0, raise a ValueError exception with the message:
size must be >= 0
if size is a float and is less than 0, raise a TypeError exception with the
message: size must be an integer
Return: Nothing
"""


def print_square(size):
    """
    Prints a square with the character #.
    Return: Nothing
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    square = '#' * size
    for i in range(0, size):
        print(square)
