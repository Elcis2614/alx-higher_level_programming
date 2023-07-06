#!/usr/bin/python3
""" Contain only function """


def find_peak(list_of_integers=[]):
    """ Finds the peak of a list """

    if (list_of_integers == []):
        return None

    elif len(list_of_integers) < 3:
        return None

    else:
        for i in range(len(list_of_integers) - 1):
            if (list_of_integers[i] >= list_of_integers[i - 1]
                    and list_of_integers[i] >= list_of_integers[i + 1]):
                return list_of_integers[i]
