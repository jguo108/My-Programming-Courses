from random import *


def print_students(header, students):
    print(header)
    print(",".join(students))


# def pick_student(students):
def pick_student(from_list, to_list):
    student_picked = choice(from_list)
    from_list.remove(student_picked)
    to_list.append(student_picked)


students = ["Harry", "Alice", "William",
            "Mary", "James", "Alex", "Sara", "Jenifer", "Mark"]

team_A = []
team_B = []

print_students("Students:", students)

while len(students) != 0:
    pick_student(students, team_A)

    if len(students) == 0:
        break

    pick_student(students, team_B)

print_students("Team A:", team_A)
print_students("Team B:", team_B)
