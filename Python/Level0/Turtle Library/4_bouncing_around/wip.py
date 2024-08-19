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

stopped = False


def setup_window():
    window.title("Bouncing Around")
    window.setup(window_width, window_height)
    # window.bgcolor("black")
    window.bgpic(
        '4_bouncing_around/Resources/Background/background.gif')
    # window.tracer(0)


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


def bind_keys():
    window.onkey(stop, "space")
    window.listen()


def stop():
    global stopped
    print("Space key pressed!")
    stopped = True


def move_jellyfish():
    jellyfish.forward(jellyfish_speed)
    if jellyfish.xcor() >= window_width/2 or \
            jellyfish.xcor() <= -window_width/2 or \
            jellyfish.ycor() >= window_height/2 or \
            jellyfish.ycor() <= -window_height/2:
        jellyfish.left(180+random.randint(-45, 45))


def game_loop():
    while True:
        # print(stopped)
        if stopped:
            break
        move_jellyfish()
        '''
        jellyfish.forward(jellyfish_speed)
        # print(f"({jellyfish.xcor()},{jellyfish.ycor()})")
        if jellyfish.xcor() >= window_width/2 or \
                jellyfish.xcor() <= -window_width/2 or \
                jellyfish.ycor() >= window_height/2 or \
                jellyfish.ycor() <= -window_height/2:
            # print("Bouncing back!")
            # jellyfish.left(180)
            jellyfish.left(180+random.randint(-45, 45))
        '''


window = turtle.Screen()
jellyfish = turtle.Turtle()

setup_window()

'''
window.onkey(pause_and_resume, "space")
window.listen()
'''
bind_keys()

create_jellyfish()

switch_jellyfish_costume()

'''
while True:
    # print(stopped)
    if stopped:
        break
    jellyfish.forward(jellyfish_speed)
    # print(f"({jellyfish.xcor()},{jellyfish.ycor()})")
    if jellyfish.xcor() >= window_width/2 or \
            jellyfish.xcor() <= -window_width/2 or \
            jellyfish.ycor() >= window_height/2 or \
            jellyfish.ycor() <= -window_height/2:
        # print("Bouncing back!")
        # jellyfish.left(180)
        jellyfish.left(180+random.randint(-45, 45))
'''
game_loop()

window.mainloop()
