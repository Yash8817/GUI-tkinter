from tkinter import *
import sqlite3

root = Tk()
root.geometry("400x600")

"""c.execute( " CREATE TABLE ADDRESS(
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer )
        " )"""
#submit function for database
def submit():
    conn  = sqlite3.connect("address_book.db")
    c = conn.cursor()

    c.execute("INSERT INTO ADDRESS VALUES(:fname,:lname,:useraddress,:usercity,:userstate,:userzipcode)",
        {
        "fname" : f_name.get(),
        "lname" : l_name.get(),
        "useraddress" : address.get(),
        "usercity" : city.get(),
        "userstate" : state.get(),
        "userzipcode" : zipcode.get()
        })
    
    conn.commit()
    c.close()

def quary():
    conn  = sqlite3.connect("address_book.db")
    c = conn.cursor()

    c.execute("SELECT *,oid FROM ADDRESS")
    records = c.fetchall()
    

    print_record = ""
    for record in records:
        print_record += str(record[0]) +" "+str(record[1])+" \t" +str(record[6])+ "\n"

    qury_label = Label(root,text=print_record)
    qury_label.grid(row=11,column=0,columnspan=2)
    
    conn.commit()
    c.close()

def delete():
    conn  = sqlite3.connect("address_book.db")
    c = conn.cursor()

    c.execute("DELETE FROM ADDRESS WHERE oid="+ delete_entry.get())
    delete_entry.delete(0,END)

    conn.commit()
    c.close()


def edit():
    conn  = sqlite3.connect("address_book.db")
    c = conn.cursor()

    record_id = delete_entry.get()
    
    c.execute("""UPDATE ADDRESS SET
    first_name =:first,
    last_name =:last,
    address =:add,
    city =:ct ,
    state =:st ,
    zipcode =:zip

    WHERE oid= :oid
    """,
            {
                "first" : f_name_editor.get(),
                "last" : l_name_editor.get(),
                "add" : address_editor.get(),
                "ct" : city_editor.get(),
                "st" : state_editor.get(),
                "zip" : zipcode_editor.get(),
                "oid" :record_id
            }
            )
    

    conn.commit()
    c.close()
    editor.destroy()

    
def update():
    global editor
    editor = Tk()
    editor.geometry("400x600")
    editor.title("Update a record")

    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor
    

    select_id =delete_entry.get()

    conn  = sqlite3.connect("address_book.db")
    c = conn.cursor()

    c.execute("SELECT * FROM ADDRESS WHERE oid="+select_id)
    records = c.fetchall()

    f_name_editor = Entry(editor,width=30 )
    f_name_editor.grid(row=0,column=1,padx=20, pady=(10,0))
    l_name_editor = Entry(editor,width=30)
    l_name_editor.grid(row=1,column=1)
    address_editor = Entry(editor,width=30)
    address_editor.grid(row=2,column=1)
    city_editor = Entry(editor,width=30)
    city_editor.grid(row=3,column=1)
    state_editor = Entry(editor,width=30)
    state_editor.grid(row=4,column=1)
    zipcode_editor = Entry(editor,width=30)
    zipcode_editor.grid(row=5,column=1)
    
    #label
    f_name_ltl = Label(editor,text="First Name:")
    f_name_ltl.grid(row=0,column=0, pady=(10,0))
    l_name_ltl = Label(editor,text="last Name:")
    l_name_ltl.grid(row=1,column=0)
    address_ltl = Label(editor,text="address :")
    address_ltl.grid(row=2,column=0)
    city_ltl = Label(editor,text="city :")
    city_ltl.grid(row=3,column=0)
    state_ltl = Label(editor,text="state :")
    state_ltl.grid(row=4,column=0)
    zipcode_ltl = Label(editor,text="zipcode :")
    zipcode_ltl.grid(row=5,column=0)

    for record in records:
        f_name_editor.insert(0,record[0])
        l_name_editor.insert(0,record[1])
        address_editor.insert(0,record[2])
        city_editor.insert(0,record[3])
        state_editor.insert(0,record[4])
        zipcode_editor.insert(0,record[5])

    edit_btn = Button(editor,text="edit record" ,command=edit)
    edit_btn.grid(row=6,column=0,columnspan=2,padx=10,ipadx=132)

    conn.commit()
    c.close()

   



#textbox
f_name = Entry(root,width=30 )
f_name.grid(row=0,column=1,padx=20, pady=(10,0))
l_name = Entry(root,width=30)
l_name.grid(row=1,column=1)
address = Entry(root,width=30)
address.grid(row=2,column=1)
city = Entry(root,width=30)
city.grid(row=3,column=1)
state = Entry(root,width=30)
state.grid(row=4,column=1)
zipcode = Entry(root,width=30)
zipcode.grid(row=5,column=1)
delete_entry = Entry(root,width=30)
delete_entry.grid(row=8,column=1,pady=10)


#label
f_name_ltl = Label(root,text="First Name:")
f_name_ltl.grid(row=0,column=0, pady=(10,0))
l_name_ltl = Label(root,text="last Name:")
l_name_ltl.grid(row=1,column=0)
address_ltl = Label(root,text="address :")
address_ltl.grid(row=2,column=0)
city_ltl = Label(root,text="city :")
city_ltl.grid(row=3,column=0)
state_ltl = Label(root,text="state :")
state_ltl.grid(row=4,column=0)
zipcode_ltl = Label(root,text="zipcode :")
zipcode_ltl.grid(row=5,column=0)
delete_ltl = Label(root,text="select ID :")
delete_ltl.grid(row=8,column=0)

#button
submit_btn = Button(root,text="add record to database" ,command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

#quary
quary_btn = Button(root,text="show result" ,command=quary)
quary_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=132)

#delete
delete_btn = Button(root,text="Delete record" ,command=delete)
delete_btn.grid(row=9,column=0,columnspan=2,pady=5,padx=10,ipadx=132)

#update
update_btn = Button(root,text="update record" ,command=update)
update_btn.grid(row=10,column=0,columnspan=2,padx=10,ipadx=132)




root.mainloop()
