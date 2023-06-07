#!/usr/bin/python3
for num in range(1, 10):
    for next_num in range(num + 1, 10):
        print("{:02d}, {:02d}".format(num, next_num), end=", ")
print("{:02d}".format(98))
