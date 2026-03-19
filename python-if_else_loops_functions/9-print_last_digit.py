#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10   # son rəqəm
    print(last_digit, end='')       # çap et
    return last_digit

# Funksiyanı sadəcə çağır
print_last_digit(98)