#!/usr/bin/env python3 

"""
Write a program that computes the total of an alternating series where each element of the series is an expression of the form ((-1)^{k+1})/(2 * k-1) for each value of k from 1 to a million, multiplied by 4. Or, in more mathematical notation
"""

import math

total = 0

for k in range(1,1000001):
    
    total += ((-1)^(k+1))/((2*k)-1) 
    
print(total*4)
