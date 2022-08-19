import tkinter as tk
from tkinter import messagebox

def really():
    if messagebox.askyesno("?", "Really?"):
        window.destroy()


window = tk.Tk()

window.geometry("250x250")
window.resizable(width=False, height=False)

window.protocol("WM_DELETE_WINDOW", really)

window.mainloop()