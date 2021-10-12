#!/usr/bin/python3
"""Function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added"""


def append_write(filename="", text=""):
    """append_write - appends a string at the end of a text file (UTF8)
        Return: The number of characters added"""
    with open(filename, mode="a", encoding="UTF8") as file:
        num_chars_written = file.write(text)
        return num_chars_written
