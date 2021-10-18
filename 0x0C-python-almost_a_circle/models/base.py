#!/usr/bin/python3
"""Module base.py contain the class that is the “base” of all other classes"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        list_dictionary_objects = []
        if list_objs is not None:
            for object in list_objs:
                list_dictionary_objects.append(cls.to_dictionary(object))
        filename = cls.__name__ + ".json"
        json_dictionary = cls.to_json_string(list_dictionary_objects)
        with open(filename, mode="w") as json_file:
            json_file.write(json_dictionary)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(5, 8, 6)
            dummy_instance.update(**dictionary)
            return dummy_instance
        if cls.__name__ == "Square":
            dummy_instance = cls(8)
            dummy_instance.update(**dictionary)
            return dummy_instance        

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        try:
            filename = cls.__name__ + ".json"
            with open(filename, mode="r") as file:
                list_dictionary = cls.from_json_string(file.read())
            return [cls.create(**dictionary) for dictionary in list_dictionary]
        except FileNotFoundError:
            return []
