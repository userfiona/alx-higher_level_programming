#!/usr/bin/python3
def no_c(my_string):
    """Can you C me now"""
    new_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_strinig
