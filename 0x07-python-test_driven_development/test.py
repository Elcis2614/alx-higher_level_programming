#!/usr/bin/python3
def fact(n):
    if (type(n) != int):
        raise TypeError("Wrong type")
    else :
        if (n <= 1):
            return (1)
        else:
            return (n * fact(n-1))
