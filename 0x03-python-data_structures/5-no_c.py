#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return None
    new_string = ''
    for idx in my_string:
        if idx == 'c' or idx == 'C':
            continue
        new_string = new_string + idx
    return new_string
