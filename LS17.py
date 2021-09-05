#!/usr/bin/env python
"""
17. Implement the following sorting algorithms: Selection sort, Insertion sort, Merge sort, Quick sort, Stooge Sort. Check Wikipedia for descriptions.
"""

def selection_sort(array):

    for i in range(len(array)):

        jMin = i

        for j in range(i, len(array)):

            if array[j] < array[jMin]: jMin = j

        if jMin != i: array[i], array[jMin] = array[jMin], array[i]

    return array


def insertion_sort(array):

    i = 1

    while i < len(array):

        j = i

        while j > 0 and array[j-1] > array[j]:

            array[j], array[j-1] = array[j-1], array[j]

            j -= 1

        i += 1

    return array


def merge_sort(array):




    return array


unsorted = [3,5,1,2,4]

print(selection_sort(unsorted))
print(insertion_sort(unsorted))
