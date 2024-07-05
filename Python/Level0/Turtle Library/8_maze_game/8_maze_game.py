# https://www.youtube.com/watch?v=inocKE13DEA&list=PLlEgNdBJEO-lNDJgg90fmfAq9RzORkQWP

# Assets:
# https://www.freepik.com/free-vector/flat-design-pixel-art-element-collection_38680436.htm#fromView=search&page=1&position=31&uuid=b75bdb87-79b5-4f17-a39f-74f3cf2f56fa
# https://www.freepik.com/free-vector/arcade-computer-game-interface-pixel-art-composition-with-retro-space-shooter-screen-aliens-combat-spacecraft_16221369.htm#fromView=search&page=2&position=4&uuid=b75bdb87-79b5-4f17-a39f-74f3cf2f56fa
# https://www.freepik.com/free-vector/flat-design-pixel-art-food-illustration_38680511.htm#fromView=search&page=2&position=37&uuid=0f669d21-60ac-4667-9e82-e1b5ed5a30e5
# https://www.freepik.com/free-vector/flat-design-pixel-art-food-illustration_38680521.htm#fromView=search&page=3&position=6&uuid=0f669d21-60ac-4667-9e82-e1b5ed5a30e5
# https://www.freepik.com/free-vector/pixel-art-pets-icons-8-bit-dogs-cats-pets-cat-dog-pixel-art-illustration-breed-pets_13031396.htm#fromView=search&page=4&position=50&uuid=0f669d21-60ac-4667-9e82-e1b5ed5a30e5
# https://www.freepik.com/free-vector/retro-8-bit-pixel-arcade-computer-game-set-isolated-icons-with-characters-monsters-spacecrafts-vector-illustration_26762888.htm#fromView=search&page=1&position=14&uuid=ae60ace2-e5bb-42c7-b59e-a0d632f6d819
# https://www.freepik.com/free-vector/different-wall-textures_959312.htm#fromView=search&page=1&position=36&uuid=8cadd5c4-16ae-430a-8354-f4e5fbacf990
# https://www.freepik.com/free-vector/abstract-shapes-textile-pattern_852280.htm#fromView=search&page=4&position=0&uuid=8ab47ac6-79be-4edd-9d27-0ceae2c770d3

import turtle
import time
import random

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
MAZE_WIDTH = 600
MAZE_HEIGHT = 600
TILE_SIZE = 24

window = None

player = None

treasures = []
treasure_locations = []

enemies = []
enemy_locations = []

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
    for enemy in enemies:
        if player.distance(enemy) < 20:
            return True
    return False


def maze_indices(x, y):
    x = MAZE_WIDTH/2 + x
    y = MAZE_HEIGHT/2 - y

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
        enemy_row, enemy_col = maze_indices(enemy_x, enemy_y)

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


def move_player(player, x_direction, y_direction):
    player_x = player.xcor()
    player_y = player.ycor()
    player_row, player_col = maze_indices(player_x, player_y)

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
        treasures[index].hideturtle()
        del treasures[index]
        del treasure_locations[index]


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
