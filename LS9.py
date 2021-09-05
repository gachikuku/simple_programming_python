#!/usr/bin/env python3 

"""
9. Write a function that concatenates two lists. [a,b,c], [1,2,3] → [a,b,c,1,2,3] 
"""

letters = ["a","b","c"]
numbers = [1,2,3]
con_list = []


#for letter in letters:
#    con_list.append(letter)
#
#for number in numbers:
#    con_list.append(number)

#or in much simplier...

con_list = letters + numbers

print(con_list)
