#!/usr/bin/python3
""" printing combination of two numbers that are different and the first digit is always lessthan the second digit"""
x = 0
y = 1
for x in range(0, 10):
    for y in range(1, 10):
        if x != y and x < y:
            if x == 8:
                print("{:d}{:d}".format(x, y))
            else:
                print("{:d}{:d}".format(x, y), end = ", ")
