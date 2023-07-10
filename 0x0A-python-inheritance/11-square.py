#!/usr/bin/python3
"""
More class base
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size):
        """Initialize a Square object with the given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """Return a formatted string representation of the Square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
