#!/usr/bin/python3
"""New class"""


class BaseGeometry:
    """Base geometry class"""
    def area(self):
        """returns a string"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the value"""
        if (type(value) != int):
            raise TypeError("{} must be an integer".format(name))
        elif (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
