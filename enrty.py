from tkinter import *

root = Tk()

e = Entry(root , width = 50)
e.pack()

def myclick():
    
    lbl = Label(root,text="hello" + e.get())
    lbl.pack()


mybtn = Button(root,text = "click..",command=myclick,fg="blue",bg="red").pack()

root.mainloop()

