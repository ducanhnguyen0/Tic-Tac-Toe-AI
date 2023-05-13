"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Check the current state by counting X and O
    # Set counter for X
    X_count = 0
    # Set counter for O
    O_count = 0

    # Loop through each square in the board
    for i in range(len(board)):
        for j in range(len(board[i])):
            # Check if square contain X or O
            if board[i][j] == "X":
                # Increase counter of X by 1 if square contain X
                X_count += 1
            elif board[i][j] == "O":
                # Increase counter of O by 1 if square contain O
                O_count += 1

    # Check the turn based on counter of each
    # if X counter bigger than O counter then it's O turn otherwise it's X turn
    return O if X_count > O_count else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Create variable to store all possible action
    possible_actions = set()

    # Loop thorugh each square in the board
    for i in range(len(board)):
        for j in range(len(board[i])):
            # Check if board is available on the board
            if board[i][j] == EMPTY:
                # add to the possible action set if it's available on the board
                possible_actions.add((i, j))

    # return set of possible moves otherwise none
    return possible_actions if possible_actions else None


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Validate action
    if action not in actions(board):
        raise NameError("Invalid action!")

    # Make a deep copy of current board
    board_copy = copy.deepcopy(board)

    # Change the board state of copy to results from making move (i, j) on the board
    board_copy[action[0]][action[1]] = player(board)

    # Return board copy state
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check row
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]

    # Check column
    for j in range(len(board)):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] != EMPTY:
            return board[0][j]

    # Check diagonal
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[2][0] == board[1][1] == board[0][2]:
        return board[2][0]


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check if there is any avaliable square in actions function or there is a winner
    if actions(board) == None or winner(board):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # Check the winner and return correspond value
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Check the state of the game
    if terminal(board):
        return None

    # Optimize Minimax with Alpha-Beta Pruning
    alpha = float('-inf')  # Keep track of max value
    beta = float('inf')  # Keep track of min value

    # return move that help X player tries to maximize the score
    if player(board) == "X":
        return Max_Value(board, alpha, beta)[1]

    # return move that help O player tries to minimize the score
    if player(board) == "O":
        return Min_Value(board, alpha, beta)[1]


# Function max produce highest value of function min
def Max_Value(board, alpha, beta):

    # Set varibale
    max_value = float('-inf')  # set to negative infinity to get the first value from first posibility path
    max_move = None  # store action that bring best result

    # Check if it reaches terminal state
    if terminal(board):
        return [utility(board), None] # return value and action in array type

    # Loop through all possible actions in set
    for action in actions(board):

        # Let min and max functions call each other recursively and get the value from array
        value = Min_Value(result(board, action), alpha, beta)[0]

        # Compare value to get the max value
        if value > max_value:
            max_value = value
            # Update varibale with action that result best
            max_move = action

        # Update alpha variable to keep track of max value while backtracking
        alpha = max(alpha, max_value)

        # Check if possible path have lower value for beta to pick then ignore and break the loop to continue with other paths to maximize value
        if alpha >= beta:
            break

    # return value and move for max player
    return [max_value, max_move]


# Function min produce lowest value of function max
def Min_Value(board, alpha, beta):

    # Set varibale
    min_value = float('inf')  # set to positive infinity to get the first value from first posibility path
    min_move = None  # store action that bring best result

    # Check if it reaches terminal state
    if terminal(board):
        return [utility(board), None]  # return value and action in array type

    # Loop through all possible actions in set
    for action in actions(board):

        # Let min and max functions call each other recursively and get the value from array
        value = Max_Value(result(board, action), alpha, beta)[0]

        # Compare value to get the min value
        if value < min_value:
            min_value = value
            # Update varibale with action that result best
            min_move = action

        # Update beta variable to keep track of min value while backtracking
        beta = min(beta, min_value)

        # Check if possible path have higher value for alpha to pick then ignore and break the loop to continue with other paths to minimize value
        if alpha >= beta:
            break

    # return array with value and move for min player
    return [min_value, min_move]

