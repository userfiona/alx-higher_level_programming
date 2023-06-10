#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
     """
    Replaces an element in a list at a specific position.

    Args:
        my_list: The list in which the element needs to be replaced.
        idx: The index position at which the element should be replaced.
        element: The new element to replace the existing one.

        Returns:
        The updated list after replacing the element, or the original list if the index is out of range.
         """

    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_listi
