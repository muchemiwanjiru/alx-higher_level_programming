#!/usr/bin/python3

""" the following test cases are for unittests for models of rectangle.py.
Unittest test cases are based on the functionality
"""

import unittest

import sys

from io import StringIO

from models.square import Square

from models.base import Base

from models.rectangle import Rectangle


""" the tests are for the  square class"""

class TestSquareMethod(unittest.TestCase):

    def test_for_areas(self):

        """the above tests the base areas"""

        Base._Base__nb_objects = 0

        R1 = Square(7)

        self.assertEqual(R1.area(), 49)

        R1 = Square(5)
        self.assertEqual(R1.area(), 25)

        R1 = Square(2, 10, 20, 12)
        self.assertEqual(R1.area(), 4)


    def test_the_base(self):
        """ check for the instance of the base """

        self.assertIsInstance(Square(20), Base)


    def test_more_than_four_args(self):

        """ the test case above checks for more than four arguments """

        with self.assertRaises(TypeError):

            Square(1, 2, 3, 4, 5)

    def test_for_size_setter(self):

        """ the test case for the getter function"""

        s = Square(2, 10, 5, 12)

        s.size = 8

        self.assertEqual(8, s.size)

    def test_the_size_private(self):

        """ unit test to check for size of square"""

        with self.assertRaises(AttributeError):

            print(Square(2, 10, 5, 12).__size)


    def test_for_size_getter(self):
        """ test for size of the getter """

        self.assertEqual(6, Square(6, 12, 30, 19).size)


    def test_for_height_getter(self):

        """ the unit test for size of the square"""

        s = Square(40, 21, 19, 12)

        s.size = 8

        self.assertEqual(8, s.height)
