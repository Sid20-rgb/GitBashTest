from _ast import Lambda

from tkinter import *

root = Tk()

e1 = Entry(root, borderwidth = 10, padx = 10, pady = 20)
e1.grid(row = 0, column= 0)

def onClick(num):
    texte = e1.get()
    display = Label(root, text = texte)
    display.grid(row = 3, column = 0)

but = Button(root, text = "Submit", bg = "Grey", command = lambda : onClick(1), fg = "White")
but.grid(row = 2, column = 0)

root.mainloop()