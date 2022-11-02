import random
import os
import tkinter as tk
import tkinter.font as font
from PIL import ImageTk, Image

# flake8: noqa

class State:
    dice_number = None


def image_selector():
    return dice_images[State.dice_number]



def roll_dice():
    result = random.randint(1, 6)
    State.dice_number = result
    label_3.configure(image=image_selector())



window = tk.Tk()
window.title("Dice Roller")

script_dir = os.path.dirname(__file__)
IMAGE_PATH = os.path.join(script_dir, "dice_images")

def load_image(name):
    return ImageTk.PhotoImage(file=os.path.join(IMAGE_PATH, name))

dice_images = {}
dice_images[1] = load_image("Alea_1.png")
dice_images[2] = load_image("Alea_2.png")
dice_images[3] = load_image("Alea_a3.png")
dice_images[4] = load_image("Alea_4.png")
dice_images[5] = load_image("Alea_5.png")
dice_images[6] = load_image("Alea_a6.png")


# font - I define a font and call it myFont
myFont = font.Font(family="Courier", size=20, weight="bold")

label_1 = tk.Label(window, text="Roll the Dice", font=myFont)
label_1.grid(row=0, column=0, columnspan=2)

# Create button #1
btn1 = tk.Button(window, text="Roll", font=myFont, command=roll_dice)
btn1.grid(row=4, column=0, columnspan=2)


# Create 3rd label used for OUTPUT display
label_3 = tk.Label(window, image=dice_images[1])
label_3.grid(row=5, column=0, columnspan=2)

window.mainloop()
