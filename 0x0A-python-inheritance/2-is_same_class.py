#!/usr/bin/python3
"""
2-is_same_class.py

Brennan D Baraban <375@holbertonschool.com>
"""

def is_same_class(obj, a_class):
    """Check if an object is an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare the object's type to.

    Returns:
        True if obj is an instance of a_class, False otherwise.
    """
    return type(obj) == a_class
