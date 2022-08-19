from cProfile import label
from curses import window
import tkinter as tk

window = tk.Tk()

label_frame_1 = tk.LabelFrame(window, text="Frame #1", width=200, height=100, bg="pink", labelanchor="nw")
label_frame_2 = tk.LabelFrame(window, text="Frame #2", width=200, height=100, bg="orange", labelanchor="ne")
label_frame_3 = tk.LabelFrame(window, text="Frame #3", width=200, height=100, bg="pink", labelanchor="w")
label_frame_4 = tk.LabelFrame(window, text="Frame #4", width=200, height=100, bg="orange", labelanchor="e")
label_frame_5 = tk.LabelFrame(window, text="Frame #5", width=200, height=100, bg="pink", labelanchor="sw")
label_frame_6 = tk.LabelFrame(window, text="Frame #6", width=200, height=100, bg="orange", labelanchor="se")

label_frame_1.pack()
label_frame_2.pack()
label_frame_3.pack()
label_frame_4.pack()
label_frame_5.pack()
label_frame_6.pack()

window.mainloop()