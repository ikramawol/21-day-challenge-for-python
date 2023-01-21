#!/usr/bin/python3
def computepay(hours, rate):
    # overtime hours means morethan 40hours
    if hours > 40:
        overtime_hours = hours - 40 #calculating overtime hours
        overtime = (overtime_hours) * (rate * 1.5) # calculating the hourly rate for the over time only
    else:
        return hours * rate #calculeting hourly rate when there where no overtime hours
        # pay computation 
    pay = (40 * rate) + overtime # 40 is the normal working hours
    return pay 

hours = int(input("Enter Hours:"))
rate = int(input("Enter Rate:"))
pay = computepay(hours, rate)
print(f"Pay:{float(pay)}")
