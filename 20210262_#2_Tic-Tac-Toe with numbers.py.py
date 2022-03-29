# Tic Tac Toe game with numbers
# Author : Omar ayman, with the help of Dr. Mohamed el-ramly
# Date : 1-3-2022
# Problem solving : Design-Analysis-Implementation-Testing
# Top Down Approach

# Empty Boxes are 20
board = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# function to display the game board on the terminal


def display_board():
    print('---------------')
    print('|', board[1], '|', board[2], '|', board[3], '|')
    print('---------------')
    print('|', board[4], '|', board[5], '|', board[6], '|')
    print('---------------')
    print('|', board[7], '|', board[8], '|', board[9], '|')
    print('---------------')


# function to get the number and the move of player 1
def get_player_action_odd(Player):
    valid_move = False

    while not valid_move:
        global n
        global action
        n = int(input("Please Enter an odd Number " + Player + " :"))
        if n % 2 == 0 or n > 9 or n in board:
            continue
        action = int(input("Please enter a block index " + Player + " :"))
        if action > 9 or action < 0:
            continue
        valid_move = action in list1 and action < 10 and board[action] == 20
    return action

# function to get the number and the move of player 2


def get_player_action_even(Player):
    valid_move = False
 # checks if the move is valid
    while not valid_move:
        global n
        global action
        n = int(input("Please Enter an Even Number " + Player + " :"))
        if n % 2 == 1 or n > 8 or n in board:
            if n == 0:
                break
            continue
        action = int(input("Please enter a block index " + Player + " :"))
        if action > 9 or action < 0:
            continue
        valid_move = action in list1 and action < 10 and board[action] == 20
    return action

# function to update the game board with a move of a player


def update_game_board(action, Player):
    board[action] = n
    display_board()

 # function to decide if a player has won


def winner():
    if (board[1]+board[2]+board[3] == 15 or
        board[1]+board[4]+board[7] == 15 or
        board[2]+board[5]+board[8] == 15 or
        board[4]+board[5]+board[6] == 15 or
        board[3]+board[6]+board[9] == 15 or
        board[1]+board[5]+board[9] == 15 or
        board[3]+board[5]+board[7] == 15):

        return True

# function that runs the game


def play_game():

    display_board()
    global nActions
    nActions = 0
    while nActions != 9:
        action1 = get_player_action_odd('P1')
        update_game_board(action1, "P1")
        display_board()
#    if  P1 wins:
        if winner():
            print('Player 1 wins!')
            break
        nActions += 1
# checks if there is a draw
        if nActions == 9:
            print("DRAW!")
            break
        action2 = get_player_action_even('P2')
        update_game_board(action2, 'P2')
#    if  P2 wins:
        if winner():
            print('Player 2 wins!')
            break
        nActions += 1


play_game()
