#Login Page
from tkinter import *


#main window
window = Tk()
window.title("SwiftRide")
window.geometry("300x200")
window.config(bg="Orange")

#gets login info by defining login and .get
def login():
    username = username_entry.get()
    password = password_entry.get()
  

  
#admin sign in/ '==' is a comparison (CASE SENSITIVE)
    if username == "admin" and password == "password":
        login_label.config(text="Login Successful!", fg="green")

    else:
        login_label.config(text="Login Failed! Please Register!", fg="red")





# entries for username and password
#Username
username = Label(text="Username:", bg="orange")
username.pack()
username_entry = Entry()
username_entry.pack()

#Password
password = Label(text="Password:", bg="orange")
password.pack()
password_entry = Entry(show="*")
password_entry.pack()

"""
#Role selection btn or field
role_btn = Button(text="Customer")
role_btn.pack()
role_btn2 = Button(text="Admin")
role_btn2.pack()
role_btn3 = Button(text="Driver")
role_btn3.pack()
Needs to be formatted next to each other i dont know how to :(
"""


# Log in button
login_btn = Button(text="Login", command=login)
login_btn.pack()

"""
#Register btn
register_btn = Button(text="Register", command=register)
register_btn.pack()
"""

# Log in status
login_label = Label(window, text="", bg="orange")
login_label.pack()

# Makes it all work (VERY IMPORTANT)
window.mainloop()
