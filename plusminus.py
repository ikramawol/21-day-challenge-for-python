#!/usr/bin/python3
import math
import os
import random
import re
import sys

def plusMinus(arr):
    pos, neg, zer = 0, 0, 0
    for i in arr:
        if i < 0:
            neg += 1
        elif i > 0:
            pos += 1
        else:
            zer += 1
    positive = pos / n
    print("{:6f}".format(positive))
    negative = neg / n
    print("{:6f}".format(negative))
    zero = zer / n
    print("{:6f}".format(zero))
if __name__ == '__main__':
    n = int(input().strip())
    
    arr = list(map(int, input().rstrip().split()))
    
    plusMinus(arr)
