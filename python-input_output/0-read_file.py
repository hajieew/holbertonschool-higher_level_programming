#!/usr/bin/python3
"""Reads a text file"""


def read_file(filename=""):
    """UTF-8 open"""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
