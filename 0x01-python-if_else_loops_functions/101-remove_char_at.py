#!/usr/bin/python3
def remove_char_at(string, n):
    if n >= 0 and n < len(string):
        result = ""
        for i in range(len(string)):
            if i != n:
                result += string[i]
        return result
    else:
        return string
