#!/usr/bin/python3
"""checking the parent class"""


def is_kind_of_class(obj, a_class):
    """Method checks is object is from a Class"""
    if (type(obj) == a_class or isinstance(obj, a_class)):
        return True
    else:
        return False
