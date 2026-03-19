#!/usr/bin/python3
letter = ord('a')
alphabet = ''
while letter <= ord('z'):
    alphabet += chr(letter)
    letter += 1
print("{}".format(alphabet), end='')
