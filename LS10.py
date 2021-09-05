#!/usr/bin/env python3 

"""
Write a function that combines two lists by alternatingly taking elements, e.g. [a,b,c], [1,2,3] → [a,1,b,2,c,3].
"""


letters = ["a","b","c"]
numbers = [1,2,3]

#Using numpy but outputs have '' around numbers
#import numpy as np
#alternate_list = np.array([[i,j] for i, j in zip(letters, numbers)]).ravel()


#This is called list comprehension using zip(can take more than 2 args) function.

def alternatelist(x,y):

    return [i for pair in zip(x,y) for i in pair]


print(alternatelist(letters,numbers))
