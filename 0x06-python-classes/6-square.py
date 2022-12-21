#!/usr/bin/python3
"""This module contains a code for
a class with one private attribute, i just hope it will work"""


class Square:
    """This class defines the square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """This returns the position"""
        return self.__position

    @size.setter
    def position(self, value):
        """This function sets the position with a tuple of 2 ints"""
        if(type(value) != tuple or len(value) != 2 or type(value[0]) !=
                int or type(value[1]) != int or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """this function returns the area of the square"""
        x = self.__size
        x = x * x
        return x

    def my_print(self):
        """This function prints the square using the # character"""
        if (self.__size == 0):
            print()
        else:
            size = self.__size
            for s in range(self.__position[1]):
                print()
            for i in range(size):
                for k in range(self.__position[0]):
                    print("{}".format(" "), end="")
                for j in range(size):
                    print("{}".format("#"), end="")
                print()
