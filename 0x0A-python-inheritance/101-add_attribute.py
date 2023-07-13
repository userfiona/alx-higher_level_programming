#!/usr/bin/python3
"""
function to add attribute to an object
if its possible
"""


def add_attribute(obj, attr, value):
    """
    adds a new attribute to an object if it’s possible
    :param obj:
    :param attr:
    :param value:
    :return: raises typeerror or setattr
    """
    if not hasattr(obj, 'value') and not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    elif hasattr(obj, '__slot__') and not hasattr(obj, attr):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, value)
