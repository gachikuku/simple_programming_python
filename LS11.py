#!/usr/bin/env python3

"""
11. Write a function that merges two sorted lists into a new sorted list. [1,4,6],[2,3,5] → [1,2,3,4,5,6]. You can do this quicker than concatenating them followed by a sort.
"""

def merge_sorted(x,y):

    z = x + y
    return sorted(z)


example_1 = [1,4,6]
example_2 = [2,3,5]


print(merge_sorted(example_1, example_2))
