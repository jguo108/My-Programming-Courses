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
    # window.bgpic('Resources\\dodge_it\\bg.gif')
    window.bgcolor('gray10')
    window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

    # Disable screen update. We will update it manually using the 'update' method
    window.tracer(0)


def create_snake():
    global snake

    snake_head = turtle.Turtle()
    # snake_head.color('green')
    # snake_head.shape('circle')
    snake_head.setheading(90)
    snake_head.shape('Resources/hungry_snake/head_up.gif')
    snake_head.penup()
    snake_head.speed(0)
    snake.append(snake_head)


def place_food():
    x = random.randint(-SCREEN_WIDTH/2, SCREEN_WIDTH/2)
    y = random.randint(-SCREEN_HEIGHT/2, SCREEN_HEIGHT/2)
    food.goto(TILE_SIZE * int(x / TILE_SIZE), TILE_SIZE * int(y / TILE_SIZE))


def create_food():
    global food
    food = turtle.Turtle()
    food.color('red')
    food.shape('circle')
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
    if abs(snake[0].xcor()) > SCREEN_WIDTH/2 or abs(snake[0].ycor()) > SCREEN_HEIGHT/2:
        game_ended = True

    # check for body collision
    for segment in snake[1:]:
        if collide(snake[0], segment):
            print('body collision happened')
            game_ended = True
            break


def grow_snake():
    global snake
    new_segment = turtle.Turtle()
    new_segment.color(random.choice(['#fad5ca', '#fdf0eb', '#f3a695']))
    new_segment.shape('circle')
    new_segment.shapesize(0.8)
    new_segment.penup()
    new_segment.speed(0)
    new_segment.goto(snake[-1].pos())
    snake.append(new_segment)


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
    snake[0].setheading(180)
    snake[0].shape('Resources/hungry_snake/head_left.gif')


def right():
    snake[0].setheading(0)
    snake[0].shape('Resources/hungry_snake/head_right.gif')


def up():
    snake[0].setheading(90)
    snake[0].shape('Resources/hungry_snake/head_up.gif')


def down():
    snake[0].setheading(270)
    snake[0].shape('Resources/hungry_snake/head_down.gif')


def bind_keys():
    global window

    window.listen()  # make the window listen for key presses
    window.onkey(left, 'Left')
    window.onkey(right, 'Right')
    window.onkey(up, 'Up')
    window.onkey(down, 'Down')


# 1. Set up game window
setup_window()


turtle.register_shape('Resources/hungry_snake/head_up.gif')
turtle.register_shape('Resources/hungry_snake/head_down.gif')
turtle.register_shape('Resources/hungry_snake/head_right.gif')
turtle.register_shape('Resources/hungry_snake/head_left.gif')

# 2. Create game objects
create_snake()
create_food()
create_score()

# 3. Bind control keys
bind_keys()

# 5. Start game loop
window.ontimer(tick, 0)

window.mainloop()
