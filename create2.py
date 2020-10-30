from tables import *
from insert import *
from create import *
import sqlite3
from sqlite3 import Error

policies_table ="""CREATE TABLE IF NOT EXISTS policies (
                                barcode text NOT NULL,
                                length text NOT NULL,
                                description text NOT NULL,
                                FOREIGN KEY(barcode) REFERENCES product(barcode)
                            );"""
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def execute_instruction(conn,instruction):
    try:
        c=conn.cursor()
        c.execute(instruction)
    except Error as e:
        print(e)


def select(conn,instruction):
    try:
        c=conn.cursor()
        c.execute(instruction)
        rows=c.fetchall()
        for row in rows:
            for element in row:
                print(element,end="\t\t")
            print("")
    except Error as e:
        print(e)

def add_employee(conn):
    emp_id="dummy"
    aadhar="dummy"
    pan="dummy"
    first="dummy"
    last="dummy"
    dob="dummy"
    phone="dummy"
    addr="dummy"
    desig="dummy"
    ins="INSERT INTO employee VALUES("+ emp_id + ","+aadhar+","+pan+","+first+","+last+","+dob+","+phone+","+addr+","+desig+");"
    execute_instruction(conn,ins)
    conn.commit()

def rem_employee(conn):
    emp_id="dummy"
    ins="DELETE FROM employee WHERE employee_id="+empid+";"
    conn.commit()

def add_product_book(conn):
    barcode="dummy"
    authorid="dummy"
    title="dummy"
    year="dummy"
    publisher="dummy"
    genre="dummy"
    cost="dummy"
    cond="dummy"
    ins="INSERT INTO book VALUES("+barcode+","+authorid+","+title+","+year+","+publisher+","+genre+","+cost+","+cond+");"
    ins2="INSERT INTO product VALUES("+barcode+",Book,in_stock);"
    execute_instruction(conn,ins)
    execute_instruction(conn,ins2)
    conn.commit()

def add_product_media(conn):
    barcode="dummy"
    title="dummy"
    year="dummy"
    runtime="dummy"
    category="dummy"
    cost="dummy"
    cond="dummy"
    genre="dummy"
    ins="INSERT INTO media VALUES("+barcode+","+title+","+year+","+runtime+","+category+","+cost+","+cond+","+genre+");"
    ins2="INSERT INTO product VALUES("+barcode+",Media,in_stock);"
    execute_instruction(conn,ins)
    execute_instruction(conn,ins2)
    conn.commit()

def rem_product(conn):
    barcode="dummy"
    type="dummy"
    if type=="Book":
        ins="DELETE FROM book WHERE barcode="+barcode+";"
    elif type=="Media":
        ins="DELETE FROM media WHERE barcode="+barcode+";"
    ins2="DELETE FROM product WHERE barcode="+barcode+";"
    execute_instruction(conn,ins)
    execite_instruction(conn,ins2)
    conn.commit()

def check_profit(conn):
    ins="SELECT (sell_cost-order_cost) as profits from profit;"
    execute_instruction(conn,ins)
    conn.commit()

def change_employee(conn):
    emp_id="dummy"
    aadhar="dummy"
    pan="dummy"
    first="dummy"
    last="dummy"
    dob="dummy"
    phone="dummy"
    addr="dummy"
    desig="dummy"
    ins1="DELETE FROM employee WHERE employee_id="+empid+";"
    ins2="INSERT INTO employee VALUES("+emp_id+","+aadhar+","+pan+","+first+","+last+","+dob+","+phone+","+addr+","+desig+");"
    execute_instruction(conn,ins1)
    execute_instruction(conn,ins2)
    conn.commit()

def change_book(conn):
    barcode="dummy"
    authorid="dummy"
    title="dummy"
    year="dummy"
    publisher="dummy"
    genre="dummy"
    cost="dummy"
    cond="dummy"
    ins="DELETE FROM book WHERE barcode="+barcode+";"
    ins2="INSERT INTO book VALUES("+barcode+","+authorid+","+title+","+year+","+publisher+","+genre+","+cost+","+cond+");"
    execute_instruction(conn,ins)
    execite_instruction(conn,ins2)
    conn.commit()

def change_media(conn):
    barcode="dummy"
    title="dummy"
    year="dummy"
    runtime="dummy"
    category="dummy"
    cost="dummy"
    cond="dummy"
    genre="dummy"
    ins="DELETE FROM media WHERE barcode="+barcode+";"
    ins2="INSERT INTO media VALUES("+barcode+","+title+","+year+","+runtime+","+category+","+cost+","+cond+","+genre+");"
    execute_instruction(conn,ins)
    execite_instruction(conn,ins2)
    conn.commit()


#NEW functions

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

def select_and_print(conn,instruction):
    try:
        c=conn.cursor()
        c.execute(instruction)
        rows=c.fetchall()
        return rows
    except Error as e:
        print(e)

def fetch_employee():
    ins0 = "SELECT * FROM employee WHERE employee_id='{}';".format(employeeid_entry.get())

    database = r"lib.db"
    conn = create_connection(database)

    if conn is not None:
        a=select_and_print(conn,ins0)
        conn.commit()
        employeeid_entry.set('a[0][0]')
        aadhar_entry.set('a[0][1]')
        pan_entry.set('a[0][2]')
        firstname_entry.set('a[0][3]')
        lastname_entry.set('a[0][4]')
        dob_entry.set('a[0][5]')
        phone_entry.set('a[0][6]')
        address_entry.set('a[0][7]')
        designation_entry.set('a[0][8]')
    else:
        print("Error! cannot create the database connection.")


def fetch_book():
    ins0 = "SELECT * FROM book WHERE barcode='{}';".format(barcode_entry.get())

    database = r"lib.db"
    conn = create_connection(database)

    if conn is not None:
        a=select_and_print(conn,ins0)
        conn.commit()
        barcode_entry.set('a[0][0]')
        authorid_entry.set('a[0][1]')
        title_entry.set('a[0][2]')
        year_entry.set('a[0][3]')
        publisher_entry.set('a[0][4]')
        genre_entry.set('a[0][5]')
        ordercost_entry.set('a[0][6]')
        condition_entry.set('a[0][7]')
    else:
        print("Error! cannot create the database connection.")

def fetch_media():
    ins0 = "SELECT * FROM media WHERE barcode='{}';".format(barcode_entry.get())

    database = r"lib.db"
    conn = create_connection(database)

    if conn is not None:
        a=select_and_print(conn,ins0)
        conn.commit()
        barcode_entry.set('a[0][0]')
        title_entry.set('a[0][1]')
        year_entry.set('a[0][2]')
        runtime_entry.set('a[0][3]')
        category_entry.set('a[0][4]')
        ordercost_entry.set('a[0][5]')
        condition_entry.set('a[0][6]')
        genre_entry.set('a[0][7]')

    else:
        print("Error! cannot create the database connection.")

def fetch_policy():
    ins0 = "SELECT * FROM policy WHERE barcode='{}';".format(barcode_entry.get())

    database = r"lib.db"
    conn = create_connection(database)

    if conn is not None:
        a=select_and_print(conn,ins0)
        conn.commit()
        barcode_entry.set('a[0][0]')
        length_entry.set('a[0][1]')
        description_entry.set('a[0][2]')
    else:
        print("Error! cannot create the database connection.")

def check_book():
    ins = "SELECT state FROM product,book WHERE book.title='{}' and book.barcode=product.barcode;".format(title_entry.get())
    database = r"lib.db"
    conn = create_connection(database)

    if conn is not None:
        a=select_and_print(conn,ins)#returns the state as list of tuples which will have only one value
        conn.commit()
        available_entry.set(a[0][0]) # display in entry box

    else:
        print("Error! cannot create the database connection.")

def check_media():
    ins = "SELECT state FROM product,media WHERE media.title='{}' and media.barcode=product.barcode;".format(title_entry.get())
    database = r"lib.db"
    conn = create_connection(database)

    if conn is not None:
        a=select_and_print(conn,ins)#returns the state as list of tuples which will have only one value
        conn.commit()
        available_entry.set(a[0][0]) # display in entry box

    else:
        print("Error! cannot create the database connection.")

def check_author():
    ins = "SELECT book.title FROM author,book WHERE author.first_name='{}' and author.last_name='{}' and author.author_id=book.author_id;".format(first_name_entry.get(),last_name_entry.get())
    database = r"lib.db"
    conn = create_connection(database)

    if conn is not None:
        a=select_and_print(conn,ins)
        conn.commit()
        for tuple in a:
            print(tuple[0]) #since i did not know how are you outputting it

    else:
        print("Error! cannot create the database connection.")

def return_item():
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
        renewed_entry.set(a[0][0])
        payment_entry.set(b[0][0])

    else:
        print("Error! cannot create the database connection.")

def billing_item():
    database = r"lib.db"
    conn = create_connection(database)
    if conn is not None:
        ins1 = "SELECT date('{}','+007 days');".format(borrowdate_entry.get())
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
        ins3 = "INSERT INTO outstanding VALUES('{}','{}','{}','{}','{}','{}','{}','{}');".format(customerid_entry.get(),employeeid_entry.get(),barcode_entry.get(),amt,penalty,status,res,borrowdate_entry.get())
        ins4 = "UPDATE product SET state='Borrowed' WHERE barcode='{}';".format(barcode_entry.get())
        ins5 = "INSERT INTO borrowed VALUES('{}','{}');".format(barcode_entry.get(),customerid_entry.get())
        execute_instruction(conn,ins3)
        execute_instruction(conn,ins4)
        execute_instruction(conn,ins5)
        conn.commit()
    else:
        print("Error! cannot create the database connection.")

def reserve_item():
    database = r"lib.db"
    conn = create_connection(database)
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
                ins3="INSERT INTO reservation VALUES ('{}','{}','{}','{}');".format(customerid_entry.get(),barcode_entry.get(),reservingdate_entry.get(),startdate_entry.get())
                execute_instruction(conn,ins3)
                conn.commit()
            else:
                print("Unavailable")  #for now
        else:
            ins4="INSERT INTO reservation VALUES ('{}','{}','{}','{}');".format(customerid_entry.get(),barcode_entry.get(),reservingdate_entry.get(),startdate_entry.get())
            ins5="UPDATE product SET state='reserved' where barcode='{}';".format(barcode_entry.get())
            execute_instruction(conn,ins4)
            execute_instruction(conn,ins5)
            conn.commit()
    else:
        print("Error! cannot create the database connection.")


def create_tables(conn):
    execute_instruction(conn, customer_table)
    execute_instruction(conn, product_table)
    execute_instruction(conn, reservation_table)
    execute_instruction(conn, profit_table)
    execute_instruction(conn, borrowed_table)
    execute_instruction(conn, employee_table)
    execute_instruction(conn, outstanding_table)
    execute_instruction(conn, author_table)
    execute_instruction(conn,book_table)
    execute_instruction(conn, media_table)
    execute_instruction(conn, salary_table)
    execute_instruction(conn, policies_table)

def insert_data(conn):
    execute_instruction(conn, insert_customer)
    execute_instruction(conn,insert_employee)
    execute_instruction(conn,insert_salary)
    execute_instruction(conn,insert_product)
    execute_instruction(conn,insert_book)
    execute_instruction(conn,insert_author)
    execute_instruction(conn, insert_media)
    execute_instruction(conn, insert_reservation)
    execute_instruction(conn, insert_borrowed)
    execute_instruction(conn, insert_profit)
    execute_instruction(conn, insert_outstanding)
    execute_instruction(conn, policies_table)

def main():
    database = r"lib.db"
    conn = create_connection(database)

    if conn is not None:
        # create projects table
        # execute_instruction(conn,"""PRAGMA foreign_keys = ON;""")
        # create_tables(conn)
        # insert_data(conn)
        # conn.commit()
        select(conn,"""select * from outstanding;""")
        #conn.commit()

    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
