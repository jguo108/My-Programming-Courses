# https://www.youtube.com/watch?v=inocKE13DEA&list=PLlEgNdBJEO-lNDJgg90fmfAq9RzORkQWP

import turtle
import time
import random

game_ended = False

TILE_SIZE = 24

player = None

treasures = []
treasure_locations = [(8, 18), (16, 3), (23, 8)]

enemies = []
enemy_locations = [(5, 21), (10, 4), (19, 13), (22, 5)]

# 25 rows x 25 columns
level = [
    'XXXXXXXXXXXXXXXXXXXXXXXXX',
    'X  XXXXXXX          XXXXX',
    'X  XXXXXXX  XXXXXX  XXXXX',
    'X       XX  XXXXXX  XXXXX',
    'X       XX  XXX        XX',
    'XXXXXX  XX  XXX        XX',
    'XXXXXX  XX  XXXXXX  XXXXX',
    'XXXXXX  XX    XXXX  XXXXX',
    'X  XXX        XXXX  XXXXX',
    'X  XXX  XXXXXXXXXXXXXXXXX',
    'X         XXXXXXXXXXXXXXX',
    'X                XXXXXXXX',
    'XXXXXXXXXXXX     XXXXX  X',
    'XXXXXXXXXXXXXXX  XXXXX  X',
    'XXX  XXXXXXXXXX         X',
    'XXX                     X',
    'XXXT        XXXXXXXXXXXXX',
    'XXXXXXXXXX  XXXXXXXXXXXXX',
    'XXXXXXXXXX              X',
    'XX   XXXXX              X',
    'XX   XXXXXXXXXXXXX  XXXXX',
    'XX    XXXXXXXXXXXX  XXXXX',
    'XX          XXXX        X',
    'XXXX    T               X',
    'XXXXXXXXXXXXXXXXXXXXXXXXX'
]


def collide(player, enemies):
    player_x = player.xcor()
    player_y = player.ycor()
    for enemy in enemies:
        if player_x == enemy.xcor() and player_y == enemy.ycor():
            game_ended = True
            return True
    return False


def coordinates_to_indices(x, y):
    x += 300

    if y <= 0:
        y = abs(y) + 300
    else:
        y = 300 - y

    row = int(y / TILE_SIZE)
    col = int(x / TILE_SIZE)

    return row, col


def indices_to_coordinates(row, col):
    x = -288 + (col * TILE_SIZE)
    y = 288 - (row * TILE_SIZE)
    return x, y


def move_enemies():
    global game_ended
    if game_ended:
        return

    for enemy in enemies:
        enemy_x = enemy.xcor()
        enemy_y = enemy.ycor()
        enemy_row, enemy_col = coordinates_to_indices(enemy_x, enemy_y)

        # up, down, left and right
        direction = random.choice([(0, 1), (0, -1), (-1, 0), (1, 0)])
        x_direction = direction[0]
        y_direction = direction[1]

        # Are we going to run into a wall?
        next_cell_row = enemy_row - y_direction
        next_cell_col = enemy_col + x_direction

        # if it is a wall ahead, we return and do not move the enenmy
        if level[next_cell_row][next_cell_col] != 'X':
            enemy.goto(enemy_x + x_direction * TILE_SIZE,
                       enemy_y + y_direction * TILE_SIZE)

    if collide(player, enemies):
        game_ended = True

    # window.ontimer(move_enemies, random.randint(100, 300))


def move_player(player, x_direction, y_direction):
    global game_ended

    player_x = player.xcor()
    player_y = player.ycor()
    player_row, player_col = coordinates_to_indices(player_x, player_y)

    # Are we going to run into a wall?
    next_cell_row = player_row - y_direction
    next_cell_col = player_col + x_direction

    # if it is a wall ahead, we return and do not move the player
    if level[next_cell_row][next_cell_col] == 'X':
        return

    player.goto(player_x + x_direction * TILE_SIZE,
                player_y + y_direction * TILE_SIZE)

    # take treasure
    if (next_cell_row, next_cell_col) in treasure_locations:
        index = treasure_locations.index((next_cell_row, next_cell_col))
        del treasure_locations[index]
        treasures[index].hideturtle()
        del treasures[index]


def up():
    move_player(player, 0, 1)


def down():
    move_player(player, 0, -1)


def left():
    move_player(player, -1, 0)


def right():
    move_player(player, 1, 0)


window = turtle.Screen()
window.bgcolor('black')
window.title('A Maze Game')
window.setup(700, 700)
window.tracer(0)
window.listen()


def bind_keys(functions, keys):
    for f, k in zip(functions, keys):
        window.onkey(f, k)


pen = turtle.Turtle()
pen.shape('square')
pen.color('white')
pen.penup()
pen.speed(0)


def create_enemies():
    global enemies, enemy_locations
    for x, y in enemy_locations:
        t = turtle.Turtle()
        t.shape('square')
        t.color('red')
        t.penup()
        t.speed(0)
        t.goto(indices_to_coordinates(x, y))
        enemies.append(t)
    # move_enemies()


def create_treasures():
    global treasures, treasure_locations
    for x, y in treasure_locations:
        t = turtle.Turtle()
        t.shape('circle')
        t.color('yellow')
        t.penup()
        t.speed(0)
        t.goto(indices_to_coordinates(x, y))
        treasures.append(t)


def create_player():
    global player
    player = turtle.Turtle()
    player.shape('square')
    player.color('green')
    player.penup()
    player.speed(0)
    place(player, 1, 1)


def place(player, row, col):
    x, y = indices_to_coordinates(row, col)
    player.goto(x, y)


def create_maze(level):
    for row in range(len(level)):
        for col in range(len(level[row])):
            character = level[row][col]
            screen_x = -288 + (col * TILE_SIZE)
            screen_y = 288 - (row * TILE_SIZE)

            if character == 'X':
                pen.goto(screen_x, screen_y)
                pen.stamp()


def tick():
    if game_ended:
        return
    move_enemies()

    turtle.update()
    window.ontimer(tick, 200)


create_maze(level)
create_player()
create_treasures()
create_enemies()
bind_keys([left, right, up, down], ['Left', 'Right', 'Up', 'Down'])

tick()
# move_enemies()

window.mainloop()
