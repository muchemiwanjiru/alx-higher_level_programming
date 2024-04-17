#!/usr/bin/python3
"""impot json"""


import json


def save_to_json_file(my_obj, filename):
    """writes to obj in json format"""
    with open(filename, "w", encoding="utf8") as f:
        json.dump(my_obj, f)
