#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return None
    new_string = ''
    for element in my_string:
        if element == 'c' or element == 'C':
            continue
        new_string = new_string + element
    return new_string
