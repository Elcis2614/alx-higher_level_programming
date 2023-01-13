#!/usr/bin/python3
"""Appending to a file"""


def append_write(filename="", text=""):
    """Appending to the file"""
    with open(filename, mode='a', encoding='utf-8') as mFile:
        mFile.write(text)
        return len(text)
