# https://projects.raspberrypi.org/en/projects/make-a-face/0

import tkinter as tk

WIDTH = 400
HEIGHT = 400


def draw_face():
    draw_circle(x=200, y=200, radius=100, color="gray15")


def draw_circle(x, y, radius, color):
    # canvas.create_oval(130, 150, 190, 210, fill="black", width=0)
    canvas.create_oval(x - radius, y - radius, x + radius,
                       y + radius, fill=color, width=0)


def draw_beads():
    for i in range(7):
        draw_circle(x=140 + i * 20, y=140, radius=4, color='lime green')


def draw_face_paint():
    # Left face
    draw_circle(x=150, y=220, radius=4, color='pink4')
    draw_circle(x=170, y=220, radius=4, color='pink4')

    # Right face
    draw_circle(x=250, y=220, radius=4, color='pink4')
    draw_circle(x=230, y=220, radius=4, color='pink4')


def draw_eyes():
    # Left eye
    draw_circle(x=160, y=180, radius=30, color='#630a0a')
    draw_circle(x=160, y=180, radius=15, color='black')
    draw_circle(x=165, y=175, radius=4, color='white')

    # Right eye
    draw_circle(x=240, y=180, radius=30, color='#630a0a')
    draw_circle(x=240, y=180, radius=15, color='black')
    draw_circle(x=245, y=175, radius=4, color='white')


def draw_feathers():
    # Left feather
    canvas.create_polygon(160, 50, 180, 50, 200, 120, fill="orange3", width=0)

    # Right feather
    canvas.create_polygon(240, 50, 220, 50, 200, 120, fill="orange3", width=0)


def draw_mouth():
    draw_circle(x=200, y=275, radius=15, color='#803f06')
    draw_circle(x=190, y=270, radius=15, color='#803f06')
    draw_circle(x=210, y=270, radius=15, color='#803f06')
    canvas.create_rectangle(185, 265, 215, 275, fill='black', width=0)


def draw_nose():
    canvas.create_polygon(200, 180, 180, 240,
                          220, 240, fill="pink4")


# Create the main window
window = tk.Tk()

# Create a canvas widget
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg='LemonChiffon4')

# Pack the canvas widget into the main window
canvas.pack()


draw_face()
draw_eyes()
draw_nose()
draw_mouth()
draw_feathers()
draw_beads()
draw_face_paint()
# Run the main event loop
window.mainloop()
