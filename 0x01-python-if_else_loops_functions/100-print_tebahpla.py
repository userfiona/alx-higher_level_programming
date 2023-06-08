#!/usr/bin/python3
for char_code in range(ord('z'), ord('A') - 1, -1):
    if char_code % 2 == 0:
        print(chr(char_code), end='')
    else:
        print(chr(char_code - 32), end='')

print()
