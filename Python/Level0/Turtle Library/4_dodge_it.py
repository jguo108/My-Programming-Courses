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

# TODO
# - add a background image
# - add sound when collide and bounce
# - change window background color


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
INITIAL_ENEMIES = 5
NUM_OF_ENEMY_COSTUMES = 31

window = None

player = None
player_speed = 2

enemies = []
enemy_costumes = []
enemy_costume_index = 0
enemy_speed = 1

score_pen = None
score = 0

tick_num = 1
game_ended = False


def register_costumes():
    for i in range(NUM_OF_ENEMY_COSTUMES):
        gif = f'Resources/dodge_it/enemy/{i+1}.gif'
        turtle.register_shape(gif)
        enemy_costumes.append(gif)
    turtle.register_shape('Resources/dodge_it/player.gif')


def left():
    global player
    player.setheading(180)


def right():
    global player
    player.setheading(0)


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


def animate_enemies():
    global enemies, enemy_costume_index
    enemy_costume_index += 1
    for enemy in enemies:
        enemy.shape(enemy_costumes[enemy_costume_index % len(enemy_costumes)])
    window.ontimer(animate_enemies, 100)


def create_enemy():
    enemy = turtle.Turtle()
    enemy.color('red')
    enemy.shape(enemy_costumes[enemy_costume_index % len(enemy_costumes)])
    enemy.penup()
    enemy.speed(0)
    enemy.goto(
        random.randint(-SCREEN_WIDTH/2+100, SCREEN_WIDTH/2-100),
        random.randint(-SCREEN_HEIGHT/2+100, SCREEN_HEIGHT/2-100))
    enemy.setheading(random.randint(0, 360))
    return enemy


def create_enemies():
    global enemies
    for _ in range(INITIAL_ENEMIES):
        enemies.append(create_enemy())


def create_player():
    global player
    player = turtle.Turtle()
    player.color('green')
    # player.shape('square')
    player.shape('Resources/dodge_it/player.gif')
    player.penup()
    player.speed(0)  # TODO: what does this do?


def create_score():
    global score_pen
    score_pen = turtle.Turtle()
    score_pen.penup()
    score_pen.hideturtle()
    score_pen.color('gray80')
    score_pen.goto(-SCREEN_WIDTH/2 + 10, SCREEN_HEIGHT/2 - 30)
    score_pen.write(f'Score: {score}', False, align='left',
                    font=('Courier', 14, 'normal'))


def move_player():
    global player, player_speed
    player.forward(player_speed)
    # border check
    bounce(player)


def move_enemies():
    global enemies
    for enemy in enemies:
        enemy.forward(enemy_speed)
        bounce(enemy)


def check_for_collision():
    global player, enemies, game_ended
    for enemy in enemies:
        if collide(player, enemy):
            game_ended = True
            break


def add_enemy():
    global enemies, score
    if tick_num % 500 == 0:
        enemies.append(create_enemy())


def tick():
    global score, tick_num, game_ended

    move_player()
    move_enemies()
    window.update()  # maunall update the screen

    check_for_collision()
    if game_ended:
        return

    update_score()
    add_enemy()

    tick_num += 1
    window.ontimer(tick, 10)  # update the screen every 10 milliseconds


def setup_window():
    global window
    window = turtle.Screen()
    window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.title('Dodge It!')
    # window.bgcolor('gray10')
    window.bgpic('Resources\\dodge_it\\bg.gif')

    # Disable screen update. We will update it manually using the 'update' method
    window.tracer(0)
    window.listen()  # make the window listen for key presses

    window.onkey(left, 'Left')
    window.onkey(right, 'Right')
    window.onkey(up, 'Up')
    window.onkey(down, 'Down')


register_costumes()
setup_window()
create_player()
create_enemies()
create_score()
animate_enemies()

# start the program after 3 seconds
window.ontimer(tick, 0)

window.mainloop()
