#!/usr/bin/python3

"""Text indentation"""



def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimiters = [".", "?", ":"]
    lines = []
    current_line = ""

    for char in text:
        current_line += char
        if char in delimiters:
            lines.append(current_line.strip())
            current_line = ""

    lines.append(current_line.strip())

    for line in lines:
        print(line)
        print()
