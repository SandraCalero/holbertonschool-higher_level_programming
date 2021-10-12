#!/usr/bin/python3
"""Class MyInt that inherits from int"""


class MyInt(int):
    """Class MyInt that inherits from int and inverts == and !="""
    def __eq__(self, x):
        """"Overwrite eq magic method in subclass calling
            the oposit magic method of super class"""
        return super().__ne__(x)

    def __ne__(self, x):
        """"Overwrite ne magic method in subclass calling
            the oposit magic method of super class"""
        return super().__eq__(x)
