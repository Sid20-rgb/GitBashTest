from tkinter import *

root = Tk()

buttonfirst = Button(root, text="North", fg = "green")
buttonfirst.pack(side = TOP)

buttonsecond = Button(root, text = "South", fg = "red")
buttonsecond.pack(side = BOTTOM)

buttonthird = Button(root, text = "East", fg = "blue")
buttonthird.pack(side = RIGHT)

buttonfourth = Button(root, text = "West", fg = "black")
buttonfourth.pack(side = LEFT)

def onclick():

    display = Label(root, text = "Clicked!").pack()

but = Button(root, text = "Click", command = onclick).pack()
root.mainloop()