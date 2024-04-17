#!/usr/bin/python3
"""a class with an area method"""


class BaseGeometry:
    """defining the method
        Raises:
            custom error
    """
    def area(self):
        raise Exception("area() is not implemented")
