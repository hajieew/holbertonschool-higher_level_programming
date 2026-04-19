#!/usr/bin/python3
"""Module that defines inherits_from function."""


def inherits_from(obj, a_class):
    """Check if object is a subclass instance but not exact class."""
    return type(obj) is not a_class and isinstance(obj, a_class)
