#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0
    num_of_elements = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            num_of_elements += 1
        except:
            continue
    print()
    return num_of_elements
