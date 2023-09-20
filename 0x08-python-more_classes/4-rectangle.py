#!/usr/bin/python3
"""Defines a Square class."""


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        super().__init__(size, size)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.width = value
        self.height = value

    def __str__(self):
        """Return the printable representation of the Square.
        Represents the square with the # character.
        """
        if self.width == 0 or self.height == 0:
            return ""

        square = []
        for i in range(self.height):
            [square.append('#') for j in range(self.width)]
            if i != self.height - 1:
                square.append("\n")
        return "".join(square)

    def __repr__(self):
        """Return the string representation of the Square."""
        return "Square({})".format(self.width)
