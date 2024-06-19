# Coding Projects in Python
from itertools import cycle
from random import randrange
import tkinter as tk
from tkinter import messagebox, font


def setup_scene():
    # Grass
    canvas.create_rectangle(-5, canvas_height-100, canvas_width+5,
                            canvas_height+5, fill='sea green', width=0)
    # Sun
    canvas.create_oval(-80, -80, 120, 120, fill='orange', width=0)


def create_catcher():
    return canvas.create_arc(
        catcher_start_x,
        catcher_start_y,
        catcher_start_x2,
        catcher_start_y2,
        start=200,
        extent=140,
        style='arc',
        outline=catcher_color,
        width=3)


def create_score():
    return canvas.create_text(
        10, 10, anchor='nw', text='Score: ' + str(score), fill='darkblue', font=game_font)


def create_lives():
    return canvas.create_text(
        canvas_width-10, 10, anchor='ne', text='Lives: ' + str(lives_remaining), fill='darkblue', font=game_font
    )


def create_eggs():
    x = randrange(10, 740)
    y = 40
    new_egg = canvas.create_oval(
        x, y, x+egg_width, y+egg_height, fill=next(egg_colors), width=0)
    eggs.append(new_egg)
    window.after(egg_interval, create_eggs)


def lose_a_life():
    global lives_remaining
    lives_remaining -= 1
    canvas.itemconfigure(lives_text, text='Lives: ' + str(lives_remaining))


def egg_dropped(egg):
    eggs.remove(egg)
    canvas.delete(egg)
    lose_a_life()
    if lives_remaining == 0:
        messagebox.showinfo('Game Over!', 'Final Score: ' + str(score))
        window.destroy()


def move_eggs():
    for egg in eggs:
        (egg_x, egg_y, egg_x2, egg_y2) = canvas.coords(egg)
        canvas.move(egg, 0, 10)
        if egg_y2 > canvas_height:
            egg_dropped(egg)
    window.after(egg_speed, move_eggs)


def increase_score(points):
    global score, egg_speed, egg_interval
    score += points
    # increase speed by difficulty_factor
    egg_speed = int(egg_speed * difficulty_factor)
    egg_interval = int(egg_interval * difficulty_factor)
    canvas.itemconfigure(score_text, text='Score: ' + str(score))


def check_catch():
    (catcher_x, catcher_y, catcher_x2, catcher_y2) = canvas.coords(catcher)
    for egg in eggs:
        (egg_x, egg_y, egg_x2, egg_y2) = canvas.coords(egg)
        if catcher_x < egg_x and egg_x2 < catcher_x2 and catcher_y2 - egg_y2 < 40:
            eggs.remove(egg)
            canvas.delete(egg)
            increase_score(egg_score)
    window.after(100, check_catch)


def move_left(event):
    (x1, y1, x2, y2) = canvas.coords(catcher)
    if x1 > 0:
        canvas.move(catcher, -20, 0)


def move_right(event):
    (x1, y1, x2, y2) = canvas.coords(catcher)
    if x2 < canvas_width:
        canvas.move(catcher, 20, 0)


canvas_width = 800
canvas_height = 600

egg_colors = cycle(
    ['light blue', 'light green', 'light pink', 'light yellow', 'light cyan'])

# egg variables
egg_width = 45
egg_height = 55
egg_score = 10
egg_speed = 500
egg_interval = 4000
difficulty_factor = 0.95

# catcher variables
catcher_color = 'blue'
catcher_width = 100
catcher_height = 100
catcher_start_x = canvas_width/2-catcher_width/2
catcher_start_y = canvas_height-catcher_height-20
catcher_start_x2 = catcher_start_x+catcher_width
catcher_start_y2 = catcher_start_y+catcher_height

# lives
lives_remaining = 3

# score
score = 0

# eggs
eggs = []

window = tk.Tk()
window.resizable(False, False)
canvas = tk.Canvas(
    window,
    width=canvas_width,
    height=canvas_height,
    background='deep sky blue')
canvas.pack()

# font
game_font = font.nametofont('TkFixedFont')
game_font.config(size=18)

setup_scene()
catcher = create_catcher()
score_text = create_score()
lives_text = create_lives()

# Keyboard movement
canvas.bind('<Left>', move_left)
canvas.bind('<Right>', move_right)
canvas.focus_set()

# After one second start eggs, then move, then check for catch
window.after(1000, create_eggs)
window.after(1000, move_eggs)
window.after(1000, check_catch)

window.mainloop()
