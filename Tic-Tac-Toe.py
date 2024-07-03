board = [' ' for _ in range(9)]


def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')


def is_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  
                      (0, 4, 8), (2, 4, 6)]          
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)


def get_available_moves(board):
    return [i for i, spot in enumerate(board) if spot == ' ']


def minimax(board, depth, is_maximizing):
    if is_winner(board, 'O'):
        return 1
    elif is_winner(board, 'X'):
        return -1
    elif ' ' not in board:
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for move in get_available_moves(board):
            board[move] = 'O'
            score = minimax(board, depth + 1, False)
            board[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in get_available_moves(board):
            board[move] = 'X'
            score = minimax(board, depth + 1, True)
            board[move] = ' '
            best_score = min(score, best_score)
        return best_score


def ai_move(board):
    best_score = -float('inf')
    best_move = None
    for move in get_available_moves(board):
        board[move] = 'O'
        score = minimax(board, 0, False)
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    board[best_move] = 'O'


def human_move(board, move):
    if board[move] == ' ':
        board[move] = 'X'
        return True
    return False


def main():
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Human player move
        move = int(input("Enter your move (0-8): "))
        if human_move(board, move):
            print_board(board)
            if is_winner(board, 'X'):
                print("You win!")
                break
            elif ' ' not in board:
                print("It's a draw!")
                break

            #1st player move
            ai_move(board)
            print("AI moved:")
            print_board(board)
            if is_winner(board, 'O'):
                print("AI wins!")
                break
            elif ' ' not in board:
                print("It's a draw!")
                break
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    main()
