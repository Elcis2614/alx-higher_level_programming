#!/usr/bin/python3
"""First task on I/OO python"""


def read_file(filename=""):
    """ Reads a file """
    with open(filename, encoding='utf-8') as m_file:
        x = m_file.read()
        while (x != ""):
            print(x, end="")
            x = m_file.read()
