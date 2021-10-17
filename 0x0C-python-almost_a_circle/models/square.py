#!/usr/bin/python3
"""Module square.py that contains class Square
that inherits from Rectangle
"""

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class

    Args:
        Rectangle (rectangle): Super class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor of instanses of Square class

        Args:
            size (int): Size of the square
            x (int): Horizontal location of the rectangle. Defaults to 0.
            y (int): Vertical location of the rectangle. Defaults to 0.
            id (int): Identification number of each instance. Defaults to None.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """get size"""
        return self.width

    @size.setter
    def size(self, value):
        """set size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.__size = value

    def __str__(self):
        """Returns [Square] (<id>) <x>/<y> - <size>"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                         self.y, self.__size)
