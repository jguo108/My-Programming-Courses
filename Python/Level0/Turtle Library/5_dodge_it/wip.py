# https: // www.tcl.tk/man/tcl8.4/TkCmd/keysyms.htm

import turtle

window_width = 600
window_height = 600


def setup_window():
    window.title("Dodge It!")
    window.setup(window_width, window_height)
    window.bgpic("5_dodge_it/Resources/Background/background.gif")


def setup_player():
    path = "5_dodge_it/Resources/Player/player.gif"
    window.addshape(path)
    player.shape(path)
    player.penup()


def move_left():
    # print("Moving left!")
    player.setheading(180)
    player.forward(10)


def move_right():
    print("Moving right!")


def move_up():
    print("Moving up!")


def move_down():
    print("Moving down!")


def bind_keys():
    # window.onkey(move_left, "Left")
    window.onkeypress(move_left, "Left")
    window.onkey(move_right, "Right")
    window.onkey(move_up, "Up")
    window.onkey(move_down, "Down")
    window.listen()


window = turtle.Screen()
player = turtle.Turtle()

setup_window()
setup_player()

bind_keys()

window.mainloop()
