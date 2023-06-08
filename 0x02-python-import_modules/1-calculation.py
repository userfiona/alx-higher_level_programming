#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv_len = len(sys.argv) - 1

    if argv_len == 0:
        print("0 arguments.")
    elif argv_len == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(argv_len))

    if argv_len > 0:
        for i in range(1, argv_len + 1):
            print("{:d}: {:s}".format(i, sys.argv[i]))
