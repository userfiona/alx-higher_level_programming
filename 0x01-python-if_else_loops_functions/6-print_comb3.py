#!/usr/bin/python3
for num in range(9):
    for next_num in range(num + 1, 10):
        print("{:d}{:d}".format(num, next_num), end=", ")
print("99")
