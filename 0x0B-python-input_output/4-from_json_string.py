#!/usr/bin/python3
"""import json"""

import json


def from_json_string(my_str):
    """return an obj in python structure"""
    py = json.loads(my_str)
    return py
