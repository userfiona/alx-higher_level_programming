#!/usr/bin/python3
"""
Square module
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize a Square object with the given size.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(self.__size, self.__size)
