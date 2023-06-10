#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    Write a function that replaces an element in a list at a specific position without modifying the original list.

    Args:
        my_list: The original list.
        idx: The index position at which the element should be replaced.
        element: The new element to replace the existing one.

    Returns:
        A new list with the specified element replaced at the given index, or a copy of the original list if the index is out of range.
    """
    if my_list:
        if idx < 0:
            return my_list
        elif idx > len(my_list) - 1:
            return my_list
        else:
            new_list = my_list[:]
            new_list[idx] = element
            return new_list
