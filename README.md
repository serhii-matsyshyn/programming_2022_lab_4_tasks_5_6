# Programming 2022 lab_4 tasks 5 and 6

#### Labyrinth Wandering Travel Game  
There are two versions of the wandering game:  
- The first is based on data and a log file specified in the laboratory task
- The second game is a complicated version of the game, which takes place on the streets of Lviv.

The game is made using the principles of OOP.

## Task 5
The module consists of two parts. The first part allows you to create a game space, and the second is actually the main cycle of the game.

Game space is created by creating rooms with a name and description. The mutual arrangement of rooms is arranged around the world. The rooms house game characters (friends and enemies) as well as items that you can try to use to fight enemies. It also determines how the character will respond to an attempt to talk to him and the object that can defeat the enemy.

After building the playing field, the location of the player who has an empty backpack where he can put items to fight enemies is established.

The main cycle of the program is executed until the player dies or two enemies die. The main cycle displays information about the current room, the characters that are there and objects in this room. The player can choose one of the following steps: go to another room, pick up an item, start a conversation or start a fight.

If a player picks up an item, it disappears from the room and appears in the player's backpack. If the player chooses the direction in which the other room is located, this room becomes the current room and the game continues. If the player starts a conversation, a message from the character is displayed on the screen. Fighting the enemy begins with entering the name of the object to fight, if such an object is in the backpack and it is such an object that can be won, the player is credited with the first victory (the game lasts up to two victories). If the item is not suitable for fighting this enemy, the player is credited with defeat.

## Task 6
Complicated version of the game.  
Wandering the streets of Lviv you can meet students, gentlemen, lotteries, thugs and slackers.  
On the street you can find various items that can be used during the game.  
If you manage to take a walk from Kozelnytska Street to Krakivska Street and return, you win. Otherwise, the game ends in your defeat.  
#### Streets in the game:
- Kozelnytska Street
- Stryiska Street
- Ring Road
- Zelena Street
- Ivana Franka Street
- Shevchenka Avenue
- Krakivska Street

There also is a hero Super Enemy, to defeat him you need to answer additional question.  
The complete log of the winning game is recorded in the log.txt file.

## How to play the game?
List of available commands in the console game:
- to move to some direction use ["north", "south", "east", "west"]
- to talk to anyone use "talk"
- to fight enemy use "fight"
- to take item from room use "take"