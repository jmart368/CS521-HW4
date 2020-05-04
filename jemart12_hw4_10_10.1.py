"""
Name: Jose Martinez
Class: CS 521 - 2020 Spring 1
Date: February 15, 2020
Homework Problem # 10.1
Description: Creating a grading scheme based on max input
"""

import sys

try:
    user_input = input('Enter scores in integer form separated by spaces: ')
    grades = user_input.split(' ')
    # convert entries into intergers
    grade_list = [int(x) for x in grades]

    # establish the max score based on the highest score entered
    highest_grade = max(grade_list)

    # create the grading scheme
    for student in range(len(grade_list)):
        if grade_list[student] >= highest_grade - 10:
            grade = 'A'
        elif grade_list[student] >= highest_grade - 20:
            grade = 'B'
        elif grade_list[student] >= highest_grade - 30:
            grade = 'C'
        elif grade_list[student] >= highest_grade - 40:
            grade = 'D'
        else:
            grade = 'F'

        print('Student {} score is {} and grade is {}'
              .format(student, grade_list[student], grade))

except ValueError:
    print('Please enter valid integer grades separated by spaces.')
    sys.exit()
