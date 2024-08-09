import turtle

window_width = 900
window_height = 900

head_width = 400
head_height = 100

body_height = 400


def setup_window():
    window.title("Ghost Face")
    window.setup(window_width, window_height)
    window.bgcolor("gray10")


def setup_pen():
    pen.color("ivory")


def draw_head():
    # pass
    pen.penup()
    pen.goto(head_width/2, head_height)
    pen.pendown()
    pen.left(90)
    pen.begin_fill()
    # pen.circle(head_width/2, 360)
    pen.circle(head_width/2, 180)
    pen.end_fill()


def draw_body():
    # pass
    pen.begin_fill()
    for _ in range(2):
        pen.forward(body_height)
        pen.left(90)
        pen.forward(head_width)
        pen.left(90)
    pen.end_fill()


def draw_face():
    pass


def draw_ghost():
    draw_head()
    draw_body()
    draw_face()


window = turtle.Screen()
pen = turtle.Turtle()

setup_window()
setup_pen()

'''
draw_head()
draw_body()
draw_face()
'''
draw_ghost()

window.mainloop()
