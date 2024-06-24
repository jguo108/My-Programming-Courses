# This should be a project that shows how you can create
# some animation by switching costumes in Python

# https://scratch.mit.edu/projects/237521692/
# https://scratch.mit.edu/projects/25383083/editor/
# https://scratch.mit.edu/projects/456587459/editor/

# Idea: draw a animated ghost face
# - reference for costumes:https://www.freepik.com/free-vector/collection-cute-halloween-ghosts_1319212.htm#fromView=search&page=1&position=29&uuid=cf5b65a7-71d0-4fe3-982e-44272b07ac6e
# - reference for animation: https://scratch.mit.edu/projects/237521692/

import turtle
from random import randint

# Fullwindow the canvas
window = turtle.Screen()
window.title('Make a Face')
window.setup(600, 600)  # width and height of the window
window.bgcolor('gray10')

# Begin!
t = turtle.Turtle()  # create a Turtle and it always start at (0, 0)
t.shape("turtle")
t.speed(0)


t.penup()
t.goto(100, 100)
t.left(90)

t.fillcolor('white')
t.begin_fill()
t.circle(100, 180)
t.forward(180)
t.left(90)
t.forward(200)
t.left(90)
t.forward(180)
t.end_fill()

t.goto(100, -80)


t.fillcolor('gray10')
t.begin_fill()
for _ in range(5):
    t.circle(20, 180)
    t.right(180)
t.end_fill()


t.hideturtle()


window.mainloop()
