import turtle

window_width = 900
window_height = 900

head_width = 400
head_height = 100

body_height = 400

# background_color = "gray50"
background_color = "gray10"


def setup_window():
    window.title("Ghost Face")
    window.setup(window_width, window_height)
    # window.bgcolor("gray50")
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
    # pen.circle(head_width/2, 360)
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

    # pen.color("red")
    # pen.color("gray50")
    pen.color(background_color)

    pen.begin_fill()
    '''
    # pen.circle(40, 180)
    pen.circle((head_width/5)/2, 180)
    pen.left(180)
    '''
    for _ in range(5):
        pen.circle((head_width/5)/2, 180)
        pen.left(180)
    pen.end_fill()


# def draw_face():
def create_face():
    window.addshape("3_ghostface/Resources/Faces/1.gif")
    # face.shape("turtle")
    face.shape("3_ghostface/Resources/Faces/1.gif")


def draw_ghost():
    draw_head()
    draw_body()
    # draw_face()
    create_face()


window = turtle.Screen()
pen = turtle.Turtle()
face = turtle.Turtle()

setup_window()
setup_pen()


'''
draw_head()
draw_body()
draw_face()
'''
draw_ghost()

window.mainloop()
