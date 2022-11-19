"""
A simple program to capture students name, score and grade
"""

# Declare variables
name_list = []
score_list = []
grade_list = []

def greeting():
    # A Greeting function
    print('*' * 42)
    print('*' * 3 + ' Welcome to pythons student tracker ' + '*' * 3)
    print('*' * 42)

def user_inputs():
    # Function to get user inputs
    student_name = input("Enter students name: ")
    student_score = int(input("Enter students score:"))
    name_list.append(student_name)
    score_list.append(student_score)
    if student_score > 70:
        grade_list.append('Distinction')
    elif student_score > 50 and student_score < 70:
        grade_list.append('Merit')
    elif student_score > 30 and student_score < 50:
        grade_list.append('Pass')
    else:
        grade_list.append('Fail')
    return student_name, student_score

def start():
    # This function calls all our other functions to make to program run
    option = 'x'
    counter = 1

    greeting()
    while not option == 'N':
        name, score = user_inputs()
        print(f"Student {name} added with {score}% score successfully")
        option = input("Continue? [Y/N]").upper()

    for student, score, grade in zip(name_list, score_list, grade_list):
        print(f"[{counter}] - {student} - {score}% - {grade}")
        counter += 1


start()