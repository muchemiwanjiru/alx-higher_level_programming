#!/usr/bin/python3
"""checks if obj is an instance of inherited
    class
"""


def inherits_from(obj, a_class):
    """return true or false"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
