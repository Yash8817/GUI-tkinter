from tkinter import *

root = Tk()
root.title("My menu")
root.geometry("400x400")

def new_file():
    pass

my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="file",menu=file_menu)
file_menu.add_command(label="New",command=new_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.destroy)

edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit",menu=edit_menu)

edit_menu.add_command(label="cut",command=new_file)
edit_menu.add_command(label="Copy",command=new_file)
edit_menu.add_command(label="paste",command=new_file)

                      
                      


root.mainloop()
