customer_table = """ CREATE TABLE IF NOT EXISTS customer (
                                    customer_id integer PRIMARY KEY,
                                    first_name text NOT NULL,
                                    last_name text NOT NULL,
                                    dob text NOT NULL,
                                    phone text NOT NULL,
                                    address text NOT NULL,
                                    Renewed text NOT NULL
                                ); """

outstanding_table = """CREATE TABLE IF NOT EXISTS outstanding (
                                customer_id integer NOT NULL,
                                employee_id integer NOT NULL,
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
                                designation text NOT NULL
                            );"""

product_table = """CREATE TABLE IF NOT EXISTS product (
                                barcode text PRIMARY KEY NOT NULL,
                                type text NOT NULL,
                                state text NOT NULL
                            );"""

salary_table = """CREATE TABLE IF NOT EXISTS salary (
                                Designation text NOT NULL,
                                Salary integer NOT NULL
                            );"""

reservation_table = """CREATE TABLE IF NOT EXISTS reservation (
                                customer_id integer NOT NULL,
                                barcode text PRIMARY KEY NOT NULL,
                                reserving_date text NOT NULL,
                                start_date text NOT NULL,
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

#

book_table = """CREATE TABLE IF NOT EXISTS book (
                                barcode text PRIMARY KEY NOT NULL,
                                author_id integer NOT NULL,
                                title text NOT NULL,
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
