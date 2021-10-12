#!/usr/bin/python3
"""Class Square that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""
    def __init__(self, size):
        Rectangle.integer_validator(self, "size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
