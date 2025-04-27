Tic-Tac-Toe with Minimax and Alpha-Beta Pruning
Overview
This project focuses on understanding and implementing the Minimax algorithm and its optimization using Alpha-Beta Pruning for the classic game of Tic-Tac-Toe.

You will play as 'O', while the AI plays as 'X'.
The AI always plays optimally using either Standard Minimax or Alpha-Beta Pruned Minimax — depending on your choice.

Features
Play Tic-Tac-Toe against an unbeatable AI.

Choose between:

Standard Minimax

Minimax with Alpha-Beta Pruning (for better performance)

Detailed performance stats after every AI move:

Recursive calls made

Time taken for move computation

How to Play
Run the script:

bash
Copy
Edit
python your_script_name.py
Choose the AI strategy:

1 for Standard Minimax

2 for Minimax with Alpha-Beta Pruning

Place your move by entering a number (0–8) as per the board layout:

diff
Copy
Edit
0 | 1 | 2
---+---+---
3 | 4 | 5
---+---+---
6 | 7 | 8
Try to beat the AI — if you can!

Project Structure
TicTacToe Class: Core game logic (board management, move validation, winner checking).

Minimax Algorithm: Implements standard Minimax for optimal AI decision-making.

Alpha-Beta Pruning: Optimizes the Minimax algorithm by pruning unnecessary recursive paths.

Best Move Finder: Selects the best move using the chosen AI strategy.

Main Game Loop: Handles user input, AI moves, and displays the board.

Key Concepts Implemented
Minimax Algorithm:

Recursively explores all possible moves.

Chooses the move that minimizes the opponent's maximum payoff.

Alpha-Beta Pruning:

Improves Minimax efficiency.

Prunes branches that cannot influence the final decision.

Tic-Tac-Toe Mechanics:

Turn-based gameplay.

Board evaluation.

Win, loss, and draw detection.

Requirements
Python 3.x

No external libraries required.

Sample Gameplay
text
Copy
Edit
Welcome to Tic-Tac-Toe!
You are 'O' and the AI is 'X'.

Choose AI strategy:

1. Standard Minimax
2. Minimax with Alpha-Beta Pruning
   Enter 1 or 2: 2

You chose: Minimax with Alpha-Beta Pruning.

Your Turn:
Enter your move (0-8): 4

O | |  
---+---+---
| X |  
---+---+---
| |

AI used Minimax with Alpha-Beta Pruning: 27 recursive calls, 0.000132 seconds
Learning Outcomes
✅ Mastered the Minimax algorithm for adversarial games.
✅ Understood and applied Alpha-Beta Pruning to optimize recursive search trees.
✅ Built a fully playable, unbeatable version of Tic-Tac-Toe with clear, structured code.
