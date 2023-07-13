#!/usr/bin/python3
"""Check if object is an instance of a class that
inherited from specified class"""


def inherits_from(obj, a_class):
    """Return True if object is an instance of a class that
    inherited from specified class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
