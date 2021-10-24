#!/usr/bin/env python3 

"""
Write a guessing game where the user has to guess a secret number. After every guess the program tells the user
whether their number was too large or too small. At the end the number of tries needed should be printed. 
It counts only as one try if they input the same number multipletimes consecutively.
"""

from random import randint

random_number = randint(1, 10)
tries = []
user_number = int(input("Guess : ")); tries.append(user_number)


while user_number != random_number:

    if user_number > random_number: 
        user_number = int(input("Too big, guess again : "))
        tries.append(user_number)
    else:
        user_number = int(input("Too small, guess again : "))
        tries.append(user_number)


#'It counts only as one try if they input the same number'.
print("Attempt #{}".format(len(list(dict.fromkeys(tries)))))
