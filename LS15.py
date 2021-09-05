#!/usr/bin/env python
"""
15. Write functions that add, subtract, and multiply two numbers in their digit-list representation (and return a new digit list). If you’re ambitious you can implement Karatsuba multiplication. Try different bases. What is the best base if you care about speed? If you couldn’t completely solve the prime number exercise above due to the lack of large numbers in your language, you can now use your own library for this task.
"""
#Functions used to add two numbers without the normal operators or rather using bitwise operators
#Really good reference link: https://realpython.com/python-bitwise-operators/

def addition(a,b):

    while b != 0:
        borrow = a & b
        a = a ^ b
        b = borrow << 1
    return a


def subtraction(a,b):

    while b != 0:
        borrow = ~a & b
        a = a ^ b
        b = borrow << 1
    return a


def multiplication(a,b):

    result = 0

    while b > 0:
        if b & 1: result = result + a
        a = a << 1
        b = b >> 1
    return result

print(addition(1,19))
print(subtraction(5,2))
print(multiplication(5,5))
