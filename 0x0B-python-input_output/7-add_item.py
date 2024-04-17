#!/usr/bin/python3
"""writes an Object to a text file
"""


import json


def save_to_json_file(my_obj, filename):

    """the value is an object to a text
    file that uses a JSON representation"""

    with open(filename, 'w', encoding='utf-8') as f:

        json.dump(my_obj, f)
