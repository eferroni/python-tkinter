from curses import window
import tkinter as tk

def switch():
    if button_1.cget("state") == tk.DISABLED:
        button_1.config(state=tk.NORMAL)
        button_1.flash()
    else:
        button_1.flash()
        button_1.config(state=tk.DISABLED)

def mouse_over(ev):
    button_1["fg"] = "green"

def mouse_out(ev):
    button_1["fg"] = "red"

window = tk.Tk()

button_1 = tk.Button(window, text="Enabled", fg="red")
button_1.bind("<Enter>", mouse_over)
button_1.bind("<Leave>", mouse_out)
button_1.pack()

button_2 = tk.Button(window, text="Enable/Disable", command=switch)
button_2.pack()

window.mainloop()