#!/usr/bin/python3
""" New class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square that inherist from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Class constructor """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ Returns printable string representation
        of an instance """
        return ("[{}] ({}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x,
            self.y, self.size))

    @property
    def size(self):
        """Size getter and setter"""
        return (self.width)

    @size.setter
    def size(self, value):
        """size getter and setter
        arg:
            value:its a value"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ This method assigns an argument to each attribute
        argument:
            args:argument
            kwargs:argument"""
        if args:
            for argmts in range(len(args)):
                if argmts == 0:
                    self.id = args[argmts]
                if argmts == 1:
                    self.size = args[argmts]
                if argmts == 2:
                    self.x = args[argmts]
                if argmts == 3:
                    self.y = args[argmts]

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Rectangle"""
        return ({'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y})
