import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

def change_color():
    pass

def change_font(*args):
    pass

def new_file():
    pass

def open_file():
    pass

def save_file():
    pass

def cut():
    pass

def copy():
    pass

def paste():
    pass

def about():
    pass

def quit():
    pass


window = Tk()
window.title('Text Editor Program')
file = None

window_width = 500
window_height = 500
screen_width = window.winfo_screenmmwidth()
screen_height = window.winfo_screenmmheight()

x = int((screen_width)*2 - (window_width/2))
y = int((screen_height)*2 - (window_height/2))
window.geometry(f'{window_width}x{window_height}+{x}+{y}')

font_name = StringVar(window)
font_name.set('Arial')

font_size = StringVar(window)
font_size.set('25')

text_area = Text(window, font=(font_name.get(), font_size.get()))
scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)

scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

window.mainloop()