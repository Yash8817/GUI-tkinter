import tkinter as tk
from tkinter import filedialog,Text
import os

root = tk.Tk()
apps = []

if os.path.isfile("save.txt"):
    with open("save.txt","r") as f:
        tempapps = f.read() 
        tempapps = tempapps.split(",")
        apps = [ x for x in tempapps if x.strip()]

def addapp():
    for widget in frame.winfo_children():
        widget.destroy()
    filename= filedialog.askopenfilename(initialdir="/",title="select file",
                                     filetypes=(("Executables","*.exe"),("All files","*.*")))
    apps.append(filename)
    print(filename)

    for app in apps:
        
        label = tk.Label(frame,text=app,bg="gray")
        label.pack()


def runapp():
    for app in apps:
        os.startfile(app)
    
canvas = tk.Canvas(height=700,width=700,bg="#263D42")
canvas.pack()
frame = tk.Frame(root,bg="white")
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1) 

openfile = tk.Button(root,text="open file",padx=10,pady=5,
                  fg="white",bg="#263D42",command =addapp)
openfile.pack()

runapps = tk.Button(root,text="run app",padx=10,pady=5,
                  fg="white",bg="#263D42",command=runapp)
runapps.pack()


for app in apps:
    label = tk.Label(frame,text=app)
    label.pack()

root.mainloop()

with open("save.txt","w") as f:
    for app in apps:
        f.write(app + ",")

