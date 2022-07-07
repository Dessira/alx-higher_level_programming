#!/usr/bin/python3
"""Module for creating a square"""


class Square:
    """A class Square that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the attributes of the square

        Args:
        size (int): size of square
        position (tuple): position of square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """set the square"""
        return(self.__size)

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        """set the square"""
        return(self.__position)

    @size.setter
    def position(self, position):
        if ((position[0] < 0 or type(position[0]) != int) or
                (position[1] < 0 or type(position[1]) != int) or
                len(position) != 2 or type(position) != tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Prints a square using '#' based on the size and position"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end='')
                for j in range(self.__size):
                    print("#", end='')
                print()

    def __str__(self):
        """Printing a Square instance should have the same behavior as my_print()"""

        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
