# Customer Register page
import tkinter as tk
from tkinter import messagebox
# messagebox gives pop ups!(?)
import subprocess


# main window
window = tk.Tk()
window.title("SwiftRide - Customer Register")
window.geometry("300x300")
window.config(bg="Orange")


# functionality
def register():
    first_name = fname_entry.get()
    last_name = lname_entry.get()
    address = address_entry.get()
    email = email_entry.get()
    phone_number = pnumber_entry.get()
    payment_method = payment_method_entry.get()
    password = password_entry.get()
    confirm_password = password_con_entry.get()

#database connection
        try:
        conn= connect('swiftride.db')
        conn.cursor()
        conn.execute(f'INSERT INTO Customer(CustomerID, FirstName, LastName, Email, Password, Address, PhoneNumber, Paymentmethod)'
                         f'VALUES (?,?,?,?,?,?,?,?);',(1, first_name, last_name, email, password, address, phone_number, payment_method)).
        conn.commit()
    except Exception as e:
        raise e
    finally:
        conn.close()
        
    #password func
    if password != confirm_password:  # != Comparison op
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

#address
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

#payment
payment_method = tk.Label(text="Payment Method:", bg="orange")
payment_method.pack()
payment_method_entry = tk.Entry()
payment_method_entry.pack()

#password
password = tk.Label(text="Password:", bg="orange")
password.pack()
password_entry = tk.Entry(show="*")
password_entry.pack()

#password
password_confirm = tk.Label(text="Confirm Password:", bg="orange")
password_confirm.pack()
password_con_entry = tk.Entry(show="*")
password_con_entry.pack()

#egibtn
register_btn = tk.Button(text="Register", command=register, activebackground="green")
register_btn.pack()

#haveacc
login = tk.Label(text="Already have an account?", bg="orange")
login.pack()
login_arrows = tk.Label(text="↓↓↓", bg="orange")
login_arrows.pack()

#login btn
def open_file():
    subprocess.Popen(['python', 'login_page.py'])
login_btn = tk.Button(text="Login", command=open_file)
login_btn.pack()

#back btn
def open_file():
    subprocess.Popen(['python', 'user_selection_register.py'])

back_btn = tk.Button(text="Back", command=open_file)
back_btn.pack(side= tk.BOTTOM, pady=5)

# Dont forget this
window.mainloop()
