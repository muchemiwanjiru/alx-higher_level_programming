#!/usr/bin/python3
""" this is the Base class"""

import json


class Base:
    """ Base class """
    """ private attr with value 0 """

    __nb_objects = 0

    def __init__(self, id=None):

        """ the base class constructor """

        if id is not None:
            self.id = id
        else:
            """ incrementing the value of id per instantiation """
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):

        """ takes a list of dictionaries as inputs"""

        if list_dictionaries is None or len(list_dictionaries) == 0:

            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):

        """ create file name based on class name"""
        """ create a new list of objects"""

        filename = "{}.json".format(cls.__name__)

        objects_list = []

        if list_objs is not None and len(list_objs) > 0:

            for instance in list_objs:

                objects_list.append(cls.to_dictionary(instance))

        with open(filename, 'w', encoding='utf-8') as f:

            f.write(cls.to_json_string(objects_list))

    @staticmethod
    def from_json_string(json_string):

        """ returns the list represented by the JSON string """
        """ checking if json string is empty"""

        if json_string is None or len(json_string) == 0:

            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):

        """ converts from dictionary to instance """

        if cls.__name__ == "Rectangle":

            dummy = cls(2, 2)

        if cls.__name__ == "Square":
            dummy = cls(2)

        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):

        """ Returns value from file"""

        filename = "{}.json".format(cls.__name__)

        list_instance = []

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                strs_file = cls.from_json_string(f.read())

            for instance in strs_file:
                list_instance.append(cls.create(**instance))

        except FileNotFoundError:
            pass

        return list_instance

    @classmethod
    def save_to_file_csv(cls, list_objs):

        """ writes a csv file"""

        filename = "{}.csv".format(cls.__name__)

        objects_list = []

        if list_objs is not None:
            for instance in list_objs:
                objects_list.append(cls.to_dictionary(instance))

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(objects_list))

    @classmethod
    def load_from_file_csv(cls):

        """ returns filename in json format"""

        filename = "{}.csv".format(cls.__name__)
        list_instance = []

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                file_strs = cls.from_json_string(f.read())

            for instance in file_strs:
                list_instance.append(cls.create(**instance))

        except FileNotFoundError:
            pass

        return list_instance
