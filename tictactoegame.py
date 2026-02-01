def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0
    while True:
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}'s turn.")
        try:
            row, col = map(int, input("Enter row and column (0-2, e.g., 1 2): ").split())
            if board[row][col] != " ":
                print("Spot taken!")
                continue
            board[row][col] = player
            if check_winner(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                break
            if is_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            turn += 1
        except (ValueError, IndexError):
            print("Invalid input. Try again.")

if __name__ == "__main__":
    main()