from curses import window
import tkinter as tk

window = tk.Tk()

canvas = tk.Canvas(window, width=400, height=400, bg="yellow")
image = tk.PhotoImage(file="logo.png")
canvas.create_image(200, 200, image=image)

button = tk.Button(window, text="Quit", command=window.destroy)


canvas.grid(row=0)
button.grid(row=1)

window.mainloop()