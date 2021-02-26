#!/usr/bin/env python3 

"""
7. Write three functions that compute the sum of the numbers in a list: using a for-loop, a while-loop and recursion.
"""


def forloopSum(array):

    total = 0

    for i in array:
        total += i

    return total



def whileloopSum(array):

    total = 0
    counter = 0
    
    while counter < len(array):

        total += array[counter] 

        counter += 1

    return total    


#https://runestone.academy/runestone/books/published/pythonds/Recursion/pythondsCalculatingtheSumofaListofNumbers.html

def recursionSum(array):

    if len(array) == 1: return array[0]
    else: return array[0] + recursionSum(array[1:])


a_array = [1,2,3,4]

print(forloopSum(a_array))
print(whileloopSum(a_array))
print(recursionSum(a_array))
