#!/usr/bin/python3
"""
   Module to add all arguments to a python list,
     then save to a file.
"""


import sys


def main():
    """
       main - main body
    """
    save_json = __import__('5-save_to_json_file').save_to_json_file
    load_json = __import__('6-load_from_json_file').load_from_json_file

    try:
        s = load_json("add_item.json")
    except FileNotFoundError:
        s = []
    s.extend(sys.argv[1:])
    save_json(s, "add_item.json")


if __name__ == "__main__":
    main()
