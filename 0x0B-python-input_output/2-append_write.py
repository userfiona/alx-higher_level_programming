#!/usr/bin/python3
"""
Module of a function that writes to a text file and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """Write to a file and return the number of characters written.

    Args:
        filename (str): Name of the file to write to.
        text (str): Text to be written.

    Returns:
        int: Number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
