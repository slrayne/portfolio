#!/usr/bin/python3
#Author: Samuel Rayne
#Date: 05/19/2023
#version: 1.0

import random

value = random.randint(0,10)

guess=int(input ("Guess a number: "))

if value == guess:
    print("You guessed correctly")
else:
    print("Better luck next time! My number was " + str(value)) 