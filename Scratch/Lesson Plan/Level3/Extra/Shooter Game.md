# 4 Shooter Game

[Spaceship Adventure Game on Scratch (mit.edu)](https://scratch.mit.edu/projects/510916536/)

[Clone wars | Web-browser, Scratch | Coding projects for kids and teens (raspberrypi.org)](https://projects.raspberrypi.org/en/projects/clone-wars)

## **Scratch Shooting Game: Bug Zapper!**

This project will be a fun and engaging shooting game that utilizes lists, clones, and custom blocks to create a dynamic and challenging experience.

**Theme:** Help Farmer Fred defend his crops from a swarm of pesky bugs!

**Sprites:**

- Player (spaceship or tractor)
- Bug (different types with varying difficulty)
- Bullet

**Gameplay:**

- Player controls their ship/tractor with arrow keys.
- Clicking the mouse fires a bullet from the ship/tractor's position.
- Bullets move in a straight line until they hit the edge of the screen or a bug.
- Different bug types have different health points (stored in a list).
- Bugs move in random patterns across the screen.
- A score counter keeps track of bugs eliminated.
- Lives system: Player loses a life when a bug reaches the bottom of the screen.

**Using Lists, Clones, and Custom Blocks:**

- **Lists:**
    - Create a list to store bug health points for different bug types (e.g., ladybug - 1 point, beetle - 2 points).
    - Use a list to keep track of active bugs on the screen (store their X and Y positions).
- **Clones:**
    - Use clones of the bullet sprite for each shot fired by the player.
    - Create clones of the bug sprite for each bug type appearing on the screen.
- **Custom Blocks:**
    - Create a custom block for "Fire Bullet" that:
        - Creates a clone of the bullet sprite at the player's position.
        - Sets the bullet's direction based on the mouse pointer's position.
    - Create a custom block for "Bug Movement" that:
        - Defines a random movement pattern for the bug (e.g., bouncing, zigzagging).
        - Updates the bug's position based on the chosen pattern.

**Engagement and Challenge:**

- Introduce different types of bugs with increasing difficulty (health and movement).
- Add power-ups that appear randomly on the screen (e.g., faster firing rate, homing bullets).
- Implement a wave system where each wave has more and harder bugs.
- Include a catchy background music and sound effects (shooting, bug zapping).

**Learning Through Play:**

This project allows players to experiment with:

- List manipulation (adding, removing, updating values).
- Clone behavior and interaction between sprites.
- Custom block creation for modularity and code organization.

This is just a basic framework. You can add more features and customize it based on your creativity!

**Additional Tips:**

- Use costumes for different bug types (ladybug, beetle, etc.).
- Animate the firing of the bullet and bug zapping for visual appeal.
- Display the remaining lives and score on the screen.
- Include a game over screen with a final score and option to replay.

By incorporating these elements, you can create a fun and educational Scratch shooting game that showcases the power of lists, clones, and custom blocks!

Absolutely! Here's how a list can be extremely useful for keeping track of active bugs on the screen and how it can be used in your Scratch game:

**Benefits of using a list:**

- **Organized Data:** A list allows you to store all the bug positions (X and Y coordinates) in a single place. This makes it easier to manage and access information about each active bug.
- **Scalability:** As you add more bug types or increase the number of bugs on screen, the list can easily accommodate them. You simply add new items containing the X and Y positions of each new bug.
- **Efficient Updates:** When a bug moves, you only need to update its corresponding entry in the list with the new X and Y coordinates. This avoids complex loops searching for individual bug sprites.
- **Collision Detection:** The list becomes critical for checking collisions between bugs and bullets. By looping through the list, you can compare the bullet's position with each bug's position in the list. If they match, it signifies a collision.

**Using the list in your Scratch game:**

1. **Initializing the List:** At the beginning of your game, create an empty list called "activeBugs."
2. **Adding Bugs:** Whenever a new bug appears on the screen (either a new clone or the start of the game), create a new entry in the "activeBugs" list.
    - This entry can be a two-value list containing the bug's initial X and Y positions.

**Example:**

`when green flag clicked
  create a list called "activeBugs"
  ;; Spawn initial bugs (replace with your bug creation code)
  create clone of bug1
  set x of bug1 to (random number between 1 and 480)
  set y of bug1 to (random number between 1 and 360)
  add [x of bug1] [y of bug1] to activeBugs ;; Add bug position to list`

1. **Updating Bug Positions:** Within your custom block for "Bug Movement," after updating the bug's X and Y coordinates, update the corresponding entry in the "activeBugs" list.

**Example (within the "Bug Movement" custom block):**

`update bug X and Y based on movement pattern
;; Update position in list
  set item # of activeBugs to [x of bug] [y of bug]`

1. **Collision Detection:** Whenever a bullet is fired (in your "Fire Bullet" custom block), loop through the "activeBugs" list.
    - For each entry (containing bug's X and Y), compare it with the bullet's current position.
    - If they match, it signifies a collision. You can then:
        - Destroy the bullet and bug sprites.
        - Update the score based on the bug's type (refer to your bug health point list).
        - Remove the bug's position from the "activeBugs" list (as it's no longer active).

**Example (within the "Fire Bullet" custom block):**

`create clone of bullet
set bullet direction based on mouse pointer

repeat for the number of items in activeBugs
  get item # of activeBugs
  if (bullet X = item 1 of list) and (bullet Y = item 2 of list) then
    destroy bullet clone
    destroy bug clone (assuming collision destroys bug)
    update score based on bug type
    delete item # of activeBugs ;; Remove bug from active list
  end if
end repeat`

By utilizing a list in this way, you can efficiently manage your active bugs, detect collisions, and keep your game logic organized and scalable.