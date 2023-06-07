#!/usr/bin/python3
for num in range(10):
    for next_num in range(num + 1, 10):
        print("{:02d}, {:02d}".format(num, next_num), end=", ")
print("89")
