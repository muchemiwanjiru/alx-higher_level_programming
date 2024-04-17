#!/usr/bin/python3
"""checks for instance"""


def is_same_class(obj, a_class):
    """checks for obj inctance
    Retrun:
        true
        false
    """

    return type(obj) is a_class
