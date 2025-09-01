# step1 : Importing
from tkinter import *


# Step2 : GUI Interaction
window = Tk()
window.geometry("700x500")
window.config(bg="white")


# Step3 : Adding INputs


# Input Box


e = Entry(window, width=50, border=3)
e.config(bg="white")
e.place(x=0, y=0)


# Button config for better clickability


button_config = {
   "width": 8,
   "height": 1,
   "relief": "raised",
   "bd": 2,
   "bg":"#e8e8e8",
   "activebackground":"#d4e8fc",
   "font":("SF Pro Text", 12),  # macOS system font
   "padx":5,  # Internal padding
   "pady":5
}


# Button Functionality
def click(num):
   result = e.get()
   e.delete(0, END)
   e.insert(0, str(result) + str(num))


# Buttons
b = Button(window, text= "1", **button_config, command=lambda:click(1))
b.place(x=10, y=60)


b = Button(window, text= "2", **button_config, command=lambda:click(2))
b.place(x=115, y=60)


b = Button(window, text= "3", **button_config, command=lambda:click(3))
b.place(x=220, y=60)


b = Button(window, text= "4", **button_config, command=lambda:click(4))
b.place(x=10, y=90)


b = Button(window, text= "5", **button_config, command=lambda:click(5))
b.place(x=115, y=90)


b = Button(window, text= "6", **button_config, command=lambda:click(6))
b.place(x=220, y=90)


b = Button(window, text= "7", **button_config, command=lambda:click(7))
b.place(x=10, y=120)


b = Button(window, text= "8", **button_config, command=lambda:click(8))
b.place(x=115, y=120)


b = Button(window, text= "9", **button_config, command=lambda:click(9))
b.place(x=220, y=120)


b = Button(window, text= "0", **button_config, command=lambda:click(0))
b.place(x=10, y=150)


# operator functions:


def add():
   n1 = e.get()
   global math
   math = "addition"
   global i
   i = int(n1)
   e.delete(0, END)


b = Button(window, text= "+", **button_config, command=add)
b.place(x=115, y=150)


def sub():
   n1 = e.get()
   global math
   math = "substraction"
   global i
   i = int(n1)
   e.delete(0, END)


b = Button(window, text= "-", **button_config, command=sub)
b.place(x=220, y=150)


def mult():
   n1 = e.get()
   global math
   math = "multiplication"
   global i
   i = int(n1)
   e.delete(0, END)


b = Button(window, text= "*", **button_config, command=mult)
b.place(x=10, y=180)


def div():
   n1 = e.get()
   global math
   math = "division"
   global i
   i = int(n1)
   e.delete(0, END)


b = Button(window, text= "/", **button_config, command=div)
b.place(x=115, y=180)


def equal():
   n2 = e.get()
   e.delete(0, END)
   if math == 'addition':
       e.insert(0, i + int(n2))
   elif math == 'substraction':
       e.insert(0, i - int(n2))
   elif math == 'multiplication':
       e.insert(0, i * int(n2))
   elif math == 'division':
       e.insert(0, i / int(n2))


b = Button(window, text= "=", **button_config, command=equal)
b.place(x=220, y=180)


def clear():
   e.delete(0, END)


b = Button(window, text= "Clear", **button_config, command=clear)
b.place(x=10, y=211)


mainloop()

