from tkinter import *

root =Tk()

r= IntVar()
r.set(2)

def clicked(value):
    lbl = Label(root,text=value).pack()

btn = Radiobutton(root,text="option 1",variable=r,value=1,command= lambda: clicked(r.get())).pack()
btn = Radiobutton(root,text="option 2",variable=r,value=2,command= lambda:clicked(r.get())).pack()

lbl = Label(root,text=r.get()).pack()



root.mainloop()
