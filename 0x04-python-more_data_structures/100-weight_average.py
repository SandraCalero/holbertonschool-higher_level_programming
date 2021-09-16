#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or my_list == []:
        return 0
    sum_product = 0
    weighted_average = 0
    for element in my_list:
        sum_product = sum_product + (element[0] * element[1])
        weighted_average = weighted_average + element[1]
    return sum_product / weighted_average
