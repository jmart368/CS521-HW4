"""
Homework Problem # 14.1
Description: Count keywords from an existing file
"""

import os.path
import sys


def key_words():
    keywords = {"and", "as", "assert", "break", "class",
                "continue", "def", "del", "elif", "else",
                "except", "False", "finally", "for", "from",
                "global", "if", "import", "in", "is", "lambda",
                "None", "nonlocal", "not", "or", "pass", "raise",
                "return", "True", "try", "while", "with", "yield"}

    filename = input('Enter a Python source code filename: ').strip()

    # check to see if the file exist
    if not os.path.isfile(filename):
        print('File {} does not exist'.format(filename))
        sys.exit()

    # open files in read mode
    infile = open(filename, 'r')

    # read the file and split its elements
    text = infile.read().split()

    # close the file after it was read
    infile.close

    # invoke number and word count
    number_count = 0
    word_count = {}
    # store and count the keywords from the set above
    for word in text:
        if word in keywords:
            number_count += 1
            if word in word_count.keys():
                word_count[word] += 1
            else:
                word_count[word] = 1

    # print the file and count the keywords
    print('The unique number of keywords in {} is {}'.format
          (filename, number_count))

    # print the keywords and the number of times it appears
    print('The keywords and the number of times each keyword appears'
          ' in this file are as follows:')
    for key in word_count.keys():
        print('{}: ({})' .format(key, word_count[key]))


if __name__ == "__main__":
    key_words()
