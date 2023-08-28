#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """function which print x elememts of a list"""
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
