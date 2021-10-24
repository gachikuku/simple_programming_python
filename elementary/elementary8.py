"""
Write a program that prints all prime numbers. (Note: if your programming language does not support arbitrary size nbers, printing all primes up to the largest number you can easily represent is fine too.)
"""

#!/usr/bin/env python3
limit = int(input("Enter range:"))
primes = []

for num in range(1, limit+1):  
   if num > 1:  
       for i in range(2, num):  
           if (num % i) == 0:  
               break  
       else:  
          primes.append(num) 

print(len(primes),"primes in",limit,"elements,",int(((len(primes)/limit))*100),"%")
