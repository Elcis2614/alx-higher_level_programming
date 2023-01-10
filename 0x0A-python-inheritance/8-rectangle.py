#!/usr/bin/python3
""" Rectangle class"""


class Rectangle(BaseGeometry):
    """ Rectangle class with height and width"""
    def __init__(self, width, height):
        """Initiate the object"""
        try:
            self.integer_validator(height)
        except Exception as e:
            return
        else:
            self.__height = height

        try:
            self.integer_validator(width)
        except Exception as e:
            return
        else:
            self.__width = width
