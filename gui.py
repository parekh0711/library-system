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
            elif 706<=event.x<=1025 and 356<=event.y<=314:
                C.destroy()
                EmployeeCheckPage(window,emp_id,2)
                #book
            elif 738<=event.x<=996 and 449<=event.y<=495:
                C.destroy()
                EmployeeCheckPage(window,emp_id,3)
                #CD


        C = Canvas(window, height=756, width=1210)
        C.bind("<Button-1>", callback)
        background_image = PhotoImage(file="images/employeemain.png")
        C.create_image(0, 0, image=background_image, anchor="nw")
        window.title("PJ Store")
        C.pack()
        window.mainloop()

class EmployeeReservationPage:
    def __init__(self, window,emp_id):
        def callback(event):
            global flag
            print(event.x,event.y)
            if 40<=event.x<=210 and 616<=event.y<=664:
                C.destroy()
                EmployeePage(window,emp_id)

        #place entry box at (412,427) and (439,259)
        C = Canvas(window, height=756, width=1210)
        C.bind("<Button-1>", callback)
        background_image = PhotoImage(file="images/employeereserve.png")
        C.create_image(0, 0, image=background_image, anchor="nw")
        window.title("PJ Store")
        C.pack()
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
