#!/usr/bin/env python3
"""Shapes with ABC and duck typing."""

from abc import ABC, abstractmethod


class VerboseList(list):
    """Abstract base class VerboseList."""

    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, list2):
        count = len(list2)
        super().extend(list2)
        print(f"Extended the list with [{count}] items")
    
    def remove(self, item):
        super().remove(item)
        print(f"Removed [{item}] from the list.")
    
    def pop(self, index = -1):
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
