# https://www.notion.so/Modern-Art-Drawing-b5381c39e76e4a09b2881e8a470a6c07

import turtle
from random import randint

# Fullscreen the canvas
screen = turtle.Screen()
screen.setup(480, 360)  # width and height of the screen

# Begin!
t = turtle.Turtle()  # create a Turtle and it always start at (0, 0)


def randomcolour():
    ### Uncomment the line below if you are not using trinket###
    turtle.colormode(255)
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    t.pencolor(red, green, blue)


def randomplace():
    t.penup()
    x = randint(-200, 120)
    y = randint(-200, 120)
    t.goto(x, y)
    t.pendown()


def randomheading():
    heading = randint(0, 360)
    t.setheading(heading)


def drawrectangle():
    randomcolour()
    randomplace()
    t.hideturtle()
    length = randint(10, 150)
    height = randint(10, 150)
    t.begin_fill()
    t.forward(length)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.end_fill()


t.shape("turtle")
t.speed(0)

randomcolour()
randomplace()
randomheading()
drawrectangle()
"""
for _ in range(1, 30):
  randomcolour()
  randomplace()
  randomheading()
  drawrectangle()
  #t.stamp()

"""

screen.mainloop()
