#!/usr/bin/python3
letter = ord('a')
while letter <= ord('z'):
    print(f"{chr(letter)}", end='')
    letter += 1
