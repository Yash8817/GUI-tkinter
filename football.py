from tkinter import *

root = Tk()
root.title("programming with yash")
root.geometry("800x800")

def left(event):
    x = -10
    y = 0
    my_canvas.move(my_img,x,y)

def right(event):
    x = 10
    y = 0
    my_canvas.move(my_img,x,y)

def up(event):
    x = 0
    y = -10
    my_canvas.move(my_img,x,y)

def down(event):
    x = 0
    y = 10
    my_canvas.move(my_img,x,y)
    
w = 600
h = 400
x = w/2
y = h/2

my_canvas = Canvas(root,width =w,height=h,bg="white")
my_canvas.pack()

img = PhotoImage(file="img/football.png")

my_img = my_canvas.create_image(280,160,anchor=NW,image=img)

root.bind("<Left>",left)
root.bind("<Right>",right)
root.bind("<Up>",up)
root.bind("<Down>",down)

root.mainloop()
