#!/usr/bin/python3
"""Function that writes an Object to a text file,
using a JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file - writes an Object to a text file,
    using a JSON representation"""
    with open(filename, mode="w") as file:
        return json.dump(my_obj, file)
