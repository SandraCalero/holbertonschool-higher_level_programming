#!/usr/bin/python3
def roman_to_int(roman_string):
    num_directory = {'I': 1, 'V': 5, 'X': 10,
                     'L': 50, 'C': 100, 'D': 500, 'M': 100}
    num_list = []
    for key in roman_string:
        num_list.append(num_directory[key])
    num_list.reverse()
    i = 0
    sum = num_list[0]
    while(i < len(num_list) - 1):
        if(num_list[i] > num_list[i + 1]):
            sum = sum - num_list[i+1]
        else:
            sum = sum + num_list[i+1]
    return sum