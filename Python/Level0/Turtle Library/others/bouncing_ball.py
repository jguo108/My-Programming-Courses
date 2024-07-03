# https://www.youtube.com/watch?v=HHQV3ifJopo&list=PLlEgNdBJEO-mRsbxRND_Cu805SCrXoOZB

import turtle

window = turtle.Screen()
window.bgcolor('black')
window.title('Bouncing Ball')
# window.setup(800, 600)

ball = turtle.Turtle()
ball.shape('circle')
ball.color('green')
ball.penup()
ball.speed(0)  # make animation as fast as possible
ball.goto(0, 200)

ball.dy = -2

while True:
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() < -400:
        ball.dy *= -1


window.mainloop()
