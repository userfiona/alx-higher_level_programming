#!/usr/bin/python3
def add_attribute(an_obj, an_attr, a_value):
    """Adds a new attribute to an object if possible.

    Args:
        an_obj (object): Object to add the attribute to.
        an_attr (str): Name of the attribute.
        a_value (any): Value of the attribute to add.

    Raises:
        TypeError: If the object cannot have a new attribute.
    """
    if not hasattr(an_obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(an_obj, an_attr, a_value)
