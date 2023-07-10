#!/usr/bin/python3
"""
Check if an object is an instance of a class that inherited
from a specified class.
"""


def inherits_from(obj, a_class):
    """Return True if the object is an instance of a class that
    inherited from the specified class, otherwise return False.
    """
    if issubclass(obj.__class__, a_class) and obj.__class__ is not a_class:
        return True
    else:
        return False

