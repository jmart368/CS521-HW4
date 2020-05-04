"""
Name: Jose Martinez
Class: CS 521 - 2020 Spring 1
Date: February 15, 2020
Homework Problem # 10.3
Description: Occurence of numbers
"""

import sys

try:
    # prompt user input
    user_input = input('Enter integers between 1 and 100 seperated by'
                       ' a space: ')
    # split the inputs by a space, no commas
    numbers = user_input.split(' ')
    # convert inputs into integers
    number_list = [int(x) for x in numbers]
    # estbalish the range from 1-100
    count = [0 for i in range(1, 100)]

    # establish a count list
    for numbers in number_list:
        count[numbers] += 1

    # check and count for duplicated entries
    for duplicates in range(len(count)):
        if count[duplicates] != 0:
            if count[duplicates] == 1:
                print('{} occurs 1 time' .format(duplicates))
            else:
                print('{} occurs {} times' .format(duplicates,
                                                   count[duplicates]))

except ValueError:
    print('Please enter a valid number in integer form. Do not use'
          ' decimals or commas as separators.')
    sys.exit()
