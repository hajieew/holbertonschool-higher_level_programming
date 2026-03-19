#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10
    print(last_digit, end='')  # eyni sətirdə çap
    return last_digit

# sadəcə funksiyanı çağır
print_last_digit(98)