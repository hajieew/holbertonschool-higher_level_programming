#!/usr/bin/python3
"""Module that defines MyList class."""


class MyList(list):
    """A custom list class that can print itself sorted."""
    def print_sorted(self):
        print(sorted(self))
