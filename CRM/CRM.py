from tkinter import *
from PIL import ImageTk,Image
import mysql.connector
import csv
from tkinter import ttk


root = Tk()
root.title("CRM")
root.geometry("400x600")

mydb = mysql.connector.connect(
    host = "localhost",
    user="root",
    password = "",
    database = "yashraj"
    )

my_cursor = mydb.cursor()

#my_cursor.execute("CREATE DATABASE ")
#my_cursor.execute("CREATE TABLE customers(first_name VARCHAR(255),last_name VARCHAR(255),zipcode INT(6),price_paid DECIMAL(10,2),user_id INT AUTO_INCREMENT PRIMARY_KEY )")
"""my_cursor.execute(" ALTER TABLE customers ADD (\
                      email VARCHAR(255),\
                      address_1 VARCHAR(255),\
                      address_2 VARCHAR(255),\
                      city VARCHAR(50),\
                      state VARCHAR(50),\
                      phone VARCHAR(255) ,\
                      payment_methon VARCHAR(50),\
                      discount_code VARCHAR(255))")
"""

def clear_fields():
    first_name_box.delete(0,END)
    last_name_box.delete(0,END)
    email_box.delete(0,END)
    address_1_box.delete(0,END)
    address_2_box.delete(0,END)
    city_name_box.delete(0,END)
    state_name_box.delete(0,END)
    zipcode_box.delete(0,END)
    phone_box.delete(0,END)
    price_paid_box.delete(0,END)
    payment_methon_box.delete(0,END)
    discount_code_box.delete(0,END)
    


def add_customer():
    null = "NULL"
    # (NULL, 'bb', 'mbn', '35', 'bnmbmn', 'bmnbm', 'nbmn', 'mnbmnb', 'mnbmn', 'bmnb', 'mnbmn', 'bmbmb', 'mbm');
    sql_command = "INSERT INTO customers( user_id, first_name, last_name, zipcode, price_paid, email, address_1, address_2, city, state,phone,payment_methon, discount_code) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values = (null,first_name_box.get(), last_name_box.get(),zipcode_box.get(),price_paid_box.get(),email_box.get(), address_1_box.get(), address_2_box.get(), city_name_box.get(), state_name_box.get(),phone_box.get(),payment_methon_box.get(), discount_code_box.get())
    
    my_cursor.execute(sql_command,values)

    mydb.commit()

    clear_fields()

def write_to_csv(result):
    with open("customers.csv","a",newline='') as f:
        w = csv.writer(f,dialect='excel')
        for record in result:
            w.writerow(record)


def list_customers():
    list_customers_quary = Tk()
    list_customers_quary.title("List all customers")
    list_customers_quary.geometry("950x600")

    my_cursor.execute("SELECT * FROM customers")
    result = my_cursor.fetchall()
    heading_list = ["user ID","first name", "last name ", "zipcode", "price paid", "email", "address 1", "address 2", "city", "state","phone","payment methon", "discount code"]

    num=0
    for lbl in heading_list:
            heading_lbl  = Label(list_customers_quary,text=lbl)
            heading_lbl.grid(row=0,column=num,padx=5)
            num +=1


    
    for index,x in enumerate(result, start=1):
        num= 0
        for y in x :            
            lookup_lbl = Label(list_customers_quary,text=y)
            lookup_lbl.grid(row=index,column=num)
            num +=1
    csv_button = Button(list_customers_quary,text="Save to Excel",command=lambda:write_to_csv(result))
    csv_button.grid(row=index+1,column=0)



def search_customers():
    
    search_customers_quary = Tk()
    search_customers_quary.title("seach customers")
    search_customers_quary.geometry("1150x800")

    def update():
        sql_command ="""UPDATE customers SET first_name = %s,last_name = %s,zipcode = %s,price_paid = %s,email = %s,address_1 = %s,address_2 = %s,city = %s,state = %s,phone = %s,payment_methon = %s,discount_code = %s WHERE user_id = %s """
        inputs = (first_name_box_2.get(), last_name_box_2.get(),zipcode_box_2.get(),price_paid_box_2.get(),email_box_2.get(), address_1_box_2.get(), address_2_box_2.get(), city_name_box_2.get(), state_name_box_2.get(),phone_box_2.get(),payment_methon_box_2.get(), discount_code_box_2.get(),id_box_2.get())

        my_cursor.execute(sql_command,inputs)
        mydb.commit()

        search_customers_quary.destroy()
        

    def edit_data( user_id ,index):
        
        sql2 = "SELECT * FROM customers where user_id = %s"
        name2 = (user_id,)
        result2 = my_cursor.execute(sql2,name2)
        result2 = my_cursor.fetchall()
        
        

        #label
        index += 1 
        first_name_label_2 =  Label(search_customers_quary,text="First name ").grid(row=index+1,column=0 , stick=W,padx=10)
        last_name_label_2 =  Label(search_customers_quary,text="last name ").grid(row=index+2,column=0, stick=W,padx=10)
        email_label_2 =  Label(search_customers_quary,text="email").grid(row=index+3,column=0, stick=W,padx=10)
        address_1_label_2 =  Label(search_customers_quary,text="address 1").grid(row=index+4,column=0, stick=W,padx=10)
        address_2_label_2 =  Label(search_customers_quary,text="address 2 ").grid(row=index+5,column=0, stick=W,padx=10)
        city_name_label_2 =  Label(search_customers_quary,text="city name ").grid(row=index+6,column=0, stick=W,padx=10)
        state_name_label_2 =  Label(search_customers_quary,text="state name ").grid(row=index+7,column=0, stick=W,padx=10)
        zipcode_label_2 =  Label(search_customers_quary,text="zipcode name ").grid(row=index+8,column=0, stick=W,padx=10)
        phone_label_2 =  Label(search_customers_quary,text="phone").grid(row=index+9,column=0, stick=W,padx=10)
        price_paid_label_2 =  Label(search_customers_quary,text="price paid").grid(row=index+10,column=0, stick=W,padx=10)
        payment_methon_label_2 =  Label(search_customers_quary,text="payment methon").grid(row=index+11,column=0, stick=W,padx=10)
        discount_code_label_2 =  Label(search_customers_quary,text="discount code").grid(row=index+12,column=0, stick=W,padx=10)
        user_id_label_2 =  Label(search_customers_quary,text="user ID").grid(row=index+13,column=0, stick=W,padx=10)

        #entry
        global first_name_box_2
        first_name_box_2 = Entry(search_customers_quary)
        first_name_box_2.grid(row=index+1,column=1)
        first_name_box_2.insert(0,result2[0][1])

        global last_name_box_2
        last_name_box_2 = Entry(search_customers_quary)
        last_name_box_2.grid(row=index+2,column=1,pady=5)
        last_name_box_2.insert(0,result2[0][2])

        global email_box_2
        email_box_2 = Entry(search_customers_quary)
        email_box_2.grid(row=index+3,column=1,pady=5)
        email_box_2.insert(0,result2[0][5])

        global address_1_box_2
        address_1_box_2 = Entry(search_customers_quary)
        address_1_box_2.grid(row=index+4,column=1,pady=5)
        address_1_box_2.insert(0,result2[0][6])

        global address_2_box_2
        address_2_box_2 = Entry(search_customers_quary)
        address_2_box_2.grid(row=index+5,column=1,pady=5)
        address_2_box_2.insert(0,result2[0][7])

        global city_name_box_2
        city_name_box_2 = Entry(search_customers_quary)
        city_name_box_2.grid(row=index+6,column=1,pady=5)
        city_name_box_2.insert(0,result2[0][8])

        global state_name_box_2
        state_name_box_2 = Entry(search_customers_quary)
        state_name_box_2.grid(row=index+7,column=1,pady=5)
        state_name_box_2.insert(0,result2[0][9])

        global zipcode_box_2
        zipcode_box_2 = Entry(search_customers_quary)
        zipcode_box_2.grid(row=index+8,column=1,pady=5)
        zipcode_box_2.insert(0,result2[0][3])

        global phone_box_2
        phone_box_2 = Entry(search_customers_quary)
        phone_box_2.grid(row=index+9,column=1,pady=5)
        phone_box_2.insert(0,result2[0][10])

        global price_paid_box_2
        price_paid_box_2 = Entry(search_customers_quary)
        price_paid_box_2.grid(row=index+10,column=1,pady=5)
        price_paid_box_2.insert(0,result2[0][4])

        global payment_methon_box_2
        payment_methon_box_2 = Entry(search_customers_quary)
        payment_methon_box_2.grid(row=index+11,column=1,pady=5)
        payment_methon_box_2.insert(0,result2[0][11])

        global discount_code_box_2
        discount_code_box_2 = Entry(search_customers_quary)
        discount_code_box_2.grid(row=index+12,column=1,pady=5)
        discount_code_box_2.insert(0,result2[0][12])

        global id_box_2
        id_box_2 = Entry(search_customers_quary)
        id_box_2.grid(row=index+13,column=1,pady=5)
        id_box_2.insert(0,result2[0][0])
        id_box_2.configure(state='readonly')

        save_record = Button(search_customers_quary,text="update record",command=update)
        save_record.grid(row=index+14,column=0,padx=10)
        


    def search_custromer():
        selected = drop.get()

        if selected == "Search by...":
            test = Label(search_customers_quary,text="You forgot to select from dropdown")
            test.grid(row=2,column=0)
        if selected == "Last name":
            sql = "SELECT * FROM customers where last_name = %s"
            
        if selected == "Email ID":
            sql = "SELECT * FROM customers where email = %s"
            
        if selected == "Custromer ID":
            sql = "SELECT * FROM customers where user_id = %s"
            
        searched = search_entry_box.get()
        name = (searched,)
        result = my_cursor.execute(sql,name)
        result = my_cursor.fetchall()

        if not result :
            result = "Record not found..."
            searched_lbl = Label(search_customers_quary,text=result)
            searched_lbl.grid(row=2,column=0,padx=10,pady=10)
                

        else:
            
            for index,x in enumerate(result, start=2):
               # print(str(index) + ":" + str(x))
                num= 1
                #global user_id
                c_id = str(x[0])
               # print(type(user_id))
                edit_btn = Button(search_customers_quary,text="edit"+c_id,command=lambda c_id=c_id: edit_data(c_id,index))
                edit_btn.grid(row=index,column=0)
                
                for y in x :            
                    searched_lbl = Label(search_customers_quary,text=y)
                    searched_lbl.grid(row=index,column=num,padx=10,pady=10)
                    num +=1
            csv_button = Button(search_customers_quary,text="Save to Excel",command=lambda:write_to_csv(result))
            csv_button.grid(row=index+1,column=0)

                
        
    search_lbl = Label(search_customers_quary,text="Search customer :")
    search_lbl.grid(row=0,column=0,padx=10)

    search_entry_box = Entry(search_customers_quary)
    search_entry_box.grid(row=0,column=1,padx=10)

    search_entry_button = Button(search_customers_quary,text="seach customer",command=search_custromer)
    search_entry_button.grid(row=1,column=0,padx=10,pady=10)

    drop = ttk.Combobox(search_customers_quary,value=["Search by...","Last name","Email ID","Custromer ID"])
    drop.current(0)
    drop.grid(row=0,column=2) 
    

title_label = Label(root,text="Yashraj customer database",font=("Helvetica",16))
title_label.grid(row=0,column=0,columnspan=2,pady="10")

#label
first_name_label =  Label(root,text="First name ").grid(row=1,column=0 , stick=W,padx=10)
last_name_label =  Label(root,text="last name ").grid(row=2,column=0, stick=W,padx=10)
email_label =  Label(root,text="email").grid(row=3,column=0, stick=W,padx=10)
address_1_label =  Label(root,text="address 1").grid(row=4,column=0, stick=W,padx=10)
address_2_label =  Label(root,text="address 2 ").grid(row=5,column=0, stick=W,padx=10)
city_name_label =  Label(root,text="city name ").grid(row=6,column=0, stick=W,padx=10)
state_name_label =  Label(root,text="state name ").grid(row=7,column=0, stick=W,padx=10)
zipcode_label =  Label(root,text="zipcode name ").grid(row=8,column=0, stick=W,padx=10)
phone_label =  Label(root,text="phone").grid(row=9,column=0, stick=W,padx=10)
price_paid_label =  Label(root,text="price paid").grid(row=10,column=0, stick=W,padx=10)
payment_methon_label =  Label(root,text="payment methon").grid(row=11,column=0, stick=W,padx=10)
discount_code_label =  Label(root,text="discount code").grid(row=12,column=0, stick=W,padx=10)

#entry 
first_name_box = Entry(root)
first_name_box.grid(row=1,column=1)

last_name_box = Entry(root)
last_name_box.grid(row=2,column=1,pady=5)

email_box = Entry(root)
email_box.grid(row=3,column=1,pady=5)

address_1_box = Entry(root)
address_1_box.grid(row=4,column=1,pady=5)

address_2_box = Entry(root)
address_2_box.grid(row=5,column=1,pady=5)

city_name_box = Entry(root)
city_name_box.grid(row=6,column=1,pady=5)

state_name_box = Entry(root)
state_name_box.grid(row=7,column=1,pady=5)

zipcode_box = Entry(root)
zipcode_box.grid(row=8,column=1,pady=5)

phone_box = Entry(root)
phone_box.grid(row=9,column=1,pady=5)

price_paid_box = Entry(root)
price_paid_box.grid(row=10,column=1,pady=5)

payment_methon_box = Entry(root)
payment_methon_box.grid(row=11,column=1,pady=5)

discount_code_box = Entry(root)
discount_code_box.grid(row=12,column=1,pady=5)

#button

add_customer_button= Button(root,text="add customer to databse",command=add_customer)
add_customer_button.grid(row=13,column=0,padx=10,pady=10)

clear_fields_button= Button(root,text="clear fields",command=clear_fields)
clear_fields_button.grid(row=13,column=1)

list_customers_button= Button(root,text="list customers",command=list_customers)
list_customers_button.grid(row=14,column=0,padx=10,pady=10)


search_customers_button= Button(root,text="search customers",command=search_customers)
search_customers_button.grid(row=14,column=1,sticky=W ,padx=10)


root.mainloop()
