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

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student
        Args:
            attrs (list) = holds attributes to be retrieved
        """

        if type(attrs) != list or attrs is None:
            return self.__dict__
        else:
            holder = {}
            for i in attrs:
                if type(i) != str:
                    return self.__dict__
                if i in self.__dict__.keys():
                    holder[i] = self.__dict__[i]
            return holder

    def reload_from_json(self, json):
        """This method replaces all attributes of the Student instance
        Args:
        json (dictionary): dictionary holding the key and value
        """

        for index in json.keys():
            self.__dict__[index] = json[index]
