#!/usr/bin/python3

"""
Base class module.

This module defines the Base class.
"""

import json


class Base:
    """
    Base class is the base class for other classes.

    Attributes:
        nb_objects (int): The number of objects created.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base instance.

        Args:
            id (int): The identifier for the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: A JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of instances to a file.

        Args:
            list_objs (list): A list of instances.
        """
        filename = "{}.json".format(cls.__name__)

        objects_list = []

        if list_objs is not None and len(list_objs) > 0:

            for instance in list_objs:

                objects_list.append(cls.to_dictionary(instance))

        with open(filename, 'w', encoding='utf-8') as f:

            f.write(cls.to_json_string(objects_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): A JSON string.

        Returns:
            list: A list of dictionaries parsed from the JSON string.
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):

        """ converts from dictionary to instance """

        if cls.__name__ == "Rectangle":

            dicti = cls(2, 2)

        if cls.__name__ == "Square":
            dicti = cls(2)

        dicti.update(**dictionary)

        return dicti

    @classmethod
    def load_from_file(cls):
        """Method that gets  a list of instances

        Returns:
            instance: returns a list of instances
        """
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as file:
            json_data = file.read()

        instance_dicts = cls.from_json_string(json_data)
        instances = [cls.create(**data) for data in instance_dicts]
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Base class method that that serializes and deserializes in CSV

        Args:
            list_objs (list ): list objects
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                writer.writerow(obj.to_csv_row())

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        instances = []
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                instance = cls.create_from_csv_row(row)
                instances.append(instance)
        return instances
