#!/usr/bin/python3
"""Define a class"""


class Rectangle:
    """Represents a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialize a new rectangle

        Args:
            width (int): width of the new rectangle
            height (int): height of the new rectangle
        """
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    def area(self):
        """
        Calculate the area of a rectangle instance
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of a rectangle instance
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return the string representation of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ''
        return (str(self.print_symbol) * self.__width + '\n') * self.__height

    def __repr__(self):
        """
        Return a string representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Properly delete an instance of the class
        """
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
