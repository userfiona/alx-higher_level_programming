#!/usr/bin/python3
"""
Search and update
functions:
def append_after(filename="", search_string="", new_string=""):
"""


def append_after(filename="", search_string="", new_string=""):
    """
    A function that inserts a line of text to a file,
    after each line containing a specific string
    :param filename:
    :param search_string:
    :param new_string:
    :return: the new string
    """
    with open(filename, encoding='utf-8') as a_file:
        line_text = ""
        for i in a_file:
            line_text += i
            if search_string in i:
                line_text += new_string

    with open(filename, mode='w', encoding='utf-8') as a_file:
        a_file.write(line_text)
