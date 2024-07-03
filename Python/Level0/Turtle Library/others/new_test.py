import turtle

# Create a turtle
t = turtle.Turtle()

# Set the shape of the turtle to a square
t.shape("square")

# Set the size of the square to 30 pixels
t.shapesize(30 / turtle.turtlesize()[1])

# Move the turtle to the center of the screen
t.penup()
t.goto(0, 0)
t.pendown()

# Draw the square
t.forward(30)
t.right(90)
t.forward(30)
t.right(90)
t.forward(30)
t.right(90)
t.forward(30)
t.right(90)
t.forward(30)
