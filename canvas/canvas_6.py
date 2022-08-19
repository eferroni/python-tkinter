import tkinter as tk

window = tk.Tk()

canvas = tk.Canvas(width=400, height=400, bg="blue")
canvas.create_text(200, 200, text="Mary had a\nlittle lamb", justify=tk.CENTER, fill="white", font=("Arial", "40", "bold"))

button = tk.Button(window, text="Quit", command=window.destroy)

canvas.grid(row=0)
button.grid(row=1)

window.mainloop()