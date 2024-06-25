# https://www.youtube.com/watch?v=PTgyzZGknvg&list=PLlEgNdBJEO-n8FdWb-7f_C4dFC07IY9tb&index=1

# Assets:
# https://scratch.mit.edu/projects/502019480/editor/
# https://www.freepik.com/free-vector/set-pixel-game-spaceships-isolated_25679780.htm#fromView=search&page=1&position=45&uuid=02df045a-cc4f-46b8-aec6-35389c5be96b
# https://www.freepik.com/free-ai-image/8-bits-astronaut-characters-gaming-assets_133331454.htm#fromView=search&page=3&position=24&uuid=9271e10b-41b7-483e-bf87-0f3a05c2ab52
# https://www.freepik.com/free-vector/retro-8-bit-pixel-arcade-computer-game-set-isolated-icons-with-characters-monsters-spacecrafts-vector-illustration_26762888.htm#fromView=search&page=2&position=2&uuid=cdb02372-e6d7-4557-a8a1-a9af8245e5c2
# https://www.freepik.com/free-photo/panoramic-view-sunset-night_13637281.htm#fromView=search&page=1&position=3&uuid=2857a55d-9599-42c8-8518-cb3d867639c6

import math
import random
import turtle


# TODO
# - add a background image
# - add sound when collide and bounce
# - change window background color


speed = 1
score = 0


def turn_left():
    global player
    player.left(30)


def turn_right():
    global player
    player.right(30)


def speedup():
    global speed
    speed += 1


def slowdown():
    global speed
    if speed > 1:
        speed -= 1


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
window.listen()  # make the window listen for key presses

# 'onkeypress' will keep runnig the function as long as the key is
# being pressed down, whereas 'onkey' will only run the functino once
# when it is pressed but not when it is being pressed down
window.onkeypress(turn_left, 'Left')
window.onkeypress(turn_right, 'Right')
window.onkey(speedup, 'Up')
window.onkey(slowdown, 'Down')


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
