#!/usr/bin/python3
""" Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class with height and width"""
    def __init__(self, width, height):
        """Initiate the object"""
        if(self.integer_validator("height", height)):
            self.__height = height
        if(self.integer_validator("width", width)):
            self.__width = width
