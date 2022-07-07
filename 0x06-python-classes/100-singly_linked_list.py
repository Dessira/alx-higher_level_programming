#!/usr/bin/python3
"""Defines a node"""


class Node():
    """A class Node that defines a node of a singly linked list
    Args:
        data (int): data of the node
        next_node (Node): next node
    """

    def __init__(self, data, next_node=None):
        """initializes attributes
        Args:
        data (int): data of the node
        next_node (Node): next node
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Set the data, check for input and raise errors"""

        return self.__data

    @data.setter
    def data(self, value):

        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Set next node check for input and raise errors"""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        
        if type(value) != Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """A class SinglyLinkedList that defines a singly linked list"""

    def __init__(self):
        """instantation of attributes"""

        self.__head = None

    def sorted_insert(self, value):
        """Adds new node into the correct position """

        new_node = Node(value)
        
        if self.__head == None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            holder = self.__head
            while (holder.next_node != None and holder.next_node.data < value):
                holder = holder.next_node
            new_node.next_node = holder.next_node
            holder.next_node = new_node

    def __str__(self):
        """Print the list"""

        holder = self.__head
        val = []
        while holder != None:
            val.append(str(holder.data))
            holder = holder.next_node
        return ('\n'.join(val))
