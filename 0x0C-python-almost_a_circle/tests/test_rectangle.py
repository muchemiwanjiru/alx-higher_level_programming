#!/usr/bin/python3
""" the tests is for unittests for models of rectangle.py.
Unittest test cases are based on the functionality
"""


import unittest

import json

from unittest.mock import patch

from models.base import Base

from io import StringIO

from models.rectangle import Rectangle

""" the test class is for rectangle method """

class TestRectangleMethods(unittest.TestCase):

    """ the class here defines tests for Rectangle a class """

    @classmethod
    def test_setUp(self):

        """ the test set up runs for each test """

        Base._Base__nb_objects = 0


    def test_docstring(self):

        """ the test docstring tests  if a docstring is present """

        self.assertIsNotNone(Rectangle.__doc__)

    def tear_Down(self):

        """ this particular test cleans up after each test """
        pass

    def test_for_class_inheritance(self):

        """ this test is for checking if Rectangle inherits from the Base """

        self.assertTrue(issubclass(Rectangle, Base))


    def test_for_area_1(self):

        """ the test case is for the area """

        r1 = Rectangle(3, 2)

        r2 = Rectangle(2, 10)

        r3 = Rectangle(8, 7, 0, 0, 12)

        self.assertEqual(r1.area(), 2 * 3)

        self.assertEqual(r2.area(), 2 * 10)

        self.assertEqual(r3.area(), 8 * 7)

    def test_for_area_2(self):

        """ the test case here checks if the return value of area method """

        r1 = Rectangle(6, 2)

        self.assertEqual(r1.area(), 12)

        r1.width = 8

        self.assertEqual(r1.area(), 16)

        r1.height = 5

        self.assertEqual(r1.area(), 40)

    def test_for_basic_display(self):

        """the test case is for display without x and y """

        J1 = Rectangle(4, 6)

        result = "####\n####\n####\n####\n####\n####\n"

        with patch('sys.stdout', new=StringIO()) as str_out:

            J1.display()

            self.assertEqual(str_out.getvalue(), result)


    def test_for_display_no_args(self):

        """ the test case is for  the Test display method that does not have arguments """

        rec = Rectangle(2, 6)

        with self.assertRaises(TypeError) as e:

            Rectangle.display()

        k = "display() missing 1 required positional argument: 'self'"

        self.assertEqual(str(e.exception), k)


    def test_to_save_to_file_2(self):

        """ this is a test case that helps to save_to_file method with None as file """

        Rectangle.save_to_file(None)

        with open("Rectangle.json", mode="r") as myFile:

            self.assertEqual([], json.load(myFile))
