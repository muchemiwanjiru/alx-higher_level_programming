#!/usr/bin/python3
"""the rectangle class instance from base class
    """

from base import Base


class Rectangle(Base):

    """ inheriting from base class"""
    """ constructor with new values other than id"""

    def __init__(self, width, height, x=0, y=0, id=None):

        """ private attributes for rectangle class"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """ public getter and setter functions for values"""

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
        """ Returns the area of the rectangle
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

        """ function to set"""
        si_id = "({}) ".format(self.id)

        si_xy = "{}/{} - ".format(self.__x, self.__y)

        si_wh = "{}/{}".format(self.__width, self.__height)

        return "[Rectangle] " + si_id + si_xy + si_wh

    def update(self, *args, **kwargs):

        """ args initiates the attributes"""

        """ the kwargs (dict):is the attribute of key-value pairs """

        if args is not None and len(args) > 0:

            att = ["id", "width", "height", "x", "y"]
            for j in range(len(args)):
                setattr(self, att[j], args[j])
            else:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):

        """Returning the value dictionary that reps a Rectangle."""

        k = {
                'x': self.__x, 'y': self.__y, 'id': self.id,
                'height': self.__height, 'width': self.__width
                }

        return k
