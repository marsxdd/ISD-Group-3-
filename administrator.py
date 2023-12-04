#Admin Page after log in
import tkinter as tk
import subprocess

#main window
window = tk.Tk()
window.title("SwiftRide - Administrator")
window.geometry("300x200")
window.config(bg="Orange")

#buttons
driver_btn = tk.Button(text="Customer Data", activebackground="green")
driver_btn.pack(pady=4)

customer_btn = tk.Button(text="Booking Data", activebackground="green")
customer_btn.pack(pady=4)

booking_btn = tk.Button(text="Driver Data", activebackground="green")
booking_btn.pack(pady=4)

logout_btn = tk.Button(text="Log out", activebackground="red")
logout_btn.pack(side= tk.BOTTOM, pady=10)

#back btn
def open_file():
    subprocess.Popen(['python', 'user_selection_login.py'])

back_btn = tk.Button(text="Back", command=open_file)
back_btn.pack(side= tk.BOTTOM, pady=4)

#LOOP
window.mainloop()
