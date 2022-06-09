#!/usr/bin/python3
def roman_to_int(roman_string):
    numerals = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
            }
    sum = 0
    for i in range(len(roman_string)):
        if i < len(roman_string) - 1:
            if (numerals[roman_string[i]] < numerals[roman_string[i + 1]]):
                sum += numerals[roman_string[i]] - 2
            else:
                sum += numerals[roman_string[i]]
        else:
            sum += numerals[roman_string[i]]
    return sum
