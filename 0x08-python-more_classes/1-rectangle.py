#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    """Defines a rectangle class"""

    def __init__(self, width=0, height=0):
        """Constructor of rectangle class"""
        self.check_width(width)
        self.check_height(height)

    @property
    def width(self):
        """Gets width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width value"""
        self.check_width(value)

    @property
    def height(self):
        """Gets height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height value"""
        self.check_height(value)

    def check_width(self, width):
        """Checks type and value of property width"""
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    def check_height(self, height):
        """Checks type and value of property height"""
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height
