import pygame
import time
import random
import turtle

window_width = 600
window_height = 600

player_speed = 1

num_of_enemy_costumes = 19
num_of_enemy_kinds = 7
enemy_costumes = {}
enemy_speed = 1

i = 0

stopped = False
points = 0

fired = False
bullet_speed = 5

particle_speed = 5


def setup_window():
    window.title("Virus War")
    window.setup(window_width, window_height)
    window.bgpic("6_virus_war/Resources/Background/background.gif")
    window.tracer(0)


def setup_sound():
    pygame.mixer.init()
    sounds['fire'] = pygame.mixer.Sound(
        '6_virus_war/Resources/Sounds/fire.mp3')
    sounds['killed'] = pygame.mixer.Sound(
        '6_virus_war/Resources/Sounds/killed.mp3')
    sounds['gameover'] = pygame.mixer.Sound(
        '6_virus_war/Resources/Sounds/gameover.mp3')


def setup_player():
    path = "6_virus_war/Resources/Player/player.gif"
    window.addshape(path)
    player.shape(path)
    player.penup()


def create_enemy():
    enemy = turtle.Turtle()
    kind = random.randint(1, num_of_enemy_kinds)
    enemies[enemy] = kind
    enemy.shape(enemy_costumes[kind][0])

    enemy.penup()
    enemy.speed(0)

    enemy.goto(
        random.randint(-window_width/2, window_width/2),
        random.randint(-window_height/2, window_height/2))
    enemy.setheading(random.randint(0, 360))


def setup_enemies():
    for i in range(num_of_enemy_kinds):
        costumes = []
        for j in range(num_of_enemy_costumes):
            path = f'6_virus_war/Resources/Enemy/Virus{i+1}/{j+1}.gif'
            window.addshape(path)
            costumes.append(path)
        enemy_costumes[i+1] = costumes

    for _ in range(3):
        create_enemy()


def setup_score():
    score.hideturtle()
    score.color("gray80")
    score.penup()
    score.goto(-window_width/2 + 10, window_height/2 - 30)
    score.write(f"Score: {points}", font=("Courier", 14, "normal"))


def setup_bullet():
    bullet.color('DarkOliveGreen2')
    bullet.shape('circle')
    bullet.penup()
    bullet.shapesize(0.3, 0.3)
    bullet.speed(0)
    bullet.hideturtle()


def setup_particles():
    for _ in range(20):
        particle = turtle.Turtle()
        particle.shape('circle')
        particle.color(random.choice(
            ['orange', 'red3', 'goldenrod', 'salmon2', 'orchid2']))
        particle.shapesize(0.1, 0.1)
        particle.penup()
        particle.hideturtle()
        particles.append(particle)


def switch_enemy_costume():
    global i
    if i == num_of_enemy_costumes:
        i = 0
    for enemy, kind in enemies.items():
        enemy.shape(enemy_costsumes[kind][i])
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
    global fired
    if not fired:
        sounds['fire'].play()

        bullet.goto(player.xcor(), player.ycor())
        bullet.setheading(player.heading())
        bullet.showturtle()
        fired = True


def bind_keys():
    window.onkey(left, 'Left')
    window.onkey(right, 'Right')
    window.onkey(up, 'Up')
    window.onkey(down, 'Down')
    window.onkey(fire, 'space')
    window.listen()


def move_player():
    player.forward(player_speed)
    if player.xcor() >= window_width/2 or \
            player.xcor() <= -window_width/2 or \
            player.ycor() >= window_height/2 or \
            player.ycor() <= -window_height/2:
        player.left(180+random.randint(-45, 45))


def move_bullet():
    global fired
    if fired:
        bullet.forward(bullet_speed)
        if bullet.xcor() < -window_width/2 or \
                bullet.xcor() > window_width/2 or \
                bullet.ycor() < -window_height/2 or \
                bullet.ycor() > window_height/2:
            bullet.hideturtle()
            fired = False
    else:
        bullet.goto(player.xcor(), player.ycor())


def move_particles():
    for particle in particles:
        particle.forward(particle_speed)


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
    enemy_killed = None
    for enemy in enemies:
        if player.distance(enemy) < 20:
            stopped = True
            return

        if bullet.distance(enemy) < 20:
            enemy_killed = enemy
            bullet.hideturtle()
            fired = False
            sounds['killed'].play()
            for particle in particles:
                particle.goto(enemy.xcor(), enemy.ycor())
                particle.setheading(random.randint(0, 360))
                particle.showturtle()
            break

    if enemy_killed is not None:
        enemy_killed.hideturtle()
        enemies.remove(enemy_killed)


def increase_enemy():
    create_enemy()
    window.ontimer(increase_enemy, 5000)


def game_loop():
    while True:
        if stopped:
            break

        move_player()
        move_enemies()
        move_bullet()
        check_collision()
        move_particles()

        window.update()
        time.sleep(0.01)

    sounds['gameover'].play()


window = turtle.Screen()
player = turtle.Turtle()
enemies = {}
score = turtle.Turtle()
sounds = {}
particles = []
bullet = turtle.Turtle()


setup_window()
setup_player()
setup_enemies()
setup_score()

setup_bullet()
setup_particles()
setup_sound()

bind_keys()

switch_enemy_costume()

window.ontimer(increase_enemy, 5000)

game_loop()

window.mainloop()
