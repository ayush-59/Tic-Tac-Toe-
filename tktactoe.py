import sys
import os
import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox


win=Tk()
win.geometry("500x500")
win.title("TIC TAC TOE")
c=Canvas(win,height=1000,width=1000,bg="red")
c.pack()

board=[" " for x in range(10)]


def isWinner(x):
    return(board[1]==x and board[2]==x and board[3]==x or
    board[4]==x and board[5]==x and board[6]==x or
    board[7]==x and board[8]==x and board[9]==x or
    board[1]==x and board[4]==x and board[7]==x or
    board[2]==x and board[5]==x and board[8]==x or
    board[3]==x and board[6]==x and board[9]==x or
    board[1]==x and board[5]==x and board[9]==x or
    board[3]==x and board[5]==x and board[7]==x )

def is_draw():
    possibleMoves=[x for x,letter in enumerate(board) if letter == " " and x!=0]
    return len(possibleMoves) == 0

def restart():
    python=sys.executable
    os.execl(python,python,*sys.argv)

def message(n):
    msg=messagebox.askquestion("msg",n+" DO YOU WANT TO PLAY AGAIN?")
    if msg=='yes':
        restart()
    else:
        win.destroy()
def playerMove(n):
    if board[n]==" ":
        board[n]='X'
    b[n].config(text=board[n])
    if isWinner('X'):
        message("YOU WIN!")
        return
    if board.count(" ")==1:
        message("GAME DRAW!")
        return
    move=compMove()
    board[move]="O"
    b[move].config(text=board[move])
    if isWinner('O'):
        message("YOU LOSE!")

def minimax(is_max):
    if isWinner('X'):
        return -100
    elif isWinner('O'):
        return 100
    elif is_draw():
        return 0

    possibleMoves = [x for x,letter in enumerate(board) if letter == " " and x != 0]

    if is_max:
        best = -1000
        for move in possibleMoves:
            board[move] = 'O'
            best = max(best, minimax(not is_max))
            board[move] = " "

        return best
    else:
        best = 1000
        for move in possibleMoves:
            board[move] = 'X'
            best = min(best, minimax(not is_max))
            board[move] = " "

        return best

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == " " and x != 0]
    best = -1000
    best_move = None
    for move in possibleMoves:
        board[move] = 'O'
        score =  minimax(False)
        board[move] = ' '
        if score > best:
            best = score
            best_move = move
    return best_move


b1=Button(c,height=10,width=20,text=board[1],bg="silver",command=lambda:playerMove(1))
b1.grid(row=1,column=1)
b2=Button(c,height=10,width=20,text=board[2],bg="silver",command=lambda:playerMove(2))
b2.grid(row=1,column=3)
b3=Button(c,height=10,width=20,text=board[3],bg="silver",command=lambda:playerMove(3))
b3.grid(row=1,column=5)
b4=Button(c,height=10,width=20,text=board[4],bg="silver",command=lambda:playerMove(4))
b4.grid(row=2,column=1)
b5=Button(c,height=10,width=20,text=board[5],bg="silver",command=lambda:playerMove(5))
b5.grid(row=2,column=3)
b6=Button(c,height=10,width=20,text=board[6],bg="silver",command=lambda:playerMove(6))
b6.grid(row=2,column=5)
b7=Button(c,height=10,width=20,text=board[7],bg="silver",command=lambda:playerMove(7))
b7.grid(row=3,column=1)
b8=Button(c,height=10,width=20,text=board[8],bg="silver",command=lambda:playerMove(8))
b8.grid(row=3,column=3)
b9=Button(c,height=10,width=20,text=board[9],bg="silver",command=lambda:playerMove(9))
b9.grid(row=3,column=5)

b=['',b1,b2,b3,b4,b5,b6,b7,b8,b9]


mainloop()
