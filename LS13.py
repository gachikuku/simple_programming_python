#!/usr/bin/env python

"""
13. Write a function that computes the list of the first 100 Fibonacci numbers. The first two Fibonacci numbers are 1 and 1. The n+1-st Fibonacci number can be computed by adding the n-th and the n-1-th Fibonacci number. The first few are therefore 1, 1, 1+1=2, 1+2=3, 2+3=5, 3+5=8.
"""


#Turns out while loops much more efficient than using recursion
#Although recursion is an interisting concept

def fib(n):

    count = 0
    a, b = 0, 1

    while count < n:

        print(a)
        a, b = b, a+b

        count += 1

print(fib(100))
