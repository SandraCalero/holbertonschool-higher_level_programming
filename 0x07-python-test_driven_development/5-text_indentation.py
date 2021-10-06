#!/usr/bin/python3
"""
text_indentation: prints a text with 2 new lines after each of
these characters: ., ? and :

text must be a string, otherwise raise a TypeError exception with the message:
text must be a string
There should be no space at the beginning or at the end of each printed line

Return: Nothing
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    Return: Nothing
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    delimiters = [".", "?", ":"]
    len_text = len(text)
    i = 0
    flag = 1
    while(i < len_text):
        if text[i] == " " and flag == 1:
            i += 1
            continue
        else:
            print("{}".format(text[i]), end='')
            flag = 0          
        if text[i] in delimiters:
            print('\n')
            flag = 1
        i += 1
