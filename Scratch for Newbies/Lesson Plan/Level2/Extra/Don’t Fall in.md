# 5 Don’t Fall in!

[Scratch coding projects for kids and teens | Don't fall in (raspberrypi.org)](https://projects.raspberrypi.org/en/projects/dont-fall-in)

[Baby bird on Scratch (mit.edu)](https://scratch.mit.edu/projects/525236983/editor/)

### Objectives

### Background

### Project

### What to learn

- Detecting key press
- Start and stop pattern

### Lesson Plan

| Step | Details |
| --- | --- |
| Setting up the Scene | * Add start, end platform and a top-down view of a sprite |
| Jump to end | * When flag clicked, go to start platform and other setting up code
* Broadcast “Start”
* Introduce detecting key press
* If space key is pressed, make character jump
* Two stage jump: first stage becomes bigger, second stage become smaller
* Forget to add the forever loop, add it now
* Test
* Add another “Start” message handler. Forever, if touching “End” color, go to “End” and stop all
* Problem: We are touching “End” in the air but still goes to “End” with a big size
* Solution: Make sure we only check if touching “End” when we are on the ground: 1) Set size back to 25 at the start 2) Add an “On the Ground” flag
* Test |
| Moving  Platform | * When flag clicked, go  to start position, point in direction 90, forever move 4 steps, if on edge bounce
* Problem: Move left and right
* Solution: change initial direction to 0
* Same code for Platform2 and Platform3 |
| Jump onto platform | * If touching “Platform X”, go to Platform X |
| Fall | * If fall (touching yellow), stop all |
| Refinement | * Start“Drum Boing” sound when space is pressed
* Play “Tada” sound when reaching the end
* Play sound “Squish Pop”
* Problem: When we fall, we can still press space and jump again
* Solution: Stop other scripts in sprite
* Problem: After playing “Squish Pop” sound, other platforms still move
* Solution: Stop all after the sound.
* Hide character before Stop All |

### Further Exploration

### Exercise