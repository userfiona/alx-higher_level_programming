#!/usr/bin/python3
def uppercase(string):
    for char in string:
        if ord('a') <= ord(char) <= ord('z'):
            char = chr(ord(char) - 32)
        print(char, end="")
    print('')
