# Turtle Race (Simulation)

### Reference

[Turtle Race! | Python | Coding projects for kids and teens (raspberrypi.org)](https://projects.raspberrypi.org/en/projects/turtle-race)

[Python Beginner Project Tutorial - Turtle Racing! (youtube.com)](https://www.youtube.com/watch?v=gQP0geNsO4A)

### Code

https://replit.com/@chairmanguo/4-Turtle-Race

### Key Points

- Turtle Module
    - Setting up screen and keep it running (’mainloop’)
    - Coordinate system and direction
    - Create a turtle
    - Basic operations (’shape’, ‘color’, ‘goto’, ‘forward’, ‘penup’, ‘pendown’, ‘left’, ‘right’, ‘turn’ ‘write’, ‘hideturtle’, ‘xcor’, ‘ycor’)
- Loop
    - “for” loop

| Steps | Note |
| --- | --- |
| Introduction |  |
| Outline | * Basic Turtle program setup: import, get screen, setup screen size (explain coordinate system), screen main loop.
* Create a turtle. Show basic moves: forward, backward, turn. Use that to show how to draw a square. Show different speeds. Finally delete the square code.
* Create 4 lanes by drawing 5 horizontal lines. Show the importance of using “penup” and “pendown”. Draw each line by moving forward, then backward, then turn right then forward and finally turn left. Do this for 5 times. And finally save work by using for loop
* Write numbers for each lane. 
* Hide turtle at the end.
* Create 4 turtles with different color and place each at the start position of each lane. 
* Pack the turtle creation code into function “create_turtle”, explain parameters and return value.
* Pack the code earlier into function “draw_track”
* Start the race using a “while True” loop, each turtle moves a random number of steps each iteration. When ever one turtle reaches the finishing line, break the loop.
* Make the turtle celebrate the win by making a full turn. Pack the celebrate code into a function “celebrate” |