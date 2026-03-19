#!/usr/bin/python3
letter = ord('a')
alphabet = ''
while letter <= ord('z'):
    if letter != ord('e') and letter != ord('q'):
        alphabet += chr(letter)
    letter += 1
print("{}".format(alphabet), end='')
