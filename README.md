# Tic Tac Toe AI: A Tic Tac Toe game AI agent

Harvard CS50AI Project

## Description:

An AI program using Minimax algorithms with Alpha-Beta pruning to play Tic Tac Toe game optimally.

## Tech Stack:

* Python

## Project Specification:

### player
The player function should take a board state as input, and return which player’s turn it is (either X or O).

### actions
The actions function should return a set of all of the possible actions that can be taken on a given board.

### result
The result function takes a board and an action as input, and should return a new board state, without modifying the original board.

### winner
The winner function should accept a board as input, and return the winner of the board if there is one.

### terminal 
The terminal function should accept a board as input, and return a boolean value indicating whether the game is over.

### utility
The utility function should accept a terminal board as input and output the utility of the board.

### minimax
The minimax function should take a board as input, and return the optimal move for the player to move on that board.

## How to run

1. Clone this project
2. Install requirements package:
   ```
   pip install -r requirements.txt
   ```
3. Run the Tic Tac Toe game:
   ```
   python runner.py
   ```
