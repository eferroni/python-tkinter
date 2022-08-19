import tkinter as tk
from tkinter import messagebox

def yes_no():
    answer = messagebox.askyesno("", "Yes or No?")
    messagebox.showinfo("Answer", str(answer))

def ok_cancel():
    answer = messagebox.askokcancel("", "OK or Cancel?")
    messagebox.showinfo("Answer", str(answer))

def retry_cancel():
    answer = messagebox.askretrycancel("", "Retry or Cancel?")
    messagebox.showinfo("Answer", str(answer))

def ask_question():
    answer = messagebox.askquestion("", "Question?")
    messagebox.showinfo("Answer", str(answer))

def show_error():
    answer = messagebox.showerror("!", "This is an error!")
    messagebox.showinfo("Return", str(answer))

def show_warning():
    answer = messagebox.showwarning("!", "This is a warning!")
    messagebox.showinfo("Return", str(answer))

window = tk.Tk()
window.geometry("500x500")

button_1 = tk.Button(window, text="Ask Yes/No", command=yes_no)
button_1.pack()

button_2 = tk.Button(window, text="Ask OK/Cancel", command=ok_cancel)
button_2.pack()

button_3 = tk.Button(window, text="Ask Retry/Cancel", command=retry_cancel)
button_3.pack()

button_4 = tk.Button(window, text="Ask Question", command=ask_question)
button_4.pack()

button_5 = tk.Button(window, text="Show Error", command=show_error)
button_5.pack()

button_6 = tk.Button(window, text="Show Warning", command=show_warning)
button_6.pack()

window.mainloop()