# This should be a project that shows how you can create some animation
# by moving a turtle in Python

# Idea: an object bouncing around in an enclosed space.
# e.g. a jelly fish moving around in an cave
#
# Jeylly fish animation:
# - https://scratch.mit.edu/projects/814193018/editor/
# - https://scratch.mit.edu/projects/502019480/editor/
# - https://scratch.mit.edu/projects/1037226962/editor/

import turtle
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
NUM_OF_COSTUMES = 6

window = None

jellyfish = None
jellyfish_speed = 2
jellyfish_costumes = []
index = 0


def register_jellyfish_costumes():
    for i in range(NUM_OF_COSTUMES):
        gif = f'Resources/bouncing_around/{i+1}_small.gif'
        turtle.register_shape(gif)
        jellyfish_costumes.append(gif)


def create_jellyfish():
    global jellyfish

    register_jellyfish_costumes()

    jellyfish = turtle.Turtle()
    jellyfish.speed(0)
    jellyfish.shape(jellyfish_costumes[index])
    jellyfish.penup()
    jellyfish.goto(
        random.randint(-SCREEN_WIDTH/2+100, SCREEN_WIDTH/2-100),
        random.randint(-SCREEN_HEIGHT/2+100, SCREEN_HEIGHT/2-100))
    jellyfish.setheading(random.randint(0, 360))


def bounce(t):
    margin = 60
    if t.xcor() > SCREEN_WIDTH/2-margin or \
            t.xcor() < -SCREEN_WIDTH/2+margin or \
        t.ycor() > SCREEN_HEIGHT/2-margin or \
            t.ycor() < -SCREEN_HEIGHT/2+margin:
        t.right(180 + random.randint(-90, 90))


def move_jellyfish():
    global jellyfish
    jellyfish.forward(jellyfish_speed)
    bounce(jellyfish)


def animate_jellyfish():
    global index, jellyfish, jellyfish, window
    index += 1
    jellyfish.shape(jellyfish_costumes[index % len(jellyfish_costumes)])

    window.ontimer(animate_jellyfish, 200)


def setup_window():
    global window

    window = turtle.Screen()
    window.title('Bouncing Around')
    window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.bgpic('Resources\\bouncing_around\\background.gif')
    window.tracer(0)


def tick():
    move_jellyfish()

    window.update()
    window.ontimer(tick, 50)


# 1. setup game window
setup_window()

# 2. create game objects
create_jellyfish()

# 3. animate game objects
animate_jellyfish()

# 4. start game loop
window.ontimer(tick, 0)

window.mainloop()
