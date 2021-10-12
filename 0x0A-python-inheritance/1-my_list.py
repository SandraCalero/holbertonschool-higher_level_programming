#!/usr/bin/python3
"""Module that containst a class MyList that inherits from list
    and Public instance method print_sorted(self) that prints the list,
    but sorted (ascending sort)"""


class MyList(list):
    """Class that inherits from list"""
    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))
