#!/usr/bin/env python3 

"""
2. Write function that reverses a list, preferably in place.
"""

#Using splicing in python3.
#a_list = [1,2,3,4,5]
#a_list[::-1]
#Or using build in function reversed(). Like in previous sorted(n) or n.sort().


sample = [1,2,3,4,5]


def Reverse(array):

    right = len(array)-1  
    left = 0

    while left < right:

        #Introducing third variable like in fibonacci but there is another way.
        #temp = array[left]
        #array[left] = array[right]
        #array[right] = temp

        #Or in more 'Python dynamic' way.
        #SWAPPING!
        array[left], array[right] = array[right], array[left]
       
        right -= 1
        left += 1

    return array

print(Reverse(sample))


"""
Interisting conclusions from https://pythoncentral.io/python-reverse-list-place/

This is a very commonly asked interview question. Try using the same approach to solve these puzzles and comment below:

LS2a. Reverse the string “hello”. Output should be “olleh”
LS2b. Reverse the “I love Python Central”. Output should be“Central Python love I”
LS2c. Check if “madam” is a palindrome or not
"""
