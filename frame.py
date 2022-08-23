from tkinter import *

root = Tk()

frame = LabelFrame(root,text="my frame..",padx=10,pady=10)
frame.pack(padx=10,pady=10)

b= Button(frame,text="click")
b1= Button(frame,text="here")
b.grid(row=0,column=0)
b1.grid(row=1,column=1)


root.mainloop()
