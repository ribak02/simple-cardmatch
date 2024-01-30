# simple-cardmatch

# Overview
This Python program is a simple card matching game built using PyQt5. The game displays a grid of cards, and the player needs to find and match pairs of cards. When two cards are matched, they remain visible. The goal is to match all pairs of cards.

# Requirements
Python 3.x
PyQt5 library
Installation
Ensure Python 3.x is installed on your system.
Install PyQt5 using pip:
bash
Copy code
pip install PyQt5
Usage
Run the script using Python:

bash
Copy code
python card_match_game.py
A window will open with a grid of cards.

# Game Features
Grid Size: The game grid is 4x4 by default, but can be adjusted by changing the SIZE variable in the script. Valid sizes include 2, 4, 6, 8, and 10.
Card Matching: Click on two cards to see if they match. Matched cards will remain visible.
Game Completion: The game ends when all pairs are matched. A popup message will announce the victory.
Code Structure
MyWindow Class: Inherits QMainWindow. Manages the game's window, UI elements, and game logic.

__init__(self, size): Initializes the game window with the specified size.
initUI(self): Sets up the UI elements including the grid of buttons (cards).
clicked(self): Handles the logic when a card is clicked.
match(self, button1, button2): Checks if two cards match.
show_popup(self, msg): Displays a popup message.
window Function: Initializes the PyQt application and opens the game window.

# Notes
The game uses a basic shuffle algorithm to randomize card positions.
The appearance of cards and text can be customized via the setStyleSheet method.
