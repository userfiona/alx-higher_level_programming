#!/usr/bin/python3
for char_code in range(ord('z'), ord('A') - 1, -1):
    char = chr(char_code)
    if char_code % 2 == 0:
        char = char.lower()
    print(char, end='')

print()
