#!/usr/bin/python3
# 3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    """Prints the integers in a list in reverse order, with one integer per line."""
    if not my_list:
        return None
    my_list.reverse()
    for i in my_list:
        print("{:d}".format(i))
