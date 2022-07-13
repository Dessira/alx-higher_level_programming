#!/usr/bin/python3
"""class Student"""


class Student:
    """A class Student that defines a student
    Args:
    first_name (string): students firstname
    last_name (string): students lastname
    age (int): students age
    """

    def __init__(self, first_name, last_name, age):
        """instantation of attributes"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Public method that retrieves a dictionary
        representation of a Student
        """

        return self.__dict__
