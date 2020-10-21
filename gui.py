from tkinter import *
from tkinter import font as tkFont
from PIL import ImageTk, Image

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
                EmpPage(window)

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

class LoadPage:
    def __init__(self, window):
        D = Canvas(window, height=608, width=400)

        def callback(event):
            global flag
            if 107 <= event.x <= 293 and 207 <= event.y <= 269:
                D.destroy()
                print("Starting game......")
                global players, numbers, role, names, player
                fptr = open("info.txt", "r")
                f1 = fptr.readlines()
                players_number = int(f1[0])
                ind = 1
                for _ in range(players_number):
                    names.append(f1[ind].strip("\n"))
                    ind += 1
                for _ in range(players_number):
                    numbers.append(f1[ind].strip("\n"))
                    ind += 1
                v = int(f1[ind].strip("\n"))
                ind += 1
                s = int(f1[ind].strip("\n"))
                count = 0
                for _ in range(v):
                    role.append("virus")
                for _ in range(s):
                    role.append("service")
                random.shuffle(role)
                # for a crazy game:
                # jobs = [0, 0, 0, 0, 0, 0]
                if players_number > 5:
                    jobs = [0, 1, 2, 3, 4, 5]
                else:
                    jobs = [1, 2, 3, 4, 5]
                hidden = [6, 7, 8, 9, 10]
                random.shuffle(jobs)
                while jobs[0] == 3 or jobs[1] == 3:
                    random.shuffle(jobs)
                random.shuffle(hidden)
                index = 0
                extra = 0
                # print(players_number)
                # print(role)
                for _ in range(players_number):
                    name = names.pop()
                    number = numbers.pop()
                    if _ > 5:
                        job = jobs[extra]
                        extra += 1
                    else:
                        job = jobs[_]
                    if job == 0:
                        job = hidden[0]
                        random.shuffle(hidden)
                    players.append(player(name, number, role.pop(), job))
                    index += 1
                random.shuffle(players)
                viruses = []
                for player in players:
                    if player.role == "virus":
                        viruses.append(player)
                for player in players:
                    if player.role == "service":
                        message = (
                            "Welcome to Deception!\n You are working for "
                            + player.role
                            + ".\n Your mission is to find all the V.I.R.U.S Agents."
                        )
                        send_info(player.number, message)
                        print(player.name,player.role,file=open("stats.txt","a+"))
                    else:
                        message = (
                            "Welcome to Deception!\n You are working for "
                            + player.role
                            + ".\n Your team is:\n"
                        )
                        for v in viruses:
                            message += v.name
                            message += "\n"
                        message += "All the best!"
                        send_info(player.number, message)
                        print(player.name,player.role,file=open("stats.txt","a+"))
                DATABASE_URL = 'postgres://xtnoshkjrfaipj:609d5dfaf6c3af5a7fd16a87c2fec1591c27eab51cc93a61126b875bc5e3e8b5@ec2-34-192-122-0.compute-1.amazonaws.com:5432/der5779vnluga7'
                conn = psycopg2.connect(DATABASE_URL, sslmode='require')
                cur=conn.cursor()
                cur.execute("""DROP TABLE IF EXISTS votes""")
                cur.execute("""CREATE TABLE votes (
                            vote VARCHAR(255) NOT NULL
                        )""")
                cur.close()
                conn.commit()
                conn.close()
                GamePage(window)

        D.bind("<Button-1>", callback)
        background = PhotoImage(file="images/names.png")
        D.create_image(0, 0, image=background, anchor="nw")
        D.pack()
        window.mainloop()






if __name__ == "__main__":
    window = Tk()
    # p1 = PhotoImage(file="images/icon.gif")
    # window.iconphoto(True, p1)
    StartPage(window)
