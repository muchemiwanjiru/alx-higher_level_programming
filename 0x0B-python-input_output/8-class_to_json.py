#!/usr/bin/python3

"""
function contains the class_to_json function
"""


def class_to_json(obj):
    """
    Returns: the dictionary with a simple data structure.
    """
    return obj.__dict__
