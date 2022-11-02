import random
import tkinter as tk
import tkinter.font as font
from PIL import Image, ImageTk
import os


class State:
    dice_number = None


# make our tkinter window
window = tk.Tk()
window.title("Number Guessing Game")

# we find the path to the script and
# then use dirname to go one directory up
# for me this goes from python_projects/random_dice/random_dice.py
# and then dirname goes up to python_projects/random_dice
path_parent = os.path.dirname(__file__)

# this finds what image is being requested
def image_finder(label):
    return ImageTk.PhotoImage(file=os.path.join(path_parent, "dice_images", label))


# this randomly generates a number and then configures
# the label to the new picture
def roll_dice():
    result = random.randint(1, 6)
    State.dice_number = result
    label_2.configure(image=image_selector())


# this just returns whatever picture in the dictionary
# depending on what number is rolled
def image_selector():
    return dice_images[State.dice_number]


# this is a dictionary to store all our pictures
dice_images = {}
dice_images[1] = image_finder("Alea_1.png")
dice_images[2] = image_finder("Alea_2.png")
dice_images[3] = image_finder("Alea_3.png")
dice_images[4] = image_finder("Alea_4.png")
dice_images[5] = image_finder("Alea_5.png")
dice_images[6] = image_finder("Alea_6.png")


# font - I define a font and call it myFont
myFont = font.Font(family="Courier", size=20, weight="bold")

# label for instructions
label_1 = tk.Label(window, text="Roll the Dice", font=myFont)
label_1.grid(row=0, column=0, columnspan=2)
# label that holds our image"""  """
label_2 = tk.Label(window, image=dice_images[1])
label_2.grid(row=1, column=0, columnspan=2)


# Create button #1
btn1 = tk.Button(window, text="Roll", font=myFont, command=roll_dice)
btn1.grid(row=4, column=0, columnspan=2)

window.mainloop()
