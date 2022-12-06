#!/usr/bin/python3
def element_at(my_list, idx):
    if (idx < 0 | idx >= len(my_list)):
        return "None"
    if (len(my_list) != 0):
        return my_list[idx]
