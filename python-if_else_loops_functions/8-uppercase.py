#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if i >= 'A' and i <= 'Z':
            print("{}".format(i), end='')
        else:
            i = chr(ord(i) - 32)
            print("{}".format(i), end='')
    print()
