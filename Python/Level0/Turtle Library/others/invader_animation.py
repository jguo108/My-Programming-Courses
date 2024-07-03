# https://www.youtube.com/watch?v=mIQR6GUxZZI&list=PLlEgNdBJEO-n9U_OcG2-KT_l2ncrJWPzc

import turtle
import time


def run():
    player.forward(5)
    window.update()
    window.ontimer(run, 1)


window = turtle.Screen()
window.title('Animation Demo')
window.bgcolor('black')

# Register shapes
turtle.register_shape('Resources\invader1.gif')
turtle.register_shape('Resources\invader2.gif')

player = turtle.Turtle()
player.shape('Resources\invader1.gif')
player.shapesize(8, 8)
player.color('chartreuse3')
player.frame = 0

'''
# !!! This approache stops the whole program each time we sleep !!!
def animate():
    player.shape('square')
    time.sleep(0.5)
    player.shape('circle')
    time.sleep(0.5)


while True:
    print('main loop')
    animate()
'''


def animate():
    '''
    if player.shape() == 'Resources\invader1.gif':
        player.shape('Resources\invader2.gif')
    else:
        player.shape('Resources\invader1.gif')
    '''

    if player.frame == 0:
        player.shape('Resources\invader2.gif')
        player.frame = 1
    else:
        player.shape('Resources\invader1.gif')
        player.frame = 0

    window.ontimer(animate, 10)


animate()

# while True:
#    window.update()

window.mainloop()
