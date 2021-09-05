#!/usr/bin/env python

"""
12.  Write a function that merges two sorted lists into a new sorted list. [1,4,6],[2,3,5] → [1,2,3,4,5,6]. You can do this quicker than concatenating them followed by a sort.
"""


def rotate(x,k):

    return x[k:] + x[:k]


example = [1,2,3,4,5]
k = 2


print(rotate(example,k))
