from tkinter import *
from PIL import ImageTk, Image
import random

#choice section
def userChoiceRock():
    userChoice = "rock"
    turn(userChoice)
    userImage.configure(image = rock)

def userChoicePaper():
    userChoice = "paper"
    turn(userChoice)
    userImage.configure(image = paper)

def userChoiceScissors():
    userChoice = "scissors"
    turn(userChoice)
    userImage.configure(image = scissors)

#gameplay setion
def turn(userChoice):
    Comp = ['rock', 'paper', 'scissors']
    CompChoice = random.choice(Comp)
    if(CompChoice == 'rock'):
        CompImage.configure(image = rock)
    elif(CompChoice == 'paper'):
        CompImage.configure(image = paper)
    else:
        CompImage.configure(image = scissors)

    if(CompChoice == userChoice):
        turnResult.configure(text = "It's a draw.", fg = "gray")
        compare.configure(text = "=")
    elif((CompChoice == 'rock' and userChoice == 'scissors') or (CompChoice == 'paper' and userChoice == 'rock') or (CompChoice == 'scissors' and userChoice == 'paper')):
        turnResult.configure(text = "You Lost, Computer Won!", fg = "red")
        compare.configure(text="<")
    else:
        turnResult.configure(text = "You win, Computer Lost!", fg = "green")
        compare.configure(text = ">")

#window
w = Tk()
w.title('Rock Paper Scissors')
icon_picture = PhotoImage(file = 'game_icon.png')
w.iconphoto(False, icon_picture)

label1 = Label(w, text= 'WELCOME TO ROCK PAPER SCISSORS GAME',justify='center',compound='center',font = ("Comic Sans MS", 20))
label2 = Label(w, text= 'User What is Your Choice??',justify='center',compound='center',font = ("Comic Sans MS", 20))

#Button and Image
rock = ImageTk.PhotoImage(Image.open('rock.png'))
rock_button = Button(w,image= rock,height=200,width=200,command=userChoiceRock)
paper = ImageTk.PhotoImage(Image.open('paper.png'))
paper_button = Button(w,image= paper,height=200,width=200,command=userChoicePaper)
scissors = ImageTk.PhotoImage(Image.open('scissors.png'))
scissors_button = Button(w,image= scissors,height=200,width=200,command=userChoiceScissors)
userImage = Label(image = rock)
userImage.image = rock
compare = Label(w, justify = CENTER,font = ("Comic Sans MS", 20))
CompImage = Label(image = paper)
CompImage.image = paper
turnResult = Label(w, width = 20, justify = CENTER,font = ("Comic Sans MS", 20))

#Grid
label1.grid(row=0,column=0,columnspan=3)
label2.grid(row=1,column=0,columnspan=3)
rock_button.grid(row=3,column=0)
paper_button.grid(row=3,column=1)
scissors_button.grid(row=3,column=2)
userImage.grid(row = 4, column = 0)
compare.grid(row = 4, column = 1)
CompImage.grid(row = 4, column = 2)
turnResult.grid(row = 5, column = 1)

w.mainloop()

