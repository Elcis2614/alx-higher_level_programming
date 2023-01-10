#!/usr/bin/python3
"""checking the parent class"""


def inherits_from(obj, a_class):
    """Method checks is object inherit from a Class"""
    return (isinstance(obj, a_class) or isinstance(type(obj), a_class))
