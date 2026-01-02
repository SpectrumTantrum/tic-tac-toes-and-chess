#!/usr/bin/env python3
"""
Tic-Tac-Toe Game
A simple command-line implementation of the classic tic-tac-toe game.
"""


def create_board():
    """Create and return an empty 3x3 game board."""
    return [[' ' for _ in range(3)] for _ in range(3)]


def display_board(board):
    """Display the current state of the game board."""
    print("\n")
    print("     0   1   2")
    print("   +---+---+---+")
    for i, row in enumerate(board):
        print(f" {i} | {row[0]} | {row[1]} | {row[2]} |")
        print("   +---+---+---+")
    print("\n")


def is_valid_move(board, row, col):
    """Check if the move is valid (within bounds and cell is empty)."""
    if 0 <= row < 3 and 0 <= col < 3:
        return board[row][col] == ' '
    return False


def make_move(board, row, col, player):
    """Place the player's mark on the board."""
    if is_valid_move(board, row, col):
        board[row][col] = player
        return True
    return False


def check_winner(board, player):
    """Check if the specified player has won the game."""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False


def is_board_full(board):
    """Check if the board is completely filled."""
    return all(cell != ' ' for row in board for cell in row)


def get_player_move(board, player):
    """Get and validate player input for their move."""
    while True:
        try:
            move = input(f"Player {player}'s turn. Enter row and column (e.g., 0 1): ")
            row, col = map(int, move.strip().split())
            
            if is_valid_move(board, row, col):
                return row, col
            else:
                print("Invalid move! That position is either taken or out of bounds.")
        except (ValueError, IndexError):
            print("Invalid input! Please enter row and column as two numbers separated by space (e.g., 0 1).")
        except KeyboardInterrupt:
            print("\n\nGame interrupted by user.")
            exit(0)


def play_game():
    """Main game loop."""
    print("=" * 40)
    print("     Welcome to Tic-Tac-Toe!")
    print("=" * 40)
    print("\nInstructions:")
    print("- Players take turns placing X and O")
    print("- Enter row and column numbers (0-2)")
    print("- First to get 3 in a row wins!\n")
    
    board = create_board()
    current_player = 'X'
    
    while True:
        display_board(board)
        
        # Get player move
        row, col = get_player_move(board, current_player)
        make_move(board, row, col, current_player)
        
        # Check for winner
        if check_winner(board, current_player):
            display_board(board)
            print(f"🎉 Congratulations! Player {current_player} wins! 🎉")
            break
        
        # Check for draw
        if is_board_full(board):
            display_board(board)
            print("It's a draw! The board is full.")
            break
        
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'
    
    # Ask to play again
    play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
    if play_again in ['yes', 'y']:
        play_game()
    else:
        print("\nThanks for playing! Goodbye!")


if __name__ == "__main__":
    play_game()
