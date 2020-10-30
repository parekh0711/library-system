from tkinter import *
from tkinter import font as tkFont
from PIL import ImageTk, Image
import sqlite3
from sqlite3 import Error

def execute_instruction(conn,instruction):
    try:
        c=conn.cursor()
        c.execute(instruction)
    except Error as e:
        print(e)

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def select(conn,instruction):
    try:
        c=conn.cursor()
        c.execute(instruction)
        rows=c.fetchall()
        for row in rows:
            for element in row:
                print(element,end="\t")
            print("")
    except Error as e:
        print(e)

def change_employee():
    fetch_employee()
    ins0 = "DELETE FROM employee WHERE employee_id='{}';".format(employeeid_entry.get())
    ins = "INSERT INTO employee VALUES({},{},'{}','{}','{}','{}','{}','{}','{}');".format(employeeid_entry.get(),aadhar_entry.get(),pan_entry.get(),firstname_entry.get(),lastname_entry.get(),dob_entry.get(),phone_entry.get(),address_entry.get(),designation_entry.get())
    database = r"lib.db"
    conn = create_connection(database)

    if conn is not None:
        execute_instruction(conn,ins0)
        execute_instruction(conn,ins)
        conn.commit()
    else:
        print("Error! cannot create the database connection.")

def fetch_employee():
    ins0 = "SELECT * FROM employee WHERE employee_id='{}';".format(employeeid_entry.get())

    database = r"lib.db"
    conn = create_connection(database)

    if conn is not None:
        select(conn,ins0)
        conn.commit()
    else:
        print("Error! cannot create the database connection.")

def select_and_print(conn,instruction):
    try:
        c=conn.cursor()
        c.execute(instruction)
        rows=c.fetchall()
        return rows
    except Error as e:
        print(e)

def delete_employee():
    ins = "DELETE FROM employee WHERE employee_id='{}';".format(employeeid_entry.get())
    database = r"lib.db"
    conn = create_connection(database)

    if conn is not None:
        execute_instruction(conn,ins)
        conn.commit()
    else:
        print("Error! cannot create the database connection.")

def add_policy():
    ins = "INSERT INTO policies VALUES('{}','{}','{}');".format(barcode_entry.get(),length_entry.get(),description_entry.get())
    database = r"lib.db"
    conn = create_connection(database)

    if conn is not None:
        execute_instruction(conn,ins)
        conn.commit()
    else:
        print("Error! cannot create the database connection.")

def delete_policy():
    ins = "DELETE FROM policies WHERE barcode='{}';".format(barcode_entry.get())
    database = r"lib.db"
    conn = create_connection(database)

    if conn is not None:
        execute_instruction(conn,ins)
        conn.commit()
    else:
        print("Error! cannot create the database connection.")

def change_policy():
    fetch_policy()
    ins0 = "DELETE FROM policies WHERE barcode='{}';".format(barcode_entry.get())
    ins = "INSERT INTO policies VALUES('{}','{}','{}');".format(barcode_entry.get(),length_entry.get(),description_entry.get())
    database = r"lib.db"
    conn = create_connection(database)

    if conn is not None:
        execute_instruction(conn,ins0)
        execute_instruction(conn,ins)
        conn.commit()
    else:
        print("Error! cannot create the database connection.")

def fetch_policy():
    ins0 = "SELECT * FROM policies WHERE barcode='{}';".format(barcode_entry.get())

    database = r"lib.db"
    conn = create_connection(database)

    if conn is not None:
        select(conn,ins0)
        conn.commit()
    else:
        print("Error! cannot create the database connection.")

def add_product_book():
    ins0 = "INSERT INTO product VALUES('{}',Book,In_stock);".format(barcode_entry.get())
    ins="INSERT INTO book VALUES('{}','{}','{}','{}','{}','{}','{}','{}');".format(barcode_entry.get(),authorid_entry.get(),title_entry.get(),year_entry.get(),publisher_entry.get(),genre_entry.get(),cost_entry.get(),cond_entry.get())
    database = r"lib.db"
    conn = create_connection(database)

    if conn is not None:
        execute_instruction(conn,ins)
        execute_instruction(conn,ins0)
        conn.commit()
    else:
        print("Error! cannot create the database connection.")

def add_product_media():
    ins0 = "INSERT INTO product VALUES('{}',CD,In_stock);".format(barcode_entry.get())
    ins="INSERT INTO media VALUES('{}','{}','{}','{}','{}','{}','{}','{}');".format(barcode_entry.get(),title_entry.get(),year_entry.get(),runtime_entry.get(),category_entry.get(),cost_entry.get(),cond_entry.get(),genre_entry.get())
    database = r"lib.db"
    conn = create_connection(database)

    if conn is not None:
        execute_instruction(conn,ins)
        execute_instruction(conn,ins0)
        conn.commit()
    else:
        print("Error! cannot create the database connection.")

def delete_product_book():
    ins = "DELETE FROM book WHERE barcode='{}';".format(barcode_entry.get())
    ins0 = "DELETE FROM product WHERE barcode='{}';".format(barcode_entry.get())
    database = r"lib.db"
    conn = create_connection(database)

    if conn is not None:
        execute_instruction(conn,ins)
        execute_instruction(conn,ins0)
        conn.commit()
    else:
        print("Error! cannot create the database connection.")

def delete_media():
    ins = "DELETE FROM media WHERE barcode='{}';".format(barcode_entry.get())
    ins0 = "DELETE FROM product WHERE barcode='{}';".format(barcode_entry.get())
    database = r"lib.db"
    conn = create_connection(database)

    if conn is not None:
        execute_instruction(conn,ins)
        execute_instruction(conn,ins0)
        conn.commit()
    else:
        print("Error! cannot create the database connection.")

def fetch_book():
    ins0 = "SELECT * FROM book WHERE barcode='{}';".format(barcode_entry.get())

    database = r"lib.db"
    conn = create_connection(database)

    if conn is not None:
        select(conn,ins0)
        conn.commit()
    else:
        print("Error! cannot create the database connection.")

def fetch_media():
    ins0 = "SELECT * FROM media WHERE barcode='{}';".format(barcode_entry.get())

    database = r"lib.db"
    conn = create_connection(database)

    if conn is not None:
        select(conn,ins0)
        conn.commit()
    else:
        print("Error! cannot create the database connection.")

def change_product_book():
    fetch_book()
    ins0 = "DELETE FROM book WHERE barcode='{}';".format(barcode_entry.get())
    ins="INSERT INTO book VALUES('{}','{}','{}','{}','{}','{}','{}','{}');".format(barcode_entry.get(),authorid_entry.get(),title_entry.get(),year_entry.get(),publisher_entry.get(),genre_entry.get(),cost_entry.get(),cond_entry.get())
    database = r"lib.db"
    conn = create_connection(database)

    if conn is not None:
        execute_instruction(conn,ins0)
        execute_instruction(conn,ins)
        conn.commit()
    else:
        print("Error! cannot create the database connection.")

def change_product_media():
    fetch_media()
    ins0 = "DELETE FROM media WHERE barcode='{}';".format(barcode_entry.get())
    ins="INSERT INTO media VALUES('{}','{}','{}','{}','{}','{}','{}','{}');".format(barcode_entry.get(),title_entry.get(),year_entry.get(),runtime_entry.get(),category_entry.get(),cost_entry.get(),cond_entry.get(),genre_entry.get())
    database = r"lib.db"
    conn = create_connection(database)

    if conn is not None:
        execute_instruction(conn,ins0)
        execute_instruction(conn,ins)
        conn.commit()
    else:
        print("Error! cannot create the database connection.")

def check_profit():
    ins="SELECT (sell_cost-order_cost) as profits from profit where barcode='{}';".format(barcode_entry.get())
    database = r"lib.db"
    conn = create_connection(database)

    if conn is not None:
        select(conn,ins)
        conn.commit()
    else:
        print("Error! cannot create the database connection.")

class StartPage:
    def __init__(self, window):
        def callback(event):
            global flag
            if 513<=event.x<=699 and 320<=event.y<=368:
                print("admin")
                C.destroy()
                AdminLoginPage(window)
            elif 463<= event.x<=751 and 385 <= event.y<=436:
                print("employee")
                C.destroy()
                EmployeeLoginPage(window)

        C = Canvas(window, height=756, width=1210)
        C.bind("<Button-1>", callback)
        background_image = PhotoImage(file="images/startfinal.png")
        C.create_image(0, 0, image=background_image, anchor="nw")
        window.title("PJ Store")
        C.pack()
        window.mainloop()

class EmployeeLoginPage:
    def __init__(self, window):
        D = Canvas(window, height=756, width=1210)

        def validate_login():
            emp_id = password_entry.get()
            D.destroy()
            password_entry.destroy()
            login_button.destroy()
            print(emp_id)
            EmployeePage(window,emp_id)

        def callback(event):
            global flag
            print(event.x,event.y)
            if 38<=event.x<=210 and 617<=event.y<=667:
                D.destroy()
                StartPage(window)

        helv36 = tkFont.Font(family='Helvetica', size=15, weight='bold')
        D.bind("<Button-1>", callback)
        background = PhotoImage(file="images/employeelogin.png")
        D.create_image(0, 0, image=background, anchor="nw")
        password= StringVar()
        password_entry = Entry(window,textvariable=password,width=30)
        password_entry['font']=helv36
        password_entry.pack()
        password_entry.place(x=460,y=269)

        login_button = Button(window,text="LOGIN",command = validate_login)
        login_button['font']=helv36
        login_button.pack()
        login_button.place(x=573,y=335)
        D.pack()
        window.mainloop()

class EmployeePage:
    def __init__(self, window,emp_id):
        def callback(event):
            global flag
            print(event.x,event.y)
            if 173<=event.x<=503 and 180<=event.y<=225:
                C.destroy()
                EmployeeReservationPage(window,emp_id)
            elif 256<=event.x<=433 and 312<=event.y<=368:
                C.destroy()
                EmployeeBillingPage(window,emp_id)
            elif 158<=event.x<=525 and 450<=event.y<=496:
                C.destroy()
                EmployeeCheckPage(window,emp_id,1)
                #author
            elif 704<=event.x<=1036 and 180<=event.y<=223:
                C.destroy()
                EmployeeReturnPage(window,emp_id)
            elif 706<=event.x<=1025 and 314<=event.y<=356:
                C.destroy()
                EmployeeCheckPage(window,emp_id,2)
                #book
            elif 738<=event.x<=996 and 449<=event.y<=495:
                C.destroy()
                EmployeeCheckPage(window,emp_id,3)
                #CD
            elif 38<=event.x<=210 and 617<=event.y<=667:
                C.destroy()
                EmployeePage(window)

        C = Canvas(window, height=756, width=1210)
        C.bind("<Button-1>", callback)
        background_image = PhotoImage(file="images/employeemain.png")
        C.create_image(0, 0, image=background_image, anchor="nw")
        window.title("PJ Store")
        C.pack()
        window.mainloop()

class EmployeeReservationPage:
    def __init__(self, window,emp_id):

        result_label=0
        helvbig = tkFont.Font(family='Helvetica', size=24, weight='bold')
        def callback(event):
            global flag
            print(event.x,event.y)
            if 40<=event.x<=210 and 616<=event.y<=664:
                C.destroy()
                EmployeePage(window,emp_id)

        def check_date(s,p):
            l1=s.split('-')
            l2=p.split('-')
            year1=l1[0]
            year2=l2[0]
            month1=l1[1]
            month2=l2[1]
            day1=l1[2]
            day2=l2[2]
            if int(year1)>int(year2):
                return True
            elif int(year1)<int(year2):
                return False
            elif int(year1)==int(year2):
                if int(month1)>int(month2):
                    return True
                elif int(month1)<int(month2):
                    return False
                elif int(month1)==int(month2):
                    if int(day1)>int(day2):
                        return True
                    elif int(day1)<int(day2):
                        return False
                    elif int(day1)==int(day2):
                        return False

        def reserve_item():
            global title_label
            database = r"lib.db"
            conn = create_connection(database)
            stat = "Error"
            if conn is not None:
                ins1 = "SELECT state FROM product WHERE barcode='{}';".format(barcode_entry.get())
                a=select_and_print(conn,ins1)
                conn.commit()
                if a[0][0]=="borrowed" or a[0][0]=="Borrowed":
                    ins2= "SELECT due_date from outstanding where barcode='{}';".format(barcode_entry.get())
                    b=select_and_print(conn,ins2)
                    conn.commit()
                    due=b[0][0]
                    start=startdate_entry.get()
                    if check_date(start,due):
                        ins3="INSERT INTO reservation VALUES ('{}','{}','{}','{}');".format(customerid_entry.get(),barcode_entry.get(),reservedate_entry.get(),startdate_entry.get())
                        execute_instruction(conn,ins3)
                        conn.commit()
                    else:
                        stat="Unavailable"  #for now
                else:
                    ins4="INSERT INTO reservation VALUES ('{}','{}','{}','{}');".format(customerid_entry.get(),barcode_entry.get(),reservedate_entry.get(),startdate_entry.get())
                    ins5="UPDATE product SET state='reserved' where barcode='{}';".format(barcode_entry.get())
                    execute_instruction(conn,ins4)
                    execute_instruction(conn,ins5)
                    conn.commit()
                    stat="Reserved"
                try:
                    title_label.destroy()
                except:
                    pass
                title_label = Label(window, text=stat)
                title_label['font']=helvbig
                title_label.pack()
                title_label.place(x=523,y=523)
            else:
                print("Error! cannot create the database connection.")

        #place entry box at (412,427) and (439,259)
        C = Canvas(window, height=756, width=1210)
        C.bind("<Button-1>", callback)
        background_image = PhotoImage(file="images/employeereserve.png")
        C.create_image(0, 0, image=background_image, anchor="nw")
        window.title("PJ Store")
        C.pack()

        helv36 = tkFont.Font(family='Helvetica', size=15, weight='bold')
        startdate= StringVar()
        startdate_entry = Entry(window,textvariable=startdate,width=15)
        startdate_entry['font']=helv36
        startdate_entry.pack()
        startdate_entry.place(x=327,y=263)

        reservedate= StringVar()
        reservedate_entry = Entry(window,textvariable=reservedate,width=15)
        reservedate_entry['font']=helv36
        reservedate_entry.pack()
        reservedate_entry.place(x=402,y=438)

        customerid= StringVar()
        customerid_entry = Entry(window,textvariable=customerid,width=15)
        customerid_entry['font']=helv36
        customerid_entry.pack()
        customerid_entry.place(x=662,y=264)

        barcode= StringVar()
        barcode_entry = Entry(window,textvariable=barcode,width=15)
        barcode_entry['font']=helv36
        barcode_entry.pack()
        barcode_entry.place(x=728,y=436)

        login_button = Button(window,text="OK",command = reserve_item,width=10)
        login_button['font']=helv36
        login_button.pack()
        login_button.place(x=572,y=625)

        window.mainloop()

class EmployeeBillingPage:
    def __init__(self, window,emp_id):
        def callback(event):
            global flag
            print(event.x,event.y)
            if 40<=event.x<=210 and 616<=event.y<=664:
                C.destroy()
                EmployeePage(window,emp_id)
            elif 577<=event.x<=670 and 622<=event.y<=675:
                billing_item()

        def billing_item():
            database = r"lib.db"
            conn = create_connection(database)
            if conn is not None:
                ins1 = "SELECT date('{}','+007 days');".format(borroweddate_entry.get())
                a=select_and_print(conn,ins1)
                conn.commit()
                res=a[0][0]
                ins2 = "SELECT renewed FROM CUSTOMER WHERE customer_id='{}';".format(customerid_entry.get())
                a=select_and_print(conn,ins2)
                conn.commit()
                if a[0][0]=="renewed":
                    amt=0
                    penalty=0
                else:
                    amt=100
                    penalty=0
                status='Not returned'
                ins3 = "INSERT INTO outstanding VALUES('{}','{}','{}','{}','{}','{}','{}','{}');".format(customerid_entry.get(),employeeid_entry.get(),barcode_entry.get(),amt,penalty,status,res,borroweddate_entry.get())
                ins4 = "UPDATE product SET state='Borrowed' WHERE barcode='{}';".format(barcode_entry.get())
                ins5 = "INSERT INTO borrowed VALUES('{}','{}');".format(barcode_entry.get(),customerid_entry.get())
                execute_instruction(conn,ins3)
                execute_instruction(conn,ins4)
                execute_instruction(conn,ins5)
                conn.commit()
            else:
                print("Error! cannot create the database connection.")

        #place entry box at (412,427) and (439,259)
        C = Canvas(window, height=756, width=1210)
        C.bind("<Button-1>", callback)
        background_image = PhotoImage(file="images/employeebilling.png")
        C.create_image(0, 0, image=background_image, anchor="nw")
        window.title("PJ Store")

        C.pack()

        helv36 = tkFont.Font(family='Helvetica', size=15, weight='bold')
        employeeid= StringVar()
        employeeid_entry = Entry(window,textvariable=employeeid,width=15)
        employeeid_entry['font']=helv36
        employeeid_entry.pack()
        employeeid_entry.place(x=415,y=207)
        employeeid.set(emp_id)

        borroweddate= StringVar()
        borroweddate_entry = Entry(window,textvariable=borroweddate,width=15)
        borroweddate_entry['font']=helv36
        borroweddate_entry.pack()
        borroweddate_entry.place(x=706,y=438)

        customerid= StringVar()
        customerid_entry = Entry(window,textvariable=customerid,width=15)
        customerid_entry['font']=helv36
        customerid_entry.pack()
        customerid_entry.place(x=413,y=417)

        barcode= StringVar()
        barcode_entry = Entry(window,textvariable=barcode,width=15)
        barcode_entry['font']=helv36
        barcode_entry.pack()
        barcode_entry.place(x=719,y=207)

        window.mainloop()

class EmployeeCheckPage:
    def __init__(self, window,emp_id,mode):
        title_label = 0
        def check_book():
            global title_label
            ins = "SELECT state FROM product,book WHERE book.title='{}' and book.barcode=product.barcode;".format(title_entry.get())
            database = r"lib.db"
            conn = create_connection(database)

            if conn is not None:
                print("hi")
                a=select_and_print(conn,ins)#returns the state as list of tuples which will have only one value
                print(a)
                #430 352
                try:
                    title_label.destroy()
                except:
                    pass
                if a ==[]:
                    a=["Not Found"]
                if a[0][0]=="in_stock":
                    a=["In Stock"]
                title_label = Label(window, text=a[0])
                title_label['font']=helvbig
                title_label.pack()
                title_label.place(x=530,y=341)
                conn.commit()

            else:
                print("Error! cannot create the database connection.")

        def check_media():
            global title_label
            ins = "SELECT state FROM product,media WHERE media.title='{}' and media.barcode=product.barcode;".format(title_entry.get())
            database = r"lib.db"
            conn = create_connection(database)

            if conn is not None:
                a=select_and_print(conn,ins)#returns the state as list of tuples which will have only one value
                try:
                    title_label.destroy()
                    print("destroyed")
                except:
                    pass
                if a ==[]:
                    a=["Not Found"]
                if a[0][0]=="in_stock":
                    a=["In Stock"]
                title_label = Label(window, text=a[0])
                title_label['font']=helvbig
                title_label.pack()
                title_label.place(x=530,y=341)
                conn.commit()
            else:
                print("Error! cannot create the database connection.")

        def check_author():
            global title_label
            name = title_entry.get().split()
            ins = "SELECT book.title FROM author,book WHERE author.first_name='{}' and author.last_name='{}' and author.author_id=book.author_id;".format(name[0],name[1])
            database = r"lib.db"
            conn = create_connection(database)

            if conn is not None:
                a=select_and_print(conn,ins)
                conn.commit()
                try:
                    title_label.destroy()
                except:
                    pass

                title_label = Label(window, text="{} books found.".format(len(a)))
                title_label['font']=helvbig
                title_label.pack()
                title_label.place(x=530,y=341)

                for tuple in a:
                    print(tuple[0])

            else:
                print("Error! cannot create the database connection.")

        def check_item():
            if mode==1:
                check_author()
            elif mode==2:
                check_book()
            elif mode==3:
                check_media()

        def callback(event):
            global flag
            print(event.x,event.y)
            if 40<=event.x<=210 and 616<=event.y<=664:
                C.destroy()
                EmployeePage(window,emp_id)
            elif 577<event.x<=690 and 502<=event.y<=560:
                check_item()

        #place entry box at (412,427) and (439,259)
        C = Canvas(window, height=756, width=1210)
        C.bind("<Button-1>", callback)
        background_image = PhotoImage(file="images/employeecheck.png")
        C.create_image(0, 0, image=background_image, anchor="nw")
        window.title("PJ Store")
        C.pack()


        helv36 = tkFont.Font(family='Helvetica', size=15, weight='bold')
        helvbig = tkFont.Font(family='Helvetica', size=24, weight='bold')
        title= StringVar()
        title_entry = Entry(window,textvariable=title,width=15)
        title_entry['font']=helv36
        title_entry.pack()
        title_entry.place(x=525,y=238)

        window.mainloop()

class EmployeeReturnPage:

    def __init__(self, window,emp_id):
        renewed_label = 0
        payment_label = 0
        helvbig = tkFont.Font(family='Helvetica', size=24, weight='bold')

        def return_item():
            global renewed_label, payment_label
            ins1 = "SELECT renewed FROM CUSTOMER WHERE customer_id='{}';".format(customerid_entry.get())
            ins2 = "SELECT (amount+penalty) AS payment FROM outstanding where customer_id='{}' and employee_id='{}' and barcode='{}';".format(customerid_entry.get(),employeeid_entry.get(),barcode_entry.get())
            ins3 = "UPDATE outstanding SET status='returned' where barcode='{}';".format(barcode_entry.get())
            ins4 = "UPDATE product SET state='in_stock' where barcode='{}';".format(barcode_entry.get())
            ins5 = "DELETE FROM borrowed WHERE barcode='{}';".format(barcode_entry.get())
            database = r"lib.db"
            conn = create_connection(database)

            if conn is not None:
                a=select_and_print(conn,ins1)
                b=select_and_print(conn,ins2)
                execute_instruction(conn,ins3)
                execute_instruction(conn,ins4)
                conn.commit()

                try:
                    renewed_label.destroy()
                except:
                    pass
                if a ==[]:
                    a=["Not Found"]
                if a[0][0]=="in_stock":
                    a=["In Stock"]
                renewed_label = Label(window, text=a[0][0])
                renewed_label['font']=helvbig
                renewed_label.pack()
                renewed_label.place(x=901,y=310)

                try:
                    payment_label.destroy()
                except:
                    pass
                if a ==[]:
                    a=["Not Found"]
                if a[0][0]=="in_stock":
                    a=["In Stock"]
                payment_label = Label(window, text="Amount = {} Rs".format(b[0][0]))
                payment_label['font']=helvbig
                payment_label.pack()
                payment_label.place(x=901,y=452)

            else:
                print("Error! cannot create the database connection.")


        def callback(event):
            global flag
            print(event.x,event.y)
            if 40<=event.x<=210 and 616<=event.y<=664:
                C.destroy()
                EmployeePage(window,emp_id)
            elif 577<=event.x<=671 and 624<=event.y<=675:
                return_item()


        C = Canvas(window, height=756, width=1210)
        C.bind("<Button-1>", callback)
        background_image = PhotoImage(file="images/employeereturn.png")
        C.create_image(0, 0, image=background_image, anchor="nw")
        window.title("PJ Store")
        C.pack()

        helv36 = tkFont.Font(family='Helvetica', size=15, weight='bold')
        employeeid= StringVar()
        employeeid_entry = Entry(window,textvariable=employeeid,width=30)
        employeeid_entry['font']=helv36
        employeeid_entry.pack()
        employeeid_entry.place(x=505,y=226)
        employeeid.set(emp_id)

        customerid= StringVar()
        customerid_entry = Entry(window,textvariable=customerid,width=30)
        customerid_entry['font']=helv36
        customerid_entry.pack()
        customerid_entry.place(x=505,y=366)

        barcode= StringVar()
        barcode_entry = Entry(window,textvariable=barcode,width=30)
        barcode_entry['font']=helv36
        barcode_entry.pack()
        barcode_entry.place(x=505,y=484)

        window.mainloop()

#Admin Pages

class AdminLoginPage:
    def __init__(self, window):
        D = Canvas(window, height=756, width=1210)

        def validate_login():
            pwd = password_entry.get()
            with open("pwd.txt","r") as source:
                test = source.read()
                test = test[:-1]
                pwd2 = ''
                for letter in test:
                    pwd2+=chr(ord(letter)-1)
                if pwd == pwd2:
                    D.destroy()
                    password_entry.destroy()
                    login_button.destroy()
                    AdminPage(window)
                else:
                    return

        def callback(event):
            global flag
            print(event.x,event.y)
            if 38<=event.x<=210 and 617<=event.y<=667:
                D.destroy()
                StartPage(window)
        helv36 = tkFont.Font(family='Helvetica', size=15, weight='bold')
        D.bind("<Button-1>", callback)
        background = PhotoImage(file="images/adminlogin.png")
        D.create_image(0, 0, image=background, anchor="nw")
        password= StringVar()
        password_entry = Entry(window,textvariable=password,show="*",width=30)
        password_entry['font']=helv36
        password_entry.pack()
        password_entry.place(x=460,y=269)
        login_button = Button(window,text="LOGIN",command = validate_login)
        login_button['font']=helv36
        login_button.pack()
        login_button.place(x=573,y=335)
        D.pack()
        window.mainloop()

class AdminPage:
    def __init__(self, window):
        def callback(event):
            global flag
            print(event.x,event.y)
            if 139<=event.x<=414 and 228<=event.y<=275:
                C.destroy()
                EmployeeAdminAddPage(window)
            elif 100<=event.x<=439 and 335<=event.y<=381:
                C.destroy()
                EmployeeAdminChangePage(window)
            elif 96<=event.x<=445 and 451<=event.y<=498:
                C.destroy()
                EmployeeAdminDeletePage(window)
            elif 860<=event.x<=1113 and 228<=event.y<=270:
                ProductAdminTypeAddPage(window)
            elif 835<=event.x<=1142 and 330<=event.y<=378:
                ProductAdminTypeChangePage(window)
            elif 835<=event.x<=1139 and 460<=event.y<=497:
                ProductAdminTypeDeletePage(window)

        C = Canvas(window, height=756, width=1210)
        C.bind("<Button-1>", callback)
        background_image = PhotoImage(file="images/adminselect.png")
        C.create_image(0, 0, image=background_image, anchor="nw")
        window.title("PJ Store")
        C.pack()
        window.mainloop()

class EmployeeAdminAddPage:
    def __init__(self, window):

        def add_employee():
            ins = "INSERT INTO employee VALUES({},{},'{}','{}','{}','{}','{}','{}','{}');".format(employeeid_entry.get(),aadhar_entry.get(),pan_entry.get(),firstname_entry.get(),lastname_entry.get(),dob_entry.get(),phone_entry.get(),address_entry.get(),designation_entry.get())
            database = r"lib.db"
            conn = create_connection(database)

            if conn is not None:
                execute_instruction(conn,ins)
                select(conn,"SELECT * FROM employee;")
                conn.commit()
            else:
                print("Error! cannot create the database connection.")

        def callback(event):
            global flag
            print(event.x,event.y)
            if 1016<=event.x<=1125 and 622<=event.y<=670:
                add_employee()
            elif 55<=event.x<=195 and 625<=event.y<=668:
                employeeid_entry.destroy()
                aadhar_entry.destroy()
                pan_entry.destroy()
                firstname_entry.destroy()
                lastname_entry.destroy()
                designation_entry.destroy()
                salary_entry.destroy()
                phone_entry.destroy()
                address_entry.destroy()
                dob_entry.destroy()
                C.destroy()
                AdminPage(window)


        C = Canvas(window, height=756, width=1210)
        C.bind("<Button-1>", callback)
        background_image = PhotoImage(file="images/adminemployee.png")
        C.create_image(0, 0, image=background_image, anchor="nw")
        window.title("PJ Store")
        C.pack()

        helv36 = tkFont.Font(family='Helvetica', size=15, weight='bold')
        employeeid= StringVar()
        employeeid_entry = Entry(window,textvariable=employeeid,width=30)
        employeeid_entry['font']=helv36
        employeeid_entry.pack()
        employeeid_entry.place(x=218,y=208)

        aadhar= StringVar()
        aadhar_entry = Entry(window,textvariable=aadhar,width=30)
        aadhar_entry['font']=helv36
        aadhar_entry.pack()
        aadhar_entry.place(x=218,y=288)

        firstname= StringVar()
        firstname_entry = Entry(window,textvariable=firstname,width=30)
        firstname_entry['font']=helv36
        firstname_entry.pack()
        firstname_entry.place(x=218,y=368)

        lastname= StringVar()
        lastname_entry = Entry(window,textvariable=lastname,width=30)
        lastname_entry['font']=helv36
        lastname_entry.pack()
        lastname_entry.place(x=218,y=448)

        pan= StringVar()
        pan_entry = Entry(window,textvariable=pan,width=30)
        pan_entry['font']=helv36
        pan_entry.pack()
        pan_entry.place(x=218,y=528)

        dob= StringVar()
        dob_entry = Entry(window,textvariable=dob,width=30)
        dob_entry['font']=helv36
        dob_entry.pack()
        dob_entry.place(x=608,y=208)

        phone= StringVar()
        phone_entry = Entry(window,textvariable=phone,width=30)
        phone_entry['font']=helv36
        phone_entry.pack()
        phone_entry.place(x=608,y=288)

        address= StringVar()
        address_entry = Entry(window,textvariable=address,width=30)
        address_entry['font']=helv36
        address_entry.pack()
        address_entry.place(x=608,y=368)

        salary= StringVar()
        salary_entry = Entry(window,textvariable=salary,width=30)
        salary_entry['font']=helv36
        salary_entry.pack()
        salary_entry.place(x=608,y=448)

        designation= StringVar()
        designation_entry = Entry(window,textvariable=designation,width=30)
        designation_entry['font']=helv36
        designation_entry.pack()
        designation_entry.place(x=608,y=528)
        window.mainloop()

class EmployeeAdminChangePage:
    def __init__(self, window):

        def change_employee():
            ins = "INSERT INTO employee VALUES({},{},'{}','{}','{}','{}','{}','{}','{}');".format(employeeid_entry.get(),aadhar_entry.get(),pan_entry.get(),firstname_entry.get(),lastname_entry.get(),dob_entry.get(),phone_entry.get(),address_entry.get(),designation_entry.get())
            database = r"lib.db"
            conn = create_connection(database)

            if conn is not None:
                execute_instruction(conn,ins)
                select(conn,"SELECT * FROM employee;")
                conn.commit()
            else:
                print("Error! cannot create the database connection.")

        def fetch_employee():
            return

        def callback(event):
            global flag
            print(event.x,event.y)
            if 1016<=event.x<=1125 and 622<=event.y<=670:
                change_employee()
            elif 520<=event.x<=685 and 622<=event.y<=666:
                fetch_employee()
            elif 55<=event.x<=195 and 625<=event.y<=668:
                employeeid_entry.destroy()
                aadhar_entry.destroy()
                pan_entry.destroy()
                firstname_entry.destroy()
                lastname_entry.destroy()
                designation_entry.destroy()
                salary_entry.destroy()
                phone_entry.destroy()
                address_entry.destroy()
                dob_entry.destroy()
                C.destroy()
                AdminPage(window)


        C = Canvas(window, height=756, width=1210)
        C.bind("<Button-1>", callback)
        background_image = PhotoImage(file="images/adminemployeechange.png")
        C.create_image(0, 0, image=background_image, anchor="nw")
        window.title("PJ Store")
        C.pack()
        helv36 = tkFont.Font(family='Helvetica', size=15, weight='bold')
        employeeid= StringVar()
        employeeid_entry = Entry(window,textvariable=employeeid,width=30)
        employeeid_entry['font']=helv36
        employeeid_entry.pack()
        employeeid_entry.place(x=218,y=208)

        aadhar= StringVar()
        aadhar_entry = Entry(window,textvariable=aadhar,width=30)
        aadhar_entry['font']=helv36
        aadhar_entry.pack()
        aadhar_entry.place(x=218,y=288)

        firstname= StringVar()
        firstname_entry = Entry(window,textvariable=firstname,width=30)
        firstname_entry['font']=helv36
        firstname_entry.pack()
        firstname_entry.place(x=218,y=368)

        lastname= StringVar()
        lastname_entry = Entry(window,textvariable=lastname,width=30)
        lastname_entry['font']=helv36
        lastname_entry.pack()
        lastname_entry.place(x=218,y=448)

        pan= StringVar()
        pan_entry = Entry(window,textvariable=pan,width=30)
        pan_entry['font']=helv36
        pan_entry.pack()
        pan_entry.place(x=218,y=528)

        dob= StringVar()
        dob_entry = Entry(window,textvariable=dob,width=30)
        dob_entry['font']=helv36
        dob_entry.pack()
        dob_entry.place(x=608,y=208)

        phone= StringVar()
        phone_entry = Entry(window,textvariable=phone,width=30)
        phone_entry['font']=helv36
        phone_entry.pack()
        phone_entry.place(x=608,y=288)

        address= StringVar()
        address_entry = Entry(window,textvariable=address,width=30)
        address_entry['font']=helv36
        address_entry.pack()
        address_entry.place(x=608,y=368)

        salary= StringVar()
        salary_entry = Entry(window,textvariable=salary,width=30)
        salary_entry['font']=helv36
        salary_entry.pack()
        salary_entry.place(x=608,y=448)

        designation= StringVar()
        designation_entry = Entry(window,textvariable=designation,width=30)
        designation_entry['font']=helv36
        designation_entry.pack()
        designation_entry.place(x=608,y=528)
        window.mainloop()

class EmployeeAdminDeletePage:
    def __init__(self, window):

        def delete_employee():
            ins = "DELETE FROM employee WHERE employee_id='{}';".format(employeeid_entry.get())
            database = r"lib.db"
            conn = create_connection(database)

            if conn is not None:
                select(conn,"select * from employee;")
                execute_instruction(conn,ins)
                select(conn,"select * from employee;")
                conn.commit()
            else:
                print("Error! cannot create the database connection.")


        def fetch_employee():
            return

        def callback(event):
            global flag
            print(event.x,event.y)
            if 1016<=event.x<=1125 and 622<=event.y<=670:
                delete_employee()
            elif 520<=event.x<=685 and 622<=event.y<=666:
                fetch_employee()
            elif 55<=event.x<=195 and 625<=event.y<=668:
                employeeid_entry.destroy()
                aadhar_entry.destroy()
                pan_entry.destroy()
                firstname_entry.destroy()
                lastname_entry.destroy()
                designation_entry.destroy()
                salary_entry.destroy()
                phone_entry.destroy()
                address_entry.destroy()
                dob_entry.destroy()
                C.destroy()
                AdminPage(window)


        C = Canvas(window, height=756, width=1210)
        C.bind("<Button-1>", callback)
        background_image = PhotoImage(file="images/adminemployeedelete.png")
        C.create_image(0, 0, image=background_image, anchor="nw")
        window.title("PJ Store")
        C.pack()
        helv36 = tkFont.Font(family='Helvetica', size=15, weight='bold')
        employeeid= StringVar()
        employeeid_entry = Entry(window,textvariable=employeeid,width=30)
        employeeid_entry['font']=helv36
        employeeid_entry.pack()
        employeeid_entry.place(x=218,y=208)

        aadhar= StringVar()
        aadhar_entry = Entry(window,textvariable=aadhar,width=30)
        aadhar_entry['font']=helv36
        aadhar_entry.pack()
        aadhar_entry.place(x=218,y=288)

        firstname= StringVar()
        firstname_entry = Entry(window,textvariable=firstname,width=30)
        firstname_entry['font']=helv36
        firstname_entry.pack()
        firstname_entry.place(x=218,y=368)

        lastname= StringVar()
        lastname_entry = Entry(window,textvariable=lastname,width=30)
        lastname_entry['font']=helv36
        lastname_entry.pack()
        lastname_entry.place(x=218,y=448)

        pan= StringVar()
        pan_entry = Entry(window,textvariable=pan,width=30)
        pan_entry['font']=helv36
        pan_entry.pack()
        pan_entry.place(x=218,y=528)

        dob= StringVar()
        dob_entry = Entry(window,textvariable=dob,width=30)
        dob_entry['font']=helv36
        dob_entry.pack()
        dob_entry.place(x=608,y=208)

        phone= StringVar()
        phone_entry = Entry(window,textvariable=phone,width=30)
        phone_entry['font']=helv36
        phone_entry.pack()
        phone_entry.place(x=608,y=288)

        address= StringVar()
        address_entry = Entry(window,textvariable=address,width=30)
        address_entry['font']=helv36
        address_entry.pack()
        address_entry.place(x=608,y=368)

        salary= StringVar()
        salary_entry = Entry(window,textvariable=salary,width=30)
        salary_entry['font']=helv36
        salary_entry.pack()
        salary_entry.place(x=608,y=448)

        designation= StringVar()
        designation_entry = Entry(window,textvariable=designation,width=30)
        designation_entry['font']=helv36
        designation_entry.pack()
        designation_entry.place(x=608,y=528)
        window.mainloop()

class ProductAdminTypePage:
    def __init__(self, window):


        def callback(event):
            global flag
            print(event.x,event.y)


        C = Canvas(window, height=756, width=1210)
        C.bind("<Button-1>", callback)
        background_image = PhotoImage(file="images/adminproducttype.png")
        C.create_image(0, 0, image=background_image, anchor="nw")
        window.title("PJ Store")
        C.pack()
        helv36 = tkFont.Font(family='Helvetica', size=15, weight='bold')

        types = ['Book','CD']
        option.set(types[0])
        menu = OptionMenu(window, option, *types)
        menu.config(font="Helvetica 15 bold")
        m = window.nametowidget(menu.menuname)
        m.config(font="Helvetica 15 bold")
        menu.pack()
        menu.place(x=138, y=325)

        window.mainloop()

if __name__ == "__main__":
    window = Tk()
    # p1 = PhotoImage(file="images/icon.gif")
    # window.iconphoto(True, p1)
    StartPage(window)
