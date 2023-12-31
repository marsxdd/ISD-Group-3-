#main.py
from tkinter import *
import subprocess
from tkinter import font

#main window/logo
window = Tk()
window.title('SwiftRide')
img = PhotoImage(file="SwiftRide.png")
window.geometry("300x200")
Label(image=img).pack()
window.config(bg="orange")

#bar ontop
frame = Frame(window)
frame.pack()

mainmenu = Menu(frame)
def open_file():
    subprocess.Popen(['python', 'login_page.py'])
mainmenu.add_command(label="Login", command=open_file)


def open_file():
    subprocess.Popen(['python', 'user_selection_register.py'])
mainmenu.add_command(label="Register", command=open_file)


mainmenu.add_command(label="Exit", command=window.destroy)

window.config(menu=mainmenu)

#custom font
custom_font = font.Font(family="Freestyle Script", size=24, weight="bold", slant="italic")
label = Label(text="Welcome to SwiftRide!", font=custom_font, bg="orange")
label.pack()

comp = Label(text="Brought to you by TransportTech Solution", font="Arial", bg="yellow")
comp.pack()

# Run the tkinter event loop
window.mainloop()
