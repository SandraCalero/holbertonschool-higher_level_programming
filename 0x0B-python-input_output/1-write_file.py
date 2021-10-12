#!/usr/bin/python3
"""Function that writes a string to a text file (UTF8) and
    returns the number of characters written"""


def write_file(filename="", text=""):
    """write_file - writes a string to a text file (UTF8)
        Return: The number of characters written"""
    with open(filename, mode="w", encoding="UTF8") as file:
        number_of_chars_written = file.write(text)
        return number_of_chars_written
