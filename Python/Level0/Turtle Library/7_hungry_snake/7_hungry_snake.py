# https://www.youtube.com/watch?v=BP7KMlbvtOo&list=PLlEgNdBJEO-n8k9SR49AshB9j7b5Iw7hZ

# Assets:
# https://www.freepik.com/free-vector/flat-snake-background_4149945.htm#fromView=search&page=2&position=36&uuid=90107521-77ac-4093-9851-86d0df4b256c
# https://www.freepik.com/free-vector/top-view-hand-drawn-snake-background_4231226.htm#fromView=search&page=5&position=16&uuid=90107521-77ac-4093-9851-86d0df4b256c
# https://www.freepik.com/free-vector/colorful-flat-snake-illustration_4453110.htm#fromView=search&page=5&position=52&uuid=90107521-77ac-4093-9851-86d0df4b256c
# https://www.freepik.com/free-vector/flat-striped-snake-background_4182522.htm#fromView=search&page=7&position=36&uuid=90107521-77ac-4093-9851-86d0df4b256c


import turtle
import math
import random

# TODO

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
TILE_SIZE = 24

window = None

snake = []

food = None

score_pen = None
score = 0

game_ended = False


def setup_window():
    global window
    window = turtle.Screen()
    window.title('Hungry Snake')
    # window.bgpic('7_hungry_snake/Resources/bg.gif')
    window.bgcolor('gray10')
    window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

    # Disable screen update. We will update it manually using the 'update' method
    window.tracer(0)


def create_segment(shape, color):
    segment = turtle.Turtle()
    # segment.color(random.choice(['#fad5ca', '#fdf0eb', '#f3a695']))
    segment.color(color)
    segment.shape(shape)
    segment.penup()
    segment.speed(0)
    return segment


def create_snake():
    global snake
    head = create_segment('circle', '#e8829b')
    snake.append(head)


def place_food():
    x = random.randint(-SCREEN_WIDTH/2, SCREEN_WIDTH/2)
    y = random.randint(-SCREEN_HEIGHT/2, SCREEN_HEIGHT/2)
    food.goto(TILE_SIZE * int(x / TILE_SIZE), TILE_SIZE * int(y / TILE_SIZE))


def create_food():
    global food
    food = turtle.Turtle()
    food.color(random.choice(
        ['#F6FFDE', '#E3F2C1', '#C9DBB2', '#AAC8A7', '#C3EDC0', '#E9FFC2', '#FDFFAE']))
    food.shape('square')
    food.shapesize(0.7, 0.7)
    food.penup()
    food.speed(0)
    place_food()


def create_score():
    global score_pen
    score_pen = turtle.Turtle()
    score_pen.penup()
    score_pen.hideturtle()
    score_pen.color('gray80')
    score_pen.goto(-SCREEN_WIDTH/2 + 10, SCREEN_HEIGHT/2 - 30)
    score_pen.write(f'Score: {score}', False, align='left',
                    font=('Courier', 14, 'normal'))


def collide(t1, t2):
    return t1.distance(t2) < 20


def update_score():
    global score
    score += 1
    score_pen.clear()
    score_pen.write(f'Score: {score}', False, align='left',
                    font=('Courier', 14, 'normal'))


def move_snake():
    global game_ended

    for i in range(len(snake)-1, 0, -1):
        snake[i].goto(snake[i-1].pos())

    snake[0].forward(TILE_SIZE)

    # check for border collision
    if abs(snake[0].xcor()) > SCREEN_WIDTH/2 or abs(snake[0].ycor()) > SCREEN_HEIGHT/2:
        game_ended = True

    # check for body collision
    for segment in snake[1:]:
        if collide(snake[0], segment):
            game_ended = True
            break


def grow_snake():
    global snake
    body_part = create_segment('circle', random.choice(
        ['#fad5ca', '#fdf0eb', '#f3a695']))

    body_part.goto(snake[-1].pos())
    snake.append(body_part)


def eat_food():
    if collide(snake[0], food):
        update_score()
        place_food()
        grow_snake()


def tick():
    global score, game_ended

    if game_ended:
        return

    move_snake()
    eat_food()

    window.update()  # maunall update the screen
    window.ontimer(tick, 200)  # update the screen every 10 milliseconds


def left():
    if snake[0].heading() != 0:
        snake[0].setheading(180)


def right():
    if snake[0].heading() != 180:
        snake[0].setheading(0)


def up():
    if snake[0].heading() != 270:
        snake[0].setheading(90)


def down():
    if snake[0].heading() != 90:
        snake[0].setheading(270)


def bind_keys():
    global window

    window.listen()  # make the window listen for key presses
    window.onkey(left, 'Left')
    window.onkey(right, 'Right')
    window.onkey(up, 'Up')
    window.onkey(down, 'Down')


# 1. Set up game window
setup_window()

# 2. Create game objects
create_snake()
create_food()
create_score()

# 3. Bind control keys
bind_keys()

# 5. Start game loop
window.ontimer(tick, 0)

window.mainloop()
