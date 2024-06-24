import turtle

# This should be a project that shows how you can create
# some animation by switching costumes in Python
# https://scratch.mit.edu/projects/237521692/
# https://scratch.mit.edu/projects/25383083/editor/
# https://scratch.mit.edu/projects/456587459/editor/


# Idea: draw a animated ghost face
# - reference for costumes:https://www.freepik.com/free-vector/collection-cute-halloween-ghosts_1319212.htm#fromView=search&page=1&position=29&uuid=cf5b65a7-71d0-4fe3-982e-44272b07ac6e
# - reference for animation: https://scratch.mit.edu/projects/237521692/

# Fullwindow the canvas

window = turtle.Screen()
window.title('Make a Face')
window.setup(900, 900)  # width and height of the window
window.bgcolor('gray10')

face = None
faces = []

HEAD_RADIUS = 200
BODY_HEIGHT = 400


def animate():
    global face

    window.ontimer(blink_eyes, 1)


def register_faces():
    for i in range(10):
        face_gif = f'Resources/make_a_face/{i+1}.gif'
        turtle.register_shape(face_gif)
        faces.append(face_gif)


def build_body():
    # Begin!
    body = turtle.Turtle()

    body.shape("turtle")
    body.speed(0)
    body.penup()

    body.goto(HEAD_RADIUS, 100)
    body.left(90)

    body.fillcolor('white')
    body.begin_fill()
    body.circle(HEAD_RADIUS, 180)
    body.forward(BODY_HEIGHT)
    body.left(90)
    body.forward(HEAD_RADIUS * 2)
    body.left(90)
    body.forward(BODY_HEIGHT)
    body.end_fill()

    body.goto(HEAD_RADIUS, 100 - BODY_HEIGHT)
    body.fillcolor('gray10')
    body.begin_fill()

    for _ in range(5):
        body.circle(HEAD_RADIUS/5, 180)
        body.right(180)
    body.end_fill()
    body.hideturtle()

    face = turtle.Turtle()
    face.speed(0)
    face.penup()
    face.goto(0, 70)
    face.shape(faces[0])
    face.shapesize(1, 1)


register_faces()
build_body()
animate()

window.mainloop()
