#!/usr/bin/python3
"""Pascal Triangle represntion"""


def pascal_triangle(n):
    """Function returns a list of lists of integers
    representing the Pascal’s triangle
    Args:
    n (int): triangle size
    """

    prod = [[1]]
    if n <= 0:
        return []

    for index in range(1, n):
        holder = []
        holder.append(1)
        for idx in range(index - 1):
            holder.append(prod[-1][idx] + prod[-1][idx + 1])
        holder.append(1)
        prod.append(holder)
    return prod
