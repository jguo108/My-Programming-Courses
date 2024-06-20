# https://www.youtube.com/watch?v=PTgyzZGknvg&list=PLlEgNdBJEO-n8FdWb-7f_C4dFC07IY9tb&index=1

# TODO
# - add a background image
# - add sound when collide and bounce
# - change window background color

import turtle
import random
import math

speed = 1
score = 0


def turn_left():
    global player
    player.left(30)


def turn_right():
    global player
    player.right(30)


def increase_speed():
    global speed
    speed += 1


def collide(t1, t2):
    distance = math.sqrt(
        math.pow(t1.xcor()-t2.xcor(), 2) +
        math.pow(t1.ycor()-t2.ycor(), 2))
    return distance < 20


def hit_border_and_bounce(t):
    if t.xcor() > 290 or t.xcor() < -290 or t.ycor() > 290 or t.ycor() < -290:
        t.right(180)


def update_score(score):
    my_pen.undo()
    my_pen.penup()
    my_pen.hideturtle()
    my_pen.setposition(-290, 310)
    score_str = f'Score: {score}'
    my_pen.write(score_str, False, align='left',
                 font=('Arial', 14, 'normal'))


# Fullscreen the canvas
window = turtle.Screen()  # TODO: how do we know how large is the screen
window.bgcolor('lightgreen')
# Disable screen update. We will update it manually using the 'update' method
window.tracer(0)

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


# Create more food
max_food = 5
all_food = []

for i in range(max_food):
    food = turtle.Turtle()
    food.color('red')
    food.shape('circle')
    food.penup()
    food.speed(0)
    food.setposition(random.randint(-300, 300), random.randint(-300, 300))
    food.setheading(random.randint(0, 360))
    all_food.append(food)

'''
# Create food
food = turtle.Turtle()
food.color('red')
food.shape('circle')
food.penup()
food.speed(0)
food.setposition(-100, -100)
'''
# Player
player = turtle.Turtle()
player.color('blue')
player.shape('turtle')
player.penup()
player.speed(0)  # TODO: what does this do?

turtle.listen()  # TODO: what does this do?
# 'onkeypress' will keep runnig the function as long as the key is
# being pressed down, whereas 'onkey' will only run the functino once
# when it is pressed but not when it is being pressed down
turtle.onkeypress(turn_left, 'Left')
turtle.onkeypress(turn_right, 'Right')
turtle.onkey(increase_speed, 'Up')

update_score(0)


def run():
    global score
    player.forward(speed)

    # border check
    hit_border_and_bounce(player)

    # collision checking
    for food in all_food:
        if collide(player, food):
            food.setposition(random.randint(-300, 300),
                             random.randint(-300, 300))
            food.setheading(random.randint(0, 360))
            score += 1
            update_score(score)
        food.forward(2)
        hit_border_and_bounce(food)

    window.update()  # maunall update the screen
    window.ontimer(run, 10)  # update the screen every 10 milliseconds


# start the program
run()

window.mainloop()
