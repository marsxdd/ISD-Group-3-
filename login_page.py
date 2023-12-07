#Need to make a 'cover' page
#login page
from tkinter import *
from tkinter import StringVar, Entry
import subprocess

#main window
window = Tk()
window.title("SwiftRide - Login")
window.geometry("300x200")
window.config(bg="Orange")


#login info
def login():
    username = username_entry.get()
    password = password_entry.get()



#username
username = Label(text="Username:", bg="orange")
username.pack()
username_var = StringVar()
username_entry = Entry(textvariable=username_var)
username_entry.pack()

#password
password = Label(text="Password:", bg="orange")
password.pack()
password_var = StringVar()
password_entry = Entry(textvariable=password_var, show="*")
password_entry.pack()


#Button funct
#Clicking Login
def open_file():
    subprocess.Popen(['python', 'user_selection_login.py'])

login_btn = Button(text="Login", command=open_file)
login_btn.pack()

#clicking register
def open_file():
    subprocess.Popen(['python', 'user_selection_register.py'])

regi_btn = Button(text="Register", command=open_file)
regi_btn.pack()

#back btn
def open_file():
    subprocess.Popen(['python', 'homepage.py'])

back_btn = Button(text="Back", command=open_file)
back_btn.pack(side=BOTTOM, pady=5)

# Makes it all work (VERY IMPORTANT)
window.mainloop()
