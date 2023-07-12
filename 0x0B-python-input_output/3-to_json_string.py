#!/usr/bin/python3
"""
Defines a function to convert an object to its JSON representation.
"""

import json


def to_json_string(my_obj):
    """Return the JSON representation of an object.

    Args:
        my_obj: The object to convert to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
