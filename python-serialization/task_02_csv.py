#!/usr/bin/env python3
"""Shebang"""

import csv
import json


def convert_csv_to_json(csv_filename):
    try:
        data = []
        with open(csv_filename, "r", newline="") as csvf:
            reader = csv.DictReader(csvf)

            for row in reader:
                data.append(row)

            with open("data.json", "w") as jsonf:
                json.dump(data, jsonf)

            return True

    except FileNotFoundError:
        return False
    except Exception:
        return False
