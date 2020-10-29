insert_customer = """INSERT INTO customer VALUES('113001','Tanaya','Jadhav','2000-05-11','9533734772','Aundh,Pune-411007','renewed'),
                                                ('113002','Soham','Parekh','2000-06-23','9533753477','Shivaji Nagar,Pune-411005','renewed'),
                                                ('113003','Karan','Malhotra','1996-12-15','9583014772','Aundh,Pune-411007','renewed'),
                                                ('113004','Sana','Mohapatra','1998-08-25','9460734662','Khadki,Pune-411003','renewed'),
                                                ('113005','Anurag','Basu','1991-04-30','8739024810','VimanNagar,Pune-411014','renewed'),
                                                ('113006','Reva','Bhandari','2000-01-01','7783940021','Kothrud,Pune-411038','renewed'),
                                                ('113007','Shahana','Desai','1993-08-13','9761114002','Baner,Pune-411045','renewed'),
                                                ('113008','Riddhima','Singh','1998-11-20','9937485662','Balewadi,Pune-411045','renewed'),
                                                ('113009','Vihaan','Deshpande','1995-05-15','9667804662','Kothrud,Pune-411038','renewed'),
                                                ('113010','Shrikant','Joshi','1990-07-17','8044128745','Camp,Pune-411001','renewed'),
                                                ('113011','Sharad','Pathak','1992-08-11','8672453745','Baner,Pune-411045','renewed'),
                                                ('113012','Rose','Modi','1990-03-19','9011567457','Aundh,Pune-411007','renewed');"""

insert_employee = """INSERT INTO employee VALUES('881109','6978256300549911','ABCDE1234F','Ramesh','Sehgal','1984-10-03','9156722008','Sanghvi,PCMC-412213','Manager'),
                                                ('881281','7034112789543324','AAAA12364F','Uma','Pethe','1982-03-27','9134267549','Sanghvi,PCMC-412213','Receptionist'),
                                                ('881110','4562890035112984','ABCDE8911E','Ramona','Singh','1987-10-03','9344167283','Aundh Gaon,Pune-411007','Helper'),
                                                ('881213','5941150793668419','ABBCE2453G','Mahesh','Gandola','1980-05-22','8679002446','Khadki,Pune-411003','Manager'),
                                                ('881228','3897748921106834','ABBBB4433H','Raina','Sahai','1985-10-13','9456990031','Sanghvi,PCMC-412213','Helper'),
                                                ('881100','2886712308765273','ABCDE7622F','Yash','Mane','1990-09-16','8665900312','Khadki,Pune-411003','Helper');"""

insert_salary = """INSERT INTO salary VALUES('Manager','30000'),
                                            ('Receptionist','20000'),
                                            ('Helper','15000');"""

insert_outstanding = """INSERT INTO outstanding VALUES('113001','881281','B1001','100','0','Not returned','2020-10-23','2020-10-16'),
                                                      ('113001','881281','M1008','150','0','Not returned','2020-10-23','2020-10-16'),
                                                      ('113003','881281','B1011','100','0','returned','2020-10-7','2020-10-1'),
                                                      ('113010','881281','B1009','100','0','Not returned','2020-10-27','2020-10-20'),
                                                      ('113010','881281','B1006','100','0','Not returned','2020-10-27','2020-10-20'),
                                                      ('113010','881281','B1005','100','0','Not returned','2020-10-27','2020-10-20'),
                                                      ('113006','881281','M1001','150','0','Not returned','2020-10-29','2020-10-22'),
                                                      ('113002','881281','B1004','150','50','Not returned','2020-10-22','2020-10-15'),
                                                      ('113002','881281','M1010','150','50','Not returned','2020-10-07','2020-10-01'),
                                                      ('113007','881281','M1004','150','0','Not returned','2020-10-24','2020-10-17'),
                                                      ('113009','881281','M1009','100','0','Not returned','2020-10-22','2020-10-15');"""

insert_borrowed = """INSERT INTO borrowed VALUES('B1001','113001'),
                                                ('M1008','113001'),
                                                ('B1011','113003'),
                                                ('B1009','113010'),
                                                ('B1006','113010'),
                                                ('B1005','113010'),
                                                ('M1001','113006'),
                                                ('B1004','113002'),
                                                ('M1010','113002'),
                                                ('M1004','113007'),
                                                ('M1009','113009');"""




insert_product = """INSERT INTO product VALUES('B1001',"Book",'Borrowed'),
                                              ('B1002',"Book",'in_stock'),
                                              ('B1003',"Book",'in_stock'),
                                              ('B1004',"Book",'Borrowed'),
                                              ('B1005',"Book",'Borrowed'),
                                              ('B1006',"Book",'Borrowed'),
                                              ('B1007',"Book",'in_stock'),
                                              ('B1008',"Book",'in_stock'),
                                              ('B1009',"Book",'Borrowed'),
                                              ('B1010',"Book",'in_stock'),
                                              ('B1011',"Book",'Borrowed'),
                                              ('M1001',"CD",'Borrowed'),
                                              ('M1002',"CD",'in_stock'),
                                              ('M1003',"CD",'in_stock'),
                                              ('M1004',"CD",'Borrowed'),
                                              ('M1005',"CD",'in_stock'),
                                              ('M1006',"CD",'in_stock'),
                                              ('M1007',"CD",'in_stock'),
                                              ('M1008',"CD",'Borrowed'),
                                              ('M1009',"CD",'Borrowed'),
                                              ('M1010',"CD",'Borrowed'),
                                              ('M1011',"CD",'in_stock'),
                                              ('M1012',"CD",'in_stock');"""

insert_reservation = """INSERT INTO reservation VALUES('113008','M1006','2020-10-22','2020-11-01'),
                                                      ('113008','B10010','2020-10-21','2020-10-31'),
                                                      ('113012','M1003','2020-10-20','2020-11-10');"""

insert_media = """INSERT INTO media VALUES('M1001','Yeh Jawani Hai Deewani','2013','2h56m','Movie','200','Good','Romance Comedy'),
                                          ('M1002','Moana','2016','1h53m','Movie','150','Very Good','Adventure'),
                                          ('M1003','International Villager','2011','51m','Music','200','Fair','Rap'),
                                          ('M1004','Up All Night','2011','45m','Music','225','Good','Pop'),
                                          ('M1005','Titanic','1997','3h13m','Movie','200','Fair','Romance'),
                                          ('M1006','Mean Girls','2004','1h37m','Movie','200','Good','Comedy Teen'),
                                          ('M1007','Reputation','2017','55m','Music','200','Very good','Electropop R&B'),
                                          ('M1008','Frozen','2013','1h49m','Movie','200','Good','Children Fantasy'),
                                          ('M1009','the Chronicles Of Narnia','2005','2h30m','Movie','225','Good','Fantasy'),
                                          ('M1010','Slumdog Millionaire','2008','2h03m','Movie','200','Good','Indie Drama'),
                                          ('M1011','Jurassic World','2015','2h04m','Movie','200','Good','Action Science Thriller'),
                                          ('M1012','Jab We Met','2007','2h35m','Movie','200','Good','Romance');"""

insert_profit = """INSERT INTO profit VALUES('B1001','200','250'),
                                            ('B1002','150','200'),
                                            ('B1003','175','200'),
                                            ('B1004','200','300'),
                                            ('B1005','150','250'),
                                            ('B1006','100','200'),
                                            ('B1007','115','260'),
                                            ('B1008','175','275'),
                                            ('B1009','100','150'),
                                            ('B1010','115','260'),
                                            ('B1011','125','170'),
                                            ('M1001','200','250'),
                                            ('M1002','150','250'),
                                            ('M1003','200','225'),
                                            ('M1004','225','275'),
                                            ('M1005','200','225'),
                                            ('M1006','200','250'),
                                            ('M1007','200','300'),
                                            ('M1008','200','250'),
                                            ('M1009','225','275'),
                                            ('M1010','200','250'),
                                            ('M1011','200','250'),
                                            ('M1012','200','250');"""

insert_author = """INSERT INTO author VALUES('3001','Agatha','Christie'),
                                            ('3002','Louisa May','Alcott'),
                                            ('3003','Paula','Hawkins'),
                                            ('3004','Chetan','Bhagat'),
                                            ('3005','Roald','Dahl'),
                                            ('3006','Dan','Brown'),
                                            ('3007','Danielle','Steel'),
                                            ('3008','Jeff','Kinney'),
                                            ('3009','Amish','-');"""

insert_book = """INSERT INTO book VALUES('B1001','3001','And Then There Were None','2004','Collins Crime Club','Thriller Suspense','200','Fair'),
                                        ('B1002','3002','Little Women','2002','Roberts Brothers','Children Literature','150','Fair'),
                                        ('B1003','3001','Murder on the Orient Express','2001','Collins Crime Club','Murder Mystery','175','Bad'),
                                        ('B1004','3003','The Girl On The Train','2015','Doubleday','Psychological Fiction','200','Very good'),
                                        ('B1005','3004','Three Mistakes Of My Life','2008','Rupa Publications','Fiction','150','Good'),
                                        ('B1006','3005','The BFG','2010','Penguin Books','Children','100','Good'),
                                        ('B1007','3006','Deception Point','2002','Pocket Books','Mystery Thriller','115','Fair'),
                                        ('B1008','3007','Fall From Grace','2018','Random House Large Print','Romance','175','Very good'),
                                        ('B1009','3005','Charlie and the Chocolate Factory','2000','Penguin Books','Childeren','100','Fair'),
                                        ('B1010','3008','The Diary of a Wimpy Kid:Rodrick Rules','2013','publisher Harry N. Abrams, Inc.','Teen Diary','115','Good'),
                                        ('B1011','3009','The immortals of Meluha','2010','Westland Press','Mythology','125','Good');"""

insert_policies = """INSERT INTO policies VALUES('B1001','7 days','In high demand'),
                                                ('B1002','7 days','In low demand'),
                                                ('B1003','7 days','In demand'),
                                                ('B1004','7 days','In high demand'),
                                                ('B1005','7 days','In demand'),
                                                ('B1006','7 days','In high demand'),
                                                ('B1007','7 days','In low demand'),
                                                ('B1008','7 days','In low demand'),
                                                ('B1009','7 days','In demand'),
                                                ('B1010','7 days','In high demand'),
                                                ('B1011','7 days','In high demand'),
                                                ('M1001','7 days','In demand'),
                                                ('M1002','7 days','In high demand'),
                                                ('M1003','7 days','In low demand'),
                                                ('M1004','7 days','In demand'),
                                                ('M1005','7 days','In demand'),
                                                ('M1006','7 days','In demand'),
                                                ('M1007','7 days','In high demand'),
                                                ('M1008','7 days','In high demand'),
                                                ('M1009','7 days','In low demand'),
                                                ('M1010','7 days','In demand'),
                                                ('M1011','7 days','In high demand'),
                                                ('M1012','7 days','In demand');"""
