#!/usr/bin/python3
""" Writting in a file """


def write_file(filename="", text=""):
    """Wirtes a file """
    with open(filename, mode='w', encoding='utf-8') as m_file:
        char = 0
        for i in text:
            m_file.write(i)
            char += 1
        return (char)
