from random import randint
import turtle
# This should be a project that shows how you can create
# some animation by switching costumes in Python

# https://scratch.mit.edu/projects/237521692/
# https://scratch.mit.edu/projects/25383083/editor/
# https://scratch.mit.edu/projects/456587459/editor/

# Idea: draw a animated ghost face
# - reference for costumes:https://www.freepik.com/free-vector/collection-cute-halloween-ghosts_1319212.htm#fromView=search&page=1&position=29&uuid=cf5b65a7-71d0-4fe3-982e-44272b07ac6e
# - reference for animation: https://scratch.mit.edu/projects/237521692/


# Fullwindow the canvas
window = turtle.Screen()
window.title('Make a Face')
window.setup(600, 600)  # width and height of the window
window.bgcolor('gray10')


def draw_oval():
    '''
    t = turtle.Turtle()
    t.penup()
    t.goto(0, 0)  # Position the turtle at the center
    t.speed(0)

    t.fillcolor('gray10')
    t.begin_fill()
    t.setheading(-45)
    for loop in range(2):
        t.circle(25, 90)
        t.circle(25/2, 90)
    t.end_fill()
    t.hideturtle()
    '''
    t = turtle.Turtle()
    t.penup()
    t.shape("circle")
    t.shapesize(2.5, 2.5)
    t.fillcolor('gray10')

    t.stamp()
    t.goto(0, 40)
    t.stamp()

    t.clearstamps()
    t.hideturtle()


def draw_eyes():
    eyes = turtle.Turtle()
    eyes.penup()
    eyes.speed(0)

    eyes.fillcolor('gray10')
    eyes.goto(-40, 80)
    eyes.begin_fill()
    eyes.circle(25)
    eyes.goto(40, 80)
    eyes.circle(25)
    eyes.end_fill()

    # eyes.hideturtle()


def draw_body():
    # Begin!
    body = turtle.Turtle()  # create a Turtle and it always start at (0, 0)
    body.shape("turtle")
    body.speed(0)

    body.penup()
    body.goto(100, 100)
    body.left(90)

    body.fillcolor('white')
    body.begin_fill()
    body.circle(100, 180)
    body.forward(180)
    body.left(90)
    body.forward(200)
    body.left(90)
    body.forward(180)
    body.end_fill()

    body.goto(100, -80)

    body.fillcolor('gray10')
    body.begin_fill()

    for _ in range(5):
        body.circle(20, 180)
        body.right(180)
    body.end_fill()

    body.hideturtle()


draw_body()
draw_eyes()
draw_oval()

window.mainloop()
