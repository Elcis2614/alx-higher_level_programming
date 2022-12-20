#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    string = ""
    t = 0
    for i in range(x):
        try:
            string += my_list[i]
            t += 1
        except TypeError:
            string += str(my_list[i])
            t += 1
        except IndexError:
            break
    print("{}".format(string))
    return (t)
