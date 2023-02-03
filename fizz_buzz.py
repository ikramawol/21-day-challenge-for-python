#!/usr/bin/python3
def fizzbuzz():
    x = 1
    while x >= 1 and x < 100:
        if x % 3 == 0:
            print("Fizz", end = " ")
        elif x % 5 == 0:
            print("Buzz", end = " ")
        elif x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz", end = " ")
        else:
            print(x, end = " ")
        x = x + 1
fizzbuzz()
