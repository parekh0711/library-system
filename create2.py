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
    ins="INSERT INTO employee VALUES("+emp_id+","+aadhar+","+pan+","+first+","+last+","+dob+","+phone+","+addr+","+desig+");"
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

def create_tables(conn):
    #execute_instruction(conn, customer_table)
    #execute_instruction(conn, product_table)
    #execute_instruction(conn, reservation_table)
    #execute_instruction(conn, profit_table)
    #execute_instruction(conn, borrowed_table)
    #execute_instruction(conn, employee_table)
    #execute_instruction(conn, outstanding_table)
    #execute_instruction(conn, author_table)
    #execute_instruction(conn,book_table)
    #execute_instruction(conn, media_table)
    #execute_instruction(conn, salary_table)
    execute_instruction(conn, policies_table)

def insert_data(conn):
    #execute_instruction(conn, insert_customer)
    #execute_instruction(conn,insert_employee)
    #execute_instruction(conn,insert_salary)
    #execute_instruction(conn,insert_product)
    #execute_instruction(conn,insert_book)
    #execute_instruction(conn,insert_author)
    #execute_instruction(conn, insert_media)
    #execute_instruction(conn, insert_reservation)
    #execute_instruction(conn, insert_borrowed)
    #execute_instruction(conn, insert_profit)
    #execute_instruction(conn, insert_outstanding)
    execute_instruction(conn, policies_table)

def main():
    database = r"lib.db"
    conn = create_connection(database)

    if conn is not None:
        # create projects table
        execute_instruction(conn,"""PRAGMA foreign_keys = ON;""")
        create_tables(conn)
        insert_data(conn)
        conn.commit()
        select(conn,"""select * from employee;""")
        #conn.commit()

    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
