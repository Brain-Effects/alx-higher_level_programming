#!/usr/bin/python3
"""
This is the "base" module.

This module provides the base for all other classes in the project.
The goal of it is to manage the id attribute in all future classes
and to avoid duplicating the same code (by extension, same bugs).
"""
import json
import os
import csv


class Base:
    """
    This is the Base class.

    This class serves as the base for all other classes in the project.
    It manages the id attribute in all future classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        This is the constructor method for the Base class.

        If id is provided, it is assigned to the public instance attribute id.
        If id is not provided, __nb_objects is incremented and its
        new value is assigned to id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This static method returns the JSON string representation of
        list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This class method writes the JSON string representation of
        list_objs to a file.
        """
        filename = cls.__name__ + ".json"
        list_dicts = []
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        This static method returns the list of the JSON string
        representation json_string.
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        This class method returns an instance with all attributes already set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        This class method returns a list of instances.
        """
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as f:
            list_dicts = cls.from_json_string(f.read())
        return [cls.create(**d) for d in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        This class method serializes list_objs to a CSV file.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csvfile:
            if list_objs is not None:
                writer = csv.writer(csvfile)
                if cls.__name__ == "Rectangle":
                    for obj in list_objs:
                        writer.writerow(
                                [obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    for obj in list_objs:
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        This class method deserializes instances from a CSV file.
        """
        filename = cls.__name__ + ".csv"
        instances = []
        try:
            with open(filename, 'r') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        dictionary = {"id": int(row[0]), "width": int(
                            row[1]), "height": int(row[2]), "x": int(
                                    row[3]), "y": int(row[4])}
                    elif cls.__name__ == "Square":
                        dictionary = {"id": int(row[0]), "size": int(
                            row[1]), "x": int(row[2]), "y": int(row[3])}
                    instances.append(cls.create(**dictionary))
        except FileNotFoundError:
            pass
        return instances
