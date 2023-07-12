#!/usr/bin/python3
"""
Define append module.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after a specific line in a file.

    Args:
        filename (str): Name of the file.
        search_string (str): String to search for in the file.
        new_string (str): String to insert after the search string.
    """
    lines = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            lines.append(line)
            if search_string in line:
                lines.append(new_string + "\n")
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(lines)
