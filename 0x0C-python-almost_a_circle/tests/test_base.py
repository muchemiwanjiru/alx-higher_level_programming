#!/usr/bin/python3

"""this file contains the  class BaseModelTest"""

import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square



class TestBaseMethod(unittest.TestCase):

    """ this defines tests for base class"""

    def test_set_up(self):
        """ Runs for each test """
        Base._Base__nb_objects = 0
        self.new_base = Base(id=1)


    def test_tear_down(self):
        """ this ceans up after each test """
        pass

    def test_docstring(self):
        """ this test is of the docstring  present """
        self.assertIsNotNone(Base.__doc__)

    def test_for_random_id(self):

        """ this test is for random arguments passed """

        test1 = Base(10)
        self.assertEqual(test1.id, 10)
        test2 = Base(14)
        self.assertEqual(test2.id, 14)
        test3 = Base()
        self.assertEqual(test3.id, 7)
        test4 = Base(-8)
        self.assertEqual(test4.id, -8)


    def test_for_0_id(self):

        """ this is the test for id to see if it duplicates """

        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(24)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 24)


    def test_for_consecutive_ids(self):

        """ this is the test for consecutive ids """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_constructor(self):

        """ this is a test for constructor signature """

        with self.assertRaises(TypeError) as e:

            Base.__init__()

        msg = "__init__() missing 1 required positional argument: 'self'"

        self.assertEqual(str(e.exception), msg)

    def test_constructor_args_2(self):

        """ this tests is for constructor signature with 2 note self args """

        with self.assertRaises(TypeError) as e:

            Base.__init__(self, 1, 2)

        msg = "__init__() takes from 1 to 2 positional arguments but 3 \
                were given"
        self.assertEqual(str(e.exception), msg)


    def test_to_json_string(self):

        """ this is a test that is used to_json_string method """

        R1 = Rectangle(20, 6, 1, 9)

        R2 = Rectangle(41, 11, 23, 54)

        dict1 = R1.to_dictionary()

        dict2 = R2.to_dictionary()

        json_dict1 = [{"x": 8, "width": 20, "id": 5, "height": 2, "y": 9}]

        json_dict2 = [{"x": 13, "width": 41, "id": 2, "height": 3, "y": 2}]

        json_string = Base.to_json_string([dict1, dict2])

        self.assertNotEqual(dict1, json_dict1)

        self.assertNotEqual(dict2, json_dict2)

        self.assertEqual(type(dict1), dict)

        self.assertEqual(type(json_string), str)

        self.assertEqual(Base.to_json_string(None), "[]")

        self.assertEqual(Base.to_json_string([]), "[]")

        self.assertTrue(type(Base.to_json_string(None)) is str)

        self.assertTrue(type(Base.to_json_string("[]")) is str)

        self.assertTrue(type(json_string), str)

        j = json.loads(json_string)

        self.assertEqual(j, [dict1, dict2])



    def test_save_to_file(self):

        """ this is a test to save_to_file method """

        import os

        R1 = Rectangle(15, 27, 7, 2)
        R2 = Rectangle(5, 10)
        Rectangle.save_to_file([R1, R2])

        with open("Rectangle.json", "r") as file:

            self.assertEqual(len(file.read()), 107)

        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r") as file:

            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Rectangle.json")

        except Exception:

            pass
        Rectangle.save_to_file([])

        with open("Rectangle.json", "r") as file:

            self.assertEqual(file.read(), "[]")

        R2 = Rectangle(5, 10)

        Rectangle.save_to_file([R2])

        with open("Rectangle.json", "r") as file:

            self.assertEqual(len(file.read()), 54)

        Square.save_to_file(None)

        with open("Square.json", "r") as file:

            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Square.json")

        except Exception:

            pass

        Square.save_to_file([])

        with open("Square.json", "r") as file:

            self.assertEqual(file.read(), "[]")

        R2 = Square(4)

        Square.save_to_file([R2])

        with open("Square.json", "r") as file:

            self.assertEqual(len(file.read()), 39)
