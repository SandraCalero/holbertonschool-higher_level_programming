#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    num = -1
    while num >= (len(my_list) * (-1)):
        print("{:d}".format(my_list[num]))
        num = num - 1
