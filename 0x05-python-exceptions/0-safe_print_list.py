#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    string = ""
    i = 0
    for i in range(x):
        try:
            string += my_list[i]
        except TypeError:
            string += str(my_list[i])
        except IndexError:
            i -= 1
            break
    print("{}".format(string))
    return (i + 1)
