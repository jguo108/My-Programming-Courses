# https://www.notion.so/Modern-Art-Drawing-b5381c39e76e4a09b2881e8a470a6c07

import turtle
from random import randint

# Fullwindow the canvas
window = turtle.Screen()
window.title('Modern Art')
window.setup(600, 600)  # width and height of the window
window.bgcolor('gray10')

# Begin!
t = turtle.Turtle()  # create a Turtle and it always start at (0, 0)
t.shape("turtle")
t.speed(0)


def randomcolour():
    turtle.colormode(255)
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    t.pencolor(red, green, blue)
    t.fillcolor(red, green, blue)


def randomplace():
    t.penup()
    x = randint(-200, 200)
    y = randint(-200, 200)
    t.goto(x, y)
    t.pendown()


def randomheading():
    heading = randint(0, 360)
    t.setheading(heading)


def drawrectangle():
    t.hideturtle()
    length = randint(10, 150)
    height = randint(10, 150)

    t.begin_fill()
    for _ in range(2):
        t.forward(length)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()


def drawsquare():
    t.hideturtle()
    side_length = randint(10, 150)

    t.begin_fill()
    for _ in range(4):
        t.forward(side_length)
        t.right(90)
    t.end_fill()


def drawcircle():
    t.hideturtle()
    radius = randint(10, 100)

    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def drawstar():
    t.hideturtle()
    size = randint(50, 150)
    num_points = randint(2, 5) * 2 + 1
    angle = 180 - (180/num_points)

    t.begin_fill()
    for _ in range(num_points):
        t.forward(size)
        t.right(angle)
    t.end_fill()


for i in range(50):
    randomcolour()
    randomplace()
    randomheading()
    # drawrectangle()
    # drawsquare()
    # drawcircle()
    drawstar()

window.mainloop()
