#!/usr/bin/python3
def search_replace(my_list, search, replace):

    """Replaces all occurrences of an element by another in a new list.
    - my_list: the initial list
    - search: the element to replace in the list
    - replace: the new element"""
    if my_list is None:
        return None
    elif search <= 0 or search > len(my_list):
        return my_list
    else:
        return[replace if elem == search else elem for elem in my_list]

# The explicit way is (starting on line 13):
#        new_list = []
#        for element in my_list:
#            if element == search:
#                element = replace
#            else:
#                element
#            new_list.append(element)
#        return new_list
#
# Note: the variable elem correspond to element
