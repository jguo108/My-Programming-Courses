# import random
# from random import randint
# from random import choice
from random import *


def print_students(header, students):
    print(header)
    print(",".join(students))


# def pick_student(students):
def pick_student(from_list, to_list):
    # student_picked = choice(students)
    student_picked = choice(from_list)
    from_list.remove(student_picked)
    to_list.append(student_picked)


# students = ["Harry", "Alice", "William",
#            "Mary", "James", "Alex", "Sara", "Jenifer"]

# students = ["Harry", "Alice", "William",
#            "Mary", "James", "Alex", "Sara", "Jenifer", "Mark"]

students = []

team_A = []
team_B = []


# print(students)

# all_names = ""
# for student in students:
#    # print(student)
#    all_names += student
#    all_names += ","

# print("Students:",)
# all_names = ",".join(students)
# print(all_names)
print_students("Students:", students)

'''
while len(students) != 0:
    # student_picked = students[random.randint(0, 7)]
    # student_picked = students[random.randint(0, len(students) - 1)]
    # student_picked = students[randint(0, len(students) - 1)]
    student_picked = choice(students)
    students.remove(student_picked)
    # print(student_picked)
    # print(students)
    team_A.append(student_picked)
    # print(team_A)

    student_picked = choice(students)
    students.remove(student_picked)
    team_B.append(student_picked)
'''

while len(students) != 0:
    pick_student(students, team_A)

    if len(students) == 0:
        break

    pick_student(students, team_B)


# print("Team A:",)
# print(",".join(team_A))

# print("Team B:",)
# print(",".join(team_B))

print_students("Team A:", team_A)
print_students("Team B:", team_B)
