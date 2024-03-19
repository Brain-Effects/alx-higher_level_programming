#!/usr/bin/python3


class Student:
    """
    `Student` is a class that defines a student by their
    first name, last name, and age.

    Attributes:
    first_name (str): The first name of the student.
    last_name (str): The last name of the student.
    age (int): The age of the student.

    The class provides a method `to_json` to retrieve a dictionary
    representation of a Student instance.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first name, last name, and age.

        Parameters:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
        dict: A dictionary that represents the Student instance with
        keys as attribute names and values as attribute values.
        """
        return self.__dict__
