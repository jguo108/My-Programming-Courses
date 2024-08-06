import turtle


def setup_window():
    window.title("Modern Art")
    window.setup(600, 600)
    window.bgcolor("gray30")


def setup_pen():
    pen.shape("turtle")
    pen.color("DarkOrange")


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

window.mainloop()

# print("End of program")
