#!/usr/bin/env python3 

"""
1. Write a function that returns the largest element in a list.
"""

#Solution using build in functions.
#sample = [1,2,3,4,5,3,1]
#sorted_sample = sorted(sample)
#print((sorted_sample[-1]))


example = [1,5,3,2]


def largest(sample):

    largest = sample[0]

    for i in sample:
        if i > largest: largest = i

    return largest


print(example)
print(largest(example))
