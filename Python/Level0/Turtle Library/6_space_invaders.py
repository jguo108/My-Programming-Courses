# https://www.youtube.com/watch?v=QvtlEj_T55o&list=PLlEgNdBJEO-lqvqL5nNNZC6KoRdSrhQwK

import turtle
import math
import random


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
INITIAL_INVADERS = 1
NUM_OF_INVADER_COSTUMES = 31

PLAYER_SPEED = 10
INVADER_SPEED = 1
BULLET_SPEED = 1

window = None

player = None

invaders = []
invader_costumes = []
invader_costume_index = 0
invader_speed = 1

bullet = None

score_pen = None
score = 0

tick_num = 1
game_ended = False


def setup_window():
    global window
    window = turtle.Screen()
    window.title('Space Invaders')
    window.bgpic('Resources\\space_invaders\\bg.gif')
    # window.bgcolor('gray10')
    window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

    # Disable screen update. We will update it manually using the 'update' method
    window.tracer(0)


def create_player():
    global player

    register_player_costume()

    player = turtle.Turtle()
    player.color('green')
    player.shape('square')
    # player.shape('Resources/dodge_it/player.gif')
    player.penup()
    player.setheading(90)
    player.goto(0, -(SCREEN_HEIGHT/2-100))
    player.speed(0)


def create_bullet():
    global bullet

    bullet = turtle.Turtle()
    bullet.color('yellow')
    bullet.shape('triangle')
    # bullet.shape('Resources/dodge_it/player.gif')
    bullet.penup()
    bullet.setheading(90)
    bullet.shapesize(0.5, 0.5)
    bullet.speed(0)


def create_score():
    global score_pen
    score_pen = turtle.Turtle()
    score_pen.penup()
    score_pen.hideturtle()
    score_pen.color('gray80')
    score_pen.goto(-SCREEN_WIDTH/2 + 10, SCREEN_HEIGHT/2 - 30)
    score_pen.write(f'Score: {score}', False, align='left',
                    font=('Courier', 14, 'normal'))


def create_invader():
    invader = turtle.Turtle()
    invader.color('red')
    invader.shape('circle')
    # invader.shape(
    #    invader_costumes[invader_costume_index % len(invader_costumes)])
    invader.penup()
    invader.speed(0)
    invader.goto(
        random.randint(-SCREEN_WIDTH/2+50, SCREEN_WIDTH/2-50),
        SCREEN_WIDTH/2-50)
    invader.setheading(random.randint(0, 360))
    return invader


def create_invaders():
    global invaders

    # register_invader_costumes()
    for _ in range(INITIAL_INVADERS):
        invaders.append(create_invader())


def register_player_costume():
    gif = f'Resources/dodge_it/player.gif'
    turtle.register_shape('Resources/dodge_it/player.gif')


def register_invader_costumes():
    for i in range(NUM_OF_INVADER_COSTUMES):
        gif = f'Resources/dodge_it/invader/{i+1}.gif'
        turtle.register_shape(gif)
        invader_costumes.append(gif)


def left():
    global player
    if player.xcor() > -SCREEN_WIDTH/2+20:
        player.setx(player.xcor() - PLAYER_SPEED)


def right():
    global player
    if player.xcor() < SCREEN_WIDTH/2-20:
        player.setx(player.xcor() + PLAYER_SPEED)


def up():
    global player
    player.setheading(90)


def down():
    global player
    player.setheading(270)


def collide(t1, t2):
    distance = math.sqrt(
        math.pow(t1.xcor()-t2.xcor(), 2) +
        math.pow(t1.ycor()-t2.ycor(), 2))
    return distance < 20


def bounce(t):
    if t.xcor() > SCREEN_WIDTH/2-10 or \
            t.xcor() < -SCREEN_WIDTH/2+10 or \
            t.ycor() > SCREEN_HEIGHT/2-10 or \
            t.ycor() < -SCREEN_HEIGHT/2+10:
        t.right(180 + random.randint(-90, 90))


def update_score():
    global score, tick_num
    # increase score every 100 ticks
    if tick_num % 100 == 0:
        score += 1
        score_pen.clear()
        score_pen.write(f'Score: {score}', False, align='left',
                        font=('Courier', 14, 'normal'))


def animate_invaders():
    global invaders, invader_costume_index

    if game_ended:
        return

    invader_costume_index += 1
    for invader in invaders:
        invader.shape(
            invader_costumes[invader_costume_index % len(invader_costumes)])
    window.ontimer(animate_invaders, 100)


def move_invaders():
    global invaders
    for invader in invaders:
        invader.sety(invader.ycor()-INVADER_SPEED)


def check_for_collision():
    global player, invaders, game_ended
    for invader in invaders:
        if collide(player, invader):
            game_ended = True
            break


def add_invader():
    global invaders, score
    if tick_num % 500 == 0:
        invaders.append(create_invader())


def tick():
    global score, tick_num, game_ended

    if game_ended:
        return

    move_invaders()
    # check_for_collision()
    # update_score()
    # add_invader()
    tick_num += 1

    window.update()  # maunall update the screen
    window.ontimer(tick, 10)  # update the screen every 10 milliseconds


def bind_keys():
    global window

    window.listen()  # make the window listen for key presses
    window.onkeypress(left, 'Left')
    window.onkeypress(right, 'Right')


# 1. Set up game window
setup_window()

# 2. Create game objects
create_player()
create_invaders()
create_bullet()
# create_score()

# 3. Bind control keys
bind_keys()

# 4. Animate game objects
# animate_invaders()

# 5. Start game loop
window.ontimer(tick, 0)

window.mainloop()
