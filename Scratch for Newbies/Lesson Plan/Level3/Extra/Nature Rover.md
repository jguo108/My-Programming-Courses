# 3 Nature Rover

[Scratch coding projects for kids and teens | Nature rover (raspberrypi.org)](https://projects.raspberrypi.org/en/projects/nature-rover)

### Objectives

### Background

**Rovers** are robots. They can be used to carry out science experiments in remote places, like Mars! They examine their surroundings and they can be directed to interesting features and take samples. If they are solar powered, they can place themselves in a sunny position to recharge their batteries.

**Scrolling** is when graphics (or objects in your scene) move left, right, up, or down on a computer screen. Scrolling makes scenes look more realistic.

**Perspective** is used in computer graphics to make a scene more realistic. Objects that are far away normally appear to be smaller and higher up the screen. Objects that are close appear to be larger and lower down the screen.

**Layers** are like stacked sheets of clear plastic that you can draw images on. If an image on the top of the stack is covering the image below it, you will not be able to see the bottom image properly. Background images should be near the **back** layer. Images closer to the viewer should be near the **front** layer.

### Project

Create a wilderness scene for a nature rover to explore.

### What to learn

- Move sprites using perspective to give the appearance of distance
- Organize costume changes with `my blocks`
- Create a realistic scene using scrolling by cloning backdrop

### Blocks

- My Blocks
- Clone
- Scrolling

### Lesson Plan

| Step | Details |
| --- | --- |
| Control the Rover | * Each on screen arrow, when clicked, broadcasts “up”, “down”, “left”,  “right” message
* Rover broadcasts “Start” message when flag clicked
* When rover receives “up” message, change y by 10, change size by -1;  when rover receives “down” message, change y by -10, change size by 1(Perspective)
* Reset rover’s size, its position and move the the front after receiving “Start” message
* Set rover’s rotation style to left/right
* When rovers receives “Left”/”right” message, point in the correct direction
* Point in direction 90 at start |
| Scroll the background | * Place the “hill” sprite at back layer after receiving “Start”
* Clone the ”hill” sprite and move the original to the far right
* When ”Hill” and its clone receives “left”, change x by 3; when receives “right”, change x by -3
* Problem: When one background gets to the end, the screen is just white
* Solution: After creating the clone, broadcast “Scroll” message. In “Scroll” message handler, check if position is too far left/right and reset if needed |
| Scroll more sprite | * Add a tree sprite
* When receiving “Left”/”Right” message, move in opposite direction
* Problem: tree gets stuck when it reaches the edge of the screen
* Solution: Forever check its x position, if if position is too far left/right and reset if needed |
| Collect a Sample | * Create a “Sample Fruit” my block
* In “Sample Fruit”, go through “inactive”, “arm 1”, “arm2”, “arm 1”, “inactive” costumes with wait 0.3 seconds in between
* Also start a “Collect” sound in the middle
* When the rover is clicked, call “Sample Fruit”
* Create a new costume for the tree with some fruit on it
* In the tree sprite, when start, switch to “tree without fruit” costume
* When the tree sprite receives “sample fruit” message, switch costume to “tree with fruit”
* In “Sample Fruit” block, after extending the arm, broadcast message “sample fruit”
* We only call “Sample Fruit” block when the rover is touching the (color of the ) fruit
* When the tree is reset due to scrolling, switch its costume to “tree with fruit” |
| Create another sample | * In a similar fashion, at my blocks for other activities the rover can perform: sample air, sample soil, recharge, sample water, sample species
 |

### Further Exploration

- Add even more samples to your project, using the prebuilt animations or ones you create yourself
- Use variables to count samples; increase the count each time a sample is collected
- Introduce an energy variable so that the rover has to use a renewable energy source like the sun, to recharge
- Animate the rover when it has collected enough samples (for example, it could do a dance and then fly away)

### Exercise