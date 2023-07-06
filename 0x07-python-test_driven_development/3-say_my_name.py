#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or last_name must be a string")

    full_name = first_name + " " + last_name
    print("My name is", full_name)
