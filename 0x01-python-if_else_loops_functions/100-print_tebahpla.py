#!/usr/bin/python3
for char_code in range(ord('z'), ord('A') - 1, -1):
    print("{:c}".format(char_code), end='')

print()
