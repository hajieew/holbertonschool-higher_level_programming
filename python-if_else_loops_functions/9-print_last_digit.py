#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        last_digit = number % 10
    else:
        if number % 10 == 0:
            last_digit = 0
        else:
            last_digit = -10 + number % 10
    return last_digit
