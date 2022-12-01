#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv as arg
    x = len(arg)
    if x == 2:
        print("1 argument:")
    else:
        if x == 1:
            print("0 arguments.")
        else:
            print("{a} arguments:".format(a=x))
    for j in range(1, x):
        print("{i}: {a}".format(i=j, a=arg[j]))
