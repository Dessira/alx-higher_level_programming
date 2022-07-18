#!/usr/bin/python3
"""Divides matrix"""


def matrix_divided(matrix, div):
    """Divides the matrix using div and return new list"""
    new = []

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    for i in matrix:
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    for index in matrix:
        sub = []
        if type(index) != list:
            raise TypeError("matrix must be a matrix
                            (list of lists) of integers/floats")
        for i in index:
            if type(i) != int and type(i) != float:
                raise TypeError("matrix must be a matrix
                                (list of lists) of integers/floats")
            sub.append(round(i / div, 2))
        new.append(sub)
    return new
