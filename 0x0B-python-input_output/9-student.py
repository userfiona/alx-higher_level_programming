#!/usr/bin/python3
"""
Module defining the Student class.
"""


class Student:
    """
    Class that defines properties of a student.

    Attributes:
        first_name (str): First name of the student.
        last_name (str): Last name of the student.
        age (int): Age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Creates new instances of the Student class.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: Dictionary representation of the Student instance.
        """
        return self.__dict__
