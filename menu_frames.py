from tkinter import *

root = Tk()
root.title("My menu")
root.geometry("400x400")

def new_file():
    pass

def file_new():
    hide_all_frames()
    new_file_frame.pack(fill="both",expand=1)
    my_lbl = Label(new_file_frame,text="you clicked file >>new file").pack()

def cut_file():
    hide_all_frames()
    cut_file_frame.pack(fill="both",expand=1)
    my_lbl = Label(cut_file_frame,text="you clicked file >>cut option").pack()

def hide_all_frames():
    new_file_frame.pack_forget()
    cut_file_frame.pack_forget()
my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="file",menu=file_menu)
file_menu.add_command(label="New",command=file_new)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.destroy)

edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="cut",command=cut_file)
edit_menu.add_command(label="Copy",command=new_file)
edit_menu.add_command(label="paste",command=new_file)



option_menu = Menu(my_menu)
my_menu.add_cascade(label="option",menu=option_menu)

option_menu.add_command(label="find",command=new_file)
option_menu.add_command(label="find next",command=new_file)

new_file_frame = Frame(root,width=400,height=400,bg="red")
cut_file_frame = Frame(root,width=400,height=400,bg="blue")





root.mainloop()
