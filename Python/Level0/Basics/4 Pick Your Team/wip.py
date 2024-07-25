# import random
# from random import randint
# from random import choice
from random import *

students = ["Harry", "Alice", "William",
            "Mary", "James", "Alex", "Sara", "Jenifer"]

team_A = []
team_B = []


# print(students)
print("Students:",)

# all_names = ""
# for student in students:
#    # print(student)
#    all_names += student
#    all_names += ","

all_names = ",".join(students)
print(all_names)

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
