# https://www.notion.so/4-Turtle-Race-09e1bed1c5674b3d9c05335d1ab91437

import turtle
from random import randint

# Fullscreen the canvas
screen = turtle.Screen()
screen.setup(481, 360)


def draw_track():
    t = turtle.Turtle()
    t.speed(10)
    t.penup()
    t.goto(-140, 80)

    # Draw lanes
    for _ in range(5):
        t.pendown()
        t.forward(280)
        t.penup()
        t.backward(280)
        t.right(90)
        t.forward(40)
        t.left(90)

    # Write lane numbers
    t.goto(-160, 60)
    t.right(90)
    for i in range(4):
        t.write(i)
        t.forward(40)

    t.hideturtle()


def create_turtle(color, start_x, start_y):
    t = turtle.Turtle()
    t.shape('turtle')
    t.color(color)
    t.penup()
    t.goto(start_x, start_y)
    return t


def celebrate(winner):
    for _ in range(10):
        winner.right(36)


def has_won(t):
    t.forward(randint(1, 5))
    if t.xcor() > 140:
        celebrate(t)
        return True
    else:
        return False


"""
def start_race():
  while True:
    james.forward(randint(1, 5))
    if james.xcor() > 140:
      celebrate(james)
      break
    alice.forward(randint(1, 5))
    if alice.xcor() > 140:
      celebrate(alice)
      break
    sarah.forward(randint(1, 5))
    if sarah.xcor() > 140:
      celebrate(sarah)
      break
    danny.forward(randint(1, 5))
    if danny.xcor() > 140:
      celebrate(danny)
      break
"""


def start_race():
    while True:
        if has_won(james):
            break
        if has_won(alice):
            break
        if has_won(sarah):
            break
        if has_won(danny):
            break


draw_track()
james = create_turtle('red', -140, 60)
alice = create_turtle('blue', -140, 20)
sarah = create_turtle('green', -140, -20)
danny = create_turtle('black', -140, -60)
start_race()

screen.mainloop()
