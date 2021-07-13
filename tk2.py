from tkinter import *

root = Tk()


root.geometry("400x250")

name = Label(root, text = "Name").place(x = 100, y = 50)
e1 = Entry(root, fg = "green", bg = "white", borderwidth = 10).place(x = 150, y =50)

address = Label(root, text = "Address").place(x = 100, y = 90)
e2 = Entry(root, fg = "green", bg = "white", borderwidth = 10).place(x = 150, y = 90)

contact = Label(root, text = "Contact").place(x = 100, y = 130)
e3 = Entry(root, fg = "green", bg = "white", borderwidth = 10).place(x = 150, y = 130)

home = Button(root, text = "Home", bg = "blue", fg = "white", borderwidth = 5).grid(row = 0, column = 10)

menu = Button(root, text = "Menu", bg = "blue", fg = "white", borderwidth = 5).grid(row = 0, column = 20 )

submit = Button(root, text = "Submit", fg = "white", bg = "black").place(x = 170, y = 180)

def myClick():
    myLabel = Label(root, text = "Button clicked").grid(row = 1, column = 80)


click = Button(root, text = "Click", fg = "white", bg = "blue", borderwidth = 5, command = myClick).grid(row = 0, column = 80)

def onClick():

    dis = Label(root, text = "textdisplay").grid(row = 1, column = 120)


display = Button(root, text = "Display", fg = "white", bg = "blue", borderwidth = 5, command = onClick).grid(row = 0, column = 120)
root.mainloop()




