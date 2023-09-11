import tkinter as tk
from tkinter import Label, Entry, IntVar, Radiobutton, StringVar, OptionMenu, Button
import smtplib

view = tk.Tk()
view.title("Login Page")
view.geometry('580x680')



view.configure(bg='#333333')


def login():
    username = entry_username.get()
    password = entry_password.get()
    try:
        # Connect to Gmail's SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Enable TLS encryption

        
        print("Login successful!")

        
        server.quit()

    except Exception as e:
        # If login fails, print an error message
        print("Login failed. Error:", str(e))

 
    

def register():
    
    
    base = tk.Tk()
    base.geometry("400x500")
    base.title("Registration Form")

    lb1 = Label(base, text="Enter Name", width=10, font=("arial", 12))
    lb1.place(x=20, y=120)
    en1 = Entry(base)
    en1.place(x=200, y=120)

    lb3 = Label(base, text="Enter Email", width=10, font=("arial", 12))
    lb3.place(x=19, y=160)
    en3 = Entry(base)
    en3.place(x=200, y=160)

    lb4 = Label(base, text="Contact Number", width=13, font=("arial", 12))
    lb4.place(x=19, y=200)
    en4 = Entry(base)
    en4.place(x=200, y=200)

    lb5 = Label(base, text="Select Gender", width=15, font=("arial", 12))
    lb5.place(x=5, y=240)
    vars = IntVar()
    Radiobutton(base, text="Male", padx=5, variable=vars, value=1).place(x=180, y=240)
    Radiobutton(base, text="Female", padx=10, variable=vars, value=2).place(x=240, y=240)
    Radiobutton(base, text="others", padx=15, variable=vars, value=3).place(x=310, y=240)

    list_of_cntry = ("United States", "India", "Nepal", "Bangladesh")
    cv = StringVar()
    drplist = OptionMenu(base, cv, *list_of_cntry)
    drplist.config(width=15)
    cv.set("United States")
    lb2 = Label(base, text="Select Country", width=13, font=("arial", 12))
    lb2.place(x=14, y=280)
    drplist.place(x=200, y=275)

    lb6 = Label(base, text="Enter Password", width=13, font=("arial", 12))
    lb6.place(x=19, y=320)
    en6 = Entry(base, show='*')
    en6.place(x=200, y=320)

    lb7 = Label(base, text="Re-Enter Password", width=15, font=("arial", 12))
    lb7.place(x=21, y=360)
    en7 = Entry(base, show='*')
    en7.place(x=200, y=360)

    Button(base, text="Register", width=10).place(x=200, y=400)

# Create the main window
'''
root = tk.Tk()
root.title("Login Page")

# Set background color
root.configure(bg="Black")
'''
# Create a frame to center the login system
frame = tk.Frame(view, bg='#012200', width=420, height=372)

frame.place(x=5,y=0)

# Center the frame using pack
frame.pack(fill="both", expand=True)

# Create a sub-frame inside the main frame
sub_frame = tk.Frame(frame, bg="#355C7D", padx=40, pady=40)
sub_frame.grid(row=4, columnspan=3, padx=10, pady=10, sticky="nsew")
view.grid_columnconfigure(0, weight=1)
view.grid_rowconfigure(0, weight=1)

# Create labels and entry widgets within the sub-frame
label_username = tk.Label(sub_frame, text="Email or phone", bg="white")
label_password = tk.Label(sub_frame, text="Password", bg="white")
#label_questionaire = tk.Label(sub_frame, text="Not Account? Create one!")
entry_username = tk.Entry(sub_frame)
entry_password = tk.Entry(sub_frame, show="*")  # Show asterisks for password

# Create login and register buttons within the sub-frame
login_button = tk.Button(sub_frame, text="Login", command=login)
register_button = tk.Button(sub_frame, text="Register", command=register)

# Place widgets in the sub-frame
label_username.grid(row=0, column=0, padx=20, pady=10, sticky="w")
entry_username.grid(row=0, column=1, padx=20, pady=10)
label_password.grid(row=1, column=0, padx=20, pady=10, sticky="w")
entry_password.grid(row=1, column=1, padx=20, pady=10)
login_button.grid(row=2, column=0, padx=10, pady=10, sticky="w")
register_button.grid(row=2, column=1, padx=10, pady=10, sticky="e")

# Start the main loop
view.mainloop()


