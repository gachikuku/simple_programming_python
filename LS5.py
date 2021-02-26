#!/usr/bin/env python3 

"""
5. Write a function that computes the running total of a list.
"""

def runningTotal(array):

    total = 0
    for i in array:
        total += i

    return total

a_array = [1,2,3,4]

print(runningTotal(a_array))
