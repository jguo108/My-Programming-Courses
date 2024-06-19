# https://projects.raspberrypi.org/en/projects/dont-collide/0

import tkinter as tk
import random

# TODO:
# - add a game over screen
# - add a game won screen
# - add a background
# - use better images for player and obstacles
# - add score text
# - use level to make the game more difficult as time progresses

game_ended = False
score = 0
level = 1


def move_player(event):
    canvas.coords(player)[0]
    canvas.coords(player)[1]

    if event.keysym == 'Left':
        canvas.move(player, -5, 0)
    elif event.keysym == 'Right':
        canvas.move(player, 5, 0)


def create_obstacle():
    global game_ended
    if not game_ended:
        height = 20 * (3 ** 0.5) / 2
        x = random.randint(0, 400)
        y = -20
        obstacle = canvas.create_polygon(
            x, y, x + 10, y + height, x - 10, y + height,
            fill="red", outline="red", width=0)
        move_obstacle(obstacle)
        window.after(random.randint(500, 2500), create_obstacle)


def move_obstacle(obstacle):
    global game_ended, score
    if not game_ended:
        score += 1
        obstacle_y = canvas.coords(obstacle)[1]
        if obstacle_y < 400:
            # Increase the speed to 2 pixels per move
            canvas.move(obstacle, 0, 4)
            # Decrease the delay to 50 milliseconds
            if check_collision(obstacle):
                game_ended = True
                return
            window.after(10, move_obstacle, obstacle)
        else:
            canvas.delete(obstacle)


def check_collision(obstacle):
    # Create bounding boxes for the player and obstacle
    player_bbox = canvas.bbox(player)
    obstacle_bbox = canvas.bbox(obstacle)

    player_x1 = player_bbox[0]
    player_y1 = player_bbox[1]
    player_x2 = player_bbox[2]
    player_y2 = player_bbox[3]

    obstacle_x1 = obstacle_bbox[0]
    obstacle_y1 = obstacle_bbox[1]
    obstacle_x2 = obstacle_bbox[2]
    obstacle_y2 = obstacle_bbox[3]

    return not (obstacle_x1 > player_x2 or
                obstacle_x2 < player_x1 or
                obstacle_y1 > player_y2 or
                obstacle_y2 < player_y1)


# Create the main window
window = tk.Tk()

# Set the window size
window.geometry("400x400")

# Create a canvas widget
canvas = tk.Canvas(window, width=400, height=400)

# Pack the canvas widget into the main window
canvas.pack()

# Create an player object on the canvas
player = canvas.create_oval(190, 340, 210, 360, fill="blue")

# Bind the move_player function to left and right arrow keys
window.bind("<Left>", move_player)
window.bind("<Right>", move_player)

window.after(1000, create_obstacle())

# Run the main event loop
window.mainloop()
