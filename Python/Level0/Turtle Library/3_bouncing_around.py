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

jellyfish = None
jellyfish_costumes = []
index = 0


def register_costumes():
    for i in range(NUM_OF_COSTUMES):
        gif = f'Resources/bouncing_around/{i+1}_small.gif'
        turtle.register_shape(gif)
        jellyfish_costumes.append(gif)


def create_jellyfish():
    global jellyfish
    jellyfish = turtle.Turtle()
    jellyfish.speed(0)
    jellyfish.shape(jellyfish_costumes[index])
    jellyfish.penup()
    jellyfish.goto(
        random.randint(-SCREEN_WIDTH/2+100, SCREEN_WIDTH-100),
        random.randint(-SCREEN_HEIGHT/2+100, SCREEN_HEIGHT/2-100))
    # jellyfish.goto(0, 0)
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
    jellyfish.forward(2)
    bounce(jellyfish)

    window.ontimer(move_jellyfish, 20)


def animate_jellyfish():
    global index, jellyfish, jellyfish
    index += 1
    jellyfish.shape(jellyfish_costumes[index % len(jellyfish_costumes)])

    window.ontimer(animate_jellyfish, 200)


window = turtle.Screen()
window.title('Bouncing Around')
window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
window.bgpic('Resources\\bouncing_around\\background.gif')


register_costumes()
create_jellyfish()
animate_jellyfish()
move_jellyfish()

window.mainloop()
