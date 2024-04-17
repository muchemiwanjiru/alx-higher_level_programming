#!/usr/bin/python3


""" Import json """
import json


def load_from_json_file(filename):
    """
    this reads an object from the JSON file

    Returns: this is a Python data
    structure represented by the JSON in the file.
    """
    with open(filename, 'r') as f:
        return json.load(f)
