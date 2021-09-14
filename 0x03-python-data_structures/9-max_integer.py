#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or my_list == []:
        return None
    else:
        num_max = my_list[0]
        for element in my_list:
            if element > num_max:
                num_max = element
        return num_max
