#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_val = 0
    max_key = None
    for i, v in a_dictionary.items():
        if v > max_val:
            max_val = v
            max_key = i
    return max_key