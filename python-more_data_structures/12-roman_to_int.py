#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    num = 0
    roman_num = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    if len(roman_string) == 1:
        return roman_num[roman_string]
    else:
        for i in range(1, len(roman_string)):
            if roman_num[roman_string[i-1]] < roman_num[roman_string[i]]:
                num -= roman_num[roman_string[i-1]]
            else:
                num += roman_num[roman_string[i-1]]
    num += roman_num[roman_string[-1]]
    return num