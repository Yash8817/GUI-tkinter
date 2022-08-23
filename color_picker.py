from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title("My menu")
root.geometry("400x400")

def color():
    my_color = colorchooser.askcolor()[1]
    color_lbl = Label(root,text="Hexa code:"+str(my_color),font=("Helveri==tica",32),bg=my_color).pack()

color_btn = Button(root,text="Pick a color",command=color).pack()
 

root.mainloop()
