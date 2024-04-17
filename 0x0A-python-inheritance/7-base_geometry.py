#!/usr/bin/python3
"""the class for BaseGeo"""


class BaseGeometry:

    """A class that has a public instance
    method of area and an integer_validator"""

    def area(self):

        """an exception is raised"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        """validates the integer value greater than 0"""

        if not isinstance(value, int):

            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
