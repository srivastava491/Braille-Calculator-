# This is a calculator for blind people if you right click on a button it will dictate whats written on it and left click will select the button

from tkinter import *
import math
import subprocess
import sys
try:
    import pyttsx3
except ImportError:
    print("pyttsx3 module not found. Installing...")

    # Install pyttsx3 using pip
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyttsx3"])

    import pyttsx3


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def rightclick(btn):
    if btn == chr(8731):
        btn = "cube root"
    elif btn == "x\u02b8":
        btn = "x to the power y"
    elif btn == "x\u00B3":
        btn = "x to the power 3"
    elif btn == "x\u00B2":
        btn = "x to the power 2"
    elif btn == chr(247):
        btn = "divide"
    elif btn == "x!":
        btn = "factorial"
    elif btn == "(":
        btn = "left sqaure bracket"
    elif btn == ")":
        btn = "right sqaure bracket"
    elif btn == "BKSP":
        btn = "Backspace"
    elif btn == "CE":
        btn = "clear"
    elif btn == ".":
        btn = "dot"
    elif btn == "%":
        btn = "Modulus"
    speak(btn)


def click(value):
    ex = entryField.get()
    answer = ''

    try:
        if value == 'BKSP':
            ex = ex[0:len(ex) - 1]
            entryField.delete(0, END)
            entryField.insert(0, ex)
            return

        elif value == 'CE':
            entryField.delete(0, END)

        elif value == '√':
            answer = math.sqrt(eval(ex))

        elif value == 'π' and len(ex) == 0:
            answer = math.pi

        elif value == 'cos θ':
            answer = math.cos(math.radians(eval(ex)))

        elif value == 'tan θ':
            answer = math.tan(math.radians(eval(ex)))

        elif value == 'sin θ':
            answer = math.sin(math.radians(eval(ex)))

        elif value == '2π' and len(ex) == 0:
            answer = 2 * math.pi

        elif value == 'cos h':
            answer = math.cosh(eval(ex))

        elif value == 'tan h':
            answer = math.tanh(eval(ex))

        elif value == 'sin h':
            answer = math.sinh(eval(ex))

        elif value == chr(8731):
            answer = eval(ex) ** (1 / 3)

        elif value == 'x\u02b8':
            entryField.insert(END, '**')
            return

        elif value == 'x\u00B3':
            answer = eval(ex) ** 3

        elif value == 'x\u00B2':
            answer = eval(ex) ** 2

        elif value == 'ln':
            answer = math.log(math.e, eval(ex))

        elif value == 'deg':
            answer = math.degrees(eval(ex))

        elif value == "rad":
            answer = math.radians(eval(ex))

        elif value == 'e' and len(ex) == 0:
            answer = math.e

        elif value == 'log₁₀':
            answer = math.log10(eval(ex))

        elif value == 'x!':
            answer = math.factorial(eval(ex))

        elif value == chr(247):
            entryField.insert(END, "/")
            return


        elif value == '=':
            try:
                answer = eval(ex)
            except ZeroDivisionError:
                entryField.delete(0, END)
                entryField.insert(0, "Cannot divide by zero")
                return
        else:
            if value == 'π':
                value = math.pi
            elif value == '2π':
                value = 2 * math.pi
            elif value == 'e':
                value = math.e
            entryField.insert(END, value)
            return
        entryField.delete(0, END)
        entryField.insert(0, answer)
        speak(answer)

    except SyntaxError:
        pass


def on_enter(event):
    ex = entryField.get()
    answer = eval(ex)
    entryField.delete(0, END)
    entryField.insert(0, answer)
    speak(answer)


def on_backspace(event):
    ex = entryField.get()
    ex = ex[0:len(ex) - 1]
    entryField.delete(0, END)
    entryField.insert(0, ex)


root = Tk()
root.title('Braille Calculator')
root.config(bg='dodgerblue3')
root.geometry('680x486+100+100')

entryField = Entry(root, font=('arial', 20, 'bold'), bg='dodgerblue3', fg='white', bd=10, relief=SUNKEN, width=30)
entryField.grid(row=0, column=0, columnspan=8)

button_text_list = [
    "BKSP", "CE", "√", "+", "π", "cos θ", "tan θ", "sin θ",
    "1", "2", "3", "-", "2π", "cos h", "tan h", "sin h",
    "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
    "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
    "0", ".", "%", "=", "log₁₀", "(", ")", "x!"
]

rowvalue = 1
columnvalue = 0

for i in button_text_list:
    button = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg='dodgerblue3', fg='white',
                    font=('arial', 18, 'bold'), activebackground='dodgerblue3')
    button.bind("<Button-1>", lambda event, i=i: click(i))
    button.bind("<Button-3>", lambda event, i=i: rightclick(i))
    button.grid(row=rowvalue, column=columnvalue, pady=1)
    columnvalue += 1
    if columnvalue > 7:
        rowvalue += 1
        columnvalue = 0

root.bind("<Return>", on_enter)
root.bind("<BackSpace>", on_backspace)
root.mainloop()

# TEAM MEMBERS:
# RIDHI TUTEJA 12213084
# MRUNMAI AJIT LAKADHE 12213086
# ASHIRVAD DAS 12213099
# SAKSHAM KUMAR 12213103
# AARAV SRIVASTAVA 12213161