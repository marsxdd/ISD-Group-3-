import tkinter as tk
import random
import subprocess
def confirm_trip():
    first_name = first_name_entry.get()
    booking_id = random.randint(1000, 9999)  # Randomized booking ID
    last_name = last_name_entry.get()
    destination = destination_entry.get()
    pickup_address = pickup_address_entry.get()
    pickup_time = pickup_time_entry.get()
    booking_date = booking_date_entry.get()
    payment_method = payment_method_entry.get()

#receipt
    receipt_window = tk.Toplevel(bg="orange")

#booking information
    booking_id_label = tk.Label(receipt_window, bg="orange", text="Booking ID: " + str(booking_id))
    booking_id_label.pack()

    name_label = tk.Label(receipt_window, bg="orange", text="Name: " + first_name + " " + last_name)
    name_label.pack()

    destination_label = tk.Label(receipt_window, bg="orange", text="Destination: " + destination)
    destination_label.pack()

    pickup_label = tk.Label(receipt_window, bg="orange", text="Pick-up Address: " + pickup_address)
    pickup_label.pack()

    pickup_time_label = tk.Label(receipt_window, bg="orange", text="Pick-up Time: " + pickup_time)
    pickup_time_label.pack()

    booking_date_label = tk.Label(receipt_window, bg="orange", text="Booking Date: " + booking_date)
    booking_date_label.pack()

    payment_method_label = tk.Label(receipt_window, bg="orange", text="Payment Method: " + payment_method)
    payment_method_label.pack()

#btn to close window
    close_button = tk.Button(receipt_window, text="Close", command=receipt_window.destroy)
    close_button.pack()

#main window
window = tk.Tk()
window.title("SwiftRide - Book a Trip")
window.geometry("300x200")
window.config(bg="Orange")

#entry fields for booking information
first_name_label = tk.Label(text="First Name:", bg="orange")
first_name_label.pack()
first_name_entry = tk.Entry()
first_name_entry.pack()

last_name_label = tk.Label(text="Last Name:", bg="orange")
last_name_label.pack()

last_name_entry = tk.Entry()
last_name_entry.pack()

destination_label = tk.Label(text="Destination:", bg="orange")
destination_label.pack()
destination_entry = tk.Entry()
destination_entry.pack()

pickup_address_label = tk.Label(text="Pick-up Address:", bg="orange")
pickup_address_label.pack()
pickup_address_entry = tk.Entry()
pickup_address_entry.pack()

pickup_time_label = tk.Label(text="Pick-up Time:", bg="orange")
pickup_time_label.pack()
pickup_time_entry = tk.Entry()
pickup_time_entry.pack()

booking_date_label = tk.Label(text="Booking Date:", bg="orange")
booking_date_label.pack()
booking_date_entry = tk.Entry()
booking_date_entry.pack()

payment_method_label = tk.Label(text="Payment Method:", bg="orange")
payment_method_label.pack()
payment_method_entry = tk.Entry()
payment_method_entry.pack()

#confirm the trip
confirm_button = tk.Button(text="Confirm Trip", command=confirm_trip)
confirm_button.pack()

def open_file():
    subprocess.Popen(['python', 'user_selection_login.py'])

back_btn = tk.Button(text="Back", command=open_file)
back_btn.pack(pady=5)


#IMPORTANT
window.mainloop()
