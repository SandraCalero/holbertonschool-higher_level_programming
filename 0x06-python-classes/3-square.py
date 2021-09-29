#!/usr/bin/python3
"""Class that defines a square"""


class Square:
    """Defines the object of class square"""
    def __init__(self, size=0):
        """Defines the squere atributes"""
        self.__size = size
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """Calculates the squere area"""
        square_area = self.__size * self.__size
        return square_area
