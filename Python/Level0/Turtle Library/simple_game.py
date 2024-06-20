# https://www.youtube.com/watch?v=PTgyzZGknvg&list=PLlEgNdBJEO-n8FdWb-7f_C4dFC07IY9tb&index=1

import turtle
import random
import math

speed = 1


def turn_left():
    global player
    player.left(30)


def turn_right():
    global player
    player.right(30)


def increase_speed():
    global speed
    speed += 1


# Fullscreen the canvas
window = turtle.Screen()  # TODO: how do we know how large is the screen
window.bgcolor('lightgreen')

# Draw border
my_pen = turtle.Turtle()
my_pen.penup()
my_pen.setposition(-300, -300)
my_pen.pendown()
my_pen.pensize(3)
for side in range(4):
    my_pen.forward(600)
    my_pen.left(90)
my_pen.hideturtle()

# Create goal
goal = turtle.Turtle()
goal.color('red')
goal.shape('circle')
goal.penup()
goal.speed(0)
goal.setposition(-100, -100)

# Player
player = turtle.Turtle()
player.color('blue')
player.shape('triangle')
player.penup()
player.speed(0)  # TODO: what does this do?

turtle.listen()  # TODO: what does this do?
turtle.onkey(turn_left, 'Left')
turtle.onkey(turn_right, 'Right')
turtle.onkey(increase_speed, 'Up')

while True:
    player.forward(speed)

    # border check
    if player.xcor() > 300 or player.xcor() < -300 or player.ycor() > 300 or player.ycor() < -300:
        player.right(180)

    # collision checking
    distance = math.sqrt(
        math.pow(player.xcor()-goal.xcor(), 2) +
        math.pow(player.ycor()-goal.ycor(), 2))
    if distance < 20:
        goal.hideturtle()

window.mainloop()
