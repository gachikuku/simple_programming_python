"""
Modify the previous program such that only multiples of three or five are considered
in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17
"""

#!/usr/bin/env python3

n = 17
total=0

for i in range(1,n-1):

    if i%3 == 0 or i%5 == 0:

        total = total + i

print(total)
