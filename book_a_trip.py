from tkinter import *
import subprocess

#main window
window = Tk()
window.title("SwiftRide - Book a Trip")
window.geometry("300x200")
window.config(bg="Orange")

def confirm_trip():
    booking_id = booking_id_entry.get()
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    destination = destination_entry.get()
    pickup_address = pickup_address_entry.get()
    pickup_time = pickup_time_entry.get()
    booking_date = booking_date_entry.get()
    payment_method = payment_method_entry.get()

#booking id
booking_id = Label(text="Booking ID:", bg="orange")
booking_id.pack()
booking_id_entry = Entry()
booking_id_entry.pack()

#first name
first_name = Label(text="First Name:", bg="orange")
first_name.pack()
first_name_entry = Entry()
first_name_entry.pack()

#last name
last_name = Label(text="Last Name:", bg="orange")
last_name.pack()
last_name_entry = Entry()
last_name_entry.pack()

#destination
destination = Label(text="Destination:", bg="orange")
destination.pack()
destination_entry = Entry()
destination_entry.pack()

#pick up ad
pickup_address = Label(text="Pickup Address:", bg="orange")
pickup_address.pack()
pickup_address_entry = Entry()
pickup_address_entry.pack()

#pick up time
pickup_time = Label(text="Pickup Time:", bg="orange")
pickup_time.pack()
pickup_time_entry = Entry()
pickup_time_entry.pack()

#date
booking_date = Label(text="Booking Date:", bg="orange")
booking_date.pack()
booking_date_entry = Entry()
booking_date_entry.pack()

#payment
payment_method = Label(text="Payment Method:")
payment_method.pack()
payment_method_entry = Entry()
payment_method_entry.pack()

#confir
confirm_btn = Button(text="Confirm Trip", command=confirm_trip)
confirm_btn.pack()

#view booking
view_booking_btn = Button(text="View Booking")
view_booking_btn.pack()

#back btn
def open_file():
    subprocess.Popen(['python', 'user_selection_login.py'])

back_btn = Button(text="Back", command=open_file)
back_btn.pack(side= BOTTOM, pady=5)


#da loop
window.mainloop()
