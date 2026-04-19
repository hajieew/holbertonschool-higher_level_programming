#!/usr/bin/python3
"""Class"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            new_dict = {}
            for item in attrs:
                if isinstance(item, str) and item in self.__dict__:
                    new_dict[item] = self.__dict__[item]
            return new_dict
        return self.__dict__
