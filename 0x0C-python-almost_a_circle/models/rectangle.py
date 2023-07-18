#!/usr/bin/python3
"""
Rectangle class based on the Base class
"""

import json
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle instance

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
            x (int): X-coordinate of the rectangle's position
            y (int): Y-coordinate of the rectangle's position
            id (int): ID of the rectangle

        Raises:
            TypeError: If width, height, x, or y is not an integer
            ValueError: If width, height, x, or y is invalid
        """
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, w):
        """Width setter

        Args:
            w (int): Width of the rectangle

        Raises:
            TypeError: If w is not an integer
            ValueError: If w <= 0
        """
        if not isinstance(w, int):
            raise TypeError("width must be an integer")
        elif w <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = w

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, h):
        """Height setter

        Args:
            h (int): Height of the rectangle

        Raises:
            TypeError: If h is not an integer
            ValueError: If h <= 0
        """
        if not isinstance(h, int):
            raise TypeError("height must be an integer")
        elif h <= 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = h

    @property
    def x(self):
        """X-coordinate getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """X-coordinate setter

        Args:
            x (int): X-coordinate value

        Raises:
            TypeError: If x is not an integer
            ValueError: If x < 0
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """Y-coordinate getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """Y-coordinate setter

        Args:
            y (int): Y-coordinate value

        Raises:
            TypeError: If y is not an integer
            ValueError: If y < 0
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """Calculate the area of the rectangle

        Returns:
            int: Area of the rectangle
        """
        return self.__height * self.__width

    def display(self):
        """Print the rectangle using '#'"""
        rect = self.__y * "\n"
        for i in range(self.__height):
            rect += (" " * self.__x)
            rect += ("#" * self.__width) + "\n"
        print(rect)

    def __str__(self):
        """Return a string representation of the rectangle

        Returns:
            str: String representation of the rectangle
        """
        return ("[Rectangle] {} {}/{} - {}/{}".format(self.id,
                                                      self.__x,
                                                      self.__y,
                                                      self.__width,
                                                      self.__height))

    def update(self, *args, **kwargs):
        """Update the attributes of the rectangle using non-keyworded arguments or keyword arguments

        Args:
            *args: Non-keyworded arguments (order: id, width, height, x, y)
            **kwargs: Keyword arguments (attribute name: value)
        """
        if args is not None and len(args) != 0:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Convert the object to a dictionary

        Returns:
            dict: Dictionary representation of the object
        """
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }