#!/usr/bin/python3
"""Dealing with Json data"""


def from_json_string(my_str):
    """ Deserialize json data into python object"""
    import json
    return (json.loads(my_str))
