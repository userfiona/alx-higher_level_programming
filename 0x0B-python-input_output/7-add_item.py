#!/usr/bin/python3
"""
Module to add all arguments to a Python list and then save to a file.
"""

import sys
import json

def main():
    """
    Main function to add arguments to a list and save to a file.
    """
    filename = "add_item.json"
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
        
    data.extend(sys.argv[1:])

    with open(filename, 'w') as file:
        json.dump(data, file)

if __name__ == "__main__":
    main()
