#!/usr/bin/python3
"""Student to disk and reload"""


class Student:
    """Student to disk and reload """

    def __init__(self, first_name, last_name, age):
        """Student to disk and reload"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Student to disk and reload"""
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json_data):
        """Student to disk and reload"""
        for key, value in json_data.items():
            setattr(self, key, value)
