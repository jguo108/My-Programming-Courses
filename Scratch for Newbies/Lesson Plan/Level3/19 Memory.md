# 6 Memory

### Reference

[Memory | Web-browser, Scratch | Coding projects for kids and teens (raspberrypi.org)](https://projects.raspberrypi.org/en/projects/memory)

[Creating a Memory Game in Scratch using LISTS and VARIABLES with SOUNDS (youtube.com)](https://www.youtube.com/watch?v=gK17t1as5K4)

### Objectives

### Background

### Project

### What to learn

### Lesson Plan

| Step | Details |
| --- | --- |
| Introduction to all sprites | * We have four fish, each one can play a Note
* We have four letters, each one represent a Note and will be played by each corresponding
* We have a crab who gives instructions |
| Crab | * When flag clicked, say “Watch and listen to the tune played. Try to repeat it!”
* After that we need to play a tune. A tune is composed of a sequence of individual notes. * How do you play a note?  |
| Music Extension | * Add the Music extension.
* In the extension, there is a “play note” block. Here, you can choose the note you want to play and the beats. You can think of the beats as how long you want the note the play.
* For example, we choose the note C, which has a numerical value of 62, and the beats 1.
* Test and hear it.
* Now let’s change the beats to 5, listen again and you can hear that the note plays for much longer
* That’s pretty much it! Back to the crab! |
| Play Tune | * Each fish can play a specific note, for example the yellow can play the note D, as you can see, we name it “Fish D”, same for the other three fish.
* Now the crab is like a conductor, who has a tune in mind, and is going to tell the fish to play it.
* Ok, let’s first look at what a tune is, it is just a sequence of notes, one after the other. Does that sound familiar? Yes! a tune is a list of notes! 
* So Let’s create a list ‘Tune’. And we want to add notes to the Tune. For this simple project, we only have four notes, D, E, F and G. So let’s make a very simple tune by adding D, E, F, and G to our Tune list. Also, it’s always a good idea to clear each list at the beginning.
* Once we have the tune, the crab needs to go through each note in the tune and tells the right fish to play it.
* We have seem many examples before about do you go through all the items in a list. So let’s do it again here.
* Create a variable ‘i’, repeat ‘length of Tune’ times, each time, the note will be played is ‘item i of Tune’. Now, how can we tell the fish that can play this note? Well, how do you tell a different sprite to do something in Scratch? Yes, broadcast! So we broadcast the note. And finally, we increase i by 1.
* Test. Nothing happens, because our fish have not response to the broadcasted message.
* Go to Fish D, when it receives message ‘d’, pay the Note D for 1 beat. If we clicked the note box, we can select the note D and it turns out to be number 62
* Test. Now we can hear the Note D being played
* Let’s add the code to the other fish.
* Test.
* Problem: Well now it seems that we have all the notes being played at the same time and it just got all mixed up. Why?
* Solution: This because the crab broadcast all the notes very quickly one after the other. And each fish, as soon as it receives the message, it starts to play the note. So, all the notes are being played at about the same time. What we really want is to have each fish wait until the previous fish has finished playing its note. Remember when we first introduced broadcast blocks, we notice that there is a variant of that block, and that is ‘broadcast and wait’ and I said that we will need that later. And now is later. What this block does is that, it broadcasts a message, but unlike the broadcast blocks, it actually waits until the the receiver has finished whatever action it will take to respond to the message before it continues with the rest of the program. It’s like you and your have just finish dinner and want to play some video game afterwards. But before the fun time, you tell your friend to do the dish washing first. In the cast of broadcast, you tell your friend to wash, and you start playing game right way without waiting for him. In contrast, you can tell your friend to wash and then you wait until he finishes before you two can start playing the games together. And this is the ‘broadcast and wait’ case. So to solve our problem here, all we need to do is to change the ‘broadcast’ to ‘broadcast and wait’
* Test. Problem Solved! |
| Letter Animation | * Now, the tune plays well and it’s good. What is not so good is, at the beginning, the crab says ‘’Watch and listen to the tuned played‘, well, right now, we can only hear the tune and not be able to see the the notes that have been played. And this is not very useful if you want the player to repeat the tune, right? So let’s add some animate to make it clear which note is being played.
* You can use any animation you want. For example, make the fish that’s playing the note to shake a little bit or make it become bigger. Doesn’t matter as long as you give the player some clear indication of which note is being played. As you can see from the demo at the beginning of this lesson, the animation we use is to have a letter that represents the note being played float above its fish and gradually disappear. That’s why we have four letter sprites here. Let’s see how that can be done.
* Let’s first look at letter D. Because this is the note that Fish D can play, when green flag clicked, we make it go to fish D. Now, we only play this animation when the fish actually plays the note. So, when does the fish play the note? Yes, when it receives the message ‘d’! So same with the letter here, when it receives message ‘d’. To play animation, we want it to be completely visible at the beginning, and and slowly fade away. How can we achieve this graphic effect. Yes! We can use the GHOST effect. Remember that ghost effect of 0 meaning no effect at all, so the sprite is completely visible; ghost effect of 100 meaning in full effect, so the sprite is completely invisible.
* So when receive the message, we set the ghost effect to 0 first. then set the size to 20% and go to Fish D. Then we repeat 50 times, each time we make the letter floats up a little bit by changing its y position by 2 and also makes it fade a little bit by change the ghost effect by 2. Note that because we repeat 50 times and each time increase the ghost effect by 2, so by the end the loop, ghost effect will become 100, meaning the letter will be completely invisible at the end, which is exactly what we want.
* Test. We can clearly see which note is being played, in this case, Note D
* Let's repeat that for the other three letters
* Test. Very cool! |
| Player test (clicking fish) | * Now the the tune has been played, it’s time to test the player’s memory! The player needs to replay the tune by clicking the fish in the correct order. So example, our tune is D, E, F, G, the players needs to click the fish D, E, F, G.
* But before that, let’s first do some cleanup. Remember custom blocks can be used to better organize your code and make it clearer.
* So far, all the code after the crab says “Watch”… is essentially doing one thing, and that is the play the tune. So, let’s create a custom block name ‘Play Tune’ and we move all the code under it, and then call ‘Play Tune’ instead.
* Test. Always remember to test your code again when you make some significant changes to make sure that you have not break the program.
* Then the crab is going to challenge the player by saying “Now, it’s your turn!”
* Challenge accepted! Now the player is going to recall very hard about the order of the notes that has just been played and click the fish in that order.
* We want to things to happen when the player clicks a fish: 1) we play the note again with the animation; 2) We need to check is this the right note, if not, the player loses and the game ended. The first one is easier so let’s tackle it first.
* In the Fish D sprite, when this sprite is clicked, all we need to do is to just broadcast the message d. This is because when the fish receives d, it will play the note and when the letter D receives message d, it will play the animation. And these two combined is exactly what we want when the fish is clicked.
* Test and click Fish D
* Repeat this for the other three fish
* Test. Looks good, we can click all the fish.
* Problem: but there is a small problem: when the tune is first being played, meaning it’s not the player’s turn yet, we can still clicked the fish and play the note.
* Solution: if you think about it, the game has two phases, the first one is to play the tune, and the second phase is when the player actually test his/her memory. So what we want is that when the game is in the first phase, we do not want the player to be able to click any of the fish. If you recall from the Supermarket example, once the customer is checking out, we do not want the customer to be able to click any of the product, very similar case here. In the supermarket example, we use a flag variable to indicate whether the customer is checking out or not. Here we also use a variable to indicate whether the game is in phase one, meaning playing the tune or in phase two, meaning testing the player. So we create a variable ‘mode’, note that this needs to be for all sprites because other sprites need it too. The ‘mode’ can be one of two: ‘play’ or ‘test’. When we play tune, set mode to ‘play’, after the crab says ’Now it’s your turn’, we set mode to ‘test’. Now, when each fish is clicked, we only broadcast the note message if ‘mode’ is ‘test’.
* Test. Problem solved! |
| Player test (check correctness) | * Ok, so now the player can try to replay the tune by clicking the fish in the right order. Let’s look at the second more challenging problem: that is how to check if the player is right or not.
* Now let think about it. The tune is D E F G, meaning that if the player wants to win, the first note he/she clicks needs to be D, the second needs to be E, the third needs to be F and the last needs to be G. The be able to check if the order player clicks in a correct, each time player clicks a note, the crab needs to know two things: 1) what note is that? 2) is it the first, second, third, or fourth note the player has clicked.
* The first thing is easy, when a fish is clicked it just needs to broadcast a message to let the crab knows that Note D has been played. Well, guess what, we already have that message, it’s message ‘d’ and it gets broadcasted when Fish D is clicked. So there is nothing that needs to be done here.
* Back to the crab sprite, when it receives message ‘d’ we want it to check if this is the correct note being played in the right order. But before we move on, note that crab should only check that when we are in the second phase of the game when the player is testing his/her [memory](http://memory.so) (use if mode = test)
* Now the crab knows what note has been clicked, how to know whether it is the first, second, third, or fourth note? Well, we can use a variable to keep track of this number, let’s called it ’note number‘, this variable must be ‘for all sprites’.
* When the program starts, we set ‘note number ’ to 0 because no fish has been clicked yet.
* Whenever a fish is clicked, we increase ‘note number’ by 1 before broadcasting the note message. This is done for all fish
* Test. As we can see, when we click the first fish, ‘note number’ is 1, second fish, ‘note number’ is 2; third fish, ‘note number’ is 3; fourth fish, ‘note number’ is 4;
* Now, you might be wondering what is this ‘note number’ good for? Well, when a fish gets clicked, we can use this number as an index to find the item in the Tune list. And if this item is the same as the note that has just been clicked, we know that the player has played the right note, otherwise, the player got it wrong. Ok, let’s look at how the code can be written. Back to the crab sprite.  When it receives message ‘d’ and the mode is ‘test’, if item ‘note number’ of the ‘Tune’ list is actually ‘d’, that means the player click the right fish. Now if this is the last note player has clicked, he/she wins the game. How do we check if this is the last note clicked? We there are 4 notes in the Tune list, and if ‘note number’ is 4, then we know it is the last note. So if ‘note number’ equals ‘length of Tune’, we play a winning sound and say “Well done!”. If the player got it wrong, we play a losing sound and say “Game over!”. 
* Now we have to write the same code for the other three notes, but change the message received and the message being compared.
* Test. Both failed and succeed. |
| Refactor | * Now before we move on. Let’s look at the current code and see if we can make it more organized.
* One very obvious problem is that, these four ‘when i received’ code scripts look almost identical except the actual note that is being compared in the if block. We have already learnt that custom blocks can be use to reduce such code repetition and it is already a good idea to make your code less repetitive. So let’s give it try.
* Create a custom block ‘Check Note’ , move all these code under ‘Check Note’, and when I received a note message, just call ‘Check Note’ instead. We can do this for the other three notes. Wow, look how much code blocks we have deleted and how much cleaner the code becomes.
* But it too early to celebrate. Can anybody spot a problem? Yes, ‘Check Note’ always checks note ‘d’. But we need to check for ‘e’, ‘f’ and ‘g’ as well.
* Now, let edit ‘Check Note’. Here, can you see that you can actually add an input to the custom block. An input is just a number or some text that you pass to the custom block when you call it. And inside that custom block, you can use that input. So in this case, we want to pass the actual note. So let’s add an input and name it ‘note’. After that, you will notice that when ‘Check Note’ is called, there is an extra bubble here where you can pass in a note. Also, in the define ‘Check Note’, there is our input ‘note’ that you can use. We want to use it in the if block comparison, so let’s drag it to replace the node ‘d’. When we call ‘Check Note’, we pass note d, e, f, and g respectively. 
* Test. Both the successful and failed case. |
| Small bug (should we mention that?) | * There is a small bug: when you win or lose and saying the words, you can still click the fish and make it play the note. This messes things up a little bit. |
| Level and Score | * Now the game can only be played once. But what we want is that, if the player gets the tune right, we will start again. 
* So in ‘Check Note’, if the player wins, we broadcast a message ‘Start’.
* Now, when green flag clicked, we also broadcast a message ‘Start’
* When the crab receives ‘Start’ message, it begins the actual game
* Test and win, and see the game start again.
* Now, it is a bit boring and too easy that the game always play the same tune again and again. Also, we the player keep winning, the game should also become more difficult. So for example, it starts with a tune of just one note. And if the player wins, the tune becomes two notes, and so on and so forth. Until the tune become so long that the player eventually fails. 
* Ok, so we create a variable ‘Level’ and set it to 1 when the program starts. And in ‘Check Note’, if the player wins, we increase ‘Level’ by 1.
* Test. As we win more and more, level becomes bigger and bigger.
* But right now, the game is still the same as before, each time the tune is still four notes. Let’s see how we can make the game more and more difficult.
* Let’s take a look at the ‘Play Tune’ custom block. This is where we create the Tune list. Right now, we add the same four notes d, e, f, g in the same order to the list everytime. What would be nice is to make the list longer and longer as level become higher. 
* Now, instead of adding the notes one after the other, we use a repeat loop, and the number we repeats is just ‘level’, in the loop we add ‘things’ to Tune. Now, if level is 1, we add 1 thing to Tune, if level is 2 we add 2 things to Tune so on and so forth.
* Well, obviously, we do not want to add ‘thing’ to Tune, we want to add one of those four notes to Tune.
* But which note? Well I don’t care. We can just randomly choose any one of those four notes and add it to the tune list. 
* Pay attention to what I have just said “We can just randomly choose any one of those four notes and add it to the tune list”.  So what are the four notes we have? Yes, d, e, f, g. What if we put them in a bag and then randomly pick one from the bag and put it into the tune list? That sounds like a good idea. 
* What can we use for that ‘bag’? Well, another list. Let’s called it “All Notes”. When the program starts, we first clear the bag and put all the fours notes into this bag. Now we have all the notes in the bag, all we need to do here is just to randomly pick one and put it into our Tune list.
* How do we pick random item from a list? Well, all items in the list are numbered from 1 to N, where N is the same as the length of the list. So we can just pick a random number from 1 to N and use that as an index to get the list item. So, here, use the ‘item of all notes’, and for the index, we use a random number that is between 1 and the length of ‘all notes’ |
| Final Test | * Final test and make Tune list visible to see that it starts with one note and gets longer and longer. Also the notes in the list are randomly generated. |

### Further Exploration

### Exercise