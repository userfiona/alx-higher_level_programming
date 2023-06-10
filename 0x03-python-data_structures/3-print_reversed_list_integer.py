#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    Prints the integers in a list in reverse order, with one integer per line.
    
    Args:
        my_list: The list of integers to be printed in reverse order.
    """
    if not my_list:
        return None
    my_list.reverse()
    for i in my_list:
        print("{:d}".format(i))
