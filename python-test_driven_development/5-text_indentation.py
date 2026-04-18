#!/usr/bin/python3
"""This module provides a function that prints text with indentation."""


def text_indentation(text):
    """Prints a text with 2 new lines after '.', '?' and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""
    i = 0
    while i < len(text):
        line += text[i]
        if text[i] in ".:?":
            print(line.strip())
            print()
            line = ""
        i += 1
    if line.strip():
        print(line.strip(), end="")
