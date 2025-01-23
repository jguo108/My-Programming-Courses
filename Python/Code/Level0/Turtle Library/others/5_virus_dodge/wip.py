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


def setup_window():
    window.title("Virus Dodge")
    window.setup(window_width, window_height)
    window.bgpic("5_virus_dodge/Resources/Background/background.gif")
    window.tracer(0)


def setup_player():
    path = "5_virus_dodge/Resources/Player/spaceship.gif"
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
        path = f'5_virus_dodge/Resources/Enemy/Virus3/{i+1}.gif'
        window.addshape(path)
        enemy_costumes.append(path)

    '''
    enemy.shape(enemy_costumes[0])
    enemy.penup()
    enemy.speed(0)

    enemy.goto(
        random.randint(-window_width/2, window_width/2),
        random.randint(-window_height/2, window_height/2))
    enemy.setheading(random.randint(0, 360))
    '''
    # for _ in range(10):
    for _ in range(3):
        '''
        enemy = turtle.Turtle()
        enemy.shape(enemy_costumes[0])
        enemy.penup()
        enemy.speed(0)

        enemy.goto(
            random.randint(-window_width/2, window_width/2),
            random.randint(-window_height/2, window_height/2))
        enemy.setheading(random.randint(0, 360))
        '''
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
    # enemy.shape(enemy_costumes[i])
    for enemy in enemies:
        enemy.shape(enemy_costumes[i])
    i += 1

    # window.ontimer(switch_jellyfish_costume, 500)
    window.ontimer(switch_enemy_costume, 100)


def left():
    # player.setheading(180)
    player.left(5)
    player.settiltangle(player.heading())


def right():
    # player.setheading(0)
    player.right(5)
    player.settiltangle(player.heading())


def up():
    # player.setheading(90)
    # player.settiltangle(player.heading())
    pass


def down():
    # player.setheading(270)
    # player.settiltangle(player.heading())
    pass


def bind_keys():
    window.onkey(left, "Left")
    window.onkey(right, "Right")
    window.onkey(up, "Up")
    window.onkey(down, "Down")
    window.listen()


def move_player():
    player.forward(player_speed)
    if player.xcor() >= window_width/2 or \
            player.xcor() <= -window_width/2 or \
            player.ycor() >= window_height/2 or \
            player.ycor() <= -window_height/2:
        player.left(180+random.randint(-45, 45))


# def move_enemy():
def move_enemies():
    '''
    enemy.forward(enemy_speed)
    if enemy.xcor() >= window_width/2 or \
            enemy.xcor() <= -window_width/2 or \
            enemy.ycor() >= window_height/2 or \
            enemy.ycor() <= -window_height/2:
        enemy.left(180+random.randint(-45, 45))
    '''
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
            break


def update_score():
    global points
    points += 1

    score.clear()
    score.write(f"Score: {points}", font=("Courier", 14, "normal"))

    # print(f"Current point: {points}")

    window.ontimer(update_score, 1000)


def increase_enemy():
    enemy = create_enemy()
    enemies.append(enemy)
    window.ontimer(increase_enemy, 3000)


def game_loop():
    # global stopped
    while True:
        if stopped:
            break

        move_player()
        # move_enemy()
        move_enemies()

        '''
        for enemy in enemies:
            if player.distance(enemy) < 20:
                stopped = True
                break
        '''
        check_collision()

        window.update()
        # time.sleep(1)
        # time.sleep(0.1)
        time.sleep(0.01)


window = turtle.Screen()
player = turtle.Turtle()
# enemy = turtle.Turtle()
enemies = []
score = turtle.Turtle()

setup_window()
setup_player()
# setup_enemy()
setup_enemies()
setup_score()

bind_keys()

switch_enemy_costume()

# update_score()
window.ontimer(update_score, 1000)
window.ontimer(increase_enemy, 3000)

game_loop()

window.mainloop()
