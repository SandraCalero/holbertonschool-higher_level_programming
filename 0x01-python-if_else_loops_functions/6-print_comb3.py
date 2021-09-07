#!/usr/bin/python3
for first_num in range(0, 9):
    for second_num in range(1, 10):
        if first_num < second_num and first_num == 8 and second_num == 9:
            print("{:d}{:d}".format(first_num, second_num), end='\n')
        elif first_num < second_num:
            print("{:d}{:d}".format(first_num, second_num), end=', ')
