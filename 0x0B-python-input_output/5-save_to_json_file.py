#!/usr/bin/python3
"""
File: 7-save_to_json_file.py
Functions:
    - save_to_json_file
"""

import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation.

    Args:
        my_obj (object): The object to write.
        filename (str): The name of the file to write to.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
