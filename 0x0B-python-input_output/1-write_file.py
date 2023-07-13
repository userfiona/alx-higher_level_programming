#!/usr/bin/python3
"""
Module of a function that writes to a text file and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """Write to a file"""
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
