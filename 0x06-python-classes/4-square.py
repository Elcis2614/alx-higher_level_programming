#!/usr/bin/python3
"""This module contains a code for
a class with one private attribute, i just hope it will work"""


class Square:
    """This class defines the square"""
    def __init__(self, size=0):
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """this function returns the area of the square"""
        x = self.__size
        x = x * x
        return x

    def size(self):
        """Returns the size of the square"""
        return self.__size

    def size(self, value):
        self.__init__(self, value)
