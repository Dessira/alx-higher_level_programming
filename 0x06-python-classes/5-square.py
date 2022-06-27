#!/usr/bin/python3

class Square:
    """A class Square that defines a square based on 4-square.py

    Attributes:
    __size (int): Private instance attribute
    """

    def __init__(self, size=0):
        """Initializes th square attributes

        Args:
        size (int): size of square
        """
        self.size = size

    @property
    def size(self):
        """Sets the square"""
        return(self.__size)

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Retuens area of square"""
        return self.__size * self.__size

    def my_print(self):
        """Prints a square using '#' based on size"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
