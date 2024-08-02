# Question 1

# 1. Python Regular Expressions Mastery



# Task 1: Name Verification



# Problem Statement:  Write a function that takes in a list of names, and verifies that the names are valid names using a regex pattern and match(), and prints the name if it is valid, "Invalid name" if the name is not.

# Use the following list as an argument to test your function.

import re

names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken", "Jordan Alexander Williams", "Madonna", "programming is cool"]

def valid_names():
    for name in names:
    #print(name)
        val_name = re.match(r"\D+[A-Z]\D+", name)
        if val_name:
            print(name)
        else:
            print("Invalid Name")
valid_names()

