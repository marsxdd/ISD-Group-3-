#driver main page
#requires attention
from tkinter import *
from tkinter import messagebox
import subprocess

#main window
window = Tk()
window.title("SwiftRide - View Trips")
window.geometry("300x200")
window.config(bg="Orange")

# Function to search for a booking by ID
def search_booking():
    booking_id = search_entry.get()
    #search for id in database?
    # display details when found

#cancel trip
def cancel_trip():
    booking_id = cancel_entry.get()
    #check if the booking ID exists in database
    #when found cancel the trip and remove the booking



#booking id
booking_id = Label(text="Booking ID:", bg="orange")
booking_id.pack()
booking_id_value = StringVar()
booking_id_entry = Entry(textvariable=booking_id_value, state='readonly')
booking_id_entry.pack()

generate_btn = Button(text="Generate ID")
generate_btn.pack()

#custom info
table_frame = Frame(bg="yellow")
table_frame.pack()

#table attempt
customer = Label(table_frame, text="Customer Name", bg="red")
customer.grid(row=0, column=0, padx=10, pady=5)

destination = Label(table_frame, text="Destination", bg="red")
destination.grid(row=0, column=1, padx=10, pady=5)

pickup_address = Label(table_frame, text="Pickup Address", bg="red")
pickup_address.grid(row=0, column=2, padx=10, pady=5)

#search for id
search_frame = Frame(bg="yellow")
search_frame.pack()

search = Label(search_frame, text="Search by Booking ID:", bg="red")
search.grid(row=0, column=0, padx=10, pady=5)

search_entry = Entry(search_frame)
search_entry.grid(row=0, column=1, padx=10, pady=5)

search_btn = Button(search_frame, text="Search", command=search_booking)
search_btn.grid(row=0, column=2, padx=10, pady=5)

#cancel trip
cancel_frame = Frame(bg="yellow")
cancel_frame.pack()

cancel = Label(cancel_frame, text="Cancel Trip (Enter Booking ID):", bg="red")
cancel.grid(row=0, column=0, padx=10, pady=5)

cancel_entry = Entry(cancel_frame)
cancel_entry.grid(row=0, column=1, padx=10, pady=5)

cancel_btn = Button(cancel_frame, text="Cancel", command=cancel_trip)
cancel_btn.grid(row=0, column=2, padx=10, pady=5)

#back
def open_file():
    subprocess.Popen(['python', 'user_selection_login.py'])

back_btn = Button(text="Back", command=open_file)
back_btn.pack(side= BOTTOM, pady=5)

#important
window.mainloop() 
