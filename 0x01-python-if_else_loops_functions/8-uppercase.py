#!/usr/bin/python3
def uppercase(str):
    s=""
    if(str != ""):
        for i in range(len(str)):
            x = ord(str[i])
            if(x >= ord('a') and x <= ord('z')):
                s += chr(x - 32)
            else:
                s += str[i]
        print("{}".format(s))
