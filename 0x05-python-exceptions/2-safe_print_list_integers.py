#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    string = ""
    t = 0
    for i in range(x):
        try:
            p = int(my_list[i])
        except (TypeError, ValueError):
            continue
        else:
            string += str(my_list[i])
            t += 1
    if (string != ""):
        string = int(string)
        print("{:d}".format(string))
    return (t)
