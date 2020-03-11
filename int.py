#!/usr/bin/python3
#Author: Samuel Rayne
#Date: 05/19/2023
#version: 1.0

guess= input("Guess a number: ")

guess= int (guess)

if guess > 3:
    print("you guessed correctly")
else:
    print("better luck next time")