#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    """Defines a rectangle class"""
    number_of_instances = 0

    def __str__(self):
        """Prints a rectangle with '#' character"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle_row = ('#' * self.__width)
            string = ""
            for i in range(0, self.__height):
                string = string + rectangle_row
                if i < self.__height - 1:
                    string = string + '\n'
            return string

    def __repr__(self):
        """Creates a new instance of rectangle class"""
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __init__(self, width=0, height=0):
        """Constructor of rectangle class"""
        Rectangle.number_of_instances += 1
        self.check_width(width)
        self.check_height(height)

    def __del__(self):
        """Deletes the instance of rectangle class"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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

    def area(self):
        """Calculates rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

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
