#!/usr/bin/python3
"""reverse items"""
def print_reversed_list_integer(my_list=[]):
   
    idx = 0
    my_list.reverse()
    while idx <= len(my_list) - 1:
        print(my_list[idx])
        idx = idx + 1


my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
