#!/usr/bin/python3
def pow(a, b):
    if (b != 0):
        t = a
        if(b > 0):
            for i in range(b - 1):
                a *= t
        else:
            for i in range(abs(b) + 1):
                a /= t
        return a
    elif (b == 0 and a != 0):
        return 1
