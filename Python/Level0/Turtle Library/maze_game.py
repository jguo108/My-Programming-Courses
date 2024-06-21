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


def move(x_direction, y_direction):
    player_x = player.xcor()
    player_y = player.ycor()
    player_row, player_col = coordinates_to_indices(player_x, player_y)

    wall_row = player_row - y_direction
    wall_col = player_col + x_direction

    if levels[0][wall_row][wall_col] == 'X':
        return

    player.goto(player_x + x_direction * TILE_SIZE,
                player_y + y_direction * TILE_SIZE)


def up():
    '''
    player_x = player.xcor()
    player_y = player.ycor()
    player_row, player_col = coordinates_to_indices(player_x, player_y)

    wall_row = player_row - 1
    wall_col = player_col

    if levels[0][wall_row][wall_col] == 'X':
        return

    player.goto(player_x, player_y + TILE_SIZE)
    '''
    move(0, 1)


def down():
    # player.goto(player.xcor(), player.ycor() - TILE_SIZE)
    move(0, -1)


def left():
    # player.goto(player.xcor() - TILE_SIZE, player.ycor())
    move(-1, 0)


def right():
    # player.goto(player.xcor() + TILE_SIZE, player.ycor())
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

player = turtle.Turtle()
player.shape('square')
player.color('blue')
player.penup()
player.speed(0)


levels = []

# 25 rows x 25 columns
level_1 = [
    'XXXXXXXXXXXXXXXXXXXXXXXXX',
    'XP XXXXXXX          XXXXX',
    'X  XXXXXXX  XXXXXX  XXXXX',
    'X       XX  XXXXXX  XXXXX',
    'X       XX  XXX     XXXXX',
    'XXXXXX  XX  XXX     XXXXX',
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
    'XXX         XXXXXXXXXXXXX',
    'XXXXXXXXXX  XXXXXXXXXXXXX',
    'XXXXXXXXXX              X',
    'XX   XXXXX              X',
    'XX   XXXXXXXXXXXXX  XXXXX',
    'XX    XXXXXXXXXXXX  XXXXX',
    'XX          XXXX        X',
    'XXXX                    X',
    'XXXXXXXXXXXXXXXXXXXXXXXXX'
]
levels.append(level_1)


def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * TILE_SIZE)
            screen_y = 288 - (y * TILE_SIZE)

            if character == 'X':
                pen.goto(screen_x, screen_y)
                pen.stamp()
            if character == 'P':
                player.goto(screen_x, screen_y)


setup_maze(levels[0])

print(f'({player.xcor()},{player.ycor()})')


'''
player_x = player.xcor()
player_y = player.ycor()

row, col = coordinates_to_indices(player_x, player_y)

print(f'({row},{col})')
'''

window.mainloop()
