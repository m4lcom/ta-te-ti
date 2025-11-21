from random import randrange

def show_board(board):
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
    print("+-------" * 3, "+", sep="")

def next_move(board):
    while True:
        move = input("Enter your move (1-9): ")
        if not move.isdigit():
            print("Invalid input, enter a number from 1 to 9.")
            continue
        move = int(move) - 1
        if move < 0 or move > 8:
            print("Number out of range, try again.")
            continue
        row, col = divmod(move, 3)
        if board[row][col] in ['O', 'X']:
            print("Square already taken, try again.")
            continue
        board[row][col] = 'O'
        break

def empty_squares(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] not in ['O', 'X']]

def winner(board, symbol):
    # Rows and columns
    for i in range(3):
        if all(board[i][j] == symbol for j in range(3)):
            return symbol
        if all(board[j][i] == symbol for j in range(3)):
            return symbol
    # Diagonals
    if all(board[i][i] == symbol for i in range(3)):
        return symbol
    if all(board[i][2 - i] == symbol for i in range(3)):
        return symbol
    return None

def machine_move(board):
    free = empty_squares(board)
    if free:
        row, col = free[randrange(len(free))]
        board[row][col] = 'X'

def main():
    board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
    board[1][1] = 'X'  # Machine starts in the center
    human_turn = True
    game_winner = None

    while empty_squares(board):
        show_board(board)
        if human_turn:
            next_move(board)
            game_winner = winner(board, 'O')
        else:
            machine_move(board)
            game_winner = winner(board, 'X')
        if game_winner:
            break
        human_turn = not human_turn

    show_board(board)
    if game_winner == 'O':
        print("You win!")
    elif game_winner == 'X':
        print("You lose!")
    else:
        print("Draw!")

if __name__ == "__main__":
    main()
