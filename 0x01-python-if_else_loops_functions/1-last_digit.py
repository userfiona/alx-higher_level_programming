#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

last_digit = abs(number) % 10

print("Last digit of", number, "is", last_digit, end="")

if last_digit > 5:
    print(f" and is greater than 5")
elif last_digit == 0:
    print(f" and is 0")
else:
    print(f" and is less than 6 and not 0")
~                                            
        for i in range(len(string)):
            if i != n:
                result += string[i]
        return result
    else:
        return string
