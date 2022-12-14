#!/usr/bin/python3
"""checking the parent class"""


def inherits_from(obj, a_class):
    """Method checks is object inherit from a Class"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
