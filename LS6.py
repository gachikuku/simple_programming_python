#!/usr/bin/env python3 

"""
Please refer to LS2.py file for further info.
"""

def stringReverse(word):

    word = list(word)
    right = len(word)-1
    left = 0

    while left < right:

        word[left], word[right] = word[right], word[left]
        
        right -= 1
        left += 1

    return word
    

def palindromeChecker(word):
    
    word = list(word)

    if word == stringReverse(word): return print(True)
    else: return print(False)

palindromeChecker("racecar")
