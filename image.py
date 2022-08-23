from tkinter import *
from PIL import ImageTk,Image

root = Tk()

my_img = ImageTk.PhotoImage(Image.open("img/user.jpg"))
lbl = Label(image = my_img)
lbl.pack()

btn = Button(root,text = "quit" , command = root.quit)
btn.pack()
