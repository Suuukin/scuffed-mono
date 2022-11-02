import random
import tkinter as tk
import tkinter.font as font
import PIL import ImageTk,Image 


class State:
    dice_number = None


def roll_dice():
    result = random.randint(1,6)
    State.dice_number = result



def image_selector():
    return 
    

canvas = tk.Canvas(tk.Tk(), width = 300, height = 300)      
canvas.pack()   


dice_1 = tk.ImageTk.Photoimage(file="Alea_1.png")
dice_2 = tk.ImageTk.Photoimage(file="Alea_2.png")
dice_3 = tk.ImageTk.Photoimage(file="Alea_3.png")
dice_4 = tk.ImageTk.Photoimage(file="Alea_4.png")
dice_5 = tk.ImageTk.Photoimage(file="Alea_5.png")
dice_6 = tk.ImageTk.Photoimage(file="Alea_6.png")


window = tk.Tk()
window.title("Number Guessing Game")

#font - I define a font and call it myFont
myFont = font.Font(family='Courier', size=20, weight='bold')

label_1 = tk.Label(window, text="Roll the Dice",font=myFont)
label_1.grid(row=0, column=0, columnspan=2)

#Create button #1 
btn1 = tk.Button(window, text="Roll", font=myFont, command=roll_dice)
btn1.grid(row=4, column=0, columnspan=2)


#Create 3rd label used for OUTPUT display
label_3 = tk.Label(window,text="", font=myFont)
label_3.grid(row=5, column=0, columnspan=2)

tk.mainloop()