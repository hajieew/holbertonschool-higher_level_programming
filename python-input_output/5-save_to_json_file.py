#!/usr/bin/python3
"""JSON"""

import json


def save_to_json_file(my_obj, filename):
    """Function"""
    with open(filename, 'w', encoding="utf-8") as f:
        return json.dump(my_obj, f)
