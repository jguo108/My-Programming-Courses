import turtle
from random import randint

window_width = 600
window_height = 600


def setup_window():
    window.title("Modern Art")
    # window.setup(600, 600)
    window.setup(window_width, window_height)
    window.bgcolor("gray10")


def setup_pen():
    pen.shape("turtle")
    pen.color("DarkOrange")
    pen.speed(0)
    turtle.colormode(255)


def pick_position():
    # x = randint(-300, 300)
    # y = randint(-300, 300)
    # x = randint(-200, 200)
    # y = randint(-200, 200)
    x = randint(-window_width/2 + 100, window_width/2 - 100)
    y = randint(-window_height/2 + 100, window_height/2 - 100)
    pen.penup()
    pen.goto(x, y)
    pen.pendown()


def pick_color():
    # pen.color("LightPink")
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    pen.color(red, green, blue)


def pick_direction():
    pen.setheading(randint(0, 360))


def draw_square():
    '''
    x = randint(-300, 300)
    y = randint(-300, 300)
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    '''
    pick_position()
    '''
    pen.color("LightPink")
    '''
    pick_color()
    pick_direction()

    side_length = randint(10, 150)
    pen.begin_fill()
    for _ in range(4):
        # pen.forward(100)
        pen.forward(side_length)
        pen.left(90)
    pen.end_fill()


def draw_circle():
    pick_position()
    pick_color()
    radius = randint(10, 100)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()


def create_art():
    for _ in range(10):
        draw_square()

    for _ in range(10):
        draw_circle()


window = turtle.Screen()
pen = turtle.Turtle()

setup_window()
'''
window.title("Modern Art")
window.setup(600, 600)
# window.bgcolor("red")
window.bgcolor("gray10")
'''

setup_pen()
'''
pen.shape("turtle")
pen.color("DarkOrange")
'''

# pen.forward(50)
# pen.forward(400)
# pen.forward(-50)
# pen.backward(50)

# pen.setheading(90)
# pen.setheading(180)
# pen.setheading(270)
# pen.setheading(360)
# pen.setheading(45)
# pen.setheading(135)
# pen.forward(50)

# pen.left(90)
# pen.right(90)

# pen.forward(100)
# pen.left(90)
# pen.forward(100)
# pen.left(90)
# pen.forward(100)
# pen.left(90)
# pen.forward(100)
# pen.left(90)

'''
pen.color("LightPink")
pen.begin_fill()
# for i in range(4):
for _ in range(4):
    pen.forward(100)
    pen.left(90)
pen.end_fill()
'''

'''
for _ in range(10):
    draw_square()

# pen.penup()
# pen.goto(150, 200)
# pen.pendown()

for _ in range(10):
    draw_circle()
'''
create_art()

window.mainloop()

# print("End of program")
