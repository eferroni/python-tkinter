from curses import window
import tkinter as tk

window = tk.Tk()

canvas = tk.Canvas(window, width=400, height=400, bg="yellow")
canvas.create_line(10, 380, 200, 10, 380, 380, 10, 380, arrow=tk.BOTH, fill="blue", smooth=False, width=3)
canvas.grid(row=0)

button = tk.Button(window, text="Quit", command=window.destroy)
button.grid(row=1)

window.mainloop()