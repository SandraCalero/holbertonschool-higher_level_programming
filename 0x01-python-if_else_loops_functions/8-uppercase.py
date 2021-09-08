#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            char_str = ord(str[i]) - 32
        else:
            char_str = ord(str[i])
        print("{}".format(chr(char_str)), end='')
    print("{}".format(''), end='\n')
