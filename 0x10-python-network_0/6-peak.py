#!/usr/bin/python3
""" Contain only function """

def find_peak(list_of_integers = []):
    """ Finds the peak of a list """

    l = list_of_integers
    if l == [] :
        return None

    elif len(l) < 3 :
        return None

    else :
        for i in range(1, len(l) - 1):
            if (l[i] >= l[i - 1] and l[i] >= l[i+1]):
                return l[i]
if __name__ == "__main__":
    print (find_peak([1,2,3,2]))
