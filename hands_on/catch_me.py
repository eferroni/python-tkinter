from random import randrange
import tkinter as tk
from turtle import width

def jumps(event=None):
    global x, y
    new_x, new_y = x, y
    while new_x - x < 75 and new_y - y < 75:
        new_x = randrange(0, 440)
        new_y = randrange(0, 440)

    button.place(x=new_x, y=new_y)

window = tk.Tk()
window.geometry("500x500")
window.resizable(width=False, height=False)

button = tk.Button(window, text="Catch me!")
x = y = 10
button.place(x=x, y=y)
button.bind("<Enter>", jumps)

window.mainloop()