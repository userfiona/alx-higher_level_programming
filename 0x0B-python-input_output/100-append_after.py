#!/usr/bin/python3

def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after each line containing a specific string in a file.

    Args:
        filename (str): Name of the file.
        search_string (str): String to search for in each line.
        new_string (str): String to insert after each line containing the search string.
    """
    lines = []
    with open(filename, "r") as file:
        for line in file:
            lines.append(line)
            if search_string in line:
                lines.append(new_string + "\n")
    with open(filename, "w") as file:
        file.writelines(lines)
