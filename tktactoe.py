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
    if board.count(" ")==1:
        message("GAME DRAW!")
    move=compMove()
    board[move]="O"
    b[move].config(text=board[move])
    if isWinner('O'):
        message("YOU LOSE!")

def compMove():
    possibleMoves=[x for x in range(1,10) if board[x]==" "]
    for x in ['O','X']:
        for let in possibleMoves:
            board[let]=x
            if isWinner(x):
                return let
            board[let]=" "

    choices=[]
    corners=[1,3,7,9]
    for x in corners:
        if x in possibleMoves:
            choices.append(x)
    if len(choices)>0:
        x=random.choice(choices)
        return x

    if 5 in possibleMoves:
        return 5

    edges=[2,4,6,8]
    for x in edges:
        if x in possibleMoves:
            choices.append(x)
    if len(choices)>0:
        x=random.choice(choices)
        return x

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
