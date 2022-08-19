import tkinter as tk

window = tk.Tk()

button_1 = tk.Button(window, text="NW")
button_1.config(anchor="nw", cursor="boat")
button_1.grid(column=0, row=0, padx=5, pady=5, ipadx=20, ipady=20)
button_2 = tk.Button(window, text="N")
button_2.config(anchor="n", cursor="clock")
button_2.grid(column=1, row=0, padx=5, pady=5, ipadx=20, ipady=20)
button_3 = tk.Button(window, text="NE")
button_3.config(anchor="ne", cursor="heart")
button_3.grid(column=2, row=0, padx=5, pady=5, ipadx=20, ipady=20)

button_4 = tk.Button(window, text="W")
button_4["anchor"] = "w"
button_4.grid(column=0, row=1, padx=5, pady=5, ipadx=20, ipady=20)
button_5 = tk.Button(window, text="CENTER")
button_5["anchor"] = "center"
button_5.grid(column=1, row=1, padx=5, pady=5, ipadx=20, ipady=20)
button_6 = tk.Button(window, text="E")
button_6["anchor"] = "e"
button_6.grid(column=2, row=1, padx=5, pady=5, ipadx=20, ipady=20)

button_7 = tk.Button(window, text="SW")
button_7["anchor"] = "sw"
button_7.grid(column=0, row=2, padx=5, pady=5, ipadx=20, ipady=20)
button_8 = tk.Button(window, text="S")
button_8["anchor"] = "s"
button_8.grid(column=1, row=2, padx=5, pady=5, ipadx=20, ipady=20)
button_9 = tk.Button(window, text="SE")
button_9["anchor"] = "se"
button_9.grid(column=2, row=2, padx=5, pady=5, ipadx=20, ipady=20)

window.mainloop()