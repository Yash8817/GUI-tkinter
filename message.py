from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root =Tk()

"""
    Types of messagebox:
    showinfo
    showwarning
    showerror
    askquestion
    askokcancel
    askyesno
"""

def popup(msgtype):
    if msgtype == "showinfo":
        messagebox.showinfo("my popup","hello world")

    if msgtype == "showwarning":
        messagebox.showwarning("my popup","hello world")

    if msgtype == "showerror":
        messagebox.showerror("my popup","hello world")

    if msgtype == "askquestion":
        messagebox.askquestion("my popup","hello world")

    if msgtype == "askokcancel":
        messagebox.askokcancel("my popup","hello world")

    if msgtype == "askyesno":
        messagebox.askyesno("my popup","hello world")

Button_showinfo = Button(root,text="showinfo popup",command=lambda: popup("showinfo")).pack()
Button_showwarning = Button(root,text="showwarning popup",command=lambda: popup("showwarning")).pack()
Button_showerror = Button(root,text="showerror popup",command=lambda: popup("showerror")).pack()
Button_askquestion =Button(root,text="askquestion popup",command=lambda: popup("askquestion")).pack()
Button_askokcancel=Button(root,text="askokcancel popup",command=lambda: popup("askokcancel")).pack()
Button_askyesno= Button(root,text="askyesno popup",command=lambda: popup("askyesno")).pack()

root.mainloop()
