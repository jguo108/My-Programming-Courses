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

window = turtle.Screen()

square = turtle.Turtle()
circle = turtle.Turtle()

square.shape('square')
circle.shape('circle')
print(f'square: {square.shapesize()}')
print(f'circle: {circle.shapesize()}')

window.mainloop()
