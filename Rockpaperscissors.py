from tkinter import *
from tkinter.ttk import*
import random
def rock_paper(player):
    choice=["rock","paper","scissors"]
    computer=random.choice(choice)
    print("Computer= ",computer)
    print("Player =", player)
    if computer==player:
          result=("Tie!!")
    elif ((player=="rock" and computer=="scissors") or (player=="scissors" and computer=="paper")
         or (player=="paper" and computer=="rock")):
        result=("Player wins!!!")
    else:
       result=("Computer wins!!")
    
    result_label.config(text=f"Player= {player} Computer= {computer}  result= {result}")   


window=Tk()
    
window.title("Rock,paper,scissors")
window.configure(background="Black")
label= Label(window,text="Choose: Rock, Paper, Scissors: ")
result_label=Label(window,text="")



rock_button=Button(window,text="rock",command=lambda: rock_paper("rock"))
paper_button=Button(window,text="paper",command=lambda: rock_paper("paper"))
scissors_button=Button(window,text="scissors",command=lambda: rock_paper("scissors"))

label.pack()
rock_button.pack()
paper_button.pack()
scissors_button.pack()
result_label.pack()

mainloop()