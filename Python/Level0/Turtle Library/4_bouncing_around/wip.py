import turtle
import random
import time

# window_width = 800
window_width = 600
window_height = 800

num_of_jellyfish_costumes = 6
jellyfish_costumes = []
jellyfish_speed = 2

i = 0

border_width = 100


def setup_window():
    window.title("Bouncing Around")
    window.setup(window_width, window_height)
    # window.bgcolor("black")
    window.bgpic(
        '4_bouncing_around/Resources/Background/background.gif')


def create_jellyfish():
    for i in range(num_of_jellyfish_costumes):
        path = f'4_bouncing_around/Resources/Jellyfish/{i+1}_small.gif'
        window.addshape(path)
        jellyfish_costumes.append(path)

    # jellyfish.shape(jellyfish_costumes[0])
    jellyfish.shape("4_bouncing_around/Resources/Jellyfish/1_small.gif")
    jellyfish.penup()
    jellyfish.speed(0)
    '''
    jellyfish.goto(
        random.randint(-window_width/2, window_width/2),
        random.randint(-window_height/2, window_height/2))
    '''
    jellyfish.goto(
        random.randint(-window_width/2 + border_width,
                       window_width/2 - border_width),
        random.randint(-window_height/2 + border_width, window_height/2 - border_width))
    jellyfish.setheading(random.randint(0, 360))


def switch_jellyfish_costume():
    global i
    if i == num_of_jellyfish_costumes:
        i = 0
    jellyfish.shape(jellyfish_costumes[i])
    i += 1

    # window.ontimer(switch_jellyfish_costume, 500)
    window.ontimer(switch_jellyfish_costume, 100)


def bounce(t):
    margin = 60
    if abs(t.xcor()) > window_width/2 - margin or \
            abs(t.ycor()) > window_height/2 - margin:
        t.right(180 + random.randint(-90, 90))


def move_jellyfish():
    jellyfish.forward(jellyfish_speed)
    bounce(jellyfish)


def game_loop():
    while True:
        move_jellyfish()
        time.sleep(0.005)


window = turtle.Screen()
jellyfish = turtle.Turtle()

setup_window()

create_jellyfish()

switch_jellyfish_costume()

# game_loop()

while True:
    jellyfish.forward(jellyfish_speed)
    # print(f"({jellyfish.xcor()},{jellyfish.ycor()})")
    if jellyfish.xcor() >= window_width/2 or \
            jellyfish.xcor() <= -window_width/2 or \
            jellyfish.ycor() >= window_height/2 or \
            jellyfish.ycor() <= -window_height/2:
        # print("Bouncing back!")
        # jellyfish.left(180)
        jellyfish.left(180+random.randint(-90, 90))


window.mainloop()
