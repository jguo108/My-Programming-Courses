# https://www.youtube.com/watch?v=QvtlEj_T55o&list=PLlEgNdBJEO-lqvqL5nNNZC6KoRdSrhQwK

# TODO:
# - add sound effects

import turtle
import random
import time


screen_width = 600
screen_height = 600
num_of_invader_costumes = 2

player_speed = 10
bullet_speed = 10


invaders = []
invader_costumes = []
i = 0
invader_x_speed = 1
invader_y_speed = 5

bullet_fired = False
points = 0

stopped = False


def setup_window():
    window.title('Space Invaders')
    window.setup(screen_width, screen_height)
    window.bgpic('6_space_invaders/Resources/Background/background.gif')

    # Disable screen update. We will update it manually using the 'update' method
    window.tracer(0)


def setup_player():
    window.addshape('6_space_invaders/Resources/Spaceship/spaceship.gif')

    player.shape('6_space_invaders/Resources/Spaceship/spaceship.gif')
    player.penup()
    player.setheading(90)
    player.goto(0, -(screen_height/2-100))
    player.speed(0)


def setup_bullet():
    window.addshape('6_space_invaders/Resources/Spaceship/bullet.gif')

    bullet.shape('6_space_invaders/Resources/Spaceship/bullet.gif')
    bullet.penup()
    bullet.setheading(90)
    bullet.shapesize(0.5, 0.5)
    bullet.speed(0)
    bullet.hideturtle()


def setup_score():
    global score
    score.penup()
    score.hideturtle()
    score.color('gray80')
    score.goto(-screen_width/2 + 10, screen_height/2 - 30)
    score.write(f'Score: {points}', False, align='left',
                font=('Courier', 14, 'normal'))


def create_invader():
    invader = turtle.Turtle()
    invader.color('red')
    invader.shape('circle')
    invader.penup()
    invader.speed(0)
    invader.goto(
        random.randint(-screen_width/2+50, screen_width/2-50),
        screen_width/2 + random.randint(-100, 0))
    invader.setheading(random.randint(0, 360))
    return invader


def setup_invaders():
    for i in range(num_of_invader_costumes):
        gif = f'6_space_invaders/Resources/Invader/{i+1}.gif'
        turtle.register_shape(gif)
        invader_costumes.append(gif)

    for _ in range(5):
        invaders.append(create_invader())


def left():
    if player.xcor() > -screen_width/2+20:
        player.setx(player.xcor() - player_speed)


def right():
    if player.xcor() < screen_width/2-20:
        player.setx(player.xcor() + player_speed)


def fire():
    global bullet_fired
    if not bullet_fired:
        bullet_fired = True
        bullet.goto(player.xcor(), player.ycor()+15)
        bullet.showturtle()


def collide(t1, t2):
    return t1.distance(t2) < 20


def update_score():
    global points
    points += 1
    score.clear()
    score.write(f'Score: {points}', False, align='left',
                font=('Courier', 14, 'normal'))


def switch_invader_costume():
    global i
    if i == num_of_invader_costumes:
        i = 0

    for invader in invaders:
        invader.shape(invader_costumes[i])
    i += 1
    window.ontimer(switch_invader_costume, 100)


def move_invaders():
    global invader_x_speed
    move_down = False
    for invader in invaders:
        invader.setx(invader.xcor() + invader_x_speed)
        if invader.xcor() > screen_width/2 or invader.xcor() < -screen_width/2:
            invader_x_speed *= -1
            move_down = True

    if move_down:
        for invader in invaders:
            invader.sety(invader.ycor()-invader_y_speed)
            if invader.ycor() < -screen_height/2:
                invader.goto(
                    random.randint(-screen_width/2+50, screen_width/2-50),
                    screen_width/2)


def move_bullet():
    global bullet_fired
    if bullet_fired:
        bullet.sety(bullet.ycor() + bullet_speed)
        if bullet.ycor() > screen_height/2:
            bullet.hideturtle()
            bullet_fired = False


def check_for_collision():
    global stopped, bullet_fired
    for invader in invaders:
        if collide(bullet, invader):
            bullet.hideturtle()
            bullet_fired = False
            bullet.goto(0, -screen_height/2)
            invader.goto(
                random.randint(-screen_width/2+50, screen_width/2-50),
                screen_width/2)
            update_score()
        if collide(player, invader):
            stopped = True
            break


def bind_keys():
    window.listen()  # make the window listen for key presses
    window.onkeypress(left, 'Left')
    window.onkeypress(right, 'Right')
    window.onkeypress(fire, 'space')


def speedup_invaders():
    global invader_y_speed
    invader_y_speed += 1
    window.ontimer(speedup_invaders, 3000)


def game_loop():
    while True:
        if stopped:
            break

        move_invaders()
        move_bullet()
        check_for_collision()

        window.update()  # maunall update the screen
        time.sleep(0.02)


window = turtle.Screen()
player = turtle.Turtle()
bullet = turtle.Turtle()
score = turtle.Turtle()

setup_window()

setup_player()
setup_invaders()
setup_bullet()
setup_score()

bind_keys()

switch_invader_costume()

window.ontimer(speedup_invaders, 3000)

game_loop()


window.mainloop()
