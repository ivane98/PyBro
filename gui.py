###gui window

# from tkinter import *

# window = Tk()
# window.geometry('500x500')
# window.title('First GUI')
# window.config(background='grey')

# window.mainloop()

###labels

# from tkinter import *

# window = Tk()

# photo = PhotoImage(file='python.png')

# label = Label(window, text='bro, do you even code?',
#                font=('Arial', 40, 'bold'), fg='#00FF00', 
#                bg='black', relief=RAISED,
#                bd=10, padx = 20, pady = 20,
#                image=photo, compound='bottom' )
# label.pack()

# window.mainloop()

###Buttons

# from tkinter import *

# window = Tk()

# photo = PhotoImage(file='python.png')

# count = 0

# def click():
#     global count
#     count += 1
#     print(count)

# button = Button(text='Click Me', command=click, fg='#00ff00', background='black', activebackground='black', activeforeground='#00ff00', image=photo, compound='bottom', font=('Comic Sans', 30))

# button.pack()


# window.mainloop()

###entrybox

# from tkinter import *

# def submit():
#     text = entry.get()
#     print('hello ' + text)

# def delete():
#     entry.delete(0, END)

# def backspace():
#     entry.delete(len(entry.get())-1, END)

# window = Tk()

# entry = Entry(window, font=('Arial', 50), fg='#00ff00', bg='black', show='*')
# # entry.insert(0,'spongebob')
# entry.pack(side='left')

# submit_button = Button(text='submit', command=submit)
# submit_button.pack(side='right')

# delete_button = Button(text='delete', command=delete)
# delete_button.pack(side='right')

# backspace_button = Button(text='backspace', command=backspace)
# backspace_button.pack(side='right')

# window.mainloop()

###checkboxes

# from tkinter import *

# def display():
#     if (x.get()==1):
#         print('yes')
#     else:
#         print('no')

# window = Tk()

# x = IntVar()
# py_photo = PhotoImage(file='python.png')

# checkbox = Checkbutton(window, text='i agree', variable=x, onvalue=1, offvalue=0, command=display, fg='#00ff00', bg='black', font=('Arial', 30), activeforeground='#00ff00', activebackground='black', image=py_photo, compound='left')
# checkbox.pack()

# window.mainloop()


###radio buttons

# from tkinter import *

# food = ['pizza', 'hamburger', 'hotdog']

# def order():
#     if (x.get() == 0):
#         print('you ordered pizza')
#     elif (x.get() == 1):
#         print('you ordered hamburger')
#     else:
#         print('you order hotdog')

# window = Tk()
# window.geometry('500x500')

# x = IntVar()

# for i in range(len(food)):
#     radiobutton = Radiobutton(window, command=order, text=food[i], variable=x, value=i, font=('Impact', 50), padx=25, indicatoron=0, width=375)
#     radiobutton.pack(anchor=W)


# window.mainloop()


###scale

# from tkinter import *

# def submit():
#     print('Temp is ' + str(scale.get()) + ' c')

# window = Tk()

# scale = Scale(window, from_=100, to=0, length=500, font=('Consolas', 20), tickinterval=10, showvalue=0, resolution=5)
# scale.pack()

# button = Button(window, text='submit', command=submit)
# button.pack()

# window.mainloop()

###listbox

# from tkinter import *

# window = Tk()

# listbox = Listbox(window)
# listbox.pack()

# listbox.insert(1, 'pizza')
# listbox.insert(2, 'humberger')
# listbox.insert(3, 'hotdog')

# window.mainloop()