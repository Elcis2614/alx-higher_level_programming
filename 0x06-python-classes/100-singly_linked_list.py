#!/usr/bin/python3
"""This module contains a code for
the class Node and another SinglyLinkedList"""


class Node:
    """This class defines the square"""
    def __init__(self, d, next_node=None):
        self.data = d
        self.next_node = next_node

    @property
    def data(self):
        """Return the data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data of the node"""
        if (type(value) != int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Return the next node of the linked list"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the value of the nextNode"""
        if (value is not None and type(value) is not Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """This new class defines a stingly linked list"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Insert the node into the correct position"""
        if(self.__head is None):
            temp = Node(value)
            self.__head = temp
        else:
            t = self.__head
            prev = t
            newNode = Node(value)
            while(True):
                if (t is None):
                    prev.next_node = newNode
                    break
                elif (t.data <= value):
                    prev = t
                    t = t.next_node
                elif (t.data >= value):
                    prev.next_node = newNode
                    newNode.next_node = t
                    break

    def __str__(self):
        """return a string version of the linked list to the std out"""
        x = self.head
        s = ""
        while (x is not None):
            s = s + str(x.data) + "\n"
            x = x.next_node
        return s
