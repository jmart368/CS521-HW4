"""
Homework Problem # 11.3
Description: Sorting grades for students
"""


def grades():
    """
    Grades sorted by ascending values
    """
    answers = [
        ['A', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['D', 'B', 'A', 'B', 'C', 'A', 'E', 'E', 'A', 'D'],
        ['E', 'D', 'D', 'A', 'C', 'B', 'E', 'E', 'A', 'D'],
        ['C', 'B', 'A', 'E', 'D', 'C', 'E', 'E', 'A', 'D'],
        ['A', 'B', 'D', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['B', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['B', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['E', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D']]

    # create a key list using the brackets
    keys = ['D', 'B', 'D', 'C', 'C', 'D', 'A', 'E', 'A', 'D']

    # Initialize score and student list
    score = list()
    student = list()

    # grade and assign the scores
    for student_score in range(len(answers)):
        correct_count = 0

        # Grade one student
        for answer_key in range(len(answers[student_score])):
            if answers[student_score][answer_key] == keys[answer_key]:
                correct_count += 1
        score.append(correct_count)
        student.append(student_score)

    # sort the student code in ascending order
    # use the lambda nested function to sort within a nested function
    student.sort(key=lambda student_grade: score[student_grade])
    for student_grade in student:
        print('Student {}\'s correct count is {}' .format
              (student_grade, score[student_grade]))


if __name__ == "__main__":
    grades()
