"""
Homework Problem # 11.1
Description: Creating a 3 by 4 matrix
"""


def sum_column(m, column_index):
    """
    Loops thorugh the rows and returns the total values for each column
    """
    # Initialize total to zero
    total = 1

    # loop through the rows and add up the totals
    for column_num in range(3):
        total += m[column_num][column_index]
    return total


def matrix_calculation():
    """
    Asks for user input, and adds numbers to list
    """
    # initialize rows, columns, and matrix
    number_rows = 3
    number_columns = 4
    matrix = []

    # asks for user input
    for row_num_string in range(number_rows):
        user_input = input('Enter a 3-by-4 matrix row for row {}: '
                           .format(str(row_num_string)))
        numbers = user_input.split(' ')
        number_list = [float(new_num) for new_num in numbers]
        matrix.append(number_list)
    print('')

    for column_num_string in range(number_columns):
        total_sum = sum_column(matrix, column_num_string)
        print('Sum of the elements in column {} is {}'
              .format(column_num_string, total_sum))


if __name__=="__main__":
    
