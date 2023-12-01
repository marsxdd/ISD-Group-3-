#Customer Register page
import tkinter as tk
from tkinter import messagebox
#messagebox gives pop ups!(?)

#main window
window = tk.Tk()
window.title("SwiftRide - Customer Register")
window.geometry("300x200")
window.config(bg="Orange")

#functionality
def register():
    first_name = fname_entry.get()
    last_name = lname_entry.get()
    address = address_entry.get()
    email = email_entry.get()
    phone_number = pnumber_entry.get()
    payment_method = payment_method_entry.get()
    password = password_entry.get()
    confirm_password = password_con_entry.get()

#Password functionality  
    if password != confirm_password: #!= Comparison op
        messagebox.showerror("Error", "Passwords do not match! Try Again")
    else:
        messagebox.showinfo("Registration", "Registration successful! :D")



# First Name
fname = tk.Label(text="First Name:", bg="orange")
fname.pack()
fname_entry = tk.Entry()
fname_entry.pack()

# Last Name
lname = tk.Label(text="Last Name:", bg="orange")
lname.pack()
lname_entry = tk.Entry()
lname_entry.pack()

# Address
address = tk.Label(text="Address:", bg="orange")
address.pack()
address_entry = tk.Entry()
address_entry.pack()

#Email
email = tk.Label(text="Email:", bg="orange")
email.pack()
email_entry = tk.Entry()
email_entry.pack()

#Phone Number
pnumber = tk.Label(text="Phone Number:", bg="orange")
pnumber.pack()
pnumber_entry = tk.Entry()
pnumber_entry.pack()

#Payment Method
payment_method = tk.Label(text="Payment Method:", bg="orange")
payment_method.pack()
payment_method_entry = tk.Entry()
payment_method_entry.pack()

#Password
password = tk.Label(text="Password:", bg="orange")
password.pack()
password_entry = tk.Entry(show="*")
password_entry.pack()

#Confirm Password
password_confirm = tk.Label(text="Confirm Password:", bg="orange")
password_confirm.pack()
password_con_entry = tk.Entry(show="*")
password_con_entry.pack()

#Register Button
register_btn = tk.Button(text="Register", command=register, activebackground="green")
register_btn.pack()

# Already have an account?
login = tk.Label(text="Already have an account?" , bg="orange")
login.pack()
login_arrows = tk.Label(text="↓↓↓" , bg="orange")
login_arrows.pack()
"""LOG IN BUTTON HERE"""

"""
↑↑↑↑↑↑↑↑Need to make button up here to get back to login page(?)↑↑↑↑
"""

#Dont forget this
window.mainloop()
