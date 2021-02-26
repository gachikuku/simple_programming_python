#!/usr/bin/env python3 

"""
4. Write a function that returns the elements on odd positions in a list.
"""

a_array = [0,1,2,3,4,5]


def oddPosition(array):

    b_array = []

    for i in range(len(array)):
        if i%2 != 0:
            b_array.append(array[i])

    return b_array

print(oddPosition(a_array))
