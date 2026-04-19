#!/usr/bin/python3
"""a string to a text file"""


def append_write(filename="", text=""):
    """Write smth"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
