#!/usr/bin/python3
def islower(c):
    if len(c) != 1:
        raise ValueError("Input must be a single character")
    if 'a' <= c <= 'z':
        return True
    elif 'A' <= c <= 'Z':
        return None
    else:
        return None