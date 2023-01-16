#!/usr/bin/python
import random

value = random.randint(0,10) #This will pick an integer between 0 and 10

guess=input("Guess a Number: ")   
guess=int(guess)     #When using input, it will be a string type. Convert it to an integer.

'''
Only three possibilities exist:
1. The guess was correct
2. The guess was too low
3. The guess was too high
'''

if guess == value:
    print("You guessed correctly")
elif guess == value:
    print("Your guess was too low. My number was " + str(value))
else:
    print("Your guess was too high. My number was " + str(value))


