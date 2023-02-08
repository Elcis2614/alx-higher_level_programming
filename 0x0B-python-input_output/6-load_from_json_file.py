#!/usr/bin/python3
""""string retrieval data"""


def load_from_json_file(filename):
    """loading data from file"""
    import json
    with open(filename, mode='r', encoding='utf-8') as file:
        return (json.load(file))
