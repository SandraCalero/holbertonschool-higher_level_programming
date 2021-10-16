#!/usr/bin/python3
"""Module rectangle.py that contains class Rectangle
that inherits from Base
"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class

    Args:
        Base ([base]): Super class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor of instanses of Rectangle class

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
            x (int): Horizontal location of the rectangle. Defaults to 0.
            y (int): Vertical location of the rectangle. Defaults to 0.
            id (int): Identification number of each instance. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #
        by taking care of x and y"""
        space = ' ' * self.__x
        drawn_rectangle = space + ('#' * self.__width)
        for line in range(0, self.__y):
            print()
        for row in range(0, self.__height):
            print(drawn_rectangle)

    def __str__(self):
        """Returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.__x,
                                                                 self.__y,
                                                                 self.__width,
                                                                 self.__height)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if len(args) > 0:
            list_values = []
            list_key = ["id", "width", "height", "x", "y"]
            dictionary = {"id": self.id, "width": self.__width,
                          "height": self.__height, "x": self.__x,
                          "y": self.__y}
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
