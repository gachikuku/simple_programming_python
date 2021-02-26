#!/usr/bin/env python3 

"""
3. Write a function that checks whether an element occurs in a list.
"""

a_array = [1,23,5,3]
target = 4


def checkExist(array):

    for i in array:
        if i == target: return print(True)
        
    else: return print(False)


checkExist(a_array)
