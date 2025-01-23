# https://www.youtube.com/watch?v=BP7KMlbvtOo&list=PLlEgNdBJEO-n8k9SR49AshB9j7b5Iw7hZ

import turtle
import math
import random

# TODO

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
INITIAL_ENEMIES = 5
NUM_OF_ENEMY_COSTUMES = 31

window = None

snake_head = None
snake_body = []
snake_speed = 1.5

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


def create_snake_head():
    global snake_head

    snake_head = turtle.Turtle()
    snake_head.color('green')
    snake_head.shape('square')
    snake_head.penup()
    snake_head.speed(0)  # TODO: what does this do?


def create_food():
    global food
    food = turtle.Turtle()
    food.color('red')
    food.shape('circle')
    food.penup()
    food.speed(0)
    food.goto(random.randint(-SCREEN_WIDTH/2+50, SCREEN_WIDTH/2-50),
              random.randint(-SCREEN_HEIGHT/2+50, SCREEN_HEIGHT/2-50))


def create_score():
    global score_pen
    score_pen = turtle.Turtle()
    score_pen.penup()
    score_pen.hideturtle()
    score_pen.color('gray80')
    score_pen.goto(-SCREEN_WIDTH/2 + 10, SCREEN_HEIGHT/2 - 30)
    score_pen.write(f'Score: {score}', False, align='left',
                    font=('Courier', 14, 'normal'))


def left():
    snake_head.setheading(180)


def right():
    snake_head.setheading(0)


def up():
    snake_head.setheading(90)


def down():
    snake_head.setheading(270)


def collide(t1, t2):
    distance = math.sqrt(
        math.pow(t1.xcor()-t2.xcor(), 2) +
        math.pow(t1.ycor()-t2.ycor(), 2))
    return distance < 20


def update_score():
    global score
    score += 1
    score_pen.clear()
    score_pen.write(f'Score: {score}', False, align='left',
                    font=('Courier', 14, 'normal'))


def move_snake():
    global game_ended
    snake_head.forward(snake_speed)
    if abs(snake_head.xcor()) > SCREEN_WIDTH/2 or abs(snake_head.ycor()) > SCREEN_HEIGHT/2:
        game_ended = True


def grow_snake():
    global snake_body
    new_segment = turtle.Turtle()
    new_segment.color('gray80')
    new_segment.shape('square')
    new_segment.penup()
    new_segment.speed(0)
    snake_body.append(new_segment)


def check_for_collision():
    if collide(snake_head, food):
        update_score()
        food.goto(random.randint(-SCREEN_WIDTH/2+50, SCREEN_WIDTH/2-50),
                  random.randint(-SCREEN_HEIGHT/2+50, SCREEN_HEIGHT/2-50))

        grow_snake()


def tick():
    global score, game_ended

    if game_ended:
        return

    move_snake()
    check_for_collision()

    window.update()  # maunall update the screen
    window.ontimer(tick, 10)  # update the screen every 10 milliseconds


def bind_keys():
    global window

    window.listen()  # make the window listen for key presses
    window.onkey(lambda: snake_head.setheading(180), 'Left')
    window.onkey(lambda: snake_head.setheading(0), 'Right')
    window.onkey(lambda: snake_head.setheading(90), 'Up')
    window.onkey(lambda: snake_head.setheading(270), 'Down')


# 1. Set up game window
setup_window()

# 2. Create game objects
create_snake_head()
create_food()
create_score()

# 3. Bind control keys
bind_keys()

# 5. Start game loop
window.ontimer(tick, 0)

window.mainloop()
