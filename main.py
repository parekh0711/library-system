from tables import *
from insert import *
from create import *
import sqlite3
from sqlite3 import Error
import pandas as pd

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

def select_and_print(conn,instruction):
    try:
        c=conn.cursor()
        c.execute(instruction)
        rows=c.fetchall()
        return rows
    except Error as e:
        print(e)

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
    execute_instruction(conn,insert_author)
    execute_instruction(conn,insert_book)
    execute_instruction(conn, insert_media)
    execute_instruction(conn, insert_reservation)
    execute_instruction(conn, insert_borrowed)
    execute_instruction(conn, insert_profit)
    execute_instruction(conn, insert_outstanding)
    execute_instruction(conn, insert_policies)

def main():
    database = r"lib.db"
    conn = create_connection(database)

    if conn is not None:
        # create projects table
        execute_instruction(conn,"""PRAGMA foreign_keys = ON;""")
        create_tables(conn)
        insert_data(conn)
        conn.commit()
        print("Database is ready.")
        # select(conn,"""select * from book;""")
        # print(pd.read_sql_query("SELECT customer_id FROM outstanding", conn))
        #conn.commit()

    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
