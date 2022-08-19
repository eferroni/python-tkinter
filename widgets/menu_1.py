from ast import main
from curses import window
from re import sub
import tkinter as tk
from tkinter import messagebox

def open_file():
    messagebox.showinfo("Open doc", "We'll open a file here...")

def about_app():
    messagebox.showinfo("About", "The application does nothing")

def are_you_sure(event=None):
    if messagebox.askyesno("", "Are you sure you want to quit the App?"):
        window.destroy()


window = tk.Tk()

main_menu = tk.Menu(window)
window.config(menu=main_menu)

# File Menu
sub_menu_file = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)

# File Open
sub_menu_file.add_command(label="Open...", command=open_file)

# File Open Recent
sub_sub_menu_file = tk.Menu(sub_menu_file, tearoff=0)
sub_menu_file.add_cascade(label="Open recent file...", menu=sub_sub_menu_file)
for i in range(8):
    number = str(i+1) 
    sub_sub_menu_file.add_command(label=f"{i}. file.txt")

# File Quit
sub_menu_file.add_separator()
sub_menu_file.add_command(label="Quit", command=are_you_sure, accelerator="Ctrl-Q")

# Help Menu
sub_menu_help = tk.Menu(main_menu)
main_menu.add_cascade(label="Help", menu=sub_menu_help, underline=0)
sub_menu_help.add_command(label="About", underline=0, command=about_app)

window.bind_all("<Control-q>", are_you_sure)
window.mainloop()