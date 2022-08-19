import tkinter as tk

def suicide():
    frame.destroy()

window = tk.Tk()

frame = tk.Frame(window, width=200, height=200, bg="green")
button = tk.Button(frame, text="Frame child")
button.place(x=10, y=10)
frame.after(5000, suicide)
frame.pack()

window.mainloop()