# 10 Race to the Island

[Boat race | Web-browser, Scratch | Coding projects for kids and teens (raspberrypi.org)](https://projects.raspberrypi.org/en/projects/boat-race)

### Objectives

### Background

### Project

### What to learn

- game with a replay
- Game pattern of Setup and Run
- broadcast and broadcast and wait
- Countdown timer

### Block

- broadcast and wait

### Lesson Plan

| Step | Details |
| --- | --- |
| Introduction | * Previously, in games “[Find the bug](../Level1%2051869bb3a8274fd0910ceb115e2e8daf/5%20Find%20the%20Bug!%200233a4c8bcd445bdaed12ee36178701c.md)” and “[Keep it alive](9%20Keep%20it%20Alive%20254a7d3e5a3341baaeaf5ac7bbec6f41.md)”, you win the game by either spending the least amount of time to complete a task, such as finding all the hidden bugs or trying to stay in the game for as long as possible, such as keeping the dragon fly alive.
* Now, there is another kind of games where you need to complete the task within a given time. Once times is up, the game ends, and you lose. So today we are going to create such a game together.
* In the game, the player steers a boat using arrow keys to reach an island within a time limit. Of course, it’s no gonna be too easy: the boat has to avoid hitting the walls and the rotating gate. Also, there will be boosters along the way to help the boat move faster so do try to use them to get to the island quicker!
* Ok, enough talking, let’s get coding! |
| Backdrop (need to decide whether to draw it in class or provided as starting file) | * Create a race course |
| Gate | * Ok the map is done but there is one thing missing: if you take a look at the final game, there is a rotating gate just before the island to make the it even more challenging. So let add that first.
* Add a new sprite using “Paint” and name it “Gate”. Go the costume tab, rename the empty costume also to “Gate”. Ok, a gate is fairly simple, it is just a rectangle with the same color as the walls. So, select the rectangle tool from the toolbox, we don’t want any outline, so choose type in 0 here. Now for the color, we want it to be the same as the walls, so let’s use the color picker tool, go to the stage, find a wall and click. Now, the color is guaranteed to the same as the walls. Ok, we are now ready to draw a rectangle. You can adjust its width and height and then finally place it at the center.
* Ok, back to the code.  First, move the gate to the right place on the stage, so roughly here. When the program starts, go to this position. Now, we want it to rotate forever. Ok, first how do we make something rotate around its center? Yes, remember the rolling hedgehog in lesson “[Catch the school bus](../Level1%2051869bb3a8274fd0910ceb115e2e8daf/3%20Catch%20the%20School%20Bus%20fdbbff664179483cb3667e1a7c54dfd5.md)”, we make it rotate by using the “turn right” block. So to make the gate rotate around its center, all we need to do is just to turn it a small number of degrees each time. Here I choose one degree, but you can set it to any degree you like, the bigger the number, the faster the gate rotates, and the harder the game becomes. If we click the turn block again and again, you can see the gate starts rotating. Now to make it keep rotating, we use a “forever” loop and move the turn block inside the loop.
* Test. Now, once the game starts, the gate starts rotating. Perfect! Looks like our boat is going to have some real obstacle to overcome! |
| Boat (Basic move and direction control) | * Ok, we now have a maze where the boat needs to navigate through. So next let’s add the boat. Let’s first add the sprite using the Paint option and rename it to “Boat”. Right now, there is just one empty costume. I have prepared two boat costumes for you in this lesson’s Resource folder, one is called “boat normal” and the other one is called “boat shattered”. Let’s add both of them to the sprite and delete the empty one. Now, we the boat will initially have the normal costume, but once it crashed into the wall or the rotation gate, we are going to change it to the crashed costume.
* When the game starts, we want the boat to start somewhere here in the lower left corner and point straight up. So let’s use a “go to” block, this block already has its current x and y values, and then make it point to 0 degree. Remember, 0 degree is straight up. Finally, let’s switch its costume to “boat normal”.
* Test. Ok, the boat goes to the starting position and points straight up. Nice.
* Next, we want the boat to start moving. So add a “forever” block and inside the block let’s make the boat move 1 step each time.
* Test. Ok, the boat moves forward, goes through the wall and disappears into nothingness. Ouch! So we need to give the player some control of where the boat is heading. 
* Now, back in the “[Turtle Crossing](../Level1%2051869bb3a8274fd0910ceb115e2e8daf/6%20Turtle%20Crossing%202cdafea6327c41f4872354ffed1c4938.md)” lesson, we have a moving turtle and we change its direction by using the four arrow keys on the keyboard, right? But the control was pretty dramatic: it’s straight up, straight down, left or right, and there is no middle ground. So for example, I can’t make the turtle point up and slightly to the right. So here, we are just gonna use the left and right arrow keys to change the boat’s direction, but we want to change it a little bit each time you press the keys. So how can we do that?
* Ok, first, how do you check if a key has been pressed? Yes, the “when key pressed” hat block. There shouldn’t be any surprise as we have seen this block many times by now. Ok, so let’s have two of them, one for the left arrow key and the other for the right arrow key.
* Next, when the left arrow key is pressed, we want the boat to turn its direction slightly to the left and when the right arrow key is pressed, we want it to turn slightly to the right. Ok, no problem, we already know how to turn a sprite, right? When the left arrow is pressed, we use the “left turn” block to make the boat face slightly more to the left. Now, it up to you what degrees to use, the bigger the number the more dramatic the turn. So I will just use 15 degrees. When the right arrow key is pressed, we use the “right turn” block to make the boat face slightly more to the right.
* Test. Now, as the boat moves, I can pressed with the left or right arrow key to steer it. Awesome! |
| Boat (Countdown) | * Ok, now the boat moves as soon as we click the green flag. Ideally, we want to give the players some time to prepare themselves before the boat starts moving. So let’s add a 3, 2, 1, countdown.
* After positioning the boat and before the forever loop starts moving it, we use three “say” blocks to say “3”, “2”, “1’, each for one second. Then finally, let’s say “GO!!!!” for one second.
* Test.  3, 2, 1, go, now the boat only starts to move after the countdown. Cool. |
| Boat (Winning) | * Ok, so now there seems to be no restriction for our boat, it can go anywhere even through the walls. If this is the case, the game would be too easy! Also, as you can see, even if the boat reaches the island, it still keeps moving without stopping. If so, then how do we know we win the game?
* Ok, let’s address the winning problem first. What we want is that, as soon as the boat reaches the island, it should say something to let the player know that he/she has won. Well, how do we it has reached the island? Remember in the “[Turtle Crossing](../Level1%2051869bb3a8274fd0910ceb115e2e8daf/6%20Turtle%20Crossing%202cdafea6327c41f4872354ffed1c4938.md)” lesson, how do we know the turtle has reached the ocean? Yes, we check if it is touching the color of the ocean! So same trick here, we check if it is touching the color of the island and if so, we win! Now, since we are making decision again, it’s time for the “if then” block again. Let’s add one after the move in the forever loop. The condition to check is whether the boat is touching the color of the island, and this can be done with the “touching color block” and we use the color picker to select the exact color of the island. So essentially, after each move, we are checking “Have we won?”. If so, let’s say “YEAH!” for one second.
* Test. Now as soon as the boat touches the island, it says “YEAH!”. That’s good. 
* Problem: But what is not good is that the boat still keeping moving and the gate is still rotating. It seems like the game has not really ended. Ideally, when we win, we want every moving things in the game to stop. 
* Solution: Ok, the problem is easy to solve, all we need is just to add the “stop all” block after the “say” block to stop everything in the game.
* Test. Now when we win, every moving thing, the gate, the boat starts right away. Perfect! |
| Boat (Collision) | * Now, let’s turn our attention to the other problem, that is the boat can now sail though walls. 
* Well checking if the boat is touching the wall is very similar to checking if it is touching the island, we check need to check if it is touching the color of the wall, which is brownish color. So, after the “if then” block to check for winning, we add another “if then” block to check for collision. Add a “touching color” block to the “if then” block and select the wall color using its color picker. 
* Ok, now let’s think about what we should do if the boat crashes into a wall. Just like when it is winning, we can also say something like “Nooooo!” for one second, then, remember we have a second costume for the boat that looks like it’s been shattered, so let’s switch to that costume. For the time being, we just stop the whole game using the “stop all” block again.
* Test. So off we go, and let’s crash into the wall, Oh nooooo! The boat has been shattered. Cool! |
| Boat (Replay) | * Ok. So very often, when you play a game and lose, it does not exit completely, instead, it automatically restarts to give you a chance to try again. Ok, to be able to restart, obviously we cannot stop everything, so let’s delete the “stop all” block. Now, let’s think about what we did to prepare the boat when the game starts: we move it to a start position, point straight up, switch to normal costume and count down from three, right? If we replay the game, do you think we need to do these preparation again? Yes, definitely! Because whenever you replay, everything should start the same. So after saying nooooo, so again move it to the same position, point straight up, switch to normal costume and count down from three.
* Test. Ok, so after the boat crashes into the wall and says noooo…, it goes straight back to the same start position and counting down again. Now you can play the game again and again, until you are bored with it. Nice! |
| Boat (Game structure) | * Ok, now we have quite some code, and before we add more, I would like take a small detour and talk about game structure. Now so far in this game, we can clearly see that each game play is divided into two phases: phase one is what I call the “Setup Phase”. Here, you do all the preparation work for each sprite, such as moving them to the right position, switching to the start costume etc etc. We have seen such phase for the boat when the green flag is clicked and when game restarts after a collision. The second phase is what I called the “Run Phase”, this where you actually use the forever loop to run the game, so the sprites move, different conditions are checked, key presses are received etc etc.  So when you create a game, it’s always a good idea to keep this two-phase structure in mind and write your code following this structure. Ok, you might say “All right, I get the idea, but how?” Let’s take a look.
* Now this block of code here is doing the preparation, right? And it is exactly the same as the block of code at the beginning of the program after the flag is clicked. They both belong to the “Setup Phase”. Now if we can send a message to the boat and say “Hey, set yourself up”, then we can send this message both at the beginning and when collision happens. Ok, so far so good? Now the question becomes, who is going to send this message? In previous lessons, we have seen message being sent using broadcast from one sprite to a different sprite, right? But no one says you cannot broadcast a message to yourself! So how about we let the boat broadcast a setup message and at the same time receives that same message do setup itself up? Let’s give it a try!
* Now, let’s move all these setup code at beginning out and put them aside. By the way if now put these two blocks of code side by side, you see even more clearly that they are exactly the same. Ok, after moving those code out, let’s add a “broadcast” block to broadcast a “Setup” message. And what should the boat do when it receives the “Setup” message? Yes, it does what this block of code does, well, setting things up.
* Test. Ok, the boat does do all the setup work: it starts at the right position, faces the right direction and counts down. Cool.
* Problem:  but what is not so cool is that it starts moving before the count down finishes. Do you know why? Any idea? So let’s put the these two scripts side by side and see what actually happens. Now, when green flag click, the program starts and it broadcasts a “Setup” message. Now when the boat itself receives this message, it is going to set things up. Now it is very important here, while the boat is run this script to setup, the green flag script here are stopping to wait for the setup. Instead, it keeps running the code after the broadcast, which is the forever loop. And what does the forever loop does? It moves the boat. So what you have is on one side, the boat is moving, on the other side, it is setting things up, including the count down, both are going on at the same time. And that’s why the boat is moving while counting down. Imagine a real life example, you and your friend walk into McDonald to order some burgers. In one scenario, your friend sits at the table and you walk to the counter to place the order. Once the staff starts to prepare your burgers, you return to the table and chat with your friends. You only go back to the counter once the burgers are ready. In different scenario, instead of returning to the table, you just wait at the counter, doing nothing until the burgers are ready. Then you return the to table, chat with your friend and starting eating. 
* Solution: So to apply the second scenario to our game here, the boat should wait for the setup to finish before it starts moving. Back in the lesson “[Knock Knock](7%20Knock,%20Knock!%20792cb37ab00a409d8b7aea90cd59ddab.md)” when we first introduced the “broadcast” block, I asked you to experiment with the “broadcast and wait” block on your own. Now, time to use that block! With this, a sprite broadcasts a message, but instead of moving on right away, it waits for whoever receiving this message to complete their work before continuing. Ok, let’s use the “broadcast and wait” block instead here. 
* Test. YEAH! The boat now waits for the setup, including the count down, to complete before it starts moving. Awesome!
* Now, here comes another benefit of creating the “Setup phase”: before that, we have all these blocks to prepare the boat again once it crashes into a wall. But now since the boat is ready to receive the “Setup” message to do all the preparation work, when it crashes, we can just broadcast message “Setup” and wait. So we can delete all of the blocks here. In lesson “Keep it alive”, when we replaced the “if then else” block by a simpler “if block”, I said that when it comes to coding, less is better. Same here, less code is better code.
* Test. Ok the boat starts moving, and let’s crash it. Now, back to the start position and count down again, and off we go! Perfect!
* Ok, so we have finished the “Setup” phase. Now, after that, there is a “Run” phase where you run the game. So which part do you think belongs to the “Run” phase? Yes, this forever loop here. Because all the interesting things happen inside this loop. You have seen how we created the “Setup” phase, can you try to use broadcast to create the “Run” phase? Let’s have a 5 mins break and see if you can figure this out! OK time’s up, let’s take a look. First we separate the forever loop from the reset, then we broadcast a message “Run”. Finally, we add a “When I received Run” hat block and join the forever loop under it. So after the setup, the boat sends out a message “Run” and then itself receives this message, it starts the loop that does everything, including moving the boat, checking for winning and crashing. 
* Test. Ok, count down, and off we go! Ok, after this change, everything works as before! Nice! Notice that when the program runs, this script is highlighted with a yellow outline, meaning it is running and not the when green flag click script here. Because this script finishes after broadcasting the “Run” message.  
* OK, after learning why we need to use “broadcast and wait” for the “Setup” message, some of you might be wondering why don’t we need to use “broadcast and wait” for the “Run” message. Any one has any idea? OK, these are all very good answers. So actually, it probably doesn’t matter that much which broadcast block you use here, because there is no other blocks to run after the broadcast. Just for fun, let’s add a say block after the broadcast, “I’m on my way!”. Now there is a block after the broadcast, and do you think whether we wait or not matters now? Let’s try.
* Test. Now as soon as the count down finishes and the boats starts to move, it says “I’m on my way”. Cool, no problem.
* Now let’s change this broadcast to “broadcast and wait” and see what happens now!
* Test. 3, 2, 1 and off we go… hmmm… the boat never says “I’m on my way!” Why? Can any one have a guess? If take a look at the code when the program runs, now you would see that both of these script are highlighted, meaning both them are running. OK, of course, the forever loop is definitely running, no problem with that? But why in this case, this script is also running? Any idea? Yes, it’s because after broadcasting the “Run” message, it waits for whoever receives that message to complete before it can continue next to say “I’m on my way!”. In this, it is the boat itself who receives the “Run” message and execute the forever loop. Now, let me ask you a question, do you think this forever loop will ever finish? No, because that’s why it is called a “forever” loop, it never finishes and just loops round and round. Now, if this is no gonna finished, then our “broadcast and wait” block will just patiently sits here waits forever! That’s why it looks like this script is running, because it is waiting for someone else to finish. And because it waits forever, the boat never have a chance to run the say block! Of course, this is just to demonstrate the difference between the “broadcast” block and “broadcast and wait” block, we don’t really need the boat to say anything once it starts moving, so let’s delete the say block and change this back to just “broadcast” |
| Boat (Booster) | * Ok, that was quite a detour. Now let’s come back to the game itself. When drawing the map, we have added several “Boosters”, all these little triangles. The purpose of these boosters is to make the boat go faster once it sails over them. So let’s add that to the game!
* All we need to do is just to check if the boat is touching the booster, and if so, let’s move it 3 steps instead of 1. So in the forever loop, add an “if then” block, for the condition, use a “touching color” block and use the color picker to select the color of the booster. If the boat is touching the booster, let’s move it 3 steps.
* Test. Off we go, now let’s try the booster, wow, the boat moves a lot quicker and this saves us time. Nice! |
| Time limit | * Ok, we can now play game and try our best not to crash the boat before reaching the island. However, the game is still a little bit too easy. Now there a lot games out there that require you to complete a task within a certain amount of time. In other words, you have limited time to complete the task, otherwise, you lose. So let’s next look at how to add some time pressure for our players.
* For that, we need a “Count down timer”. If you have ever watched a rocket launch, there is always a timer counting down from 10 and once it reaches 0, the rocket is lifted off from the ground. Here, we are going to add a similar timer. If we want to give the player one minute or 60 seconds to play the game, the timer starts at 60, then it goes down by one every second, and once it becomes 0 before the player reaches the island, instead of lifting off a rocket, the game ends and we lose. 
* Ok, here we a something whose value decreases as time goes by…hmmm…I think I have seen something similar in a previous lesson? Can you recall what that is? Yes! It’s the energy level of our dragonfly in the the “[Keep it alive](9%20Keep%20it%20Alive%20254a7d3e5a3341baaeaf5ac7bbec6f41.md)” lesson: we keep decreasing the energy level by one for every second that passes and if it drops to 0, the dragonfly is dead and the game ends. So very similar to what we want to do here: we keep decreasing the timer by one for every second that passes and if it drops to 0, time is up and the game ends.
* Ok, just like the case of energy level, we add the count down timer code to the Stage itself. To keep track of the number of time left, we create a new variable called “time left”. 
Now, when flag is clicked, we first set time left to 60 seconds using the “set variable to” block, that’s all the time a player has to navigate the boat to the island. OK, now we want to keep decreasing “time left” by one every second until it become 0. So we want to repeatedly do something until some condition is true. Does that suggest what block to use? Yes, the “repeat until” block. So let’s add that after setting the “time left” variable. Ok, we repeat until there is not more time left, so what do you think the condition should be? When can we say that there is no time left? Yes, when “time left” is equal to 0. And how to we check if “time left” is 0? Yes, we can use the “equal” block in the Operators category. So let’s ad “time left” variable to the left and type in 0 on the right. And let’s add this “equal” block to the “repeat until” block. Ok, so we repeat until no more time is left, when this is the case, this repeat loop completes, and we just stop the game by adding the “stop all” block after it. Ok, now what do we need to do inside the loop? Well, when there is still time left, we decrease “time left” by 1, which is the same as changing it by -1, then we wait for 1 second.
* Test. Let’s test this. But before that, in order to not wait for 60 seconds before time runs out, let’s set “time left” to 10 so that test can be quicker. Now as soon as we click the flag, notice the “time left” variable on the top left corner, it starts to count down. Ok, the boat moves, and …. time is up, everything stops. 
* Problem: Let’s start the game again, now WATCH when the boat is counting down from 3. While it is doing that, the time at upper left corner also starts ticking. So when the boat finally moves,  the time left is just 6 seconds instead of the 10 seconds we set at the beginning. I think that is a bit unfair to the player. Ideally, “time left” should only start ticking after the “Setup” phase has completed. 
* Solution: Ok, let’s go back to the boat, it finishes all the setup after this “say GO!!” block, right? So THIS IS when we should tell the stage to start the timer. So far we have been using broadcast to send messages between sprites. But this can also be used to send messages between sprite and the stage, after all, a stage can be viewed as a special sprite. So we can broadcast a message “Start timer” after this “say” block to let the stage know. Now back to the stage, instead of starting the timer when flag is clicked, it now starts it when it receives the “Start timer” message. 
* Test. Now, the timer only starts counting down from 60 after the boat has finished saying 3, 2, 1, Go. And if we crash the boat, it goes back to the start position, and again  the timer only starts counting down from 60 after the boats has finished saying 3, 2, 1, Go. So this works both when we start the game and when we replay it. Nice! |
| Small bug? | * The timer still counts down when the boat crashes, and this continues when the boat starts again before it moves. So do we need to address that? |

### Further Exploration

- Can you add more obstacles to your game? For example, you could add green slime to your backdrop and make changes to the code so that the slime slows the boat down when the player lets them touch.
- You could add a moving obstacle, for example a log or a shark!

![https://projects-static.raspberrypi.org/projects/boat-race/224753f5c55d0bd88106b93d0afb7b6d39fb98af/en/images/boat-obstacles.png](https://projects-static.raspberrypi.org/projects/boat-race/224753f5c55d0bd88106b93d0afb7b6d39fb98af/en/images/boat-obstacles.png)

- Can you turn your game into a race between two players? The second player will need to control their boat using the up arrow to move forward and the left and right arrow keys to turn.
- Can you create more levels by adding different backdrops, and can you then allow the player to choose between levels?

- The player can only restart for 3 times
- Can you make the wall, booster and island all sprites?
- What are the other ways to make your game even more challenging?