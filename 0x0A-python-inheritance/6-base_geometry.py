#!/usr/bin/python3
"""
Module creating a class.
"""


class BaseGeometry:
    """
    BaseGeometry class.
    """
    def area(self):
        """
        Calculate the area.

        Raises:
            Exception: If the area method is not implemented.

        Returns:
            None
        """
        raise Exception("area() is not implemented")
