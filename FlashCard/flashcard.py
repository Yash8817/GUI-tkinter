from tkinter import *
from PIL import ImageTk,Image
from random import randint
import random
root =Tk()
root.title("Flascard")
root.geometry("400x500")

#states function
def random_state():
    global our_state
    global random_no
    our_state= ["bihar","maharashtra","gujarat","nagaland","karnataka","punjab","rajasthan","westbengal"]                            
    random_no = randint(0,len(our_state)-1)
    state = "states/" + our_state[random_no] + ".png"
    global state_image
    state_image = ImageTk.PhotoImage(Image.open(state))
    show_state_img.config(image=state_image)

def states_answer():    
    answer = ans_input.get()
    answer = answer.replace(" ","")

    if answer.lower() == our_state[random_no]:
        response = "Correct  " + our_state[random_no].title()
    else:
        response = "Incorrect  " + our_state[random_no].title()
    state_ans_lbl.config(text=response)
    ans_input.delete(0,"end")
    random_state()

def capital_answer():
    if capital_radio.get() == our_state_capital[answer]:
        response = "Correct! " 
        note =  our_state_capital[answer].title() + " is the capital of " +answer.title()
    else:
        response = "Incorrect! "
        note =  our_state_capital[answer].title() + " is the capital of " +answer.title()
    random_state()
    states_capital()
    capital_ans_lbl.config(text=response)
    capital_note_lbl.config(text=note)

def hide_all_frames():
    for widget in state_frame.winfo_children():
        widget.destroy()
    for widget in state_capital_frame.winfo_children():
        widget.destroy()
    for widget in add_frame.winfo_children():
        widget.destroy()
        
    state_frame.pack_forget()
    state_capital_frame.pack_forget()
    add_frame.pack_forget()

def states():
    hide_all_frames()
    state_frame.pack(fill="both",expand=1)

    global show_state_img
    show_state_img = Label(state_frame)
    show_state_img.pack(pady=15)
    random_state()

    global ans_input
    ans_input = Entry(state_frame,font=("Helvetica",18),bd=2)             
    ans_input.pack(pady=15)

    random_btn = Button(state_frame,text="Pass",command=states)                    
    random_btn.pack(pady=10)

    ans_btn = Button(state_frame,text="Answer",command=states_answer)                    
    ans_btn.pack(pady=10)

    global state_ans_lbl
    state_ans_lbl  = Label(state_frame,text="",font=("Helvetica",18),bg="white")                       
    state_ans_lbl.pack(pady=15)

    
def states_capital():
    hide_all_frames()
    state_capital_frame.pack(fill="both",expand=1)
    #my_lbl = Label(,text="state capital").pack()

    global show_state_img
    show_state_img = Label(state_capital_frame)
    show_state_img.pack(pady=15)

    global our_states
    our_state= ["bihar","maharashtra","gujarat","nagaland","karnataka","punjab","rajasthan","westbengal"]

    global our_state_capital
    our_state_capital = {
        "bihar" : "patna",
        "maharashtra" : "mumbai",
        "gujarat" : "gandhinagar",
        "nagaland":"kohima",
        "karnataka":"bangalore",
        "punjab":"chandigarh",
        "rajasthan":"jaipur",
        "westbengal":"kolkata"
        }

    answer_list = []
    count = 1
    global answer
    while count<4:
        rand_no = random_no = randint(0,len(our_state)-1)

        if count == 1:
            answer = our_state[rand_no]
            state = "states/" + our_state[rand_no] + ".png"
            global state_image
            state_image = ImageTk.PhotoImage(Image.open(state))
            show_state_img.config(image=state_image)


        answer_list.append(our_state[rand_no])

        our_state.remove(our_state[rand_no])

        random.shuffle(our_state)

        count += 1

    random.shuffle(answer_list)

    global capital_radio
    capital_radio = StringVar()
    capital_radio.set(our_state_capital[answer_list[0]])

    capital_state_button1 = Radiobutton(state_capital_frame,text= our_state_capital[answer_list[0]].title(),variable=capital_radio,value=our_state_capital[answer_list[0]]).pack()
    capital_state_button2 = Radiobutton(state_capital_frame,text= our_state_capital[answer_list[1]].title(),variable=capital_radio,value=our_state_capital[answer_list[1]]).pack()
    capital_state_button3 = Radiobutton(state_capital_frame,text= our_state_capital[answer_list[2]].title(),variable=capital_radio,value=our_state_capital[answer_list[2]]).pack()

    random_btn = Button(state_capital_frame,text="Pass",command=states_capital)                    
    random_btn.pack(pady=10)

    capital_ans_btn = Button(state_capital_frame,text="Answer",command=capital_answer)                    
    capital_ans_btn.pack(pady=10)

    global capital_ans_lbl
    global capital_note_lbl
    capital_ans_lbl  = Label(state_capital_frame,text="",font=("Helvetica",18),bg="white")                          
    capital_ans_lbl.pack(pady=5)
    capital_note_lbl  = Label(state_capital_frame,text="",font=("Helvetica",18),bg="white")                          
    capital_note_lbl.pack(pady=5)


def random_no():
    global num_1
    global num_2
    num_1 = randint(0,10)
    num_2 = randint(0,10)

    global add_img_1
    global add_img_2
    card1 = "images/" + str(num_1) + ".png"
    card2 = "images/" + str(num_2)+ ".png"
    add_img_1 = ImageTk.PhotoImage(Image.open(card1))
    add_img_2 = ImageTk.PhotoImage(Image.open(card2))
    
    add_1.config(image=add_img_1)
    add_2.config(image=add_img_2)
    

def add_answer():
    
    answer = num_1 + num_2

    try:
        if int(add_ans.get()) == answer:
            response = "Correct! " + str(num_1)+ " + " + str(num_2)+" = " + str(answer)            
        else:
            response = "Wrong! " + str(num_1)+ " + " + str(num_2)+" = " + str(answer) + " not " + str(add_ans.get())
    except ValueError:
        response= "Not a Number!!"
        
    add_ans_lbl.config(text=response)

    add_ans.delete(0,"end")
    random_no()
    
#add function
def add():
    hide_all_frames()
    add_frame.pack(fill="both",expand=1)
    my_lbl = Label(add_frame,text="Addition card",font=("Helvetica",15)).pack(pady=15)
    pic_frame = Frame(add_frame,width=400,height=300)
    pic_frame.pack()

    global num_1
    global num_2
    num_1 = randint(0,10)
    num_2 = randint(0,10)

    #label inside pic frame
    global add_1
    global add_2
    add_1 = Label(pic_frame)
    add_2 = Label(pic_frame)
    math_sign = Label(pic_frame,text="+",font=("Helvetica",28))

    add_1.grid(row=0,column=0)
    math_sign.grid(row=0,column=1)
    add_2.grid(row=0,column=2)

    global add_img_1
    global add_img_2
    card1 = "images/" + str(num_1) + ".png"
    card2 = "images/" + str(num_2)+ ".png"
    add_img_1 = ImageTk.PhotoImage(Image.open(card1))
    add_img_2 = ImageTk.PhotoImage(Image.open(card2))
    
    add_1.config(image=add_img_1)
    add_2.config(image=add_img_2)
                                
    #ans part
    global add_ans
    add_ans = Entry(add_frame,font=("Helvetica",18))
    add_ans.pack(pady=25)
    add_ans_btn = Button(add_frame,text="Answer",command=add_answer)
    add_ans_btn.pack()

    global add_ans_lbl
    add_ans_lbl = Label(add_frame,text="",font=("Helvetica",20))
    add_ans_lbl.pack(pady=40)

#menu
my_menu = Menu(root)
root.config(menu=my_menu)

#menu items
states_menu = Menu(my_menu)
my_menu.add_cascade(label="Geography",menu=states_menu)
states_menu.add_command(label="States",command=states)
states_menu.add_command(label="States capital",command = states_capital)                    
states_menu.add_separator()
states_menu.add_command(label="Exit",command=root.destroy)

#math items
math_menu = Menu(my_menu)
my_menu.add_cascade(label="Math",menu=math_menu)
math_menu.add_command(label="Addition",command=add)


#frames
state_frame =Frame(root,width=500,height= 500,bg="white")
state_capital_frame =Frame(root,width=500,height= 500)
add_frame =Frame(root,width=500,height= 500)

root.mainloop()
            
