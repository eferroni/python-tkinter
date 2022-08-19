import tkinter as tk
from tkinter import messagebox

def click(event=None):
    global switch
    if switch:
        button2.config(command=lambda:None)
        button2.config(text="Gee!")
    else:
        button2.config(command=peekaboo)
        button2.config(text="Peekaboo!")
    switch = not switch

def peekaboo():
    messagebox.showinfo("", "PEEKABOO")

switch = True
window = tk.Tk()

button1 = tk.Button(window, text="On/Off", command=click)
button1.pack()

button2 = tk.Button(window, text="Peekaboo!", command=peekaboo)
button2.pack()

window.mainloop()
