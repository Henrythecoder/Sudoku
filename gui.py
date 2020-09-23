from tkinter import *
import tkinter as tk
import Game


root = Tk()





#L1 = Label(root, text="SUDOKU")
#L1.grid(row=0, column=0)


entries = []
colourselection= ['green3', "red3"]

def display_board():
    global entries
    spacex = 0
    spacey = 0
    sem = 0
    sem_y = 0
    for a in range(0, 11):
        for b in range(0, 12):
            if spacex > 2:
                spacex = 0
            entry = tk.StringVar()
            checkA = a - spacey
            if checkA % 3 == 0 and a != 0 and sem_y != 1:

                canvas = Canvas(root, width=1,height=5)
                #canvas.create_line(0, 0, 15, 0)
                canvas.grid(row=a, column=b)

                if b == 11:
                    sem_y = 1
                    spacey += 1
                continue
            checkB = b - spacex
            if checkB % 3 == 0 and b != 0 and sem != 1:
                canvas = Canvas(root, width =5, height=1)
                #canvas.create_line(0, 0, 0, 15)
                canvas.grid(row=a, column=b)
                spacex += 1
                sem = 1
                if b == 11: # last iteration happens here so reset sem_y to allow checkA to happen again in checkA if statement
                    sem_y = 0
                continue

            if Game.board[a-spacey][b-spacex] == 0:
                temp = Entry(root,width=7, textvariable=entry, justify="center", font=("Calibri",20), relief=SOLID)
            else:
                temp = Entry(root, width=7, textvariable=entry, justify="center", foreground="blue",font=("Calibri", 20), relief=SOLID, state="readonly")
            entry.set(Game.board[a-spacey][b-spacex])
            temp.grid(row=a, column=b, ipady=25, ipadx=0)
            #temp.place(x=a, y=b, width=80, height=80)

            entries.append(temp)
            sem = 0

def check():
    global entries
    Game.solve(Game.board)
    # traverse entries and solved Game.board; if no match then change background to red
    index = 0;
    for i in range(9):

        for j in range(9):

            if entries[index].get() != str(Game.board[i][j]):

                entries[index].config(bg="red3")

            else:
                entries[index].config(bg="white")

            index += 1


def solve():
    global entries
    Game.solve(Game.board)
    #traverse entries and solved Game.board; if no match then change background to red
    index = 0;
    for i in range(9):

        for j in range(9):

            if entries[index].get() != str(Game.board[i][j]):
                entries[index].delete(0 , END)
                entries[index].insert(0,str(Game.board[i][j]))
                entries[index].config(bg="red3")

            index += 1


display_board()
#print(entries[0].config(bg="red3"))# way to change color will be used when number is in incorrect location

check_button = tk.Button(text="check",width=20, height=4, relief=SOLID,bg="blue", font="bold", command=check)
check_button.grid(row=5, column=20)

solve_button = tk.Button(text="solve",width=20, height=4, relief=SOLID,bg="green",command=solve,font="bold")
solve_button.grid(row=8, column=20)






#E1 = Entry(root, text="8")
#E1.grid(row=1, column=1)

#t = Label(root, text=str(Game.board[0][0]))
#t.grid(row=0, column=1)





root.mainloop()