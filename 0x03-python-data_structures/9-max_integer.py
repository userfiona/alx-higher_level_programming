#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    Function that finds the maximum integer in a list.

    Args:
        my_list (list): The input list of integers.

    Returns:
        int: The maximum integer in the list, or None if the list is empty.

    """
    if len(my_list) < 1:
        return None
    sorted_list = my_list.copy()
    sorted_list.sort()
    return sorted_list[-1]
