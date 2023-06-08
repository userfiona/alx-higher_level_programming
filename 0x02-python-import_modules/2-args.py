#!/usr/bin/python3

import sys

if __name__ == "__main__":
    arguments = len(sys.argv) - 1

    if arguments == 0:
        print("0 arguments.")
    else:
        print(f"{arguments} argument{'s' if arguments > 1 else ''}:")
        for i in range(1, len(sys.argv)):
            print(f"{i}: {sys.argv[i]}")
