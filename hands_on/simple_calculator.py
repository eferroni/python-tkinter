from curses import window
import tkinter as tk
from tkinter import messagebox


def digits_only_entry_1(*args):
    global entry_1_last_string
    string = entry_1_variable.get()
    if string == '' or string.isdigit():
        entry_1_last_string = string
    else:
        entry_1_variable.set(entry_1_last_string)

def digits_only_entry_2(*args):
    global entry_2_last_string
    string = entry_2_variable.get()
    if string == '' or string.isdigit():
        entry_2_last_string = string
    else:
        entry_2_variable.set(entry_2_last_string)

def evaluate():
    selected_method = method.get()
    value_1 = entry_1_variable.get()
    value_2 = entry_2_variable.get()
    if value_1 == '' or value_2 == '':
        messagebox.showerror("Error!", "Inform two values")
        return
    if selected_method == "+":
        result = int(value_1) + int(value_2)
    elif selected_method == "-":
        result = int(value_1) - int(value_2)
    elif selected_method == "*":
        result = int(value_1) * int(value_2)
    else:
        result = int(value_1) / int(value_2)
    messagebox.showinfo("Result", str(result))

window = tk.Tk()
window.title("Calculator")

entry_1_last_string = ''
entry_1_variable = tk.StringVar()
entry_1 = tk.Entry(window, textvariable=entry_1_variable)
entry_1_variable.set(entry_1_last_string)
entry_1_variable.trace("w", digits_only_entry_1)
entry_1.grid(row=0, column=0, rowspan=4)
entry_1.focus_set()

method = tk.StringVar(value="+")
radio_1 = tk.Radiobutton(window, text="+", value="+", variable=method)
radio_1.grid(row=0, column=1)
radio_2 = tk.Radiobutton(window, text="-", value="-", variable=method)
radio_2.grid(row=1, column=1)
radio_3 = tk.Radiobutton(window, text="*", value="*", variable=method)
radio_3.grid(row=2, column=1)
radio_4 = tk.Radiobutton(window, text="/", value="/", variable=method)
radio_4.grid(row=3, column=1)

entry_2_last_string = ''
entry_2_variable = tk.StringVar()
entry_2 = tk.Entry(window, textvariable=entry_2_variable)
entry_2_variable.set(entry_1_last_string)
entry_2_variable.trace("w", digits_only_entry_1)
entry_2.grid(row=0, column=2, rowspan=4)

button = tk.Button(window, text="Evaluate", command=evaluate)
button.grid(row=4, columnspan=3)

window.mainloop()