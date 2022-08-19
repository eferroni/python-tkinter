from cProfile import label
import tkinter as tk

def to_string(x):
    return f"Current counter\nvalue is:\n{x}"

def plus():
    global counter
    counter += 1
    text.set(to_string(counter))

counter = 0
window = tk.Tk()

button = tk.Button(window, text="Go on!", command=plus)
button.pack()

text = tk.StringVar()
label = tk.Label(window, textvariable=text, height=8)
text.set(to_string(counter))
label.pack()

window.mainloop()