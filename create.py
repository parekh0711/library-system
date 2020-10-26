
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
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
                print(element,end="\t")
            print("")
    except Error as e:
        print(e)

def main():
    database = r"lib.db"

    customer_table = """ CREATE TABLE IF NOT EXISTS customer (
                                        customer_id integer PRIMARY KEY,
                                        first_name text NOT NULL,
                                        last_name text NOT NULL,
                                        dob text NOT NULL,
                                        phone text NOT NULL,
                                        address text NOT NULL
                                    ); """

    outstanding_table = """CREATE TABLE IF NOT EXISTS outstanding (
                                    customer_id integer PRIMARY KEY NOT NULL,
                                    employee_id integer NOT NULL,
                                    renewed text NOT NULL,
                                    barcode text NOT NULL,
                                    amount numeric NOT NULL,
                                    penalty numeric NOT NULL,
                                    status text NOT NULL,
                                    due_date text NOT NULL,
                                    borrowed_date text NOT NULL,
                                    FOREIGN KEY(customer_id) REFERENCES customer(customer_id) ON DELETE CASCADE,
                                    FOREIGN KEY(employee_id) REFERENCES employee(employee_id) ON DELETE SET NULL
                                );"""

    employee_table = """CREATE TABLE IF NOT EXISTS employee (
                                    employee_id integer PRIMARY KEY NOT NULL,
                                    aadhar integer NOT NULL,
                                    pan text NOT NULL,
                                    first_name text NOT NULL,
                                    last_name text NOT NULL,
                                    dob text NOT NULL,
                                    phone text NOT NULL,
                                    address text NOT NULL,
                                    salary numeric NOT NULL,
                                    designation text NOT NULL
                                );"""

    product_table = """CREATE TABLE IF NOT EXISTS product (
                                    barcode text PRIMARY KEY NOT NULL,
                                    type text NOT NULL
                                );"""

    reservation_table = """CREATE TABLE IF NOT EXISTS reservation (
                                    customer_id integer NOT NULL,
                                    barcode text NOT NULL,
                                    FOREIGN KEY(customer_id) REFERENCES customer(customer_id) ON DELETE CASCADE,
                                    FOREIGN KEY(barcode) REFERENCES product(barcode) ON DELETE SET NULL
                                );"""
    profit_table ="""CREATE TABLE IF NOT EXISTS profit (
                                    barcode text PRIMARY KEY NOT NULL,
                                    order_cost text NOT NULL,
                                    sell_cost text NOT NULL,
                                    FOREIGN KEY(barcode) REFERENCES product(barcode) ON DELETE SET NULL
                                );"""

    borrowed_table ="""CREATE TABLE IF NOT EXISTS borrowed (
                                    barcode text PRIMARY KEY NOT NULL,
                                    customer_id text NOT NULL,
                                    FOREIGN KEY(barcode) REFERENCES product(barcode) ON DELETE SET NULL,
                                    FOREIGN KEY(customer_id) REFERENCES customer(customer_id) ON DELETE CASCADE
                                );"""

    

    book_table = """CREATE TABLE IF NOT EXISTS book (
                                    barcode text PRIMARY KEY NOT NULL,
                                    author_id integer NOT NULL,
                                    title text NOT NULL,
                                    state text NOT NULL,
                                    year text NOT NULL,
                                    publisher text NOT NULL,
                                    genre text NOT NULL,
                                    order_cost numeric NOT NULL,
                                    current_condition text NOT NULL,
                                    FOREIGN KEY(barcode) REFERENCES product(barcode),
                                    FOREIGN KEY(author_id) REFERENCES author(author_id)
                                );"""

    author_table ="""CREATE TABLE IF NOT EXISTS author (
                                    author_id integer PRIMARY KEY NOT NULL,
                                    first_name text NOT NULL,
                                    last_name text NOT NULL
                                );"""

    policies_table ="""CREATE TABLE IF NOT EXISTS policies (
                                    barcode text NOT NULL,
                                    length text NOT NULL,
                                    description text NOT NULL,
                                    FOREIGN KEY(barcode) REFERENCES product(barcode),
                                );"""

    media_table = """CREATE TABLE IF NOT EXISTS media (
                                    barcode text PRIMARY KEY NOT NULL,
                                    title text NOT NULL,
                                    year integer NOT NULL,
                                    runtime text NOT NULL,
                                    category text NOT NULL,
                                    order_cost numeric NOT NULL,
                                    current_condition text NOT NULL,
                                    genre text NOT NULL,
                                    FOREIGN KEY(barcode) REFERENCES product(barcode)
                                );"""

    conn = create_connection(database)

    if conn is not None:
        # create projects table
        execute_instruction(conn,"""PRAGMA foreign_keys = ON;""")
        # execute_instruction(conn, customer_table)
        # execute_instruction(conn, product_table)
        # execute_instruction(conn, reservation_table)
        # execute_instruction(conn, profit_table)
        # execute_instruction(conn, borrowed_table)
        # execute_instruction(conn, employee_table)
        # execute_instruction(conn, outstanding_table)
        # execute_instruction(conn, author_table)
        # execute_instruction(conn,book_table)
        # execute_instruction(conn, policies_table)
        # execute_instruction(conn, media_table)
        #select(conn,"""select * from outstanding;""")
        conn.commit()
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
