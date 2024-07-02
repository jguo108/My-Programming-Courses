# https://scratch.mit.edu/projects/274837412/editor/
# https://pickcoloronline.com/

import turtle

PIXEL_SIZE = 50
HEAD_X_PIXELS = 8
HEAD_Y_PIXELS = 8

HEAD_WIDTH = PIXEL_SIZE * HEAD_X_PIXELS
HEAD_HEIGHT = PIXEL_SIZE * HEAD_Y_PIXELS

SCREEN_WIDTH = 700
SCREEN_HEITGH = 700


def draw_pixel(x, y, size, color):
    global pen
    pen.up()
    pen.goto(x, y)
    pen.down()
    pen.fillcolor(color)
    pen.pencolor(color)
    pen.begin_fill()
    for i in range(4):
        pen.forward(size)
        pen.right(90)
    pen.end_fill()


window = turtle.Screen()
window.bgcolor('Gray30')
window.title('Steve')
window.setup(SCREEN_WIDTH, SCREEN_HEITGH)
window.tracer(0)

pen = turtle.Turtle()  # create a Turtle and it always start at (0, 0)
pen.shape("turtle")
# pen.speed(0)
pen.hideturtle()

head = [
    ['#2f200d', '#2d2315', '#312417', '#312417',
        '#271e11', '#292013', '#2d2315', '#2c2215'],
    ['#2d2315', '#2d2315', '#2d2315', '#342819',
        '#412d1a', '#3f2d1c', '#2e2316', '#2b2114'],
    ['#2d2315', '#af866c', '#b68b72', '#bf9380',
        '#b68872', '#b68b74', '#a4745b', '#35291a'],
    ['#a37b67', '#ad826d', '#a37b67', '#a67e6d',
        '#96705d', '#b48672', '#95674e', '#95674e'],
    ['#ad826d', '#ffffff', '#5141a3', '#ad7867',
        '#b48672', '#5141a3', '#ffffff', '#a37b67'],
    ['#946149', '#ab7863', '#b07f72', '#654134',
        '#654134', '#b6856c', '#9a684a', '#7a5238'],
    ['#895d46', '#8f5e43', '#402515', '#834b40',
        '#834b40', '#432616', '#885d41', '#7b523c'],
    ['#6a4531', '#68442f', '#402515', '#412113',
        '#432616', '#432616', '#7d543e', '#744e37'],
]

count = 0
current_x = -(HEAD_WIDTH / 2)
current_y = HEAD_HEIGHT / 2
for r in range(HEAD_Y_PIXELS):
    for c in range(HEAD_X_PIXELS):
        draw_pixel(current_x, current_y, PIXEL_SIZE, head[r][c])
        current_x += PIXEL_SIZE
        count += 1
    current_x = -(HEAD_WIDTH / 2)
    current_y -= PIXEL_SIZE

pen.up()

window.mainloop()
