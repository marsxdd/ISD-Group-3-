#Driver Register page
#Basically Customer Register page witha tweak
import tkinter as tk
from tkinter import messagebox
import subprocess
#messagebox gives pop ups!(?)

#main window
window = tk.Tk()
window.title("SwiftRide - Driver Register")
window.geometry("300x300")
window.config(bg="Orange")

#functionality
def register():
    first_name = fname_entry.get()
    last_name = lname_entry.get()
    address = address_entry.get()
    email = email_entry.get()
    phone_number = pnumber_entry.get()
    vehicle_number = vehicle_number_entry.get()
    password = password_entry.get()
    confirm_password = password_con_entry.get()

#password confir
    if password != confirm_password: #!= Comparison op
        messagebox.showerror(title="Error!")
    else:
        messagebox.showinfo(title="Success!")



#first name
fname = tk.Label(text="First Name:", bg="orange")
fname.pack()
fname_entry = tk.Entry()
fname_entry.pack()

#last name
lname = tk.Label(text="Last Name:", bg="orange")
lname.pack()
lname_entry = tk.Entry()
lname_entry.pack()

#ddress
address = tk.Label(text="Address:", bg="orange")
address.pack()
address_entry = tk.Entry()
address_entry.pack()

#email
email = tk.Label(text="Email:", bg="orange")
email.pack()
email_entry = tk.Entry()
email_entry.pack()

#phone number
pnumber = tk.Label(text="Phone Number:", bg="orange")
pnumber.pack()
pnumber_entry = tk.Entry()
pnumber_entry.pack()

#vehicle number
vehicle_number = tk.Label(text="Vehicle Registration Number:", bg="orange")
vehicle_number.pack()
vehicle_number_entry = tk.Entry()
vehicle_number_entry.pack()

#password
password = tk.Label(text="Password:", bg="orange")
password.pack()
password_entry = tk.Entry(show="*")
password_entry.pack()

#password confi
password_confirm = tk.Label(text="Confirm Password:", bg="orange")
password_confirm.pack()
password_con_entry = tk.Entry(show="*")
password_con_entry.pack()

#regi btn
register_btn = tk.Button(text="Register", command=register, activebackground="green")
register_btn.pack()

#haveanacc
login = tk.Label(text="Already have an account?" , bg="orange")
login.pack()
login_arrows = tk.Label(text="↓↓↓" , bg="orange")
login_arrows.pack()

#open another .py file;to connect
def open_file():
    subprocess.Popen(['python', 'login_page.py'])

login_btn = tk.Button(text="login", command=open_file)
login_btn.pack()

#back btn
def open_file():
    subprocess.Popen(['python', 'user_selection_register.py'])

back_btn = tk.Button(text="Back", command=open_file)
back_btn.pack(side= tk.BOTTOM, pady=5)

#Dont forget this
window.mainloop()
