#!/usr/bin/python3
"""removing C and c"""
"""simple way"""
def no_c(my_string):
    return my_string.translate({ord(i): None for i in 'cC'})

""" another way """
"""def no_c(my_string):
    new_str = ""
    for i in my_string:
        if i != "c" and i != "C":
            new_str += i
    return new_str"""

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
