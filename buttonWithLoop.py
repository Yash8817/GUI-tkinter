from tkinter import *

root =Tk()

r= IntVar()
r.set(2)


MODES = [
    ("Chesse","Chesse"),
    ("Onion","Onion"),
    ("Pepperoni","Pepperoni"),
    ("Mushroom","Mushroom"),
    ]
pizza = StringVar()
pizza.set("Chesse")

for text, mode in MODES:
    Radiobutton(root,text=text,variable=pizza,value=mode).pack(anchor=W)


def clicked(value):
    lbl = Label(root,text=value).pack()




btn = Button(root,text="add pizza",command=lambda:clicked(pizza.get())).pack()



root.mainloop()
