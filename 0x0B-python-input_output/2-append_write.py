#!/usr/bin/python3
"""Append to a file"""


def write_file(filename="", text=""):
    """Append to a file"""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
