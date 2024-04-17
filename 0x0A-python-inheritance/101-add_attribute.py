#!/usr/bin/python3
"""function that adds attributes to objects"""


def add_new_attribute(obj, name, value):

    """adds the new attribute to an object
        Raises: TypeError
    """

    if hasattr(obj, '__dict__'):
        obj.__dict__[name] = value

    else:
        raise TypeError("can't add new attribute")
