#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Function that deletes the element at a specific index in a list.

    Args:
        my_list (list): The input list.
        idx (int): The index of the element to be deleted.

    Returns:
        list: The modified list after deleting the element at the specified index.
            If the index is out of range or negative, the original list is returned.

    """
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        del my_list[idx]
        return my_list
