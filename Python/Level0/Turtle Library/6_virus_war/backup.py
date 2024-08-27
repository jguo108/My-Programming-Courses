# https: // www.tcl.tk/man/tcl8.4/TkCmd/keysyms.htm

import turtle
import random
import time

window_width = 600
window_height = 600

player_speed = 2

num_of_enemy_costumes = 19
enemy_costumes = []
enemy_speed = 1

i = 0

stopped = False
points = 0

bullets = []
bullet_speed = 5


def setup_window():
    window.title("Virus War")
    window.setup(window_width, window_height)
    window.bgpic("6_virus_war/Resources/Background/background.gif")
    window.tracer(0)


def setup_player():
    path = "6_virus_war/Resources/Player/player.gif"
    window.addshape(path)
    player.shape(path)
    player.penup()


def create_enemy():
    enemy = turtle.Turtle()
    enemy.shape(enemy_costumes[0])
    enemy.penup()
    enemy.speed(0)

    enemy.goto(
        random.randint(-window_width/2, window_width/2),
        random.randint(-window_height/2, window_height/2))
    enemy.setheading(random.randint(0, 360))

    return enemy


def setup_enemies():
    for i in range(num_of_enemy_costumes):
        path = f'6_virus_war/Resources/Enemy/Virus3/{i+1}.gif'
        window.addshape(path)
        enemy_costumes.append(path)

    for _ in range(3):
        enemy = create_enemy()
        enemies.append(enemy)


def setup_score():
    score.hideturtle()
    score.color("gray80")
    score.penup()
    score.goto(-window_width/2 + 10, window_height/2 - 30)
    score.write(f"Score: {points}", font=("Courier", 14, "normal"))


def switch_enemy_costume():
    global i
    if i == num_of_enemy_costumes:
        i = 0
    for enemy in enemies:
        enemy.shape(enemy_costumes[i])
    i += 1

    window.ontimer(switch_enemy_costume, 100)


def update_score():
    global points
    points += 10

    score.clear()
    score.write(f"Score: {points}", font=("Courier", 14, "normal"))


def left():
    player.left(30)


def right():
    player.right(30)


def up():
    global player_speed
    player_speed += 1


def down():
    global player_speed
    player_speed -= 1


def fire():
    bullet = turtle.Turtle()

    bullet.color('DarkOliveGreen2')
    bullet.shape('circle')
    bullet.penup()
    bullet.shapesize(0.3, 0.3)
    bullet.speed(0)

    bullet.goto(player.xcor(), player.ycor())
    bullet.setheading(player.heading())
    bullets.append(bullet)


def bind_keys():
    window.onkey(left, "Left")
    window.onkey(right, "Right")
    window.onkey(up, "Up")
    window.onkey(down, "Down")
    window.onkey(fire, 'space')
    window.listen()


def move_player():
    player.forward(player_speed)
    if player.xcor() >= window_width/2 or \
            player.xcor() <= -window_width/2 or \
            player.ycor() >= window_height/2 or \
            player.ycor() <= -window_height/2:
        player.left(180+random.randint(-45, 45))


def move_bullets():
    for bullet in bullets:
        bullet.forward(bullet_speed)
        if bullet.xcor() < -window_width/2 or \
                bullet.xcor() > window_width/2 or \
                bullet.ycor() < -window_height/2 or \
                bullet.ycor() > window_height/2:
            bullet.hideturtle()


def move_enemies():
    for enemy in enemies:
        enemy.forward(enemy_speed)
        if enemy.xcor() >= window_width/2 or \
                enemy.xcor() <= -window_width/2 or \
                enemy.ycor() >= window_height/2 or \
                enemy.ycor() <= -window_height/2:
            enemy.left(180+random.randint(-45, 45))


def check_collision():
    global stopped
    for enemy in enemies:
        if player.distance(enemy) < 20:
            stopped = True
            return

    enemies_to_removed = []
    bullets_to_removed = []
    for bullet in bullets:
        for enemy in enemies:
            if bullet.distance(enemy) < 20:
                enemies_to_removed.append(enemy)
                bullets_to_removed.append(bullet)
                update_score()

    for enemy in enemies_to_removed:
        enemy.hideturtle()
        enemies.remove(enemy)

    for bullet in bullets_to_removed:
        bullet.hideturtle()
        bullets.remove(bullet)


def increase_enemy():
    enemy = create_enemy()
    enemies.append(enemy)
    window.ontimer(increase_enemy, 5000)


def game_loop():
    while True:
        if stopped:
            break

        move_player()
        move_enemies()
        move_bullets()
        check_collision()

        window.update()
        time.sleep(0.01)


window = turtle.Screen() 
player = turtle.Turtle()
enemies = []
score = turtle.Turtle()

setup_window()
setup_player()
setup_enemies()
setup_score()

bind_keys()

switch_enemy_costume()

window.ontimer(increase_enemy, 5000)

game_loop()

window.mainloop()
