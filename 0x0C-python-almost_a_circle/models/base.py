#!/usr/bin/python3
"""Module base.py contain the class that is the “base” of all other classes"""


class Base:
    """Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor of instances of Base class

        Args:
            id (int): Identification number of each instance.
            Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
