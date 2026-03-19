#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if i >= 'A' and i <= 'Z':
            print(f"{i}, end=''")
        else:
            i = chr(ord(i) - 32)
            print(f"{i}, end=''")
    print()

str = 'HellO'
uppercase(str)
