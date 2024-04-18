#!/usr/bin/python3

"""
Square class module.

This module defines the Square class.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class represents a square.

    Attributes:
        size (int): The size of the square (width and height).
        x (int): The x-coordinate of the square's position.
        y (int): The y-coordinate of the square's position.
        id (int): The unique identifier for the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square (width and height).
            x (int, optional): The x-coordinate.
            y (int, optional): The y-coordinate.
            id (int, optional):.
        """
        super().__init__(size, size, x, y, id)
        self.__width = size
        self.__height = size

    @property
    def size(self):
        """
        int: The size of the square (width and height).
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square (width and height).

        Args:
            value (int): The size value to set.

        Raises:
            ValueError: If the value is less than or equal to 0.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Get a string representation of the square.

        Returns:
            str: A string representation of the square.
        """
        iid = "({})".format(self.id)
        xy = " {}/{} - ".format(self.x, self.y)
        size = "{}".format(self.height)
        return "[Square]" + iid + xy + size

    def update(self, *args, **kwargs):
        """
        Update the square.

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if args:
            attributes = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)

        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Convert the square attributes to a dictionary.

        Returns:
            dict: A dictionary representing the square.
        """
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y,
                }
