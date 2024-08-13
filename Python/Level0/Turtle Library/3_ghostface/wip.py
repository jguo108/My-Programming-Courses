import turtle
import time

window_width = 900
window_height = 900

head_width = 400
head_height = 100

body_height = 400

face_height = 70

num_of_face_costumes = 43

# background_color = "gray50"
background_color = "gray10"

face_costumes = []


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
    # window.addshape("3_ghostface/Resources/Faces/1.gif")
    # for _ in range(43):
    # for i in range(43):
    for i in range(num_of_face_costumes):
        # window.addshape("3_ghostface/Resources/Faces/1.gif")
        # window.addshape(f"3_ghostface/Resources/Faces/{i}.gif")
        path = f"3_ghostface/Resources/Faces/{i+1}.gif"
        # window.addshape(f"3_ghostface/Resources/Faces/{i+1}.gif")
        # face_costumes.append(f"3_ghostface/Resources/Faces/{i+1}.gif")
        window.addshape(path)
        face_costumes.append(path)

    # face.shape("turtle")
    face.shape("3_ghostface/Resources/Faces/1.gif")
    face.speed(0)
    face.penup()
    face.goto(0, face_height)


def draw_ghost():
    draw_head()
    draw_body()
    # draw_face()
    create_face()


def animate_face():
    # pass
    '''
    for i in range(num_of_face_costumes):
        # face.shape(f"3_ghostface/Resources/Faces/{i+1}.gif")
        face.shape(face_costumes[i])
        # time.sleep(1)
        # time.sleep(0.1)
        time.sleep(0.05)
    '''

    i = 0
    while True:
        if i == num_of_face_costumes:
            i = 0
        face.shape(face_costumes[i])
        time.sleep(0.05)
        i += 1


i = 0


def switch_face_costume():
    global i
    # i = 0
    face.shape(face_costumes[i])
    i += 1
    window.ontimer(switch_face_costume, 50)


def animate_arms():
    print("Animating arms!")


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

# animate_face()

# window.ontimer(switch_face_costume, 1000)
# window.ontimer(switch_face_costume, 0)
switch_face_costume()

animate_arms()

window.mainloop()
