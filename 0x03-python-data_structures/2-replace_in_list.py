#!/usr/bin/python3
def replace_in_list(my_list, idx, element
    """ 
        
    Returns:
        The updated list after replacing the element, or the original list if the index is out of range.
    """ 
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
