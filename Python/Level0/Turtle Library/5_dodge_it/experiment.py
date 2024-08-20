# Note:
# https://www.notion.so/5-Dodge-It-93e5fc0c71514f8eaea8e791af06c705

# https://www.youtube.com/watch?v=PTgyzZGknvg&list=PLlEgNdBJEO-n8FdWb-7f_C4dFC07IY9tb&index=1

# Assets:
# https://scratch.mit.edu/projects/502019480/editor/
# https://www.freepik.com/free-vector/set-pixel-game-spaceships-isolated_25679780.htm#fromView=search&page=1&position=45&uuid=02df045a-cc4f-46b8-aec6-35389c5be96b
# https://www.freepik.com/free-ai-image/8-bits-astronaut-characters-gaming-assets_133331454.htm#fromView=search&page=3&position=24&uuid=9271e10b-41b7-483e-bf87-0f3a05c2ab52
# https://www.freepik.com/free-vector/retro-8-bit-pixel-arcade-computer-game-set-isolated-icons-with-characters-monsters-spacecrafts-vector-illustration_26762888.htm#fromView=search&page=2&position=2&uuid=cdb02372-e6d7-4557-a8a1-a9af8245e5c2
# https://www.freepik.com/free-photo/panoramic-view-sunset-night_13637281.htm#fromView=search&page=1&position=3&uuid=2857a55d-9599-42c8-8518-cb3d867639c6

import turtle
import math
import random
import time


# TODO
# - add sound when collide and bounce
# - add game over screen
# - add replay button

screen_width = 600
screen_height = 600
initial_enemies = 3
num_of_enemy_costumes = 31

player_speed = 10

enemies = []
enemy_costumes = []
enemy_costume_index = 0
enemy_speed = 1

score = None
points = 0

stopped = False


def setup_window():
    window.title('Dodge It!')
    window.setup(screen_width, screen_height)
    window.bgpic('5_dodge_it/Resources/Background/background.gif')

    # Disable screen update. We will update it manually using the 'update' method
    window.tracer(0)


def create_player():
    window.addshape('5_dodge_it/Resources/Player/player.gif')
    player.shape('5_dodge_it/Resources/Player/player.gif')
    player.penup()


def create_score():
    score.penup()
    score.hideturtle()
    score.color('gray80')
    score.goto(-screen_width/2 + 10, screen_height/2 - 30)
    score.write(f'Score: {points}', False, align='left',
                font=('Courier', 14, 'normal'))


def create_enemy():
    enemy = turtle.Turtle()
    enemy.shape(enemy_costumes[enemy_costume_index % len(enemy_costumes)])
    enemy.penup()
    enemy.speed(0)
    enemy.goto(
        random.randint(-screen_width/2, screen_width/2),
        random.randint(-screen_height/2, screen_height/2))
    enemy.setheading(random.randint(0, 360))
    return enemy


def create_enemies():
    for i in range(num_of_enemy_costumes):
        gif = f'5_dodge_it/Resources/Enemy/{i+1}.gif'
        window.addshape(gif)
        enemy_costumes.append(gif)

    for _ in range(initial_enemies):
        enemies.append(create_enemy())


def left():
    x = player.xcor()
    player.setx(x - player_speed)


def right():
    x = player.xcor()
    player.setx(x + player_speed)


def up():
    y = player.ycor()
    player.sety(y + player_speed)


def down():
    y = player.ycor()
    player.sety(y - player_speed)


def bounce(t):
    if t.xcor() > screen_width/2 or \
        t.xcor() < -screen_width/2 or \
            t.ycor() > screen_height/2 or\
            t.ycor() < -screen_height/2:
        t.right(180 + random.randint(-45, 45))


def update_score():
    global points

    if stopped:
        return
    points += 1
    score.clear()
    score.write(f'Score: {points}', False, align='left',
                font=('Courier', 14, 'normal'))
    window.ontimer(update_score, 1000)


def animate_enemies():
    global enemy_costume_index

    if stopped:
        return

    enemy_costume_index += 1
    for enemy in enemies:
        enemy.shape(enemy_costumes[enemy_costume_index % len(enemy_costumes)])
    window.ontimer(animate_enemies, 100)


def move_enemies():
    for enemy in enemies:
        player_x = player.xcor()
        player_y = player.ycor()
        enemy.setheading(enemy.towards(player_x, player_y))
        enemy.forward(enemy_speed)
        bounce(enemy)


def check_collision():
    global stopped
    for enemy in enemies:
        if player.distance(enemy) < 20:
            stopped = True
            break


def add_enemy():
    if stopped:
        return
    new_enemy = create_enemy()
    enemies.append(new_enemy)
    window.ontimer(add_enemy, 5000)


def bind_keys():
    window.onkeypress(left, 'Left')
    window.onkeypress(right, 'Right')
    window.onkeypress(up, 'Up')
    window.onkeypress(down, 'Down')
    window.listen()  # make the window listen for key presses


def game_loop():
    while True:
        if stopped:
            break

        move_enemies()
        check_collision()
        window.update()
        time.sleep(0.001)


window = turtle.Screen()
player = turtle.Turtle()
score = turtle.Turtle()

# 1. Set up game window
setup_window()

# 2. Create game objects
create_player()
create_enemies()
create_score()

# 3. Bind control keys
bind_keys()

# 4. Animate game objects
animate_enemies()

window.ontimer(update_score, 1000)
window.ontimer(add_enemy, 5000)

# 5. Start game loop
game_loop()

window.mainloop()
