# Library Management System

A simple Library management system for libraries to automate various proccesses. It can be scaled up as required and is very lightweight as it uses sqlite3. GUI made using tkinter. The schema is included in the repo.
All database queries are seperate functions in gui.py for ease of checking. All insert and create queries are in seperate py files named insert and create and the creation  of tables can be done initially by running main.py

It has two modes, Admin and Employee

# Admin Features
The password for admin mode is aa#1111AA.

- Add Product (CD/Book)
- Change Product (CD/Book)
- Delete Product (CD/Book)
- Add Employee
- Change Employee 
- Delete Employee
- Add Policy
- Change Policy
- Delete Policy
- Check Profit (For any product)

# Employee Features
The employee id has to be entered before logging in and it is auto filled for the rest of the session.

- Reserve product
- Billing
- Check Book
- Check CD
- Check Author
- Return Item
- Add Customer

# Supported Platforms

- Windows
- Linux

# Requirements

- python3.x with tkinter and sqlite3
- Pandas

# Running Instructions

- To create your own mock database, run main.py
- Then run gui.py to perform various operations.
- To customise insert statements while creating database, modify insert.py

# Screenshots

![Main-Page](https://github.com/parekh0711/library-system/blob/main/screenshots/screenshot1.png)
![Admin-login](https://github.com/parekh0711/library-system/blob/main/screenshots/screenshot0.png)
![Admin-page](https://github.com/parekh0711/library-system/blob/main/screenshots/screenshot2.png)
![Admin-operation](https://github.com/parekh0711/library-system/blob/main/screenshots/screenshot3.png)
![Employee-operation](https://github.com/parekh0711/library-system/blob/main/screenshots/screenshot5.png)

