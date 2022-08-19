import tkinter as tk

def on_off():
    global switch
    if switch:
        label.unbind("<Button-1>")
    else:
        label.bind("<Button-1>", rhyme)
    switch = not switch

def rhyme(dummy):
    global words, word_no
    word_no += 1
    label.config(text=words[0: word_no % len(words) + 1])

switch = True
words= ["Old", "MacDonald", "Has", "A", "Farm"]
word_no = 0

window = tk.Tk()

button = tk.Button(window, text="On / Off", command=on_off)
button.pack()

label = tk.Label(window, text=words[0])
label.bind("<Button-1>", rhyme)
label.pack()

window.mainloop()