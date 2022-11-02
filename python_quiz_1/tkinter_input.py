import tkinter as tk
import tkinter.font as font


root = tk.Tk()
root.title('Python Tkinter Input')

number_input = None

def update_number():
    number_input = txtinput.get()
    txtinput.delete(0, tk.END)
    label1.configure(text=number_input)

myFont = font.Font(family="Courier", size=20, weight="bold")
txtinput = tk.Entry(root, width=21, borderwidth=5, font=myFont)
txtinput.grid(row=0, column=0, columnspan=4)

label1 = tk.Label(root, text=number_input, font=myFont)
label1.grid(row=5, column=0, columnspan=4)


button = tk.Button(root, width=21, borderwidth=5, font=myFont,text='Update Number', command=update_number)
button.grid(row=2, column=0, columnspan=4)

tk.mainloop()