#!/usr/bin/python3
"""Function that adds a new attribute to an object if it’s possible"""


def add_attribute(obj, key, value):
    """add_attribute - adds a new attribute to an object if it’s possible

    Args:
        obj (class): Object to add attribute
        key (string): key of attribute
        value (string): value of attribute
    """
    if "__dict__" in dir(obj):
        setattr(obj, key, value)
    else:
        raise TypeError("can't add new attribute")
