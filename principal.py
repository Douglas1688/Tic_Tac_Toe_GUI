from tkinter import messagebox
import tkinter as tk
from tkinter import *

root = tk.Tk()
#root.geometry("500x500")
root.title("TIC-TAC-TOE")



clicked =True
count = 0


def disable_all_buttons():
    btn1.config(state=DISABLED)
    btn2.config(state=DISABLED)
    btn3.config(state=DISABLED)
    btn4.config(state=DISABLED)
    btn5.config(state=DISABLED)
    btn6.config(state=DISABLED)
    btn7.config(state=DISABLED)
    btn8.config(state=DISABLED)
    btn9.config(state=DISABLED)




def checkifwon():
    global winner
    winner = False
    if btn1["text"] == "X" and btn2["text"] == "X" and btn3["text"]=="X":
        btn1.config(bg="red")
        btn2.config(bg="red")
        btn3.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X  Wins!!")
        disable_all_buttons()

    elif btn4["text"] == "X" and btn5["text"] == "X" and btn6["text"]=="X":
        btn4.config(bg="red")
        btn5.config(bg="red")
        btn6.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X  Wins!!")
        disable_all_buttons()

    elif btn7["text"] == "X" and btn8["text"] == "X" and btn9["text"]=="X":
        btn7.config(bg="red")
        btn8.config(bg="red")
        btn9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X  Wins!!")
        disable_all_buttons()
    elif btn1["text"] == "X" and btn4["text"] == "X" and btn7["text"]=="X":
        btn1.config(bg="red")
        btn4.config(bg="red")
        btn7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X  Wins!!")
        disable_all_buttons()
    elif btn2["text"] == "X" and btn5["text"] == "X" and btn8["text"]=="X":
        btn2.config(bg="red")
        btn5.config(bg="red")
        btn8.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X  Wins!!")
        disable_all_buttons()
    elif btn3["text"] == "X" and btn6["text"] == "X" and btn9["text"]=="X":
        btn3.config(bg="red")
        btn6.config(bg="red")
        btn9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X  Wins!!")
        disable_all_buttons()
    elif btn1["text"] == "X" and btn5["text"] == "X" and btn9["text"]=="X":
        btn1.config(bg="red")
        btn5.config(bg="red")
        btn9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X  Wins!!")
        disable_all_buttons()
    elif btn3["text"] == "X" and btn5["text"] == "X" and btn7["text"]=="X":
        btn3.config(bg="red")
        btn5.config(bg="red")
        btn7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X  Wins!!")
        disable_all_buttons()
    elif btn1["text"] == "O" and btn2["text"] == "O" and btn3["text"]=="O":
        btn1.config(bg="red")
        btn2.config(bg="red")
        btn3.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O  Wins!!")
        disable_all_buttons()

    elif btn4["text"] == "O" and btn5["text"] == "O" and btn6["text"]=="O":
        btn4.config(bg="red")
        btn5.config(bg="red")
        btn6.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O  Wins!!")
        disable_all_buttons()

    elif btn7["text"] == "O" and btn8["text"] == "O" and btn9["text"]=="O":
        btn7.config(bg="red")
        btn8.config(bg="red")
        btn9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O  Wins!!")
        disable_all_buttons()
    elif btn1["text"] == "O" and btn4["text"] == "O" and btn7["text"]=="O":
        btn1.config(bg="red")
        btn4.config(bg="red")
        btn7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O  Wins!!")
        disable_all_buttons()
    elif btn2["text"] == "O" and btn5["text"] == "O" and btn8["text"]=="O":
        btn2.config(bg="red")
        btn5.config(bg="red")
        btn8.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O  Wins!!")
        disable_all_buttons()
    elif btn3["text"] == "O" and btn6["text"] == "O" and btn9["text"]=="O":
        btn3.config(bg="red")
        btn6.config(bg="red")
        btn9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O  Wins!!")
        disable_all_buttons()
    elif btn1["text"] == "O" and btn5["text"] == "O" and btn9["text"]=="O":
        btn1.config(bg="red")
        btn5.config(bg="red")
        btn9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O  Wins!!")
        disable_all_buttons()
    elif btn3["text"] == "O" and btn5["text"] == "O" and btn7["text"]=="O":
        btn3.config(bg="red")
        btn5.config(bg="red")
        btn7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O  Wins!!")
        disable_all_buttons()


    if count == 9 and winner == False:
        messagebox.showinfo("Tic Tac Toe", "It's a Tie!!\nNo one wins!!")
        disable_all_buttons()


def b_click(b):
    global clicked, count
    if b["text"] ==" " and clicked == True:
        b["text"] = "X"
        clicked = False
        count+=1
        checkifwon()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count +=1
        checkifwon()
    else:
        messagebox.showerror("Tic Tac Toe", "Hey!, That box has alredy been selected\nPick Another box")

def reset():
    global btn1, btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9
    global clicked, count
    count=  0

    btn1 = Button(root,text=" ", font=("Helvetica", 20), height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(btn1))
    btn2 = Button(root,text=" ", font=("Helvetica", 20), height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(btn2))
    btn3 = Button(root,text=" ", font=("Helvetica", 20), height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(btn3))

    btn4 = Button(root,text=" ", font=("Helvetica", 20), height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(btn4))
    btn5 = Button(root,text=" ", font=("Helvetica", 20), height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(btn5))
    btn6 = Button(root,text=" ", font=("Helvetica", 20), height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(btn6))

    btn7 = Button(root,text=" ", font=("Helvetica", 20), height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(btn7))
    btn8 = Button(root,text=" ", font=("Helvetica", 20), height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(btn8))
    btn9 = Button(root,text=" ", font=("Helvetica", 20), height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(btn9))

    btn1.grid(row=0,column=0)
    btn2.grid(row=0,column=1)
    btn3.grid(row=0,column=2)

    btn4.grid(row=1,column=0)
    btn5.grid(row=1,column=1)
    btn6.grid(row=1,column=2)

    btn7.grid(row=2,column=0)
    btn8.grid(row=2,column=1)
    btn9.grid(row=2,column=2)


my_menu = Menu(root)
root.config(menu=my_menu)

option_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label= "Options", menu=option_menu)
option_menu.add_command(label="Rest Game",command=reset)

reset()
root.mainloop()