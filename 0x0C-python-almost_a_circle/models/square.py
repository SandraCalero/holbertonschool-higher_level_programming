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
        self.width = value
        self.height = value

    def __str__(self):
        """Returns [Square] (<id>) <x>/<y> - <size>"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                         self.y, self.width)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if len(args) > 0:
            list_values = []
            list_key = ["id", "size", "x", "y"]
            dictionary = {"id": self.id, "size": self.width,
                          "x": self.x, "y": self.y}
            for num in args:
                list_values.append(num)
            size_list = len(list_values)
            i = 0
            while i < size_list:
                dictionary[list_key[i]] = list_values[i]
                i += 1
            for key, value in dictionary.items():
                setattr(self, key, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        list_key = ["id", "size", "x", "y"]
        return {key: getattr(self, key) for key in list_key}
