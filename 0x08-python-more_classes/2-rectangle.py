#!/usr/bin/python3
""""Rectangle class with more atttriubte"""


class Rectangle:
    """This is a class with attributes"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """returns the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value"""
        if (type(value) != int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise TypeError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Returns the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of the height"""
        if (type(value) != int):
            raise TypeError("height must be an integer")
        elif (height < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """return the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if (self.__width == 0 or self.__height == 0):
            return 0
        return (self.__width + self.__height) * 2
