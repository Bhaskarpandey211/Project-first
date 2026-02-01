# Beginners Level Tic-Tac-Toe Game in Python
# This is a very simple version for learning basics.

# Create a 3x3 board with empty spaces
board = [[" " for _ in range(3)] for _ in range(3)]

# Start with player X
player = "X"

# Function to print the board
def print_board():
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check if someone won
def check_win():
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

# Main game loop
while True:
    # Show the board
    print_board()
    
    # Ask for player's move
    print(f"Player {player}, your turn!")
    row = int(input("Enter row (0, 1, or 2): "))
    col = int(input("Enter column (0, 1, or 2): "))
    
    # Check if the spot is empty
    if board[row][col] == " ":
        board[row][col] = player
    else:
        print("That spot is taken! Try again.")
        continue
    
    # Check for a winner
    winner = check_win()
    if winner:
        print_board()
        print(f"Player {winner} wins!")
        break
    
    # Check for a draw (board full)
    if all(board[r][c] != " " for r in range(3) for c in range(3)):
        print_board()
        print("It's a draw!")
        break
    
    # Switch to the other player
    player = "O" if player == "X" else "X"