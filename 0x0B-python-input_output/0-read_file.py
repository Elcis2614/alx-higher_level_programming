#!/usr/bin/python3
"""First task on I/OO python"""


def read_file(filename=""):
    """ Reads a file """
    with open(filename, encoding='uft-8') as m_file:
        for line in m-file:
            print(line, end="")
