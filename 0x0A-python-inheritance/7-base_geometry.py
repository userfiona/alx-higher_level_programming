#!/usr/bin/python3
"""Module defining the BaseGeometry class."""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Raises an exception."""
        raise NotImplementedError("area() is not implemented")

    @staticmethod
    def integer_validator(name, value):
        """Validates that the value is an integer greater than 0."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
