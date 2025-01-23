import turtle
import time

window_width = 900
window_height = 900

head_width = 400
head_height = 100

body_height = 400

face_height = 70

num_of_face_costumes = 43

background_color = "gray10"

face_costumes = []

i = 0


def setup_window():
    window.title("Ghost Face")
    window.setup(window_width, window_height)
    window.bgcolor(background_color)


def setup_pen():
    pen.color("ivory")
    pen.speed(0)


def draw_head():
    # pass
    pen.penup()
    pen.goto(head_width/2, head_height)
    pen.pendown()
    pen.left(90)
    pen.begin_fill()
    pen.circle(head_width/2, 180)
    pen.end_fill()


def draw_body():
    # pass
    pen.penup()
    pen.begin_fill()
    for _ in range(2):
        pen.forward(body_height)
        pen.left(90)
        pen.forward(head_width)
        pen.left(90)
    pen.end_fill()

    pen.forward(body_height)
    pen.left(90)
    pen.forward(head_width)
    pen.left(90)

    pen.color(background_color)

    pen.begin_fill()
    for _ in range(5):
        pen.circle((head_width/5)/2, 180)
        pen.left(180)
    pen.end_fill()


def create_face():
    for i in range(num_of_face_costumes):
        path = f"3_ghostface/Resources/Faces/{i+1}.gif"
        window.addshape(path)
        face_costumes.append(path)

    face.shape("3_ghostface/Resources/Faces/1.gif")
    face.speed(0)
    face.penup()
    face.goto(0, face_height)


def draw_ghost():
    draw_head()
    draw_body()
    create_face()


def switch_face_costume():
    global i
    if i == num_of_face_costumes:
        i = 0
    face.shape(face_costumes[i])
    i += 1
    window.ontimer(switch_face_costume, 50)


window = turtle.Screen()
pen = turtle.Turtle()
face = turtle.Turtle()

setup_window()
setup_pen()

draw_ghost()

switch_face_costume()

window.mainloop()
