# TKinter Rock Paper Scissors


# VARIABLE CONTROL SETTINGS
import tkinter as tk
import random as rand
import time
from PIL import Image, ImageTk
root = tk.Tk()
score = [0, 0, 0]
result = ['You Win', 'Draw', 'You Loose']
C_Input_Text = ['I Chose Rock', 'I Chose Paper', 'I Chose Scissors']


# CANVAS CONTROL SETTINGS
countdown_colour = 'orange'
main_bg_colour = 'purple'
width1 = 800 # Window Width
height1 = 600 # Window Height
canvas = tk.Canvas(root, width=width1, height=height1, bg=main_bg_colour)
root.attributes("-fullscreen", True)
root.configure(bg=main_bg_colour)
root.title(" Rock Paper Scissors App ") 
canvas.pack(fill="both", expand=True)
computer_token = None 

res_label = tk.Label(root, text="", bg=main_bg_colour, font=("Comic Sans", 30))               
canvas.create_window(300,400, window=res_label) 

c_res_label = tk.Label(root, text="", bg=main_bg_colour, font=("Comic Sans", 30))               
canvas.create_window(300,500, window=c_res_label)

def countdown(count=3): 
    time.sleep(1)
    res=f"{count}.."

    if(count!=0):
        res_label.configure(text=res)
        root.after(1000, countdown, count-1)

    else:
        res_label.configure(text="GO!")
        root.after(1000, main)

"""
Loads and displays the action buttons (R, P, S)
"""
def main():
    rock_button=tk.Button(root, text='Rock', command=rock, bg='lime', fg='black', font=('Comic Sans', 9, 'bold'),width=15)
    canvas.create_window(90, 190, window=rock_button)

    paper_button=tk.Button(root, text='Paper', command=paper, bg='yellow', fg='black', font=('Comic Sans', 9, 'bold'),width=15)
    canvas.create_window(90, 220, window=paper_button)

    scissors_button=tk.Button(root, text='Scissors', command=scissors, bg='orange', fg='black', font=('Comic Sans', 9, 'bold'),width=15)
    canvas.create_window(90, 250, window=scissors_button)
    
def loadImage(raw_token, c_choice):
    global user_token
    global computer_token
    raw_token = raw_token.resize((100, 100))
    user_token = ImageTk.PhotoImage(raw_token) 
    label1 = tk.Label(root, image=user_token, bg='purple')
    label1.place(x=425, y=100)

    if(c_choice == 1): computer_raw_token = Image.open("assets/rock.png")
    elif(c_choice == 2): computer_raw_token = Image.open("assets/paper.jpg")
    else: computer_raw_token = Image.open("assets/scissor.jpg")
    computer_raw_token = computer_raw_token.resize((100, 100))
    computer_token = ImageTk.PhotoImage(computer_raw_token) 
    label2 = tk.Label(root, image=computer_token, bg='purple')
    label2.place(x=425, y=300)

    label3 = tk.Label(root, text="V", bg='purple', font=("Helvetica", 24))
    label3.place(x=425, y=220)
    
def rock(): # ROCK CONTROL SETTINGS   
    C_Input = rand.randint(1,3)  
    raw_token = Image.open("assets/rock.png")
    loadImage(raw_token, C_Input)
    
    if C_Input==1:
        res=result[1]
        score[1]+=1
        c_res=C_Input_Text[0]
        
    elif C_Input==2:
        res=result[2]
        score[2]+=1
        c_res=C_Input_Text[1]
     
    elif C_Input==3:
        res=result[0]
        score[0]+=1
        c_res=C_Input_Text[2]
    
    scores()
 
    res_label.configure(text=res)
    c_res_label.configure(text=c_res)

def paper(): # PAPER CONTROL SETTINGS 
    C_Input = rand.randint(1,3)

    raw_token = Image.open("assets/paper.jpg")
    loadImage(raw_token, C_Input)
    
    if C_Input==1:
        res=result[0]
        score[0]+=1
        c_res=C_Input_Text[0]
    
    elif C_Input==2:
        res=result[1]
        score[1]+=1
        c_res=C_Input_Text[1]
       
    elif C_Input==3:
        res=result[2]
        score[2]+=1
        c_res=C_Input_Text[2]
    
    scores()

    res_label.configure(text=res)
    c_res_label.configure(text=c_res)
    
def scissors(): # SCISSORS CONTROL SETTINGS 
    C_Input = rand.randint(1,3)
    
    raw_token = Image.open("assets/scissor.jpg")
    loadImage(raw_token, C_Input)
    
    if C_Input==1:
        res=result[2]
        score[2]+=1
        c_res=C_Input_Text[0]
       
    elif C_Input==2:
        res=result[0]
        score[0]+=1
        c_res=C_Input_Text[1]
        
    elif C_Input==3:
        res=result[1]
        score[1]+=1
        c_res=C_Input_Text[2]
        
    scores()

    res_label.configure(text=res)
    c_res_label.configure(text=c_res)
 
def scores(): # SCORE DISPLAY CONTROL SETTINGS
    
    wins = tk.Label(root, text=("Wins: "+ str(score[0])), bg=main_bg_colour, font=("Comic Sans", 30))
    canvas.create_window(300,100, window=wins)
    
    draws = tk.Label(root, text=("Draws: "+str(score[1])), bg=main_bg_colour, font=("Comic Sans", 30))
    canvas.create_window(300,200, window=draws)
    
    losses = tk.Label(root, text=("Losses: "+str(score[2])), bg=main_bg_colour, font=("Comic Sans", 30))
    canvas.create_window(300,300, window=losses)

countdown()
root.mainloop()