#! /usr/bin/env python
# Rent Share
# Copyright 2018 Brandon Townes

print("Welcome to Rent Share v.1!", "The Millennial way to split bills", '\n')

# inputs
p1 = input("Please enter the Boyfriend's name: ")
p1Income = int(input("How much do you make a month? "))

p2 = input("Now enter the Girlfriend's name: ")
p2Income = int(input("And the Girlfriend's income?: "))

totalRent = int(input("Enter the total bills for this month: "))

# Functions


def RentShare():
    totalIncome = p1Income + p2Income
    p1Percent = p1Income / totalIncome
    p2Percent = p2Income / totalIncome
    totalforP1 = totalRent * p1Percent
    totalforP2 = totalRent * p2Percent
    print(p1, '- your total for this month is:', '\n', totalforP1)
    print(p2, '- your total for this month is:', '\n', totalforP2)


RentShare()
