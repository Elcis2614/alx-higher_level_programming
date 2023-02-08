#!/usr/bin/python3
"""json  file in wirte mode classic encoder"""


def save_to_json_file(my_obj, filename):
    """save string to json file"""
    import json
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
