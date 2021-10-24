"""
Write a program that asks the user for a number n and gives them the possibility
to choose between computing the sum and computing the product of 1,…,n.
"""
#!/usr/bin/env python3
n = int(input("Enter a number: "))
choice = int(input("Enter 1 for SUM or 2 for PRODUCT: "))


def computeSum(n):
    return int((n*(n+1))/2)


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


if choice == 1:
    print(computeSum(n))
else:
    print(factorial(n))
