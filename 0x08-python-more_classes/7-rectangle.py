#!/usr/bin/python3
"""
Defining my class Rectangle
"""


class Rectangle:

    """public attribute"""
    number_of_instances = 0
    print_symbol = '#'

    """Representing my rectangle."""
    def __init__(self, width=0, height=0):
        """Initializing a new Rectangle.
        Args:
            width (int): new rectangle width.
            height (int): new rectangle height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter of the rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter of the rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        perim = (self.__height + self.__width)*2
        if (self.__width == 0 or self.__height == 0):
            perim = 0
        return perim

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += str(self.print_symbol) * self.__width + "\n"
        return rectangle_str[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """built-in method that is used to check for deleted object instance
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
