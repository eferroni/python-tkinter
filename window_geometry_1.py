import tkinter as tk

def click(*args):
    global size, grows
    if grows:
        size += 50
        if size >= 500:
            grows = False
    else:
        size -= 50
        if size <= 100:
            grows = True

    window.geometry(f"{size}x{size}")

size = 100
grows = True

window = tk.Tk()
window.minsize(width=100, height=100)
window.maxsize(width=500, height=500)
window.geometry("100x100")
window.bind("<Button-1>", click)
window.mainloop()