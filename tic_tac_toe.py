import os
import time
import random 

#define the board
board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]

#print the introduction
def print_intro():
    print(
    """
START THE GAME!
""")

#Design the board

def printBoard():
    print('   |   |   ')
    print(' '+ board[1] +' | ' +board[2] +' | ' + board[3]+' ')
    print('   |   |   ')
    print('---|---|---')
    print('   |   |   ')
    print(' '+ board[4] + ' | ' +board[5] +' | ' + board[6]+' ')
    print('   |   |   ')
    print('---|---|---')
    print('   |   |   ')
    print(' '+ board[7] + ' | ' +board[8] +' | ' + board[9]+' ')
    print('   |   |   ')

def IsWinner(board, player):
    if (board[1] == player and board[2] == player and board[3] == player) or \
            (board[4] == player and board[5] == player and board[6] == player) or \
            (board[7] == player and board[8] == player and board[9] == player) or \
            (board[1] == player and board[4] == player and board[7] == player) or \
            (board[2] == player and board[5] == player and board[8] == player) or \
            (board[3] == player and board[6] == player and board[9] == player) or \
            (board[1] == player and board[5] == player and board[9] == player) or \
            (board[3] == player and board[5] == player and board[7] == player):
        return True
    else:
        return False

def IsBoardFull(board): 
    if board.count(' ') > 1:
        return False
    else:
        return True

#let machine move
def machine_move(board, player):
    #if the center square is empty choose that
    if board[5] == ' ':
        return 5

    while True:
        move = random.randint(1,9)
        #if the move is empty, go ahead and return
        if board[move] ==' ':
            return move 
            break

    return 5

while True:
    os.system("cls")
    print_intro()
    printBoard()

    player_pos = input("Choose a space for X. ")
    player_pos = int(player_pos)

    #check if the chosen space is empty
    if board[player_pos] == " ":
        board[player_pos] = "X"
    else:
        print("The space is not empy, choose anothe space")
        time.sleep(1)


#check if the winner is X
    if IsWinner(board, "X"):
        os.system("cls")
        print_intro()
        printBoard()
        print("X wins!")
        break

    os.system("cls")

    printBoard()

    if IsBoardFull(board):
        print("Full !")
        break

    #get O input
    player_pos = machine_move(board, "O")    

    #check if the space is free
    if board[player_pos] == " ":
        board[player_pos] = "O"
    else:
        print("this space is not free!")
        time.sleep(1)

# check if O win
    if IsWinner(board, "O"):
        os.system("cls")
        print_intro
        printBoard()
        print("O wins!")
        break

#check if the board is full
    if IsBoardFull(board):
        print("It is Full !")
        break


    


        