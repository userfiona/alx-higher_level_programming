#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
    for content in dir(hidden_4):
        if not content.startswith("__"):
            print(content)
