# Eric Schemenauer, Advanced Calculator, 9/21/2022, Vic High

import tkinter as tk
import tkinter.font as font
import decimal as dec

window = tk.Tk()
window.title("Advanced Calculator")

# define font
myFont = font.Font(family="Courier", size=20, weight="bold")

# making text box
txtDisplay = tk.Entry(window, width=21, borderwidth=5, font=myFont)
txtDisplay.grid(row=0, column=0, columnspan=4)

# making variables in class
class State:
    first_number = 0 
    second_number = 0 
    operation = 0
    final_answer = 0
    line = ''


# making more variables for operators


MULT = 1
DIV = 2
ADD = 3
SUB = 4


# clear the text box then insert line variable
def update_line(LINE):
    txtDisplay.delete(0, tk.END)
    txtDisplay.insert(0, LINE)

# when number clicked add the number to the line and update then line
def button_clicked(button_value):
    State.line = State.line+button_value
    update_line(State.line)

# when operator clicked set first number to line
# switch to Decimal type
def operation_pressed(operator):
    State.operation = dec.Decimal(operator)
    State.first_number = dec.Decimal(State.line)
    State.line = ''
    update_line(State.line)

# make line empty string then update line
def clear():
    State.line = ''
    update_line(State.line)

# set variables to default and update line
def full_clear():
    clear()
    State.first_number = 0
    State.operation = 0
    State.second_number = 0
    State.final_answer = 0

# remove last character from line and update line
def delete():
    State.line = State.line[:-1]
    update_line(State.line)

# multiply line by -1 and update line
def negative():
    State.line = dec.Decimal(State.line)*-1
    State.line = str(State.line)
    update_line(State.line)

# selects command for each button depending on label
def do_command(label, operator):
    if operator is label:
        if label == 'C':
            clear()
        elif label == 'CE':
            full_clear()
        elif label == 'del':
            delete()
        elif label == '(-)':
            negative()
        elif label == '=':
            equals()
        else:
            button_clicked(label)
    else:
        operation_pressed(operator)


# makes button with no kwargs right now
def make_btn(label, padding=None, operator=None):
#    for args in kwargs.values():
#        padding = padx
    if padding is None:
        PADX = 20
    else:
        PADX = padding
    if operator is None:
        operator = label
    return tk.Button(
        window,
        text=label,
        padx=PADX,
        pady=10,
        font=myFont,
        command=lambda: do_command(label, operator),
    )


def equals():
    # sets second number to Decimal type
    State.second_number = dec.Decimal(State.line)
    # clears text box then checks if first number was inputted
    # if inputted checks operation value and does correct operation
    txtDisplay.delete(0, tk.END)
    # if first number was not entered just return second number
    if State.first_number != 0:
        # if first number is not 0 than proceed to the operation
        if State.operation == 1:
            State.final_answer = State.first_number * State.second_number
        elif State.operation == 2:
            # if dividing by zero print math error
            if State.second_number == 0:
                State.line = 'Math error'
                update_line(State.line)
                return
            else:
                State.final_answer = State.first_number / State.second_number
        elif State.operation == 3:
            State.final_answer = State.first_number + State.second_number
        elif State.operation == 4:
            State.final_answer = State.first_number - State.second_number
        # update line to be the final answer then update line
        State.line = str(State.final_answer)
        update_line(State.line)
    elif State.first_number == 0:
        update_line(State.line)
    # set variables back to default
    State.first_number = 0
    State.second_number = 0
    State.operation = 0
    State.final_answer = 0


# making buttons
btn1 = make_btn('1')
btn2 = make_btn('2')
btn3 = make_btn('3')
btn4 = make_btn('4')
btn5 = make_btn('5')
btn6 = make_btn('6')
btn7 = make_btn('7')
btn8 = make_btn('8')
btn9 = make_btn('9')
btn0 = make_btn('0')

# operator buttons in form (label, padx, operation)
btnadd = make_btn('+', 20, ADD)
btnsub = make_btn('-', 20, SUB)
btnmult = make_btn('*', 20, MULT)
btndiv = make_btn('÷', 20, DIV)
btnCE = make_btn('CE', 12)
btnC = make_btn('C')
btnperiod = make_btn('.')
btnequal = make_btn('=')
btndel = make_btn('del', 4)
btnnegative = make_btn('(-)', 4)

# placing buttons in grid
btnCE.grid(row=1, column=0)
btndiv.grid(row=6, column=2)
btndel.grid(row=1, column=2)
btnC.grid(row=1, column=3)
btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)
btnmult.grid(row=2, column=3)
btn4.grid(row=3, column=0)
btn5.grid(row=3, column=1)
btn6.grid(row=3, column=2)
btnsub.grid(row=4, column=3)
btn4.grid(row=4, column=0)
btn5.grid(row=4, column=1)
btn6.grid(row=4, column=2)
btn1.grid(row=5, column=0)
btn2.grid(row=5, column=1)
btn3.grid(row=5, column=2)
btnadd.grid(row=5, column=3)
btnperiod.grid(row=6, column=0)
btn0.grid(row=6, column=1)
btnequal.grid(row=6, column=3)
btnnegative.grid(row=1, column=1)



# Stop tkinter window from immediately closing
tk.mainloop()