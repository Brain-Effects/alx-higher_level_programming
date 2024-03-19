#!/usr/bin/python3


class Student:
    """
    This class defines a student by their first name, last name, and age.

    Public instance attributes:
    - first_name
    - last_name
    - age

    The class provides a method to retrieve a dictionary
    representation of a Student instance.
    """

    def __init__(self, first_name, last_name, age):
        """
        This method initializes a Student instance.

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
        This method retrieves a dictionary representation of a
        Student instance.

        Returns:
        dict: A dictionary that represents the Student instance.
        """
        return self.__dict__
