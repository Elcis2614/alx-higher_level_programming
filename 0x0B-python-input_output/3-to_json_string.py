#!/usr/bin/python3
"""Dealing with Json"""


def to_json_string(my_obj):
    """Returns a Json represention of a string"""
    import json
    return (json.dumps(my_obj))
