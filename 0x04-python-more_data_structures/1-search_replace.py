#!/usr/bin/python3
def search_replace(my_list, search, replace):

    """Replaces all occurrences of an element by another in a new list.
    - my_list: the initial list
    - search: the element to replace in the list
    - replace: the new element"""
    if my_list is None:
        return None
    elif search < 0 or search > len(my_list):
        return my_list
    else:
        new_list = my_list[:]
        new_list[search - 1] = replace
        return new_list
