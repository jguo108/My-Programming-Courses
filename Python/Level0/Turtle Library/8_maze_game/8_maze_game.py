# https://www.youtube.com/watch?v=inocKE13DEA&list=PLlEgNdBJEO-lNDJgg90fmfAq9RzORkQWP

import turtle
import time
import random

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
TILE_SIZE = 24

window = None

player = None

treasures = []
treasure_locations = []

enemies = []
enemy_locations = [(5, 21), (10, 4), (19, 13), (22, 5)]

game_ended = False

# 25 rows x 25 columns
maze = [
    '*************************',
    '*P *******          *****',
    '*  *******  ******  *****',
    '*       **  ******  *****',
    '*       **  ***        **',
    '******  **  ***      E **',
    '******  **  ******  *****',
    '******  **    ****  *****',
    '*  ***        ****T *****',
    '*  ***  *****************',
    '*   E     ***************',
    '*                ********',
    '************     *****  *',
    '***************  *****  *',
    '***  **********         *',
    '***                     *',
    '*** T       *************',
    '**********  *************',
    '**********              *',
    '**   *****   E          *',
    '**   *************  *****',
    '**    ************  *****',
    '**    E     ****        *',
    '****    T               *',
    '*************************'
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
        if maze[next_cell_row][next_cell_col] != '*':
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
    if maze[next_cell_row][next_cell_col] == '*':
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
    move_player(player, x_direction=0, y_direction=1)


def down():
    move_player(player, x_direction=0, y_direction=-1)


def left():
    move_player(player, x_direction=-1, y_direction=0)


def right():
    move_player(player, x_direction=1, y_direction=0)


def setup_window():
    global window
    window = turtle.Screen()
    window.bgcolor('black')
    window.title('A Maze Game')
    window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.tracer(0)
    window.listen()


def bind_keys():
    window.onkey(left, 'Left')
    window.onkey(right, 'Right')
    window.onkey(up, 'Up')
    window.onkey(down, 'Down')


def create_enemy(x, y):
    enemy = turtle.Turtle()
    enemy.shape('square')
    enemy.color('red')
    enemy.penup()
    enemy.speed(0)
    enemy.goto(x, y)
    enemies.append(enemy)


def create_treasure(x, y):
    treasure = turtle.Turtle()
    treasure.shape('circle')
    treasure.color('yellow')
    treasure.penup()
    treasure.speed(0)
    treasure.goto(x, y)
    treasures.append(treasure)


def create_player(x, y):
    global player
    player = turtle.Turtle()
    player.shape('square')
    player.color('green')
    player.penup()
    player.speed(0)
    player.goto(x, y)


def setup_maze():
    pen = turtle.Turtle()
    pen.shape('square')
    pen.color('white')
    pen.penup()
    pen.speed(0)

    for row in range(len(maze)):
        for col in range(len(maze[row])):
            cell = maze[row][col]
            x = -288 + (col * TILE_SIZE)
            y = 288 - (row * TILE_SIZE)

            if cell == '*':
                pen.goto(x, y)
                pen.stamp()
            elif cell == 'P':
                create_player(x, y)
            elif cell == 'T':
                create_treasure(x, y)
                treasure_locations.append((row, col))
            elif cell == 'E':
                create_enemy(x, y)
                enemy_locations.append((row, col))


def tick():
    if game_ended:
        return
    move_enemies()

    window.update()
    window.ontimer(tick, 150)


setup_window()

bind_keys()

setup_maze()

tick()

window.mainloop()
