#!/usr/bin/python3
"""
Module 0-read_file.
Reads from a file and prints.
"""


def read_file(filename=""):
    """Reads from filename and prints its contents to stdout.

    Args:
        filename (str): Name of the file to read.
    """
    with open(filename, 'r') as file:
        read_text = file.read()
        print(read_text, end="")
