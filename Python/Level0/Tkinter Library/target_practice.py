# https://projects.raspberrypi.org/en/pathways/python-intro

# Tkinter color chart
# https://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html

# TODO
# - getting stuck at how to get the color of a specific pixel in the canvas
#   We need this color to determine where the arrow has hit on the targer

import tkinter as tk
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400


def create_scene():
    # TODO: how to remove the border of the window?
    canvas.create_rectangle(0, CANVAS_HEIGHT*0.6,
                            CANVAS_WIDTH + 5, CANVAS_HEIGHT + 5, fill='sea green', width=0)

    canvas.create_polygon(150, 350, 200, 150, 250, 350, fill='LightSalmon4')
    canvas.create_oval(120, 120, 280, 280, fill='orchid4', width=0)
    canvas.create_oval(150, 150, 250, 250, fill='orchid1', width=0)
    canvas.create_oval(180, 180, 220, 220, fill='light goldenrod', width=0)


arrow = None


def draw_arrow():
    global arrow
    canvas.delete(arrow)
    arrow_x = random.randint(100, 300)
    arrow_y = random.randint(100, 300)
    arrow = canvas.create_oval(arrow_x, arrow_y, arrow_x + 10, arrow_y + 10,
                               fill='indian red', width=0)
    window.after(1000, draw_arrow)


window = tk.Tk()
window.resizable(False, False)
canvas = tk.Canvas(
    window,
    width=CANVAS_WIDTH,
    height=CANVAS_HEIGHT,
    background='deep sky blue')
canvas.pack()


create_scene()
# draw_arrow()


window.mainloop()
