import tkinter as tk

def on_off():
    global button
    state = button.cget("text")
    fg = button.cget("foreground")
    if state == "OFF":
        state = "ON"
        fg = "green"
    else:
        state = "OFF"
        fg = "red"
    button.config(text = state)
    button.config(foreground = fg)

window = tk.Tk()

button = tk.Button(window, text="OFF", command=on_off, foreground="red")
button.place(x=50, y=100, width=100)

window.mainloop()