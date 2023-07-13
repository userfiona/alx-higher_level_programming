#!/usr/bin/python3
"""Can I?"""


def add_attribute(obj, attr, value):
    """Can I?"""
    if not hasattr(obj, 'value') and not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    elif hasattr(obj, '__slot__') and not hasattr(obj, attr):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, value)
