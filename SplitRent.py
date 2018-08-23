#!/usr/bin/env python
# Rent Share
# Copyright 2018 Brandon Townes

print("Welcome to Rent Share v.1!", "The Millennial way to split bills", '\n')

# inputs

# Convert variables into a dictionary -  personIncome = name : income
# https://automatetheboringstuff.com/chapter4/

#p1 = input("Please enter the Boyfriend's name: ")

print("Please enter the Boyfriend's name: ")
p1 = input()
p1Income = float(input("How much do you make a month? "))

p2 = input("Now enter the Girlfriend's name: ")
p2Income = float(input("And the Girlfriend's income?: "))

totalRent = float(input("Enter the total bills for this month: "))

# Function


# convert this to a for loop - iteriate over each key, take the value and % by the totalRent variable.
def RentShare():
    totalIncome = p1Income + p2Income
    p1Percent = p1Income / totalIncome
    p2Percent = p2Income / totalIncome
    totalforP1 = totalRent * p1Percent
    totalforP2 = totalRent * p2Percent
    print("%s, the total for you this month is: %s" % (p1, totalforP1))
    print("%s, the total for you this month is: %s" % (p2, totalforP2))
    # investigate combining this into one print statement
    # also, maybe break these into new lines


RentShare()

#
# Ideas
#
# print(p1, '- your total for this month is:', '\n', totalforP1)

#
