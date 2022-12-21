#!/usr/bin/python3
"""This module contains a code for
a class with one private attribute, i just hope it will work"""


class Square:
    """This class defines the square"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """this function returns the area of the square"""
        return self.__size

    @size.setter
    def size(self, size):
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

    def my_print(self):
        """This function prints the square using the # character"""
        if (self.__size == 0):
            print("\n")
        else:
            size = self.__size
            for i in range(size):
                for j in range(size):
                    print("{}".format("#"), end="")
                print()
