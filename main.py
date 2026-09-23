# TKinter Rock Paper Scissors


# VARIABLE CONTROL SETTINGS
import customtkinter as ctk
import random as rand
import time
from PIL import Image
root = ctk.CTk()
score = [0, 0, 0]
result = ['You Win', 'Draw', 'You Loose']
C_Input_Text = ['I Chose Rock', 'I Chose Paper', 'I Chose Scissors']


# CANVAS CONTROL SETTINGS
countdown_colour = 'orange'
main_bg_colour = 'purple'
width1 = 800 # Window Width
height1 = 600 # Window Height
canvas = ctk.CTkCanvas(root, width=width1, height=height1, bg=main_bg_colour)
root.attributes("-fullscreen")
root.configure(fg_color=main_bg_colour)
root.title(" Rock Paper Scissors App ") 
canvas.pack(fill="both", expand=True)
computer_token = None 

res_label = ctk.CTkLabel(root, text="", bg_color=main_bg_colour, font=("Comic Sans", 30))               
canvas.create_window(300,400, window=res_label) 

c_res_label = ctk.CTkLabel(root, text="", bg_color=main_bg_colour, font=("Comic Sans", 30))               
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
    rock_button=ctk.CTkButton(root, text='Rock', command=rock, bg_color='lime', fg_color='black', font=('Comic Sans', 9, 'bold'),width=15)
    canvas.create_window(90, 190, window=rock_button)

    paper_button=ctk.CTkButton(root, text='Paper', command=paper, bg_color='yellow', fg_color='black', font=('Comic Sans', 9, 'bold'),width=15)
    canvas.create_window(90, 220, window=paper_button)

    scissors_button=ctk.CTkButton(root, text='Scissors', command=scissors, bg_color='orange', fg_color='black', font=('Comic Sans', 9, 'bold'),width=15)
    canvas.create_window(90, 250, window=scissors_button)
    

def loadImage(raw_token):
    computer_token = ctk.CTkImage(light_image=raw_token, dark_image=raw_token, size=(100, 100)) 
    label1 = ctk.CTkLabel(root, image=computer_token, bg_color='purple')
    label1.place(x=425, y=0)

def rock(): # ROCK CONTROL SETTINGS   
    C_Input = rand.randint(1,3)  
    raw_token = Image.open("assets/rock.png")
    loadImage(raw_token)
    
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
    loadImage(raw_token)
    
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
    loadImage(raw_token)
    
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
    
    wins = ctk.CTkLabel(root, text=("Wins: "+ str(score[0])), bg_color=main_bg_colour, font=("Comic Sans", 30))
    canvas.create_window(300,100, window=wins)
    
    draws = ctk.CTkLabel(root, text=("Draws: "+str(score[1])), bg_color=main_bg_colour, font=("Comic Sans", 30))
    canvas.create_window(300,200, window=draws)
    
    losses = ctk.CTkLabel(root, text=("Losses: "+str(score[2])), bg_color=main_bg_colour, font=("Comic Sans", 30))
    canvas.create_window(300,300, window=losses)

countdown()
root.mainloop()