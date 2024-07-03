# https://www.notion.so/Modern-Art-Drawing-b5381c39e76e4a09b2881e8a470a6c07

import turtle
from random import randint

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

window = None
pen = None


def setup_window():
    global window
    window = turtle.Screen()
    window.title('Modern Art')
    window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)  # width and height of the window
    window.bgcolor('gray10')


def create_pen():
    global pen
    pen = turtle.Turtle()  # create a Turtle and it always start at (0, 0)
    pen.shape("turtle")
    pen.speed(0)


def pick_colour():
    turtle.colormode(255)
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    pen.pencolor(red, green, blue)
    pen.fillcolor(red, green, blue)


def pick_position():
    pen.penup()
    x = randint(-200, 200)
    y = randint(-200, 200)
    pen.goto(x, y)
    pen.pendown()


def pick_heading():
    heading = randint(0, 360)
    pen.setheading(heading)


def draw_rectangle():
    pen.hideturtle()
    length = randint(10, 150)
    height = randint(10, 150)

    pen.begin_fill()
    for _ in range(2):
        pen.forward(length)
        pen.right(90)
        pen.forward(height)
        pen.right(90)
    pen.end_fill()


def draw_square():
    pen.hideturtle()
    side_length = randint(10, 150)

    pen.begin_fill()
    for _ in range(4):
        pen.forward(side_length)
        pen.right(90)
    pen.end_fill()


def draw_circle():
    pen.hideturtle()
    radius = randint(10, 100)

    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()


def draw_star():
    pen.hideturtle()
    size = randint(50, 150)
    num_points = randint(2, 5) * 2 + 1
    angle = 180 - (180/num_points)

    pen.begin_fill()
    for _ in range(num_points):
        pen.forward(size)
        pen.right(angle)
    pen.end_fill()


def create_art():
    for i in range(50):
        pick_colour()
        pick_position()
        pick_heading()
        # draw_rectangle()
        # draw_square()
        # draw_circle()
        draw_star()


setup_window()

create_pen()

create_art()

window.mainloop()
