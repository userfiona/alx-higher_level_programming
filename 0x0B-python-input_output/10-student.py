#!/usr/bin/python3
"""
Module 10-student.py
Creates a student class (based on 9-student.py)
"""


class Student:
    """Class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): List of attributes to include in the dictionary.
                Defaults to None.

        Returns:
            dict: Dictionary representation of the Student instance.
        """
        my_dict = {}
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            for x in attrs:
                if x in self.__dict__:
                    my_dict[x] = self.__dict__[x]
            return my_dict
        return self.__dict__.copy()
