#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    roman_len = len(roman_string)

    if not roman_string or not isinstance(roman_string, str):
        return 0

    for i in range(roman_len):
        if i < roman_len - 1 and roman_dictionary[roman_string[i]] < roman_dictionary[roman_string[i + 1]]:
            result -= roman_dictionary[roman_string[i]]
        else:
            result += roman_dictionary[roman_string[i]]

    return result
