from tkinter import *
import subprocess

# main window
window = Tk()
window.title("SwiftRide - User Selection")
window.geometry("300x200")
window.config(bg="Orange")

#Label
label = Label(text="Who's Logging in?",bg="orange")
label.pack()

#Button funct
#admin
def open_file():
    subprocess.Popen(['python', 'administrator.py'])

admin_login_btn = Button(text="Admin", command=open_file, activebackground="red")
admin_login_btn.pack()

#customer
def open_file():
    subprocess.Popen(['python', 'book_a_trip.py'])
customer_btn = Button(text="Customer", command=open_file)
customer_btn.pack()

#driver
def open_file():
    subprocess.Popen(['python', 'view_trips.py'])
driver_btn = Button(text="Driver", command=open_file)
driver_btn.pack()

#back btn
def open_file():
    subprocess.Popen(['python', 'login_page.py'])

back_btn = Button(text="Back", command=open_file)
back_btn.pack(side= BOTTOM, pady=5)

#IMPORTANT!
window.mainloop()
