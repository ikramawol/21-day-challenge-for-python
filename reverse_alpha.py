#!/usr/bin/python3
""" reverce alphabete and making the letters upper and lowercase interchangabley"""
x = 90
while x >= 65 and x <= 90:
    if x % 2 == 0:
        print((chr(x).lower()), end = "")
    else:
        print(chr(x), end = "")
    x = x - 1
    
