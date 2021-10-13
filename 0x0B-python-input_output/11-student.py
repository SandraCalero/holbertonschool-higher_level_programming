#!/usr/bin/python3
""" Student class module
"""


class Student:
    """ Student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list:
            if all(isinstance(element, str) for element in attrs):
                dict = {}
                for element in attrs:
                    if element in self.__dict__:
                        dict[element] = getattr(self, element)
                return dict
        return vars(self)

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
