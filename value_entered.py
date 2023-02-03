#!/usr/bin/python3
""" A program that accepts inputs and evaluates if the value entered is number or not.
Then computes its total value, counts the number of values entered by the user, and the average of the numbers.
"""
total = 0
average = 0
count = 0

while True:
    value =input("Enter a number:")
    if value == "done":
        break
    try:
        number = float(value)
        total = number + total
        count = count + 1
    except:
        print("Invalid Input")
    average = total/count
print(total, count, average)
