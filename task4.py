#!python3

"""
Write a program to ask the user to input a length in centimeters. Convert this into feet and inches.  Round your inches to the nearest whole inch.
You will likely need to make use of at least one of the following:
* % modulus
* math.floor()

Sample output:
```
Enter a length in centimeters: 172
172 centimeters is 5 feet and 8 inches

Enter a length in centimeters: 32
32 centimeters is 1 feet and 1 inches
```
"""
import math

cm = float(input("Enter a length in centimeters: "))

inches = cm / 2.54
feet = math.floor(inches / 12)
leftover = round(inches - feet * 12)

print(f"{int(cm)} centimeters is {feet} feet and {leftover} inches")


