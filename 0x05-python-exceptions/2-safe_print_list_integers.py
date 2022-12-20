#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    t = 0
    for i in range(x):
        try:
            p = int(my_list[i])
        except (TypeError, ValueError):
            continue
        else:
            t += 1
            print("{:d}".format(my_list[i]), end="")
    print("")
    return (t)
