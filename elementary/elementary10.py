#!/usr/bin/env python3 


#Write a program that prints the next 20 leap years.

import datetime

this_year = int(f"{datetime.datetime.now():%Y}")

next_20_leap_years = []


while len(next_20_leap_years) < 20:

    this_year += 1

    if this_year%4 == 0 and this_year%100 == 0 and this_year%400 == 0:
        next_20_leap_years.append(this_year)
    
    elif this_year%4 == 0 and this_year%100 != 0:
        next_20_leap_years.append(this_year)


print(next_20_leap_years)
