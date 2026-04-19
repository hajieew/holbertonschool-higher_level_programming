#!/usr/bin/env python3
"""Abstract Animal classes using ABC."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class Animal."""

    @abstractmethod
    def sound(self):
        """Abstract method that must be implemented by subclasses."""
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"
    
class Cat(Animal):
    def sound(self):
        return "Meow"
