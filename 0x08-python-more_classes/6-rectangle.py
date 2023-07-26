#!/usr/bin/python3
"""
6-rectangle: class Rectangle
"""


class Rectangle:
    """
    Class Rectangle defines a rectangle.

    Attributes:
        width (int): width of the rectangle.
        height (int): height of the rectangle.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter function for private attribute width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter function for private attribute width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter function for private attribute height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter function for private attribute height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.__width + self.__height) if self.__width and self.__height else 0

    def __str__(self):
        """Return a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return (("#" * self.__width + "\n") * self.__height).strip()

    def __repr__(self):
        """Return a string representation of the rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Properly delete the instance of a class."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
