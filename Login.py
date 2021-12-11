from tkinter import *
from PIL import ImageTk
import tkinter.messagebox
from tkinter import ttk
import mysql.connector as mysql



#connecting to the database
mydb = mysql.connect(
host="34.121.245.150",
user='root',
password="Mpgradney2017",
database = "streaming")


cur = mydb.cursor()
print("Connection made...")


cur.execute('''CREATE TABLE if not exists user (
id INT NOT NULL,
username VARCHAR(30) NOT NULL,
password TEXT NOT NULL,
country TEXT NOT NULL,
netflix BIT(1),
hulu BIT(1),
disney BIT(1)

)''')

#create login class ClassName(object):
class login:
    def __init__(self,root):
        self.root = Tk()
        self.root.title("Login and registration system for Apps")
        self.root.geometry("1500x700+0+0")
        self.create_elements()
        self.root.mainloop()

    def create_elements(self):
        self.username = Label(self.root, text="Username:", font=('Verdana', 14, 'bold'))
        self.username.place(x=50, y=50)

        self.entry_username = Entry(self.root, font=('Verdana', 14))
        self.entry_username.place(x=160, y=50)

        self.password = Label(self.root, text="Password:", font=('Verdana', 14, 'bold'))
        self.password.place(x=50, y=90)

        self.entry_password = Entry(self.root, font=('Verdana', 14))
        self.entry_password.place(x=160, y=90)

        self.login_button = ttk.Button(self.root, text="Login", height=2, width=10, command=self.login_user)
        self.login_button.place(x=50, y=160)

        self.new_user = Label(self.root, text="New User?", font=('Verdana', 10, 'bold'))
        self.new_user.place(x=150, y=140)

        self.register_button = ttk.Button(self.root, text="Sign Up", height=2, width=10, command=self.destroy_login)
        self.register_button.place(x=150, y=160)

    def destroy_login(self):
        self.root.destroy()
        register = Register()

    def login_user(self):
        username = self.entry_username.get()
        userpassword = self.entry_password.get()

        if(username == "" or userpassword == ""):
            showinfo("Oops!","Your information can't be empty!")
            return

        mydb = mysql.connect(
        host="34.121.245.150",
        user='root',
        password="Mpgradney2017",
        database = "streaming")


        mycursor = mydb.cursor()
        sql = "select user, pass from users where user=%s and pass=%s"
        val = (username, userpassword)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()
        self.entry_username.delete(0, END)
        self.entry_password.delete(0, END)
        if result:
            showinfo("Success","You're logged in!")
        else:
            showinfo("Failed","You've entered wrong credentials!")

class Register():
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1500x700")
        self.root.title("Register Window")
        self.create_elements()
        self.root.mainloop()

    def create_elements(self):

        self.username = Label(self.root, text="Username:", font=('Verdana', 14, 'bold'))
        self.username.place(x=50, y=50)

        self.entry_username = Entry(self.root, font=('Verdana', 14))
        self.entry_username.place(x=160, y=50)

        self.password = Label(self.root, text="Password:", font=('Verdana', 14, 'bold'))
        self.password.place(x=50, y=90)

        self.entry_password = Entry(self.root, font=('Verdana', 14))
        self.entry_password.place(x=160, y=90)

        self.name = Label(self.root, text="Name:", font=('Verdana', 14, 'bold'))
        self.name.place(x=50, y=130)

        self.entry_name = Entry(self.root, font=('Verdana', 14))
        self.entry_name.place(x=160, y=130)

        self.register_button = ttk.Button(self.root, text="Sign Up", height=2, width=10, command=self.register_user)
        self.register_button.place(x=50, y=180)

        self.existing_user = Label(self.root, text="Existing User?", font=('Verdana', 10, 'bold'))
        self.existing_user.place(x=150, y=160)

        self.login_button = ttk.Button(self.root, text="Login", height=2, width=10, command=self.destroy_register)
        self.login_button.place(x=150, y=180)

    def destroy_register(self):
        self.root.destroy()
        login = Login()

    def register_user(self):
        username = self.entry_username.get()
        userpassword = self.entry_password.get()
        name = self.entry_name.get()

        if(username == "" or userpassword == "" or name == ""):
            showinfo("Oops!","Your information can't be empty!")
            return

        mydb = mysql.connect(
        host="34.121.245.150",
        user='root',
        password="Mpgradney2017",
        database = "streaming")

        mycursor = mydb.cursor()

        mycursor.execute("select count(*) from users")
        result = mycursor.fetchone()
        old_count = result[0]

        sql = "INSERT INTO users (user, pass, name) VALUES (%s, %s, %s)"
        val = (username, userpassword, name)
        mycursor.execute(sql, val)
        mydb.commit()

        mycursor.execute("select count(*) from users")
        result = mycursor.fetchone()
        new_count = result[0]

        self.entry_username.delete(0, END)
        self.entry_password.delete(0, END)
        self.entry_name.delete(0, END)

        if(old_count + 1 == new_count):
            showinfo("Success","Your information is saved successfully!")
        else:
            showinfo("Failed","Your information couldn't save successfully!")

if __name__ == '__main__':
    login = login()
