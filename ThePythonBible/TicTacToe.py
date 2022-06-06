# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 17:02:08 2022

@author: rzemi
"""

board=[" " for i in range(9)]

def PrintBoard():
    row1="|{}|{}|{}|".format(board[0], board[1],board[2])
    row2="|{}|{}|{}|".format(board[3], board[4],board[5])
    row3="|{}|{}|{}|".format(board[6], board[7],board[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()
    return

def PlayerMove(icon):
    try:
        if icon=="X":
            number=1
        elif icon=="O":
            number=2
        print("Your turn player{}".format(number))
        choice=int(input("Enter your move 1-9: ").strip())
        while board[choice-1]!=" ":
            print()
            print("That space is taken!")
            PrintBoard()
            choice=int(input("Again! Enter your move 1-9: ").strip())
        board[choice-1]=icon
        PrintBoard()
    except:
        print("Somethin went wrong! Try Again")
        PlayerMove(icon)
        
def IsVictory(icon):
    if (board[0] ==icon and board[1]==icon and board[2]==icon) or \
        (board[3] ==icon and board[4]==icon and board[5]==icon) or \
        (board[6] ==icon and board[7]==icon and board[8]==icon) or \
        (board[0] ==icon and board[3]==icon and board[6]==icon) or \
        (board[1] ==icon and board[4]==icon and board[7]==icon) or \
        (board[2] ==icon and board[5]==icon and board[9]==icon) or \
        (board[0] ==icon and board[4]==icon and board[8]==icon) or \
        (board[2] ==icon and board[4]==icon and board[6]==icon):
            return True
    else:
        return False
    
def IsDraw():
    if " " not in board:
        return True
    else:
        return False
    
PrintBoard()

while True:
    PlayerMove("X")
    PrintBoard()
    if IsVictory("X"):
        print("X wins!")
        break
    elif IsDraw():
        print("It's a draw!")
        break
    PlayerMove("O")
    PrintBoard()
    if IsVictory("O"):
        print("O wins!")
        break
    elif IsDraw():
        print("It's a draw!")
        break