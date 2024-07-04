# https://www.youtube.com/watch?v=QvtlEj_T55o&list=PLlEgNdBJEO-lqvqL5nNNZC6KoRdSrhQwK

# TODO:
# - add sound effects

import turtle
import math
import random


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
INITIAL_INVADERS = 5
NUM_OF_INVADER_COSTUMES = 2

PLAYER_SPEED = 10
INVADER_Y_SPEED = 5
BULLET_SPEED = 10

window = None

player = None

invaders = []
invader_costumes = []
invader_costume_index = 0
invader_x_speed = 1


bullet = None
bullet_fired = False

score_pen = None
score = 0

tick_num = 1
game_ended = False


def setup_window():
    global window
    window = turtle.Screen()
    window.title('Space Invaders')
    window.bgpic('6_space_invaders/Resources/bg.gif')
    # window.bgcolor('gray10')
    window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

    # Disable screen update. We will update it manually using the 'update' method
    window.tracer(0)


def create_player():
    global player

    register_player_costume()

    player = turtle.Turtle()
    # player.color('green')
    # player.shape('square')
    player.shape('6_space_invaders/Resources/spaceship.gif')
    player.penup()
    player.setheading(90)
    player.goto(0, -(SCREEN_HEIGHT/2-100))
    player.speed(0)


def create_bullet():
    global bullet

    register_bullet_costume()

    bullet = turtle.Turtle()
    bullet.color('yellow')
    # bullet.shape('triangle')
    bullet.shape('6_space_invaders/Resources/bullet.gif')
    bullet.penup()
    bullet.setheading(90)
    bullet.shapesize(0.5, 0.5)
    bullet.speed(0)
    bullet.hideturtle()


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
        SCREEN_WIDTH/2 + random.randint(-100, 0))
    invader.setheading(random.randint(0, 360))
    return invader


def create_invaders():
    register_invader_costumes()
    for _ in range(INITIAL_INVADERS):
        invaders.append(create_invader())


def register_player_costume():
    turtle.register_shape('6_space_invaders/Resources/spaceship.gif')


def register_bullet_costume():
    turtle.register_shape('6_space_invaders/Resources/bullet.gif')


def register_invader_costumes():
    for i in range(NUM_OF_INVADER_COSTUMES):
        gif = f'6_space_invaders/Resources/invader/{i+1}.gif'
        turtle.register_shape(gif)
        invader_costumes.append(gif)


def left():
    if player.xcor() > -SCREEN_WIDTH/2+20:
        player.setx(player.xcor() - PLAYER_SPEED)


def right():
    if player.xcor() < SCREEN_WIDTH/2-20:
        player.setx(player.xcor() + PLAYER_SPEED)


def fire():
    global bullet_fired
    if not bullet_fired:
        bullet_fired = True
        bullet.goto(player.xcor(), player.ycor()+15)
        bullet.showturtle()


def collide(t1, t2):
    return t1.distance(t2) < 20


def increase_score():
    global score
    score += 1
    score_pen.clear()
    score_pen.write(f'Score: {score}', False, align='left',
                    font=('Courier', 14, 'normal'))


def animate_invaders():
    global invader_costume_index

    if game_ended:
        return

    invader_costume_index += 1
    for invader in invaders:
        invader.shape(
            invader_costumes[invader_costume_index % len(invader_costumes)])
    window.ontimer(animate_invaders, 100)


def move_invaders():
    global invader_x_speed
    move_down = False
    for invader in invaders:
        invader.setx(invader.xcor() + invader_x_speed)
        if invader.xcor() > SCREEN_WIDTH/2 or invader.xcor() < -SCREEN_WIDTH/2:
            invader_x_speed *= -1
            move_down = True

    if move_down:
        for invader in invaders:
            invader.sety(invader.ycor()-INVADER_Y_SPEED)
            if invader.ycor() < -SCREEN_HEIGHT/2:
                invader.goto(
                    random.randint(-SCREEN_WIDTH/2+50, SCREEN_WIDTH/2-50),
                    SCREEN_WIDTH/2)


def move_bullet():
    global bullet_fired
    if bullet_fired:
        bullet.sety(bullet.ycor() + BULLET_SPEED)
        if bullet.ycor() > SCREEN_HEIGHT/2:
            bullet.hideturtle()
            bullet_fired = False


def check_for_collision():
    global game_ended, bullet_fired
    for invader in invaders:
        if collide(bullet, invader):
            bullet.hideturtle()
            bullet_fired = False
            bullet.goto(0, -SCREEN_HEIGHT/2)
            invader.goto(
                random.randint(-SCREEN_WIDTH/2+50, SCREEN_WIDTH/2-50),
                SCREEN_WIDTH/2)
            increase_score()
        if collide(player, invader):
            game_ended = True
            break


def add_invader():
    if tick_num % 500 == 0:
        invaders.append(create_invader())


def tick():
    global tick_num

    if game_ended:
        return

    move_invaders()
    move_bullet()
    check_for_collision()
    # add_invader()
    tick_num += 1

    window.update()  # maunall update the screen
    window.ontimer(tick, 20)  # update the screen every 10 milliseconds


def bind_keys():
    global window

    window.listen()  # make the window listen for key presses
    window.onkeypress(left, 'Left')
    window.onkeypress(right, 'Right')
    window.onkeypress(fire, 'space')


# 1. Set up game window
setup_window()

# 2. Create game objects
create_player()
create_invaders()
create_bullet()
create_score()

# 3. Bind control keys
bind_keys()

# 4. Animate game objects
animate_invaders()

# 5. Start game loop
window.ontimer(tick, 0)

window.mainloop()
