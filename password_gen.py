from tkinter import *
from random import randint

root = Tk()

root.geometry("500x300")

def new_rand():
    pass_entry.delete(0,END)
    pass_length = int(entry.get())
    my_pass = ""

    for x in range(pass_length):
        my_pass += chr(randint(33,126))

    pass_entry.insert(0,my_pass)

def clipper():
    root.clipboard_clear()
    root.clipboard_append(pass_entry.get())
    
lf = LabelFrame(root,text="How many character?")
lf.pack(pady=20)

entry = Entry(lf,font=("Helvetica",24))
entry.pack(padx=20,pady=20)

pass_entry = Entry(root,text="",font=("Helvetica",24),bd=0,bg="systembuttonface")
pass_entry.pack(pady=20)

my_frame = Frame(root)
my_frame.pack(pady=20)

button = Button(my_frame,text="Generate strong password" , command= new_rand)
button.grid(row=0,column=0,padx=10)

cpy_button = Button(my_frame,text="Copy to clipboard",command=clipper)
cpy_button.grid(row=0,column=1,padx=10)

root.mainloop()
