import turtle


def setup_window():
    window.title("Modern Art")
    window.setup(600, 600)
    window.bgcolor("gray30")


def setup_pen():
    pen.shape("turtle")
    pen.color("DarkOrange")


def draw_square():
    pen.color("LightPink")
    pen.begin_fill()
    for _ in range(4):
        pen.forward(100)
        pen.left(90)
    pen.end_fill()


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

for _ in range(10):
    draw_square()

# pen.penup()
# pen.goto(150, 200)
# pen.pendown()

window.mainloop()

# print("End of program")
