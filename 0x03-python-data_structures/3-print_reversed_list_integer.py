#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i, j in enumerate(my_list):
        print(my_list[len(my_list) - i - 1])
