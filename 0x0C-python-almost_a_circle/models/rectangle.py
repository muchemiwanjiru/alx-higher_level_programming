#!/usr/bin/python3

"""
Rectangle class module.

This module defines the Rectangle class, which is a subclass of the Base class.
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class represents a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle's position.
        y (int): The y-coordinate of the rectangle's position.
        id (int): The unique identifier for the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate.
            y (int, optional): The y-coordinate .
            id (int, optional): .
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):

        """get width value"""

        return self.__width

    @width.setter
    def width(self, value):
        """ set width value"""

        if not isinstance(value, int):

            raise TypeError("width must be an integer")

        if value <= 0:

            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):

        """get height value"""

        return self.__height

    @height.setter
    def height(self, value):

        """ set height value"""
        if not isinstance(value, int):

            raise TypeError("height must be an integer")

        if value <= 0:

            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):

        """get x value"""

        return self.__x

    @x.setter
    def x(self, value):

        """ set x value"""

        if not isinstance(value, int):

            raise TypeError("x must be an integer")

        if value < 0:

            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):

        """get y value"""

        return self.__y

    @y.setter
    def y(self, value):

        """ set y value"""

        if not isinstance(value, int):

            raise TypeError("y must be an integer")

        if value < 0:

            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):

        """ public class area"""

        will_print = self.__y * "\n"
        for i in range(self.__height):
            will_print += " " * self.__x
            will_print += "#" * self.__width + "\n"

        print(will_print, end="")

    def __str__(self):
        """
        Get a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle.
        """
        iid = "({})".format(self.id)
        xy = " {}/{} - ".format(self.__x, self.__y)
        widhe = "{}/{}".format(self.__width, self.__height)
        return "[Rectangle] " + iid + xy + widhe

    def update(self, *args, **kwargs):
        """
        Update the rectangle attributes.

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)

        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Convert the rectangle attributes to a dictionary.

        Returns:
            dict: A dictionary representing the rectangle.
        """
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y,
                }
