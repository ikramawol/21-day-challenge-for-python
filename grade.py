#!/usr/bin/python3
def computegrade(x):
    
    if x >= 0.9:
        return "A"
    elif x >= 0.8:
        return "B"
    elif x >= 0.7:
        return "C"
    elif x >= 0.6:
        return "D"
    elif x < 0.6:
        return "F"
        
score = float(input("Enter score:"))
grade = computegrade(score)
print(grade)
