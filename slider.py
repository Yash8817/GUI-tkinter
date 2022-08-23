from tkinter import *

root = Tk()
root.geometry("400x400")

def slide():
    root.geometry(str(horizontal.get()) +"x" + str(vertical.get()))


vertical = Scale(root,from_=0,to=400)
vertical.pack()

horizontal = Scale(root,from_=0,to=400,orient=HORIZONTAL)
horizontal.pack()

    

btn = Button(root,text="click",command=slide).pack()



root.mainloop()
