import tkinter as  tk
from tkinter import Button, messagebox

window = tk.Tk()


def hello(event=None):
    messagebox.showinfo("", "Hello!")

button = tk.Button(window, text="Button")
button.pack()

label = tk.Label(window, text="Label")
label.pack()

frame = tk.Frame(window, height=30, width=100, bg="blue")
frame.pack()

window.bind_all("<Button-1>", hello)

window.mainloop()