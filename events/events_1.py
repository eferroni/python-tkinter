import tkinter as tk
from tkinter import messagebox

def clicked(event=None):
    if event is None:
        messagebox.showinfo("info", "some\ninfo")
    else:
        string = "x=" + str(event.x) + ", y=" + str(event.y) + \
            ", num=" + str(event.num) + ", type=" + event.type
        messagebox.showinfo("info", string)

window = tk.Tk()

label = tk.Label(window, text="Label")
label.bind("<Button-1>", clicked)
label.pack()

button1 = tk.Button(window, text="Show Info", command=clicked)
button1.pack()
button2 = tk.Button(window, text="Quit", command=window.destroy)
button2.pack()

frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
frame.bind("<Button-1>", clicked)
frame.pack()

window.mainloop()
