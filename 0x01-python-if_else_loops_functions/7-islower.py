#!/usr/bin/python3
def islower(c):
    x = ord(c)
    if(x >= ord('a') and x <= ord('z')):
        return True
    elif(x >= ord('A') and x <= ord('Z')):
        return False
