from curses import window
import tkinter as tk
from tkinter import messagebox

def show():
    messagebox.showinfo("", f"counter={counter}, state={switch.get()}")

def count():
    global counter
    counter += 1


window = tk.Tk()

switch = tk.IntVar()
counter = 0

button = tk.Button(window, text="Show", command=show)
button.pack()

check_button = tk.Checkbutton(window, text="Tick", variable=switch, command=count)
check_button.pack()

window.mainloop()