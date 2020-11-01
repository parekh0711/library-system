from tkinter import *
from tkinter import font as tkFont
from PIL import ImageTk, Image
import sqlite3
from sqlite3 import Error
import pandas as pd

#PASSWORD = aa#1111AA


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

def select_and_print(conn,instruction):
    try:
        c=conn.cursor()
        c.execute(instruction)
        rows=c.fetchall()
        return rows
    except Error as e:
        print(e)

class StartPage:
    def __init__(self, window):
        def callback(event):
            global flag
            if 513<=event.x<=699 and 320<=event.y<=368:
                C.destroy()
                AdminLoginPage(window)
            elif 463<= event.x<=751 and 385 <= event.y<=436:
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
            EmployeePage(window,emp_id)

        def callback(event):
            global flag
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
                EmployeeLoginPage(window)
            elif 425<=event.x<=786 and 567<=event.y<=620:
                C.destroy()
                EmployeeCustomerAddPage(window,emp_id)

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

        def find_barcodes():
            database = r"lib.db"
            conn = create_connection(database)
            ins = "select barcode from product;"
            res = select_and_print(conn,ins)
            ls = []
            for tuple in res:
                ls.append(tuple[0])
            return ls

        def find_customerids():
            database = r"lib.db"
            conn = create_connection(database)
            ins = "select customer_id from customer;"
            res = select_and_print(conn,ins)
            ls = []
            for tuple in res:
                ls.append(tuple[0])
            return ls


        def callback(event):
            global flag
            if 40<=event.x<=210 and 616<=event.y<=664:
                C.destroy()
                menu2.destroy()
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
                ins1 = "SELECT state FROM product WHERE barcode='{}';".format(barcode.get())
                a=select_and_print(conn,ins1)
                conn.commit()
                if a[0][0]=="borrowed" or a[0][0]=="Borrowed":
                    ins2= "SELECT due_date from outstanding where barcode='{}';".format(barcode.get())
                    b=select_and_print(conn,ins2)
                    conn.commit()
                    due=b[0][0]
                    start=startdate_entry.get()
                    if check_date(start,due):
                        ins3="INSERT INTO reservation VALUES ('{}','{}','{}','{}');".format(customerid.get(),barcode.get(),reservedate_entry.get(),startdate_entry.get())
                        execute_instruction(conn,ins3)
                        conn.commit()
                    else:
                        stat="Unavailable"
                else:
                    ins4="INSERT INTO reservation VALUES ('{}','{}','{}','{}');".format(customerid.get(),barcode.get(),reservedate_entry.get(),startdate_entry.get())
                    ins5="UPDATE product SET state='reserved' where barcode='{}';".format(barcode.get())
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

        # customerid= StringVar()
        # customerid_entry = Entry(window,textvariable=customerid,width=15)
        # customerid_entry['font']=helv36
        # customerid_entry.pack()
        # customerid_entry.place(x=662,y=264)


        types = find_customerids()
        customerid = StringVar(window)
        customerid.set(types[0])
        menu = OptionMenu(window, customerid, *types)
        menu.config(font="Helvetica 15 bold")
        m = window.nametowidget(menu.menuname)
        m.config(font="Helvetica 15 bold")
        menu.pack()
        menu.place(x=662, y=264)

        types2 = find_barcodes()
        barcode = StringVar(window)
        barcode.set(types2[0])
        menu2 = OptionMenu(window, barcode, *types2)
        menu2.config(font="Helvetica 15 bold")
        m2 = window.nametowidget(menu2.menuname)
        m2.config(font="Helvetica 15 bold")
        menu2.pack()
        menu2.place(x=728, y=436)
        #hee

        login_button = Button(window,text="OK",command = reserve_item,width=10)
        login_button['font']=helv36
        login_button.pack()
        login_button.place(x=572,y=625)

        window.mainloop()

class EmployeeBillingPage:
    def __init__(self, window,emp_id):

        def callback(event):
            global flag
            if 40<=event.x<=210 and 616<=event.y<=664:
                C.destroy()
                EmployeePage(window,emp_id)
            elif 577<=event.x<=670 and 622<=event.y<=675:
                billing_item()
                print("Done")

        def find_barcodes():
            database = r"lib.db"
            conn = create_connection(database)
            ins = "select barcode from product;"
            res = select_and_print(conn,ins)
            ls = []
            for tuple in res:
                ls.append(tuple[0])
            return ls

        def find_customerids():
            database = r"lib.db"
            conn = create_connection(database)
            ins = "select customer_id from customer;"
            res = select_and_print(conn,ins)
            ls = []
            for tuple in res:
                ls.append(tuple[0])
            return ls

        def billing_item():
            database = r"lib.db"
            conn = create_connection(database)
            if conn is not None:
                ins1 = "SELECT date('{}','+007 days');".format(borroweddate_entry.get())
                a=select_and_print(conn,ins1)
                conn.commit()
                res=a[0][0]
                ins2 = "SELECT renewed FROM CUSTOMER WHERE customer_id='{}';".format(customerid.get())
                a=select_and_print(conn,ins2)
                conn.commit()
                if a[0][0]=="renewed":
                    amt=0
                    penalty=0
                else:
                    amt=100
                    penalty=0
                status='Not returned'
                ins3 = "INSERT INTO outstanding VALUES('{}','{}','{}','{}','{}','{}','{}','{}');".format(customerid.get(),employeeid_entry.get(),barcode.get(),amt,penalty,status,res,borroweddate_entry.get())
                ins4 = "UPDATE product SET state='Borrowed' WHERE barcode='{}';".format(barcode.get())
                ins5 = "INSERT INTO borrowed VALUES('{}','{}');".format(barcode.get(),customerid.get())
                execute_instruction(conn,ins3)
                execute_instruction(conn,ins4)
                execute_instruction(conn,ins5)
                conn.commit()
            else:
                print("Error! cannot create the database connection.")

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

        types = find_customerids()
        customerid = StringVar(window)
        customerid.set(types[0])
        menu = OptionMenu(window, customerid, *types)
        menu.config(font="Helvetica 15 bold")
        m = window.nametowidget(menu.menuname)
        m.config(font="Helvetica 15 bold")
        menu.pack()
        menu.place(x=413, y=417)

        # customerid= StringVar()
        # customerid_entry = Entry(window,textvariable=customerid,width=15)
        # customerid_entry['font']=helv36
        # customerid_entry.pack()
        # customerid_entry.place(x=413,y=417)

        types2 = find_barcodes()
        barcode = StringVar(window)
        barcode.set(types2[0])
        menu2 = OptionMenu(window, barcode, *types2)
        menu2.config(font="Helvetica 15 bold")
        m2 = window.nametowidget(menu2.menuname)
        m2.config(font="Helvetica 15 bold")
        menu2.pack()
        menu2.place(x=719, y=207)

        # barcode= StringVar()
        # barcode_entry = Entry(window,textvariable=barcode,width=15)
        # barcode_entry['font']=helv36
        # barcode_entry.pack()
        # barcode_entry.place(x=719,y=207)

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
                a=select_and_print(conn,ins)#returns the state as list of tuples which will have only one value
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
            ins1 = "SELECT renewed FROM CUSTOMER WHERE customer_id='{}';".format(customerid.get())
            ins2 = "SELECT (amount+penalty) AS payment FROM outstanding where customer_id='{}' and employee_id='{}' and barcode='{}';".format(customerid.get(),employeeid_entry.get(),barcode.get())
            ins3 = "UPDATE outstanding SET status='returned' where barcode='{}';".format(barcode.get())
            ins4 = "UPDATE product SET state='in_stock' where barcode='{}';".format(barcode.get())
            ins5 = "DELETE FROM borrowed WHERE barcode='{}';".format(barcode.get())
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

        def find_barcodes():
            database = r"lib.db"
            conn = create_connection(database)
            ins = "select barcode from product;"
            res = select_and_print(conn,ins)
            ls = []
            for tuple in res:
                ls.append(tuple[0])
            return ls

        def find_customerids():
            database = r"lib.db"
            conn = create_connection(database)
            ins = "select customer_id from outstanding;"
            res = select_and_print(conn,ins)
            ls = []
            for tuple in res:
                ls.append(tuple[0])
            return list(set(ls))

        def callback(event):
            global flag
            if 40<=event.x<=210 and 616<=event.y<=664:
                C.destroy()
                EmployeePage(window,emp_id)
            elif 577<=event.x<=671 and 624<=event.y<=675:
                return_item()
                print("Done")


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

        types = find_customerids()
        customerid = StringVar(window)
        customerid.set(types[0])
        menu = OptionMenu(window, customerid, *types)
        menu.config(font="Helvetica 15 bold")
        m = window.nametowidget(menu.menuname)
        m.config(font="Helvetica 15 bold")
        menu.pack()
        menu.place(x=505, y=366)

        # customerid= StringVar()
        # customerid_entry = Entry(window,textvariable=customerid,width=30)
        # customerid_entry['font']=helv36
        # customerid_entry.pack()
        # customerid_entry.place(x=505,y=366)

        # barcode= StringVar()
        # barcode_entry = Entry(window,textvariable=barcode,width=30)
        # barcode_entry['font']=helv36
        # barcode_entry.pack()
        # barcode_entry.place(x=505,y=484)

        types2 = find_barcodes()
        barcode = StringVar(window)
        barcode.set(types2[0])
        menu2 = OptionMenu(window, barcode, *types2)
        menu2.config(font="Helvetica 15 bold")
        m2 = window.nametowidget(menu2.menuname)
        m2.config(font="Helvetica 15 bold")
        menu2.pack()
        menu2.place(x=505, y=484)

        window.mainloop()

class EmployeeCustomerAddPage:

    def __init__(self, window,emp_id):

        def add_customer():
            ins = "INSERT INTO customer VALUES('{}','{}','{}','{}','{}','{}','{}');".format(customerid_entry.get(),firstname_entry.get(),lastname_entry.get(),dob_entry.get(),phone_entry.get(),address_entry.get(),"Renewed")
            database = r"lib.db"
            conn = create_connection(database)

            if conn is not None:
                execute_instruction(conn,ins)
                print(pd.read_sql_query("SELECT * FROM customer", conn))
                conn.commit()
            else:
                print("Error! cannot create the database connection.")

        def callback(event):
            global flag
            if 40<=event.x<=210 and 616<=event.y<=664:
                C.destroy()
                EmployeePage(window,emp_id)
            elif 565<=event.x<=671 and 619<=event.y<=679:
                add_customer()
                print("Added")


        C = Canvas(window, height=756, width=1210)
        C.bind("<Button-1>", callback)
        background_image = PhotoImage(file="images/employeecustomeradd.png")
        C.create_image(0, 0, image=background_image, anchor="nw")
        window.title("PJ Store")
        C.pack()

        helv36 = tkFont.Font(family='Helvetica', size=15, weight='bold')

        customerid= StringVar()
        customerid_entry = Entry(window,textvariable=customerid,width=15)
        customerid_entry['font']=helv36
        customerid_entry.pack()
        customerid_entry.place(x=413,y=230)

        firstname= StringVar()
        firstname_entry = Entry(window,textvariable=firstname,width=15)
        firstname_entry['font']=helv36
        firstname_entry.pack()
        firstname_entry.place(x=413,y=368)

        lastname= StringVar()
        lastname_entry = Entry(window,textvariable=lastname,width=15)
        lastname_entry['font']=helv36
        lastname_entry.pack()
        lastname_entry.place(x=413,y=492)

        dob= StringVar()
        dob_entry = Entry(window,textvariable=dob,width=25)
        dob_entry['font']=helv36
        dob_entry.pack()
        dob_entry.place(x=659,y=230)

        phone= StringVar()
        phone_entry = Entry(window,textvariable=phone,width=25)
        phone_entry['font']=helv36
        phone_entry.pack()
        phone_entry.place(x=659,y=368)

        address= StringVar()
        address_entry = Entry(window,textvariable=address,width=25)
        address_entry['font']=helv36
        address_entry.pack()
        address_entry.place(x=659,y=492)

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
                C.destroy()
                ProductAdminTypePage(window,1) #add
            elif 835<=event.x<=1142 and 330<=event.y<=378:
                C.destroy()
                ProductAdminTypePage(window,2) #change
            elif 835<=event.x<=1139 and 460<=event.y<=497:
                C.destroy()
                ProductAdminTypePage(window,3) #delete
            elif 876<=event.x<=1088 and 558<=event.y<=594:
                C.destroy()
                AuthorAdminAddPage(window) #addauthor
            elif 551<=event.x<=760 and 225<=event.y<=274:
                C.destroy()
                PolicyAdminAddPage(window)
            elif 513<=event.x<=785 and 329<=event.y<=378:
                C.destroy()
                PolicyAdminChangePage(window)
            elif 511<=event.x<=799 and 450<=event.y<=499:
                C.destroy()
                PolicyAdminDeletePage(window)
            elif 536<=event.x<=770 and 558<=event.y<=595:
                C.destroy()
                ProfitAdminCheckPage(window)
            elif 76<=event.x<=219 and 613<=event.y<=661:
                C.destroy()
                AdminLoginPage(window)


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
            desig = designation.get().split(",")[0]
            ins = "INSERT INTO employee VALUES({},{},'{}','{}','{}','{}','{}','{}','{}');".format(employeeid_entry.get(),aadhar_entry.get(),pan_entry.get(),firstname_entry.get(),lastname_entry.get(),dob_entry.get(),phone_entry.get(),address_entry.get(),desig)
            database = r"lib.db"
            conn = create_connection(database)

            if conn is not None:
                execute_instruction(conn,ins)
                print(pd.read_sql_query("SELECT * FROM employee", conn))
                conn.commit()
            else:
                print("Error! cannot create the database connection.")

        def callback(event):
            global flag
            if 1016<=event.x<=1125 and 622<=event.y<=670:
                add_employee()
            elif 55<=event.x<=195 and 625<=event.y<=668:
                employeeid_entry.destroy()
                aadhar_entry.destroy()
                pan_entry.destroy()
                firstname_entry.destroy()
                lastname_entry.destroy()
                menu2.destroy()
                # salary_entry.destroy()
                phone_entry.destroy()
                address_entry.destroy()
                dob_entry.destroy()
                C.destroy()
                AdminPage(window)

        def find_desigs():
            database = r"lib.db"
            conn = create_connection(database)
            ins = "select * from salary;"
            res = select_and_print(conn,ins)
            ls = []
            for tuple in res:
                ls.append(tuple[0]+","+str(tuple[1]))
            return ls


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

        firstname= StringVar()
        firstname_entry = Entry(window,textvariable=firstname,width=30)
        firstname_entry['font']=helv36
        firstname_entry.pack()
        firstname_entry.place(x=218,y=288)

        lastname= StringVar()
        lastname_entry = Entry(window,textvariable=lastname,width=30)
        lastname_entry['font']=helv36
        lastname_entry.pack()
        lastname_entry.place(x=218,y=368)

        dob= StringVar()
        dob_entry = Entry(window,textvariable=dob,width=30)
        dob_entry['font']=helv36
        dob_entry.pack()
        dob_entry.place(x=218,y=448)

        phone= StringVar()
        phone_entry = Entry(window,textvariable=phone,width=30)
        phone_entry['font']=helv36
        phone_entry.pack()
        phone_entry.place(x=218,y=528)

        aadhar= StringVar()
        aadhar_entry = Entry(window,textvariable=aadhar,width=30)
        aadhar_entry['font']=helv36
        aadhar_entry.pack()
        aadhar_entry.place(x=608,y=208)

        pan= StringVar()
        pan_entry = Entry(window,textvariable=pan,width=30)
        pan_entry['font']=helv36
        pan_entry.pack()
        pan_entry.place(x=608,y=288)

        # designation= StringVar()
        # designation_entry = Entry(window,textvariable=designation,width=30)
        # designation_entry['font']=helv36
        # designation_entry.pack()
        # designation_entry.place(x=608,y=368)

        types2 = find_desigs()
        designation = StringVar(window)
        designation.set(types2[0])
        menu2 = OptionMenu(window, designation, *types2)
        menu2.config(font="Helvetica 15 bold")
        m2 = window.nametowidget(menu2.menuname)
        m2.config(font="Helvetica 15 bold")
        menu2.pack()
        menu2.place(x=608, y=408)

        # salary= StringVar()
        # salary_entry = Entry(window,textvariable=salary,width=30)
        # salary_entry['font']=helv36
        # salary_entry.pack()
        # salary_entry.place(x=608,y=448)

        address= StringVar()
        address_entry = Entry(window,textvariable=address,width=30)
        address_entry['font']=helv36
        address_entry.pack()
        address_entry.place(x=608,y=528)
        window.mainloop()

class EmployeeAdminChangePage:
    def __init__(self, window):

        def change_employee():
            desig = designation.get().split(",")[0]
            ins0="DELETE FROM employee WHERE employee_id='{}';".format(employeeid.get())
            ins = "INSERT INTO employee VALUES({},{},'{}','{}','{}','{}','{}','{}','{}');".format(employeeid.get(),aadhar_entry.get(),pan_entry.get(),firstname_entry.get(),lastname_entry.get(),dob_entry.get(),phone_entry.get(),address_entry.get(),desig)
            database = r"lib.db"
            conn = create_connection(database)

            if conn is not None:
                execute_instruction(conn,ins0)
                conn.commit()
                execute_instruction(conn,ins)
                conn.commit()
                print(pd.read_sql_query("SELECT * FROM employee", conn))
            else:
                print("Error! cannot create the database connection.")

        def find_desigs():
            database = r"lib.db"
            conn = create_connection(database)
            ins = "select * from salary;"
            res = select_and_print(conn,ins)
            ls = []
            for tuple in res:
                ls.append(tuple[0]+","+str(tuple[1]))
            return ls

        def fetch_employee():
            ins0 = "SELECT * FROM employee WHERE employee_id='{}';".format(employeeid.get())

            database = r"lib.db"
            conn = create_connection(database)

            if conn is not None:
                a=select_and_print(conn,ins0)
                # b= select_and_print(conn,ins)
                conn.commit()
                # salary.set(b[0][0])
                aadhar.set(a[0][1])
                pan.set(a[0][2])
                firstname.set(a[0][3])
                lastname.set(a[0][4])
                dob.set(a[0][5])
                phone.set(a[0][6])
                address.set(a[0][7])
                for index,tuple in enumerate(types):
                    if a[0][8] in tuple:
                        designation.set(types[index])
            else:
                print("Error! cannot create the database connection.")

        def find_empids():
            database = r"lib.db"
            conn = create_connection(database)
            ins = "select employee_id from employee;"
            res = select_and_print(conn,ins)
            ls = []
            for tuple in res:
                ls.append(tuple[0])
            return ls

        def callback(event):
            global flag
            if 916<=event.x<=1125 and 622<=event.y<=666:
                change_employee()
            elif 520<=event.x<=685 and 622<=event.y<=666:
                fetch_employee()
            elif 55<=event.x<=195 and 625<=event.y<=668:
                menu2.destroy()
                aadhar_entry.destroy()
                pan_entry.destroy()
                firstname_entry.destroy()
                lastname_entry.destroy()
                menu.destroy()
                # salary_entry.destroy()
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

        types2 = find_empids()
        employeeid = StringVar(window)
        employeeid.set(types2[0])
        menu2 = OptionMenu(window, employeeid, *types2)
        menu2.config(font="Helvetica 15 bold")
        m2 = window.nametowidget(menu2.menuname)
        m2.config(font="Helvetica 15 bold")
        menu2.pack()
        menu2.place(x=218, y=208)

        # employeeid= StringVar()
        # employeeid_entry = Entry(window,textvariable=employeeid,width=30)
        # employeeid_entry['font']=helv36
        # employeeid_entry.pack()
        # employeeid_entry.place(x=218,y=208)

        firstname= StringVar()
        firstname_entry = Entry(window,textvariable=firstname,width=30)
        firstname_entry['font']=helv36
        firstname_entry.pack()
        firstname_entry.place(x=218,y=288)

        lastname= StringVar()
        lastname_entry = Entry(window,textvariable=lastname,width=30)
        lastname_entry['font']=helv36
        lastname_entry.pack()
        lastname_entry.place(x=218,y=368)

        dob= StringVar()
        dob_entry = Entry(window,textvariable=dob,width=30)
        dob_entry['font']=helv36
        dob_entry.pack()
        dob_entry.place(x=218,y=448)

        phone= StringVar()
        phone_entry = Entry(window,textvariable=phone,width=30)
        phone_entry['font']=helv36
        phone_entry.pack()
        phone_entry.place(x=218,y=528)

        aadhar= StringVar()
        aadhar_entry = Entry(window,textvariable=aadhar,width=30)
        aadhar_entry['font']=helv36
        aadhar_entry.pack()
        aadhar_entry.place(x=608,y=208)

        pan= StringVar()
        pan_entry = Entry(window,textvariable=pan,width=30)
        pan_entry['font']=helv36
        pan_entry.pack()
        pan_entry.place(x=608,y=288)

        types = find_desigs()
        designation = StringVar(window)
        designation.set(types[0])
        menu = OptionMenu(window, designation, *types)
        menu.config(font="Helvetica 15 bold")
        m = window.nametowidget(menu.menuname)
        m.config(font="Helvetica 15 bold")
        menu.pack()
        menu.place(x=608, y=408)

        address= StringVar()
        address_entry = Entry(window,textvariable=address,width=30)
        address_entry['font']=helv36
        address_entry.pack()
        address_entry.place(x=608,y=528)
        window.mainloop()

class EmployeeAdminDeletePage:
    def __init__(self, window):

        def delete_employee():
            ins = "DELETE FROM employee WHERE employee_id='{}';".format(employeeid.get())
            database = r"lib.db"
            conn = create_connection(database)

            if conn is not None:
                execute_instruction(conn,ins)
                print(pd.read_sql_query("SELECT * FROM employee", conn))
                conn.commit()
            else:
                print("Error! cannot create the database connection.")

        def find_desigs():
            database = r"lib.db"
            conn = create_connection(database)
            ins = "select * from salary;"
            res = select_and_print(conn,ins)
            ls = []
            for tuple in res:
                ls.append(tuple[0]+","+str(tuple[1]))
            return ls

        def fetch_employee():
            ins0 = "SELECT * FROM employee WHERE employee_id='{}';".format(employeeid.get())

            database = r"lib.db"
            conn = create_connection(database)

            if conn is not None:
                a=select_and_print(conn,ins0)
                conn.commit()
                aadhar.set(a[0][1])
                pan.set(a[0][2])
                firstname.set(a[0][3])
                lastname.set(a[0][4])
                dob.set(a[0][5])
                phone.set(a[0][6])
                address.set(a[0][7])
                for index,tuple in enumerate(types):
                    if a[0][8] in tuple:
                        designation.set(types[index])
            else:
                print("Error! cannot create the database connection.")

        def find_empids():
            database = r"lib.db"
            conn = create_connection(database)
            ins = "select employee_id from employee;"
            res = select_and_print(conn,ins)
            ls = []
            for tuple in res:
                ls.append(tuple[0])
            return ls

        def callback(event):
            global flag
            if 916<=event.x<=1125 and 622<=event.y<=666:
                try:
                    delete_employee()
                    print("Deleted")
                except:
                    print("Already Deleted.")
            elif 520<=event.x<=685 and 622<=event.y<=666:
                try:
                    fetch_employee()
                except:
                    print("Deleted.")
            elif 55<=event.x<=195 and 625<=event.y<=668:
                menu2.destroy()
                aadhar_entry.destroy()
                pan_entry.destroy()
                firstname_entry.destroy()
                lastname_entry.destroy()
                menu.destroy()
                # salary_entry.destroy()
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

        types2 = find_empids()
        employeeid = StringVar(window)
        employeeid.set(types2[0])
        menu2 = OptionMenu(window, employeeid, *types2)
        menu2.config(font="Helvetica 15 bold")
        m2 = window.nametowidget(menu2.menuname)
        m2.config(font="Helvetica 15 bold")
        menu2.pack()
        menu2.place(x=218, y=208)

        firstname= StringVar()
        firstname_entry = Entry(window,textvariable=firstname,width=30)
        firstname_entry['font']=helv36
        firstname_entry.pack()
        firstname_entry.place(x=218,y=288)

        lastname= StringVar()
        lastname_entry = Entry(window,textvariable=lastname,width=30)
        lastname_entry['font']=helv36
        lastname_entry.pack()
        lastname_entry.place(x=218,y=368)

        dob= StringVar()
        dob_entry = Entry(window,textvariable=dob,width=30)
        dob_entry['font']=helv36
        dob_entry.pack()
        dob_entry.place(x=218,y=448)

        phone= StringVar()
        phone_entry = Entry(window,textvariable=phone,width=30)
        phone_entry['font']=helv36
        phone_entry.pack()
        phone_entry.place(x=218,y=528)

        aadhar= StringVar()
        aadhar_entry = Entry(window,textvariable=aadhar,width=30)
        aadhar_entry['font']=helv36
        aadhar_entry.pack()
        aadhar_entry.place(x=608,y=208)

        pan= StringVar()
        pan_entry = Entry(window,textvariable=pan,width=30)
        pan_entry['font']=helv36
        pan_entry.pack()
        pan_entry.place(x=608,y=288)

        types = find_desigs()
        designation = StringVar(window)
        designation.set(types[0])
        menu = OptionMenu(window, designation, *types)
        menu.config(font="Helvetica 15 bold")
        m = window.nametowidget(menu.menuname)
        m.config(font="Helvetica 15 bold")
        menu.pack()
        menu.place(x=608, y=408)

        address= StringVar()
        address_entry = Entry(window,textvariable=address,width=30)
        address_entry['font']=helv36
        address_entry.pack()
        address_entry.place(x=608,y=528)
        window.mainloop()

class ProductAdminTypePage:
    def __init__(self, window,mode):


        def callback(event):
            global flag
            if 567<=event.x<=652 and 555<=event.y<=602:
                menu.destroy()
                C.destroy()
                tp = option.get()
                if tp == "Book":
                    if mode == 1:
                        ProductAdminAddPage(window,1)
                    elif mode == 2:
                        ProductAdminChangePage(window,1)
                    elif mode == 3:
                        ProductAdminDeletePage(window,1)
                elif tp=="CD":
                    if mode == 1:
                        CDAdminAddPage(window,2)
                    elif mode == 2:
                        CDAdminChangePage(window,2)
                    elif mode == 3:
                        CDAdminDeletePage(window,2)
            elif 52<=event.x<=194 and 621<=event.y<=668:
                C.destroy()
                menu.destroy()
                AdminPage(window)

        C = Canvas(window, height=756, width=1210)
        C.bind("<Button-1>", callback)
        background_image = PhotoImage(file="images/adminproducttype.png")
        C.create_image(0, 0, image=background_image, anchor="nw")
        window.title("PJ Store")
        C.pack()
        helv36 = tkFont.Font(family='Helvetica', size=15, weight='bold')

        types = ['Book','CD']
        option = StringVar(window)
        option.set(types[0])
        menu = OptionMenu(window, option, *types)
        menu.config(font="Helvetica 25 bold")
        m = window.nametowidget(menu.menuname)
        m.config(font="Helvetica 25 bold")
        menu.pack()
        menu.place(x=515, y=363)

        window.mainloop()

class ProductAdminAddPage:
    def __init__(self, window,mode):


        def add_product_book():
            ins0 = "INSERT INTO product VALUES({},'Book','In_stock');".format(barcode_entry.get())
            ins="INSERT INTO book VALUES('{}','{}','{}','{}','{}','{}','{}','{}');".format(barcode_entry.get(),authorid.get(),title_entry.get(),year_entry.get(),publisher_entry.get(),genre_entry.get(),ordercost_entry.get(),condition_entry.get())
            database = r"lib.db"
            conn = create_connection(database)

            if conn is not None:
                execute_instruction(conn,ins)
                execute_instruction(conn,ins0)
                conn.commit()
                print(pd.read_sql_query("SELECT * FROM book", conn))
                print("Added")

            else:
                print("Error! cannot create the database connection.")

        def callback(event):
            global flag
            if 52<=event.x<=194 and 621<=event.y<=668:
                C.destroy()
                barcode_entry.destroy()
                menu.destroy()
                title_entry.destroy()
                condition_entry.destroy()
                publisher_entry.destroy()
                genre_entry.destroy()
                year_entry.destroy()
                ordercost_entry.destroy()
                AdminPage(window)
            elif 563<=event.x<=648 and 614<=event.y<=664:
                add_product_book()

        def find_authors():
            database = r"lib.db"
            conn = create_connection(database)
            ins = "select author_id from author;"
            res = select_and_print(conn,ins)
            ls = []
            for tuple in res:
                ls.append(tuple[0])
            return ls


        C = Canvas(window, height=756, width=1210)
        C.bind("<Button-1>", callback)
        background_image = PhotoImage(file="images/adminproductadd.png")
        C.create_image(0, 0, image=background_image, anchor="nw")
        window.title("PJ Store")
        C.pack()
        helv36 = tkFont.Font(family='Helvetica', size=15, weight='bold')


        barcode= StringVar()
        barcode_entry = Entry(window,textvariable=barcode,width=25)
        barcode_entry['font']=helv36
        barcode_entry.pack()
        barcode_entry.place(x=345,y=236)


        types = find_authors()
        authorid = StringVar(window)
        authorid.set(types[0])
        menu = OptionMenu(window, authorid, *types)
        menu.config(font="Helvetica 15 bold")
        m = window.nametowidget(menu.menuname)
        m.config(font="Helvetica 15 bold")
        menu.pack()
        menu.place(x=345, y=339)

        title= StringVar()
        title_entry = Entry(window,textvariable=title,width=25)
        title_entry['font']=helv36
        title_entry.pack()
        title_entry.place(x=345,y=436)

        condition= StringVar()
        condition_entry = Entry(window,textvariable=condition,width=25)
        condition_entry['font']=helv36
        condition_entry.pack()
        condition_entry.place(x=345,y=550)

        publisher= StringVar()
        publisher_entry = Entry(window,textvariable=publisher,width=15)
        publisher_entry['font']=helv36
        publisher_entry.pack()
        publisher_entry.place(x=674,y=236)

        genre= StringVar()
        genre_entry = Entry(window,textvariable=genre,width=15)
        genre_entry['font']=helv36
        genre_entry.pack()
        genre_entry.place(x=674,y=339)

        year= StringVar()
        year_entry = Entry(window,textvariable=year,width=15)
        year_entry['font']=helv36
        year_entry.pack()
        year_entry.place(x=674,y=436)

        ordercost= StringVar()
        ordercost_entry = Entry(window,textvariable=ordercost,width=15)
        ordercost_entry['font']=helv36
        ordercost_entry.pack()
        ordercost_entry.place(x=674,y=550)


        window.mainloop()

class ProductAdminChangePage:
    def __init__(self, window, mode):

        def find_authors():
            database = r"lib.db"
            conn = create_connection(database)
            ins = "select author_id from author;"
            res = select_and_print(conn,ins)
            ls = []
            for tuple in res:
                ls.append(tuple[0])
            return ls

        def find_barcodes():
            database = r"lib.db"
            conn = create_connection(database)
            ins = "select barcode from book;"
            res = select_and_print(conn,ins)
            ls = []
            for tuple in res:
                ls.append(tuple[0])
            return ls

        def change_product_book():
            print("hi")
            ins0 = "DELETE FROM book WHERE barcode='{}';".format(barcode.get())
            ins="INSERT INTO book VALUES('{}','{}','{}','{}','{}','{}','{}','{}');".format(barcode.get(),authorid.get(),title_entry.get(),year_entry.get(),publisher_entry.get(),genre_entry.get(),ordercost_entry.get(),condition_entry.get())
            database = r"lib.db"
            conn = create_connection(database)

            if conn is not None:
                execute_instruction(conn,ins0)
                execute_instruction(conn,ins)
                conn.commit()
                print(pd.read_sql_query("SELECT * FROM book", conn))
                print("done")
            else:
                print("Error! cannot create the database connection.")

        def fetch_book():
            ins0 = "SELECT * FROM book WHERE barcode='{}';".format(barcode.get())
            print(barcode.get())
            database = r"lib.db"
            conn = create_connection(database)

            if conn is not None:
                a=select_and_print(conn,ins0)
                # print(a)
                conn.commit()
                authorid.set(a[0][1])
                title.set(a[0][2])
                year.set(a[0][3])
                publisher.set(a[0][4])
                genre.set(a[0][5])
                ordercost.set(a[0][6])
                condition.set(a[0][7])
            else:
                print("Error! cannot create the database connection.")

        def callback(event):
            global flag
            if 52<=event.x<=194 and 621<=event.y<=668:
                C.destroy()
                menu2.destroy()
                menu.destroy()
                title_entry.destroy()
                condition_entry.destroy()
                publisher_entry.destroy()
                genre_entry.destroy()
                year_entry.destroy()
                ordercost_entry.destroy()
                AdminPage(window)
            elif 563<=event.x<=648 and 614<=event.y<=664:
                change_product_book()
            elif 908<=event.x<=1077 and 617<=event.y<=667:
                fetch_book()



        C = Canvas(window, height=756, width=1210)
        C.bind("<Button-1>", callback)
        background_image = PhotoImage(file="images/adminproductchange.png")
        C.create_image(0, 0, image=background_image, anchor="nw")
        window.title("PJ Store")
        C.pack()
        helv36 = tkFont.Font(family='Helvetica', size=15, weight='bold')

        types = find_authors()
        authorid = StringVar(window)
        authorid.set(types[0])
        menu = OptionMenu(window, authorid, *types)
        menu.config(font="Helvetica 15 bold")
        m = window.nametowidget(menu.menuname)
        m.config(font="Helvetica 15 bold")
        menu.pack()
        menu.place(x=345, y=339)


        types2 = find_barcodes()
        barcode = StringVar(window)
        barcode.set(types2[0])
        menu2 = OptionMenu(window, barcode, *types2)
        menu2.config(font="Helvetica 15 bold")
        m2 = window.nametowidget(menu2.menuname)
        m2.config(font="Helvetica 15 bold")
        menu2.pack()
        menu2.place(x=345, y=236)

        title= StringVar()
        title_entry = Entry(window,textvariable=title,width=25)
        title_entry['font']=helv36
        title_entry.pack()
        title_entry.place(x=345,y=436)

        condition= StringVar()
        condition_entry = Entry(window,textvariable=condition,width=25)
        condition_entry['font']=helv36
        condition_entry.pack()
        condition_entry.place(x=345,y=550)

        publisher= StringVar()
        publisher_entry = Entry(window,textvariable=publisher,width=15)
        publisher_entry['font']=helv36
        publisher_entry.pack()
        publisher_entry.place(x=674,y=236)

        genre= StringVar()
        genre_entry = Entry(window,textvariable=genre,width=15)
        genre_entry['font']=helv36
        genre_entry.pack()
        genre_entry.place(x=674,y=339)

        year= StringVar()
        year_entry = Entry(window,textvariable=year,width=15)
        year_entry['font']=helv36
        year_entry.pack()
        year_entry.place(x=674,y=436)

        ordercost= StringVar()
        ordercost_entry = Entry(window,textvariable=ordercost,width=15)
        ordercost_entry['font']=helv36
        ordercost_entry.pack()
        ordercost_entry.place(x=674,y=550)

        window.mainloop()

class ProductAdminDeletePage:
    def __init__(self, window, mode):

        def find_authors():
            database = r"lib.db"
            conn = create_connection(database)
            ins = "select author_id from author;"
            res = select_and_print(conn,ins)
            ls = []
            for tuple in res:
                ls.append(tuple[0])
            return ls

        def find_barcodes():
            database = r"lib.db"
            conn = create_connection(database)
            ins = "select barcode from book;"
            res = select_and_print(conn,ins)
            ls = []
            for tuple in res:
                ls.append(tuple[0])
            return ls

        def delete_product_book():
            ins = "DELETE FROM book WHERE barcode='{}';".format(barcode.get())
            ins0 = "DELETE FROM product WHERE barcode='{}';".format(barcode.get())
            database = r"lib.db"
            conn = create_connection(database)

            if conn is not None:
                execute_instruction(conn,ins)
                execute_instruction(conn,ins0)
                conn.commit()
                print("Deleted")
            else:
                print("Error! cannot create the database connection.")

        def fetch_book():
            ins0 = "SELECT * FROM book WHERE barcode='{}';".format(barcode.get())
            print(barcode.get())
            database = r"lib.db"
            conn = create_connection(database)

            if conn is not None:
                a=select_and_print(conn,ins0)
                # print(a)
                conn.commit()
                authorid.set(a[0][1])
                title.set(a[0][2])
                year.set(a[0][3])
                publisher.set(a[0][4])
                genre.set(a[0][5])
                ordercost.set(a[0][6])
                condition.set(a[0][7])
            else:
                print("Error! cannot create the database connection.")

        def callback(event):
            global flag
            if 52<=event.x<=194 and 621<=event.y<=668:
                C.destroy()
                menu2.destroy()
                menu.destroy()
                title_entry.destroy()
                condition_entry.destroy()
                publisher_entry.destroy()
                genre_entry.destroy()
                year_entry.destroy()
                ordercost_entry.destroy()
                AdminPage(window)
            elif 563<=event.x<=648 and 614<=event.y<=664:
                try:
                    delete_product_book()
                except:
                    print("Book already deleted.")
            elif 908<=event.x<=1077 and 617<=event.y<=667:
                fetch_book()



        C = Canvas(window, height=756, width=1210)
        C.bind("<Button-1>", callback)
        background_image = PhotoImage(file="images/adminproductchange.png")
        C.create_image(0, 0, image=background_image, anchor="nw")
        window.title("PJ Store")
        C.pack()
        helv36 = tkFont.Font(family='Helvetica', size=15, weight='bold')

        types = find_authors()
        authorid = StringVar(window)
        authorid.set(types[0])
        menu = OptionMenu(window, authorid, *types)
        menu.config(font="Helvetica 15 bold")
        m = window.nametowidget(menu.menuname)
        m.config(font="Helvetica 15 bold")
        menu.pack()
        menu.place(x=345, y=339)


        types2 = find_barcodes()
        barcode = StringVar(window)
        barcode.set(types2[0])
        menu2 = OptionMenu(window, barcode, *types2)
        menu2.config(font="Helvetica 15 bold")
        m2 = window.nametowidget(menu.menuname)
        m2.config(font="Helvetica 15 bold")
        menu2.pack()
        menu2.place(x=345, y=236)

        title= StringVar()
        title_entry = Entry(window,textvariable=title,width=25)
        title_entry['font']=helv36
        title_entry.pack()
        title_entry.place(x=345,y=436)

        condition= StringVar()
        condition_entry = Entry(window,textvariable=condition,width=25)
        condition_entry['font']=helv36
        condition_entry.pack()
        condition_entry.place(x=345,y=550)

        publisher= StringVar()
        publisher_entry = Entry(window,textvariable=publisher,width=15)
        publisher_entry['font']=helv36
        publisher_entry.pack()
        publisher_entry.place(x=674,y=236)

        genre= StringVar()
        genre_entry = Entry(window,textvariable=genre,width=15)
        genre_entry['font']=helv36
        genre_entry.pack()
        genre_entry.place(x=674,y=339)

        year= StringVar()
        year_entry = Entry(window,textvariable=year,width=15)
        year_entry['font']=helv36
        year_entry.pack()
        year_entry.place(x=674,y=436)

        ordercost= StringVar()
        ordercost_entry = Entry(window,textvariable=ordercost,width=15)
        ordercost_entry['font']=helv36
        ordercost_entry.pack()
        ordercost_entry.place(x=674,y=550)

        window.mainloop()

class CDAdminAddPage:
    def __init__(self, window,mode):


        def add_product_media():
            ins0 = "INSERT INTO product VALUES({},'CD','In_stock');".format(barcode_entry.get())
            ins="INSERT INTO media VALUES('{}','{}','{}','{}','{}','{}','{}','{}');".format(barcode_entry.get(),title_entry.get(),year_entry.get(),runtime_entry.get(),category_entry.get(),ordercost_entry.get(),condition_entry.get(),genre_entry.get())
            database = r"lib.db"
            conn = create_connection(database)

            if conn is not None:
                execute_instruction(conn,ins)
                execute_instruction(conn,ins0)
                conn.commit()
                print(pd.read_sql_query("SELECT * FROM media", conn))
                print("Added.")
            else:
                print("Error! cannot create the database connection.")

        def callback(event):
            global flag
            if 52<=event.x<=194 and 621<=event.y<=668:
                C.destroy()
                barcode_entry.destroy()
                runtime_entry.destroy()
                title_entry.destroy()
                condition_entry.destroy()
                category_entry.destroy()
                genre_entry.destroy()
                year_entry.destroy()
                ordercost_entry.destroy()
                AdminPage(window)
            elif 563<=event.x<=648 and 614<=event.y<=664:
                add_product_media()

        C = Canvas(window, height=756, width=1210)
        C.bind("<Button-1>", callback)
        background_image = PhotoImage(file="images/adminCDadd.png")
        C.create_image(0, 0, image=background_image, anchor="nw")
        window.title("PJ Store")
        C.pack()
        helv36 = tkFont.Font(family='Helvetica', size=15, weight='bold')


        barcode= StringVar()
        barcode_entry = Entry(window,textvariable=barcode,width=25)
        barcode_entry['font']=helv36
        barcode_entry.pack()
        barcode_entry.place(x=345,y=236)

        title= StringVar()
        title_entry = Entry(window,textvariable=title,width=25)
        title_entry['font']=helv36
        title_entry.pack()
        title_entry.place(x=345,y=336)


        year= StringVar()
        year_entry = Entry(window,textvariable=year,width=25)
        year_entry['font']=helv36
        year_entry.pack()
        year_entry.place(x=345,y=436)

        runtime= StringVar()
        runtime_entry = Entry(window,textvariable=runtime,width=25)
        runtime_entry['font']=helv36
        runtime_entry.pack()
        runtime_entry.place(x=345,y=550)

        category= StringVar()
        category_entry = Entry(window,textvariable=category,width=15)
        category_entry['font']=helv36
        category_entry.pack()
        category_entry.place(x=674,y=236)

        ordercost= StringVar()
        ordercost_entry = Entry(window,textvariable=ordercost,width=15)
        ordercost_entry['font']=helv36
        ordercost_entry.pack()
        ordercost_entry.place(x=674,y=339)

        condition= StringVar()
        condition_entry = Entry(window,textvariable=condition,width=15)
        condition_entry['font']=helv36
        condition_entry.pack()
        condition_entry.place(x=674,y=436)

        genre= StringVar()
        genre_entry = Entry(window,textvariable=genre,width=15)
        genre_entry['font']=helv36
        genre_entry.pack()
        genre_entry.place(x=674,y=550)


        window.mainloop()

class CDAdminChangePage:
    def __init__(self, window,mode):

        def find_barcodes():
            database = r"lib.db"
            conn = create_connection(database)
            ins = "select barcode from media;"
            res = select_and_print(conn,ins)
            ls = []
            for tuple in res:
                ls.append(tuple[0])
            return ls

        def change_product_media():
            ins0 = "DELETE FROM media WHERE barcode='{}';".format(barcode.get())
            ins="INSERT INTO media VALUES('{}','{}','{}','{}','{}','{}','{}','{}');".format(barcode.get(),title_entry.get(),year_entry.get(),runtime_entry.get(),category_entry.get(),ordercost_entry.get(),condition_entry.get(),genre_entry.get())
            database = r"lib.db"
            conn = create_connection(database)

            if conn is not None:
                execute_instruction(conn,ins0)
                execute_instruction(conn,ins)
                conn.commit()
                print(pd.read_sql_query("SELECT * FROM media", conn))
                print("Changed")
            else:
                print("Error! cannot create the database connection.")

        def fetch_media():
            ins0 = "SELECT * FROM media WHERE barcode='{}';".format(barcode.get())

            database = r"lib.db"
            conn = create_connection(database)

            if conn is not None:
                a=select_and_print(conn,ins0)
                conn.commit()
                title.set(a[0][1])
                year.set(a[0][2])
                runtime.set(a[0][3])
                category.set(a[0][4])
                ordercost.set(a[0][5])
                condition.set(a[0][6])
                genre.set(a[0][7])

            else:
                print("Error! cannot create the database connection.")

        def callback(event):
            global flag
            if 52<=event.x<=194 and 621<=event.y<=668:
                C.destroy()
                menu2.destroy()
                runtime_entry.destroy()
                title_entry.destroy()
                condition_entry.destroy()
                category_entry.destroy()
                genre_entry.destroy()
                year_entry.destroy()
                ordercost_entry.destroy()
                AdminPage(window)
            elif 563<=event.x<=648 and 614<=event.y<=664:
                change_product_media()
            elif 908<=event.x<=1077 and 617<=event.y<=667:
                fetch_media()

        C = Canvas(window, height=756, width=1210)
        C.bind("<Button-1>", callback)
        background_image = PhotoImage(file="images/adminCDchange.png")
        C.create_image(0, 0, image=background_image, anchor="nw")
        window.title("PJ Store")
        C.pack()
        helv36 = tkFont.Font(family='Helvetica', size=15, weight='bold')

        types2 = find_barcodes()
        barcode = StringVar(window)
        barcode.set(types2[0])
        menu2 = OptionMenu(window, barcode, *types2)
        menu2.config(font="Helvetica 15 bold")
        m2 = window.nametowidget(menu2.menuname)
        m2.config(font="Helvetica 15 bold")
        menu2.pack()
        menu2.place(x=345, y=236)

        title= StringVar()
        title_entry = Entry(window,textvariable=title,width=25)
        title_entry['font']=helv36
        title_entry.pack()
        title_entry.place(x=345,y=336)


        year= StringVar()
        year_entry = Entry(window,textvariable=year,width=25)
        year_entry['font']=helv36
        year_entry.pack()
        year_entry.place(x=345,y=436)

        runtime= StringVar()
        runtime_entry = Entry(window,textvariable=runtime,width=25)
        runtime_entry['font']=helv36
        runtime_entry.pack()
        runtime_entry.place(x=345,y=550)

        category= StringVar()
        category_entry = Entry(window,textvariable=category,width=15)
        category_entry['font']=helv36
        category_entry.pack()
        category_entry.place(x=674,y=236)

        ordercost= StringVar()
        ordercost_entry = Entry(window,textvariable=ordercost,width=15)
        ordercost_entry['font']=helv36
        ordercost_entry.pack()
        ordercost_entry.place(x=674,y=339)

        condition= StringVar()
        condition_entry = Entry(window,textvariable=condition,width=15)
        condition_entry['font']=helv36
        condition_entry.pack()
        condition_entry.place(x=674,y=436)

        genre= StringVar()
        genre_entry = Entry(window,textvariable=genre,width=15)
        genre_entry['font']=helv36
        genre_entry.pack()
        genre_entry.place(x=674,y=550)


        window.mainloop()

class CDAdminDeletePage:
    def __init__(self, window,mode):

        def find_barcodes():
            database = r"lib.db"
            conn = create_connection(database)
            ins = "select barcode from media;"
            res = select_and_print(conn,ins)
            ls = []
            for tuple in res:
                ls.append(tuple[0])
            return ls

        def fetch_media():
            ins0 = "SELECT * FROM media WHERE barcode='{}';".format(barcode.get())

            database = r"lib.db"
            conn = create_connection(database)

            if conn is not None:
                a=select_and_print(conn,ins0)
                conn.commit()
                title.set(a[0][1])
                year.set(a[0][2])
                runtime.set(a[0][3])
                category.set(a[0][4])
                ordercost.set(a[0][5])
                condition.set(a[0][6])
                genre.set(a[0][7])

            else:
                print("Error! cannot create the database connection.")

        def delete_media():
            ins = "DELETE FROM media WHERE barcode='{}';".format(barcode.get())
            ins0 = "DELETE FROM product WHERE barcode='{}';".format(barcode.get())
            database = r"lib.db"
            conn = create_connection(database)

            if conn is not None:
                execute_instruction(conn,ins)
                execute_instruction(conn,ins0)
                conn.commit()
                print(pd.read_sql_query("SELECT * FROM media", conn))
                print("Deleted.")
            else:
                print("Error! cannot create the database connection.")

        def callback(event):
            global flag
            if 52<=event.x<=194 and 621<=event.y<=668:
                C.destroy()
                menu2.destroy()
                runtime_entry.destroy()
                title_entry.destroy()
                condition_entry.destroy()
                category_entry.destroy()
                genre_entry.destroy()
                year_entry.destroy()
                ordercost_entry.destroy()
                AdminPage(window)
            elif 509<=event.x<=709 and 627<=event.y<=676:
                try:
                    delete_media()
                except:
                    print("CD is already deleted.")
            elif 908<=event.x<=1077 and 617<=event.y<=667:
                try:
                    fetch_media()
                except:
                    print("CD does not exist.")

        C = Canvas(window, height=756, width=1210)
        C.bind("<Button-1>", callback)
        background_image = PhotoImage(file="images/adminCDchange.png")
        C.create_image(0, 0, image=background_image, anchor="nw")
        window.title("PJ Store")
        C.pack()
        helv36 = tkFont.Font(family='Helvetica', size=15, weight='bold')

        types2 = find_barcodes()
        barcode = StringVar(window)
        barcode.set(types2[0])
        menu2 = OptionMenu(window, barcode, *types2)
        menu2.config(font="Helvetica 15 bold")
        m2 = window.nametowidget(menu2.menuname)
        m2.config(font="Helvetica 15 bold")
        menu2.pack()
        menu2.place(x=345, y=236)

        title= StringVar()
        title_entry = Entry(window,textvariable=title,width=25)
        title_entry['font']=helv36
        title_entry.pack()
        title_entry.place(x=345,y=336)


        year= StringVar()
        year_entry = Entry(window,textvariable=year,width=25)
        year_entry['font']=helv36
        year_entry.pack()
        year_entry.place(x=345,y=436)

        runtime= StringVar()
        runtime_entry = Entry(window,textvariable=runtime,width=25)
        runtime_entry['font']=helv36
        runtime_entry.pack()
        runtime_entry.place(x=345,y=550)

        category= StringVar()
        category_entry = Entry(window,textvariable=category,width=15)
        category_entry['font']=helv36
        category_entry.pack()
        category_entry.place(x=674,y=236)

        ordercost= StringVar()
        ordercost_entry = Entry(window,textvariable=ordercost,width=15)
        ordercost_entry['font']=helv36
        ordercost_entry.pack()
        ordercost_entry.place(x=674,y=339)

        condition= StringVar()
        condition_entry = Entry(window,textvariable=condition,width=15)
        condition_entry['font']=helv36
        condition_entry.pack()
        condition_entry.place(x=674,y=436)

        genre= StringVar()
        genre_entry = Entry(window,textvariable=genre,width=15)
        genre_entry['font']=helv36
        genre_entry.pack()
        genre_entry.place(x=674,y=550)


        window.mainloop()

class PolicyAdminAddPage:
    def __init__(self, window):

        def add_policy():
            ins = "INSERT INTO policies VALUES('{}','{}','{}');".format(barcode.get(),length_entry.get(),description_entry.get())
            database = r"lib.db"
            conn = create_connection(database)

            if conn is not None:
                execute_instruction(conn,ins)
                conn.commit()
                print(pd.read_sql_query("SELECT * FROM policies", conn))
                print("Added")
            else:
                print("Error! cannot create the database connection.")

        def find_barcodes():
            database = r"lib.db"
            conn = create_connection(database)
            ins = "select barcode from product;"
            res = select_and_print(conn,ins)
            ls = []
            for tuple in res:
                ls.append(tuple[0])
            return ls

        def callback(event):
            global flag
            if 52<=event.x<=194 and 621<=event.y<=668:
                C.destroy()
                menu2.destroy()
                description_entry.destroy()
                length_entry.destroy()
                AdminPage(window)
            elif 563<=event.x<=647 and 617<=event.y<=666:
                add_policy()


        C = Canvas(window, height=756, width=1210)
        C.bind("<Button-1>", callback)
        background_image = PhotoImage(file="images/adminpolicyadd.png")
        C.create_image(0, 0, image=background_image, anchor="nw")
        window.title("PJ Store")
        C.pack()
        helv36 = tkFont.Font(family='Helvetica', size=15, weight='bold')

        types2 = find_barcodes()
        barcode = StringVar(window)
        barcode.set(types2[0])
        menu2 = OptionMenu(window, barcode, *types2)
        menu2.config(font="Helvetica 15 bold")
        m2 = window.nametowidget(menu2.menuname)
        m2.config(font="Helvetica 15 bold")
        menu2.pack()
        menu2.place(x=428, y=278)

        description= StringVar()
        description_entry = Entry(window,textvariable=description,width=25)
        description_entry['font']=helv36
        description_entry.pack()
        description_entry.place(x=428,y=403)


        length= StringVar()
        length_entry = Entry(window,textvariable=length,width=25)
        length_entry['font']=helv36
        length_entry.pack()
        length_entry.place(x=428,y=513)

        window.mainloop()

class PolicyAdminChangePage:
    def __init__(self, window):

        def fetch_policy():
            ins0 = "SELECT * FROM policies WHERE barcode='{}';".format(barcode.get())
            database = r"lib.db"
            conn = create_connection(database)

            if conn is not None:
                a=select_and_print(conn,ins0)
                conn.commit()
                length.set(a[0][1])
                description.set(a[0][2])
            else:
                print("Error! cannot create the database connection.")

        def change_policy():
            ins0 = "DELETE FROM policies WHERE barcode='{}';".format(barcode.get())
            ins = "INSERT INTO policies VALUES('{}','{}','{}');".format(barcode.get(),length_entry.get(),description_entry.get())
            database = r"lib.db"
            conn = create_connection(database)

            if conn is not None:
                execute_instruction(conn,ins0)
                execute_instruction(conn,ins)
                conn.commit()
                print(pd.read_sql_query("SELECT * FROM policies", conn))
                print("Changed.")
            else:
                print("Error! cannot create the database connection.")

        def find_barcodes():
            database = r"lib.db"
            conn = create_connection(database)
            ins = "select barcode from product;"
            res = select_and_print(conn,ins)
            ls = []
            for tuple in res:
                ls.append(tuple[0])
            return ls

        def callback(event):
            global flag
            if 52<=event.x<=194 and 621<=event.y<=668:
                C.destroy()
                menu2.destroy()
                description_entry.destroy()
                length_entry.destroy()
                AdminPage(window)
            elif 563<=event.x<=647 and 617<=event.y<=666:
                change_policy()
                print("Changed")
            elif 905<=event.x<=1078 and 616<=event.y<=666:
                fetch_policy()

        C = Canvas(window, height=756, width=1210)
        C.bind("<Button-1>", callback)
        background_image = PhotoImage(file="images/adminpolicychange.png")
        C.create_image(0, 0, image=background_image, anchor="nw")
        window.title("PJ Store")
        C.pack()
        helv36 = tkFont.Font(family='Helvetica', size=15, weight='bold')

        types2 = find_barcodes()
        barcode = StringVar(window)
        barcode.set(types2[0])
        menu2 = OptionMenu(window, barcode, *types2)
        menu2.config(font="Helvetica 15 bold")
        m2 = window.nametowidget(menu2.menuname)
        m2.config(font="Helvetica 15 bold")
        menu2.pack()
        menu2.place(x=428, y=278)

        description= StringVar()
        description_entry = Entry(window,textvariable=description,width=25)
        description_entry['font']=helv36
        description_entry.pack()
        description_entry.place(x=428,y=403)


        length= StringVar()
        length_entry = Entry(window,textvariable=length,width=25)
        length_entry['font']=helv36
        length_entry.pack()
        length_entry.place(x=428,y=513)

        window.mainloop()

class PolicyAdminDeletePage:
    def __init__(self, window):

        def fetch_policy():
            ins0 = "SELECT * FROM policies WHERE barcode='{}';".format(barcode.get())
            database = r"lib.db"
            conn = create_connection(database)

            if conn is not None:
                a=select_and_print(conn,ins0)
                conn.commit()
                length.set(a[0][1])
                description.set(a[0][2])
            else:
                print("Error! cannot create the database connection.")

        def delete_policy():
            ins = "DELETE FROM policies WHERE barcode='{}';".format(barcode.get())
            database = r"lib.db"
            conn = create_connection(database)

            if conn is not None:
                execute_instruction(conn,ins)
                conn.commit()
                print(pd.read_sql_query("SELECT * FROM policies", conn))
                print("Deleted")
            else:
                print("Error! cannot create the database connection.")

        def find_barcodes():
            database = r"lib.db"
            conn = create_connection(database)
            ins = "select barcode from product;"
            res = select_and_print(conn,ins)
            ls = []
            for tuple in res:
                ls.append(tuple[0])
            return ls

        def callback(event):
            global flag
            if 52<=event.x<=194 and 621<=event.y<=668:
                C.destroy()
                menu2.destroy()
                description_entry.destroy()
                length_entry.destroy()
                AdminPage(window)
            elif 563<=event.x<=647 and 617<=event.y<=666:
                try:
                    delete_policy()
                except:
                    print("Already deleted.")
            elif 905<=event.x<=1078 and 616<=event.y<=666:
                try:
                    fetch_policy()
                except:
                    print("Deleted")

        C = Canvas(window, height=756, width=1210)
        C.bind("<Button-1>", callback)
        background_image = PhotoImage(file="images/adminpolicychange.png")
        C.create_image(0, 0, image=background_image, anchor="nw")
        window.title("PJ Store")
        C.pack()
        helv36 = tkFont.Font(family='Helvetica', size=15, weight='bold')

        types2 = find_barcodes()
        barcode = StringVar(window)
        barcode.set(types2[0])
        menu2 = OptionMenu(window, barcode, *types2)
        menu2.config(font="Helvetica 15 bold")
        m2 = window.nametowidget(menu2.menuname)
        m2.config(font="Helvetica 15 bold")
        menu2.pack()
        menu2.place(x=428, y=278)

        description= StringVar()
        description_entry = Entry(window,textvariable=description,width=25)
        description_entry['font']=helv36
        description_entry.pack()
        description_entry.place(x=428,y=403)


        length= StringVar()
        length_entry = Entry(window,textvariable=length,width=25)
        length_entry['font']=helv36
        length_entry.pack()
        length_entry.place(x=428,y=513)

        window.mainloop()

class ProfitAdminCheckPage:
    def __init__(self, window):
        title_label = 0
        helvbig = tkFont.Font(family='Helvetica', size=24, weight='bold')

        def check_profit():
            global title_label
            ins="SELECT (sell_cost-order_cost) as profits from profit where barcode='{}';".format(barcode.get())
            database = r"lib.db"
            conn = create_connection(database)

            if conn is not None:
                a = select_and_print(conn,ins)
                prof = a[0][0]
                try:
                    title_label.destroy()
                except:
                    pass

                title_label = Label(window, text="Profit is {} Rs".format(prof))
                title_label['font']=helvbig
                title_label.pack()
                title_label.place(x=483,y=435)

                conn.commit()
            else:
                print("Error! cannot create the database connection.")

        def find_barcodes():
            database = r"lib.db"
            conn = create_connection(database)
            ins = "select barcode from product;"
            res = select_and_print(conn,ins)
            ls = []
            for tuple in res:
                ls.append(tuple[0])
            return ls

        def callback(event):
            global flag
            if 52<=event.x<=194 and 621<=event.y<=668:
                C.destroy()
                menu2.destroy()
                try:
                    title_label.destroy()
                except:
                    pass
                AdminPage(window)
            elif 563<=event.x<=647 and 617<=event.y<=666:
                check_profit()


        C = Canvas(window, height=756, width=1210)
        C.bind("<Button-1>", callback)
        background_image = PhotoImage(file="images/adminprofitcheck.png")
        C.create_image(0, 0, image=background_image, anchor="nw")
        window.title("PJ Store")
        C.pack()
        helv36 = tkFont.Font(family='Helvetica', size=15, weight='bold')

        types2 = find_barcodes()
        barcode = StringVar(window)
        barcode.set(types2[0])
        menu2 = OptionMenu(window, barcode, *types2)
        menu2.config(font="Helvetica 15 bold")
        m2 = window.nametowidget(menu2.menuname)
        m2.config(font="Helvetica 15 bold")
        menu2.pack()
        menu2.place(x=500, y=325)

        window.mainloop()

class AuthorAdminAddPage:
    def __init__(self, window):

        def add_author():
            ins = "INSERT INTO author VALUES('{}','{}','{}');".format(authorid_entry.get(),firstname_entry.get(),lastname_entry.get())
            database = r"lib.db"
            conn = create_connection(database)

            if conn is not None:
                execute_instruction(conn,ins)
                print(pd.read_sql_query("SELECT * FROM author", conn))
                # print("Added.")
                conn.commit()
            else:
                print("Error! cannot create the database connection.")

        def callback(event):
            global flag
            if 566<=event.x<=654 and 626<=event.y<=675:
                add_author()
                print("Added")
            elif 55<=event.x<=195 and 625<=event.y<=668:
                authorid_entry.destroy()
                firstname_entry.destroy()
                lastname_entry.destroy()
                C.destroy()
                AdminPage(window)

        C = Canvas(window, height=756, width=1210)
        C.bind("<Button-1>", callback)
        background_image = PhotoImage(file="images/adminauthoradd.png")
        C.create_image(0, 0, image=background_image, anchor="nw")
        window.title("PJ Store")
        C.pack()

        helv36 = tkFont.Font(family='Helvetica', size=15, weight='bold')
        authorid= StringVar()
        authorid_entry = Entry(window,textvariable=authorid,width=30)
        authorid_entry['font']=helv36
        authorid_entry.pack()
        authorid_entry.place(x=421,y=283)

        firstname= StringVar()
        firstname_entry = Entry(window,textvariable=firstname,width=30)
        firstname_entry['font']=helv36
        firstname_entry.pack()
        firstname_entry.place(x=421,y=396)

        lastname= StringVar()
        lastname_entry = Entry(window,textvariable=lastname,width=30)
        lastname_entry['font']=helv36
        lastname_entry.pack()
        lastname_entry.place(x=421,y=520)

        window.mainloop()

if __name__ == "__main__":
    window = Tk()
    StartPage(window)
