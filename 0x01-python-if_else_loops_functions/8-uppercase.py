#!/usr/bin/python3
def uppercase(string):
    for char in string:
        char_code = ord(char)
        if 97 <= char_code <= 122:
            char_code -= 32
        print("{:c}".format(char_code), end="")
    print()
