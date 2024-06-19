# https://www.youtube.com/watch?v=FtqWCo1_I4g

import tkinter as tk
import random

ROWS = 25
COLS = 25
TILE_SIZE = 25
WINDOW_WIDTH = COLS * TILE_SIZE
WINDOW_HEIGHT = ROWS * TILE_SIZE


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y


window = tk.Tk()
window.title('Snake Game')
window.resizable(False, False)  # Disable resizing

# center the window (optional)
'''
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))
window.geometry(f'{window_width}x{window_height}+{x}+{y}')
'''

# Create canvas
canvas = tk.Canvas(master=window, bg='black',
                   width=WINDOW_WIDTH,
                   height=WINDOW_HEIGHT,
                   borderwidth=0,  # Remove border
                   highlightthickness=0)  # Remove highlight
canvas.pack()
# window.update()


snake = Tile(5*TILE_SIZE, 5*TILE_SIZE)  # Single tile, snakes's head
snake_body = []  # mutilpe Tile objects
direction_x = 0
direction_y = 0
food = Tile(10*TILE_SIZE, 10*TILE_SIZE)  # Food
game_over = False
score = 0


def change_direction(e):
    global direction_x, direction_y

    if game_over:
        return

    if e.keysym == 'Up' and direction_y != 1:  # when the snake is going up we cannot make it go down
        direction_x = 0
        direction_y = -1
    elif e.keysym == 'Down' and direction_y != -1:  # when the snake is going down we cannot make it go up
        direction_x = 0
        direction_y = 1
    elif e.keysym == 'Left' and direction_x != 1:  # when the snake is going left we cannot make it go right
        direction_x = -1
        direction_y = 0
    elif e.keysym == 'Right' and direction_x != -1:  # when the snake is going right we cannot make it go left
        direction_x = 1
        direction_y = 0


def move():
    global snake, game_over, food, snake_body, score
    if game_over:
        return

    # if snake touches the edge
    if snake.x < 0 or snake.x >= WINDOW_WIDTH or snake.y < 0 or snake.y >= WINDOW_HEIGHT:
        game_over = True
        return

    # if snake touches itself
    for tile in snake_body:
        if tile.x == snake.x and tile.y == snake.y:
            game_over = True
            return

    # check for collision with food
    if snake.x == food.x and snake.y == food.y:
        snake_body.append(Tile(food.x, food.y))
        food.x = random.randint(0, COLS-1) * TILE_SIZE
        food.y = random.randint(0, ROWS-1) * TILE_SIZE
        score += 1

    # update snake body
    for i in range(len(snake_body)-1, -1, -1):
        tile = snake_body[i]
        if i == 0:
            tile.x = snake.x
            tile.y = snake.y
        else:
            tile.x = snake_body[i-1].x
            tile.y = snake_body[i-1].y

    snake.x += direction_x * TILE_SIZE
    snake.y += direction_y * TILE_SIZE


def render():
    global snake, food, snake_body, game_over, score
    canvas.delete('all')

    # Render food
    canvas.create_rectangle(food.x, food.y, food.x +
                            TILE_SIZE, food.y + TILE_SIZE, fill='red')

    # Render snake head
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE,
                            snake.y + TILE_SIZE, fill='lime green')

    # Render snake body
    for tile in snake_body:
        canvas.create_rectangle(tile.x, tile.y, tile.x + TILE_SIZE,
                                tile.y + TILE_SIZE, fill='lime green')

    if game_over:
        # Render 'Game over: Score'
        canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2,
                           font='Arial 20', text=f'Game Over: {score}', fill='white')
    else:
        # Render 'Score'
        canvas.create_text(30, 20, font='Arial 10',
                           text=f'Score: {score}', fill='white')

    window.after(100, tick)  # draw rectangle every 100ms, 10FPS


def tick():
    move()
    render()


tick()

window.bind('<KeyRelease>', change_direction)

window.mainloop()
