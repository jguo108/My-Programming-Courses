# https://www.youtube.com/watch?v=inocKE13DEA&list=PLlEgNdBJEO-lNDJgg90fmfAq9RzORkQWP

import turtle
import time


TILE_SIZE = 24


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


def move(x_direction, y_direction):
    player_x = player.xcor()
    player_y = player.ycor()
    player_row, player_col = coordinates_to_indices(player_x, player_y)

    # Are we going to run into a wall?
    wall_row = player_row - y_direction
    wall_col = player_col + x_direction

    if level[wall_row][wall_col] == 'X':
        return

    player.goto(player_x + x_direction * TILE_SIZE,
                player_y + y_direction * TILE_SIZE)

    # take treasure
    for t in treasures:
        if t.xcor() == player_x and t.ycor() == player_y:
            t.hideturtle()
            treasures.remove(t)
            break


def up():
    move(0, 1)


def down():
    move(0, -1)


def left():
    move(-1, 0)


def right():
    move(1, 0)


window = turtle.Screen()
window.bgcolor('black')
window.title('A Maze Game')
window.setup(700, 700)

window.listen()
window.onkey(left, 'Left')
window.onkey(right, 'Right')
window.onkey(up, 'Up')
window.onkey(down, 'Down')

pen = turtle.Turtle()
pen.shape('square')
pen.color('white')
pen.penup()
pen.speed(0)

player = None

PLAYER_START_ROW = 1
PLAYER_START_COL = 1

treasures = []

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
    'X  XXX        XXXXT XXXXX',
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


def create_treasures():
    global treasures, treasure_locations
    treasure_locations = [
        (8, 18)
    ]
    for x, y in treasure_locations:
        t = turtle.Turtle()
        t.shape('circle')
        t.color('yellow')
        t.penup()
        t.speed(0)
        t.goto(indices_to_coordinates(x, y))
        # t.showturtle()
        treasures.append(t)


def create_player():
    global player
    player = turtle.Turtle()
    player.shape('square')
    player.color('blue')
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


create_maze(level)
create_player()
create_treasures()

window.mainloop()
