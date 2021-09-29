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

    @property
    def size(self):
        """Gets the squere size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the squere size"""
        self.__size = value
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """Calculates the squere area"""
        square_area = self.__size * self.__size
        return square_area

    def my_print(self):
        """Prints in stdout the square with '#' character"""
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__size):
                print ("{}".format('#' * self.__size))
