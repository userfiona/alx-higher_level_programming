#!/usr/bin/python3
"""
Contains the "class_to_json" function.
"""


def class_to_json(obj):
    """
    Return the dictionary description with simple data structures
    (list, dictionary, string, integer, and boolean)
    for JSON serialization of an object.

    Args:
        obj (object): The object to convert to a dictionary.

    Returns:
        dict: The dictionary representation of the object.
    """
    return obj.__dict__
