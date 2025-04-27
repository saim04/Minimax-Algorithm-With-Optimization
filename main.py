import time
import math

# Constants for The Game 
HUMAN = 'O'
AI = 'X'
EMPTY = ' '

# Class for the TicTacToe
class TicTacToe:
    def __init__(self):
        self.board = [EMPTY] * 9

    def display_board(self):
        for i in range(3):
            print(" | ".join(self.board[i*3:(i+1)*3]))
            if i < 2:
                print("--+---+--")
        print()

    def make_move(self, index, player):
        if self.board[index] == EMPTY:
            self.board[index] = player
            return True
        return False

    def undo_move(self, index):
        self.board[index] = EMPTY

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == EMPTY]

    def is_winner(self, player):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],   # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],   # columns
            [0, 4, 8], [2, 4, 6]               # diagonals
        ]
        return any(all(self.board[i] == player for i in condition) for condition in win_conditions)

    def is_draw(self):
        return EMPTY not in self.board and not self.is_winner(AI) and not self.is_winner(HUMAN)

    def game_over(self):
        return self.is_winner(AI) or self.is_winner(HUMAN) or self.is_draw()

# Minimax Algorithm
def minimax(board, depth, is_maximizing, call_counter):
    call_counter[0] += 1

    if board.is_winner(AI):
        return 10 - depth
    if board.is_winner(HUMAN):
        return depth - 10
    if board.is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in board.available_moves():
            board.make_move(move, AI)
            score = minimax(board, depth + 1, False, call_counter)
            board.undo_move(move)
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for move in board.available_moves():
            board.make_move(move, HUMAN)
            score = minimax(board, depth + 1, True, call_counter)
            board.undo_move(move)
            best_score = min(best_score, score)
        return best_score

# Minimax Algorithm Optimizied with Alpha-Beta Pruning
def minimax_alpha_beta(board, depth, alpha, beta, is_maximizing, call_counter):
    call_counter[0] += 1

    if board.is_winner(AI):
        return 10 - depth
    if board.is_winner(HUMAN):
        return depth - 10
    if board.is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in board.available_moves():
            board.make_move(move, AI)
            score = minimax_alpha_beta(board, depth + 1, alpha, beta, False, call_counter)
            board.undo_move(move)
            best_score = max(best_score, score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = math.inf
        for move in board.available_moves():
            board.make_move(move, HUMAN)
            score = minimax_alpha_beta(board, depth + 1, alpha, beta, True, call_counter)
            board.undo_move(move)
            best_score = min(best_score, score)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return best_score

# Find the best move
def best_move(board, use_alpha_beta=False):
    best_score = -math.inf
    move = None
    call_counter = [0]
    start_time = time.time()

    for possible_move in board.available_moves():
        board.make_move(possible_move, AI)
        if use_alpha_beta:
            score = minimax_alpha_beta(board, 0, -math.inf, math.inf, False, call_counter)
        else:
            score = minimax(board, 0, False, call_counter)
        board.undo_move(possible_move)

        if score > best_score:
            best_score = score
            move = possible_move

    elapsed_time = time.time() - start_time
    return move, call_counter[0], elapsed_time

# Main Game
if __name__ == "__main__":
    game = TicTacToe()
    print("\nWelcome to Tic-Tac-Toe!")
    print("You are 'O' and the AI is 'X'.")
    print("Input a number between 0-8 to place your move:")
    print(" 0 | 1 | 2 ")
    print("---+---+---")
    print(" 3 | 4 | 5 ")
    print("---+---+---")
    print(" 6 | 7 | 8 \n")

    # Ask user to choose the AI strategy
    use_alpha_beta = None
    while use_alpha_beta is None:
        print("Choose AI strategy:")
        print("1. Standard Minimax")
        print("2. Minimax with Alpha-Beta Pruning")
        choice = input("Enter 1 or 2: ")
        if choice == '1':
            use_alpha_beta = False
            print("\nYou chose: Standard Minimax.\n")
        elif choice == '2':
            use_alpha_beta = True
            print("\nYou chose: Minimax with Alpha-Beta Pruning.\n")
        else:
            print("Invalid choice. Please enter 1 or 2.\n")

    game.display_board()

    while not game.game_over():
        # Human Move
        print("Your Turn:")
        valid_input = False
        while not valid_input:
            try:
                human_move = int(input("Enter your move (0-8): "))
                if human_move < 0 or human_move > 8:
                    print("Invalid input! Please enter a number between 0 and 8.")
                elif not game.make_move(human_move, HUMAN):
                    print("Cell already taken! Choose another.")
                else:
                    valid_input = True
            except ValueError:
                print("Invalid input! Please enter an integer between 0 and 8.")
        
        game.display_board()

        if game.game_over():
            break

        # AI Move
        print("AI's Turn...")
        move, calls, duration = best_move(game, use_alpha_beta=use_alpha_beta)
        game.make_move(move, AI)
        game.display_board()

        if use_alpha_beta:
            print(f"AI used Minimax with Alpha-Beta Pruning: {calls} recursive calls, {duration:.6f} seconds")
        else:
            print(f"AI used Standard Minimax: {calls} recursive calls, {duration:.6f} seconds")

    # Final Result
    print("\nGame Over!")
    if game.is_winner(HUMAN):
        print("Congratulations! You win!")
    elif game.is_winner(AI):
        print("AI wins! Better luck next time!")
    else:
        print("It's a Draw!")