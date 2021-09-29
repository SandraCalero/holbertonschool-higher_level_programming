#!/usr/bin/python3
"""Class that defines a square"""


class Square:
    """Defines the object of class square"""
    def __init__(self, size=0, position=(0, 0)):
        """Defines the squere atributes"""
        self.__size = size
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__position = position
        if type(position) is not tuple or len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        if position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')

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

    @property
    def position(self):
        """Gets the square position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the squere position"""
        if type(value) is not tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        """Calculates the squere area"""
        square_area = self.__size * self.__size
        return square_area

    def my_print(self):
        """Prints a square with '#' character"""
        if self.__size == 0:
            print("")
        else:
            square_row = '#' * self.__size
            square_position = ' ' * self.__position[0]
            for space in range(0, self.__position[1]):
                print("")
            else:
                for i in range(0, self.__size):
                    print("{}{}".format(square_position, square_row))
