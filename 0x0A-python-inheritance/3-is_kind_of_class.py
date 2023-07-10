#!/usr/bin/python3
"""
Module containing is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or if the object is an instance
    of a class that inherited from the specified class.

    Args:
        obj (object): The object to check.
        a_class (class): The class to compare the object's type to.

    Returns:
        True if the object is an instance of the class or its subclass,
        otherwise False.
    """
    return isinstance(obj, a_class)
