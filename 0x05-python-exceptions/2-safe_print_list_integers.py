#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """a functin which print the first x elements of a list that are integers"""
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
