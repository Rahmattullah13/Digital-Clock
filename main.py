from tkinter import*
from tkinter import font
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")

def time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(100, time)
    
label = Label(root, font=("Jetbrains Mono", 80), background="Black", foreground="cyan")
label.pack(anchor="center")
time()

mainloop()