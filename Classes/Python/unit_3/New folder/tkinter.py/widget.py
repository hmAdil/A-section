import tkinter
from tkinter import *
from tkinter import messagebox

# Create the main window
win = Tk()
win.title("adaRSH")
win.geometry('500x600')

# Define button click functions
def click_green():
    messagebox.showinfo("Message", "Green button clicked")

def click_blue():
    messagebox.showinfo("Message", "Blue button clicked")

def click_red():
    messagebox.showinfo("Message", "Red button clicked")

def click_yellow():
    messagebox.showinfo("Message", "Yellow button clicked")

# Create buttons with text and commands
a = Button(win, text="Green", bg="green", fg="black", pady=10, command=click_green)
b = Button(win, text="Yellow", bg="yellow", fg="black", pady=10, command=click_yellow)
c = Button(win, text="Blue", bg="blue", fg="black", pady=10, command=click_blue)
d = Button(win, text="Red", bg="red", fg="black", pady=10, command=click_red)

# Arrange buttons on the window
a.pack(side=TOP)
b.pack(side=BOTTOM)
c.pack(side=RIGHT)
d.pack(side=LEFT)

# Run the application
win.mainloop()


import tkinter 
from tkinter import *
from tkinter import messagebox
win=Tk()
win.title("ADARSH COLLECTIONS")
win.geometry("1000x1000")


import tkinter
from tkinter import *
from tkinter import messagebox

# Create the main window
win = Tk()
win.title("adaRSH")
win.geometry('500x600')

# Define button click functions
def click_green():
    messagebox.showinfo("Message", "Green button clicked")

def click_blue():
    messagebox.showinfo("Message", "Blue button clicked")

def click_red():
    messagebox.showinfo("Message", "Red button clicked")

def click_yellow():
    messagebox.showinfo("Message", "Yellow button clicked")

# Create buttons with text and commands
a = Button(win, text="Green", bg="green", fg="black", pady=10, command=click_green)
b = Button(win, text="Yellow", bg="yellow", fg="black", pady=10, command=click_yellow)
c = Button(win, text="Blue", bg="blue", fg="black", pady=10, command=click_blue)
d = Button(win, text="Red", bg="red", fg="black", pady=10, command=click_red)

# Arrange buttons on the window
a.pack(side=TOP)
b.pack(side=BOTTOM)
c.pack(side=RIGHT)
d.pack(side=LEFT)

# Run the application
win.mainloop()

