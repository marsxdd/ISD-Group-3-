#User selection - register
from tkinter import *
import tkinter as tk
import subprocess

# main window
window = Tk()
window.title("SwiftRide - Register Selection")
window.geometry("300x200")
window.config(bg="Orange")

#Label
label = Label(text="Who's Registering?",bg="orange")
label.pack()

#Button funct
#CUSTOMER
def open_file():
    subprocess.Popen(['python', 'customerregister.py'])

login3_btn = tk.Button(text="Customer", command=open_file)
login3_btn.pack()

#DRIVER
def open_file():
    subprocess.Popen(['python', 'driverregister.py'])

login4_btn = tk.Button(text="Driver", command=open_file)
login4_btn.pack()

#back
def open_file():
    subprocess.Popen(['python', 'user_selection_login.py'])

back_btn = tk.Button(text="Back", command=open_file)
back_btn.pack(side= tk.BOTTOM, pady=5)



#IMPORTANT THING
window.mainloop()
