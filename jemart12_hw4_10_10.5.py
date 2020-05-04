"""
Name: Jose Martinez
Class: CS 521 - 2020 Spring 1
Date: February 15, 2020
Homework Problem # 10.5
Description: Capturing distinct numbers from user input
"""

import sys

try:
    # prompt user input to enter numbers in interger form
    user_input = input('Enter ten numbers in interger form'
                       ' followed by a space: ')
    # use the split to allow spacing
    numbers = user_input.split(' ')

    # prompt the user to enter exactly 10 values
    while len(numbers) != 10:
        print('You must enter 10 numbers in interger form'
              ' using a space in between them')
        sys.exit()

    # convert the user's entry in to a list with int form
    list1 = [int(x) for x in numbers]
    list2 = []

    # capture the elements in list1 and copy them to empty list2
    for user_num in list1:
        if user_num not in list2:
            list2.append(user_num)

    # remove the brackets from the list by creating a string
    list_string = ' ' .join(str(unique_list) for unique_list in list2)

    print('The distinct numbers are: {}' .format(list_string))

except ValueError:
    print('Please enter a valid interger number')
    sys.exit()
