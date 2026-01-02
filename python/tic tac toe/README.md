# Tic-Tac-Toe (Python)

A simple command-line implementation of the classic tic-tac-toe game written in Python.

## Features

- Interactive command-line interface
- Two-player gameplay (X and O)
- Input validation
- Win detection (rows, columns, diagonals)
- Draw detection
- Option to play multiple games

## Requirements

- Python 3.x

## How to Run

```bash
python3 tic_tac_toe.py
```

Or make it executable and run directly:

```bash
chmod +x tic_tac_toe.py
./tic_tac_toe.py
```

## How to Play

1. The game starts with Player X
2. Players take turns entering their moves
3. Enter the row and column numbers (0-2) separated by a space
   - Example: `0 1` places a mark at row 0, column 1
4. The first player to get three marks in a row (horizontally, vertically, or diagonally) wins
5. If all cells are filled without a winner, the game is a draw

## Game Board Layout

```
     0   1   2
   +---+---+---+
 0 |   |   |   |
   +---+---+---+
 1 |   |   |   |
   +---+---+---+
 2 |   |   |   |
   +---+---+---+
```

## Example Game

```
Player X's turn. Enter row and column (e.g., 0 1): 0 0
Player O's turn. Enter row and column (e.g., 0 1): 1 1
Player X's turn. Enter row and column (e.g., 0 1): 0 1
Player O's turn. Enter row and column (e.g., 0 1): 2 2
Player X's turn. Enter row and column (e.g., 0 1): 0 2
🎉 Congratulations! Player X wins! 🎉
```

## Game Logic

The game includes:
- **Board Creation**: Creates a 3x3 grid
- **Move Validation**: Ensures moves are within bounds and positions are empty
- **Win Detection**: Checks all rows, columns, and diagonals
- **Draw Detection**: Checks if the board is full without a winner
- **Player Switching**: Alternates between X and O players
