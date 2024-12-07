Cluedo Game Project

This is a digital version of the board game Cluedo and features interactive game play as well as dynamic setup with randomly assignment of weapons and characters to rooms.

How to Play
Objective: Solve the mystery by correctly identifying:

The Murderer: One of the characters.
The Weapon: One of the six possible weapons.
The Room: One of the mansion’s nine rooms.

Setup
At the start, the solution (murderer, weapon, room) is randomly selected.
Cards representing the remaining options are distributed among the players.
The notebook begins empty and updates dynamically as suggestions are made and refutations occur.

Game Flow
Dice Roll & Movement:
    Roll two six-sided dice to determine how far you can move.
    Move along a grid of rooms and corridors.

Actions:
When in a room, you may:
    Make a Suggestion: Propose a suspect, weapon, and room.
    Make an Accusation: Declare your final answer. A correct accusation wins the game; an incorrect one ends your participation.
    Pass Your Turn: Skip your action phase.
NPCs will also make decisions based on their strategic logic.

Refutations:
    If another player has a card matching the suggestion, they must reveal one to the suggester.


File Directory
accusations.py       # Handles accusations and solution validation
card_dealing.py      # Distributes cards among players
characters.py        # Defines characters and assigns starting rooms
game_loop.py         # Core gameplay loop
main.py              # Initializes and starts the game
mansion.py           # Mansion grid layout and movement logic
NPCs.py              # Smarter NPC logic and notebook handling
players.py           # Player class for human-controlled turns
solution.py          # Randomly selects the solution
suggestions.py       # Manages suggestions and refutations
testing.py           # Unit tests for core functionalities
weapons.py           # Defines weapons and assigns rooms


To clone the game use the command "git clone <https://github.com/kscheer6/CluedoGame>" in your terminal and navigate to the project directory "cd KatherineScheer_Project2_SourceCode"


Players can perform the following actions:
Move around the "board".
Make a suggestion: Propose a character, a weapon, and the current room to gain information from NPCs.
Make an accusation: Declare your final answer. Correct accusation wins the came. Incorrect accusation ends it.
End the game: Quit the game at any time.
