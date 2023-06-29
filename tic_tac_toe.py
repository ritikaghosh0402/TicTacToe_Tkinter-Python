from tkinter import *
import random

def next_turn(row, column):

    global player
    if btn[row][column]["text"] =="" and check_winner() is False:

        if player == players[0]:
            btn[row][column]["text"] = player
            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+" turn"))
            elif check_winner() is True:
                label.config(text=(players[0] + " Wins"))
            elif check_winner() == "Tie":
                label.config(text=("Tie!"))

        else:
            btn[row][column]["text"] = player
            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0] + " turn"))
            elif check_winner() is True:
                label.config(text=(players[1] + " Wins"))
            elif check_winner() == "Tie":
                label.config(text=("Tie!"))

def check_winner():

    for row in range(3):
        if btn[row][0]["text"] == btn[row][1]["text"] == btn[row][2]["text"] != "":
            btn[row][0].config(bg="#0416b3")
            btn[row][1].config(bg="#0416b3")
            btn[row][2].config(bg="#0416b3")
            return True

    for column in range(3):
        if btn[0][column]["text"] == btn[1][column]["text"] == btn[2][column]["text"] != "":
            btn[0][column].config(bg="#0416b3")
            btn[1][column].config(bg="#0416b3")
            btn[2][column].config(bg="#0416b3")
            return True

    if btn[0][0]["text"] == btn[1][1]["text"] == btn[2][2]["text"] !="":
        btn[0][0].config(bg="#0416b3")
        btn[1][1].config(bg="#0416b3")
        btn[2][2].config(bg="#0416b3")
        return True

    elif btn[0][2]["text"] == btn[1][1]["text"] == btn[2][0]["text"] !="":
        btn[0][2].config(bg="#0416b3")
        btn[1][1].config(bg="#0416b3")
        btn[2][0].config(bg="#0416b3")
        return True

    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                btn[row][column].config(bg="#b800f0")
        return "Tie"

    else:
        return False

def empty_spaces():

    total_spaces = 9
    for row in range(3):
        for column in range (3):
            if btn[row][column]["text"] !="":
                total_spaces -=1

    if total_spaces == 0:
        return False
    else:
        return True

def new_game():

    global player
    player = random.choice(players)
    label.config(text=player+" turn")

    for row in range(3):
        for column in range(3):
            btn[row][column].config(text="",bg="#F0F0F0")

ttt = Tk()
ttt.title("Tic Tac Toe")
players = ["X","O"]
player = random.choice(players)
btn = [[0,0,0],
      [0,0,0],
      [0,0,0]]


label = Label(text=player + " turn", font=("Open Sans",40))
label.pack(side="top")

reset_btn = Button(text="Restart",font=("Open Sans",20), command=new_game)
reset_btn.pack(side="top")

frame = Frame(ttt)
frame.pack()

for row in range(3):
    for column in range(3):
        btn[row][column] = Button(frame, text="",font=("Open Sans",40), width=5, height=2,command=lambda row=row, column=column: next_turn(row,column))
        btn[row][column].grid(row=row,column=column)

ttt.mainloop()