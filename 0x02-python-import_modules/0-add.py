#!/usr/bin/python3
if __name__ == "__main__":
    from add_0 import add as addition
    a = 1
    b = 2
    print("{x} + {y} = {z}".format(x=a, y=b, z=addition(a, b)))
