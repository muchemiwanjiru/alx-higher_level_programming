#!/usr/bin/python3
""" checking for a valid integer and summing them up
"""

def add_integer(a, b=98):
    """function that adds two valid number

    Args:
        a (int, float): parameter to be used by the function
        b (int, float, optional): number to be a used by the
                                function. Defaults to 98.

    Raises:
        TypeError: if a is not a valid data type (int, float)
        TypeError: if b is not a valid data type (int, float)

    Returns:
        int, float: sm of a and b
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
