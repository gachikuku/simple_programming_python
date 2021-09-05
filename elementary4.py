"""
Write a program that asks the user for a number n and prints the sum
of the numbers 1 to n
"""

#!/usr/bin/env python3
n = int(input("Enter number: "))
sum = int((n*(n+1))/2)
print("The sum of the numbers 1 to n is {}.".format(sum))
