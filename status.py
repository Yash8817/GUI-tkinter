from tkinter import *
from PIL import ImageTk,Image

root = Tk()

my_img0 = ImageTk.PhotoImage(Image.open("img/user0.jpg"))
my_img1 = ImageTk.PhotoImage(Image.open("img/user1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("img/user2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("img/user3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("img/user4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("img/user5.jpg"))
my_img6 = ImageTk.PhotoImage(Image.open("img/user6.jpg"))

image_list = [my_img0,my_img1,my_img2,my_img3,my_img4,my_img5,my_img6]

status =Label(root,text="Image 1 of " + str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)

lbl = Label(image = my_img0)
lbl.grid(row=0,column=0,columnspan=3)



def forwad(image_number):
    global lbl
    global btn_forwad
    global btn_back
    lbl.grid_forget()

    lbl = Label(image = image_list[image_number-1])
    btn_forwad = Button(root,text = ">>" , command=lambda: forwad(image_number+1))
    btn_back = Button(root,text = "<<" , command = lambda: back(image_number-1))

    if image_number  == len(image_list):
        btn_forwad = Button(root,text = ">>" , state= DISABLED)
        
    lbl.grid(row=0,column=0,columnspan=3)
    btn_back.grid(row=1,column=0)
    btn_forwad.grid(row=1,column=2)

    status =Label(root,text="Image "+str(image_number)+" of " + str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)

    

def back(image_number):
    global lbl
    global btn_forwad
    global btn_back
    lbl.grid_forget()

    lbl = Label(image = image_list[image_number-1])
    btn_forwad = Button(root,text = ">>" , command=lambda: forwad(image_number+1))
    btn_back = Button(root,text = "<<" , command = lambda: back(image_number-1))

    if image_number  == 1:
        btn_back = Button(root,text = "<<" , state = DISABLED)
        
    lbl.grid(row=0,column=0,columnspan=3)
    btn_back.grid(row=1,column=0)
    btn_forwad.grid(row=1,column=2)

    status =Label(root,text="Image "+str(image_number)+" of " + str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)


btn_back = Button(root,text = "<<" , command = back ,state = DISABLED)
btn_quit = Button(root,text = "Exit viewer" , command = root.quit)
btn_forwad = Button(root,text = ">>" , command=lambda: forwad(2))

btn_back.grid(row=1,column=0)
btn_quit.grid(row=1,column=1)
btn_forwad.grid(row=1,column=2,pady=10)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)

root.mainloop()
