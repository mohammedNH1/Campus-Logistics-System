import tkinter as tk
from tkinter import ttk, messagebox
from DataBase import database 
import re
import hashlib
from PIL import Image, ImageTk
import pyotp
import qrcode
from io import BytesIO

user_id = ""
# Submit button action
def sign_up():
    def login(): 
        root.destroy()
        log_in()  # log_in window
    def input_valid():
        
        Fname = entry_first_name.get()
        Lname = entry_last_name.get()
        email = entry_email.get()
        number = entry_phone_number.get()
        id = entry_id.get()
        password = entry_password.get()
        type = user_type_var.get()

        valid_phone_number = re.search("^(05)" ,number)
        if type == 'Student':
            valid_ID = len(id) == 10
        else:
            valid_ID = len(id) == 6        
        valid_pass = len(password) >= 6
        valid_email = re.search("(@ksu.edu.sa)$", email)
        if not valid_phone_number:
             messagebox.showinfo("Phone number invalid", "Number must start with 05")
             print("invalid phone number 05")
        elif not valid_ID:
             if type == "Student":
                 messagebox.showinfo("ID invalid", "ID must be 10 digits")
             else:
                 messagebox.showinfo("ID invalid", "ID must be 6 digits")
             print("invalid digits ID")
        elif not valid_pass:
             messagebox.showinfo("Password invalid", "password must be atleast 6 digits")
             print("invalid password wrong ")
        elif not valid_email:
             messagebox.showinfo("Email invalid", "Email must ends with @ksu.edu.sa ")
             print("invalid email")
        else:
            password = hashlib.sha256(password.encode()).hexdigest()
            DB = database()
            DB.insertUser(id , Fname , Lname , type , email , number , password )
            root.destroy()
            flag = OTP()     # window
            if flag:
                if type == "Courier":
                    courier_window()
                else:
                    user_window()

   
    # Toggle switch style update
    def toggle_switch():
        selected = user_type_var.get()

        # Check and update the appearance of the toggles based on selection
        if selected == "Student":
            toggle_Student.config(bg="#43a047", fg="white",)
            toggle_faculty.config(bg="#263238", fg="white",)
            toggle_Courier.config(bg="#263238", fg="white",)
        elif selected == "Faculty":
            toggle_faculty.config(bg="#43a047", fg="white",)
            toggle_Student.config(bg="#263238", fg="white",)
            toggle_Courier.config(bg="#263238", fg="white",)
        elif selected == "Courier":
            toggle_Courier.config(bg="#43a047", fg="white",)
            toggle_Student.config(bg="#263238", fg="white",)
            toggle_faculty.config(bg="#263238", fg="white",)

    # Create main application window
    root = tk.Tk()
    root.title("Sign Up")  # Changed to "Sign Up"
    root.configure(bg="#37474f")  # Set a masculine background color

    # Center window on screen
    window_width = 700
    window_height = 700
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    position_top = int(screen_height / 2 - window_height / 2)
    position_left = int(screen_width / 2 - window_width / 2)

    root.geometry(f'{window_width}x{window_height}+{position_left}+{position_top - 50}')

    # Create a frame for form fields with bold, masculine colors
    frame = tk.Frame(root, bg="#263238", padx=20, pady=20, relief=tk.GROOVE, borderwidth=3)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Form Title
    title_label = tk.Label(root, text="Sign Up", font=("Arial", 20, "bold"), bg="#37474f", fg="#64b5f6")
    title_label.place(relx=0.5, rely=0.1, anchor="center")

    # First Name
    tk.Label(frame, text="First Name:", font=("Arial", 12, "bold"), bg="#263238", fg="#81c784").grid(row=0, column=0, sticky="w", pady=10, padx=10)
    entry_first_name = tk.Entry(frame, font=("Arial", 12), borderwidth=2)
    entry_first_name.grid(row=0, column=1, pady=10, padx=10)

    # Last Name
    tk.Label(frame, text="Last Name:", font=("Arial", 12, "bold"), bg="#263238", fg="#81c784").grid(row=1, column=0, sticky="w", pady=10, padx=10)
    entry_last_name = tk.Entry(frame, font=("Arial", 12), borderwidth=2)
    entry_last_name.grid(row=1, column=1, pady=10, padx=10)

    # ID
    tk.Label(frame, text="ID:", font=("Arial", 12, "bold"), bg="#263238", fg="#81c784").grid(row=2, column=0, sticky="w", pady=10, padx=10)
    entry_id = tk.Entry(frame, font=("Arial", 12),  borderwidth=2)
    entry_id.grid(row=2, column=1, pady=10, padx=10)

    # Type (Toggle buttons placed next to each other)
    tk.Label(frame, text="Type:", font=("Arial", 12, "bold"), bg="#263238", fg="#81c784").grid(row=3, column=0, sticky="w", pady=10, padx=10)
    user_type_var = tk.StringVar(value="Student")  # Default to "User"

    # Create a frame to hold the toggle switches
    toggle_frame = tk.Frame(frame, bg="#263238")
    toggle_frame.grid(row=3, column=1, pady=10, padx=10)

    # Create the toggle buttons
    toggle_Student = tk.Button(toggle_frame, text="Student", font=("Arial", 12), width=12, bg="#43a047", fg="white",  borderwidth=2, command=lambda: user_type_var.set("Student"))
    toggle_faculty = tk.Button(toggle_frame, text="Faculty", font=("Arial", 12), width=12, bg="#263238", fg="white",  borderwidth=2, command=lambda: user_type_var.set("Faculty"))
    toggle_Courier = tk.Button(toggle_frame, text="Courier", font=("Arial", 12), width=12, bg="#263238", fg="white",  borderwidth=2, command=lambda: user_type_var.set("Courier"))

    # Position the toggle buttons horizontally
    toggle_Student.grid(row=0, column=0, padx=10)
    toggle_faculty.grid(row=0, column=1, padx=10)
    toggle_Courier.grid(row=0, column=2, padx=10)

    # Password
    tk.Label(frame, text="Password:", font=("Arial", 12, "bold"), bg="#263238", fg="#81c784").grid(row=4, column=0, sticky="w", pady=10, padx=10)
    entry_password = tk.Entry(frame, font=("Arial", 12), show="•",  borderwidth=2)
    entry_password.grid(row=4, column=1, pady=10, padx=10)

    # Email
    tk.Label(frame, text="Email:", font=("Arial", 12, "bold"), bg="#263238", fg="#81c784").grid(row=5, column=0, sticky="w", pady=10, padx=10)
    entry_email = tk.Entry(frame, font=("Arial", 12),  borderwidth=2)
    entry_email.grid(row=5, column=1, pady=10, padx=10)

    # Phone Number
    tk.Label(frame, text="Phone Number:", font=("Arial", 12, "bold"), bg="#263238", fg="#81c784").grid(row=6, column=0, sticky="w", pady=10, padx=10)
    entry_phone_number = tk.Entry(frame, font=("Arial", 12),  borderwidth=2)
    entry_phone_number.grid(row=6, column=1, pady=10, padx=10)

    button_frame = tk.Frame(root, bg="#37474f")
    button_frame.place(relx=0.5, rely=0.85, anchor="center")  # Adjusted position slightly
    submit_button = tk.Button(button_frame, text="Submit", font=("Arial", 12, "bold"), bg="#43a047", fg="white", command=input_valid)
    submit_button.grid(row=0, column=1, padx=10, ipadx=20, ipady=5)

    login_button = tk.Button(button_frame, text="Login", font=("Arial", 12, "bold"), bg="#0288d1", fg="white", command= login)
    login_button.grid(row=0, column=0, padx=10, ipadx=20, ipady=5)

    # Update toggle appearance on selection
    user_type_var.trace_add("write", lambda *args: toggle_switch())
    
                 
    # Run the Tkinter event loop
    root.mainloop()


# Login button action
# def login():
#     user_id = entry_id.get()
#     password = entry_password.get()
#     user_type = user_type_var.get()

#     if not all([user_id, password, user_type]):
#         messagebox.showwarning("Incomplete Data", "Please fill in all fields!")
#     else:
#         messagebox.showinfo("Success", f"Welcome, {user_type}!")

# Toggle switch style update


# def login():
#     user_id = entry_id.get()
#     password = entry_password.get()

#     if not all([user_id, password]):
#         messagebox.showwarning("Incomplete Data", "Please fill in all fields!")
#     else:
#         messagebox.showinfo("Success", f"Welcome, {user_id}!")

# Create main application window

def log_in():
    # Create main application window
    def check_availablity():
        id = entry_id.get()
        password = entry_password.get()
        if id == "admin" and password == "123":
            root.destroy()
            admin()
        else:
            password = hashlib.sha256(password.encode()).hexdigest()
            checkDB = database()
            flag = checkDB.retrieveUser(id , password)
            checkOTP = OTP()
            if checkOTP:
                if flag == True:

                    root.destroy()
                    global user_id
                    user_id = id
                    user_window()
                elif flag == "Courier":
                    root.destroy()
                    courier_window()
                else:
                    messagebox.showwarning("Error", "ID or password is Wrong")
               

        
    
        
    root = tk.Tk()
    root.title("Login Page")
    root.geometry("700x500")  # Window size
    root.configure(bg="#37474f")

    # Center window on screen
    window_width = 700
    window_height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_left = int(screen_width / 2 - window_width / 2)
    root.geometry(f'{window_width}x{window_height}+{position_left}+{position_top}')

    # Create a frame for form fields
    frame = tk.Frame(root, bg="#263238", padx=20, pady=20, relief=tk.GROOVE, borderwidth=3)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Form Title
    title_label = tk.Label(root, text="Login", font=("Arial", 20, "bold"), bg="#37474f", fg="#64b5f6")
    title_label.place(relx=0.5, rely=0.1, anchor="center")

    # User ID
    tk.Label(frame, text="User ID:", font=("Arial", 12, "bold"), bg="#263238", fg="#81c784").grid(row=0, column=0, sticky="w", pady=10, padx=10)
    entry_id = tk.Entry(frame, font=("Arial", 12), relief=tk.SUNKEN, borderwidth=2)
    entry_id.grid(row=0, column=1, pady=10, padx=10)

    # Password
    tk.Label(frame, text="Password:", font=("Arial", 12, "bold"), bg="#263238", fg="#81c784").grid(row=1, column=0, sticky="w", pady=10, padx=10)
    entry_password = tk.Entry(frame, font=("Arial", 12), show="*", relief=tk.SUNKEN, borderwidth=2)
    entry_password.grid(row=1, column=1, pady=10, padx=10)
    
    def func():
        root.destroy()
        sign_up()
    # Buttons
    button_frame = tk.Frame(root, bg="#37474f")
    button_frame.place(relx=0.5, rely=0.85, anchor="center")

    signup_button = tk.Button(button_frame, text="Signup", font=("Arial", 12, "bold"), bg="#43a047", fg="white", command=func)
    signup_button.grid(row=0, column=0, padx=10, ipadx=20, ipady=5)     #row=0, column=1, padx=10, ipadx=20, ipady=5

    

    login_button = tk.Button(button_frame, text="Login", font=("Arial", 12, "bold"), bg="#0288d1", fg="white", command=check_availablity)
    login_button.grid(row=0, column=1, padx=10, ipadx=20, ipady=5)


    
    # Run the Tkinter event loop
    root.mainloop()


# Call the login function to start the application
def OTP():
    # Generate a secret key for pyotp
    secret_key = pyotp.random_base32()

    # Function to generate a QR code for Google Authenticator
    def generate_qr_code():
        totp = pyotp.TOTP(secret_key)
        uri = totp.provisioning_uri(name="user@example.com", issuer_name="OTP Verification App")
        qr = qrcode.make(uri)
        return qr

    # Function to verify the OTP
    def submit_otp():
        otp = otp_entry.get()
        totp = pyotp.TOTP(secret_key)
        if totp.verify(otp):  # Verify the OTP
            messagebox.showinfo("Success", "OTP Verified Successfully!")
            root.destroy()
            return True
        else:
            messagebox.showerror("Error", "Invalid OTP. Please try again.")
            

    # Countdown function
    def countdown(time_left):
        if time_left >= 0:
            timer_label.config(text=f"Time Left: {time_left}s")
            root.after(1000, countdown, time_left - 1)  # Update every second
        else:
            otp_entry.config(state='disabled')  # Disable OTP entry after time runs out
            messagebox.showinfo("Time's Up", "OTP has expired. Timer will restart.")
            otp_entry.config(state='normal')  # Re-enable OTP entry for the next OTP
            countdown(30)

    # Create the main application window
    root = tk.Tk()
    root.title("OTP Entry with Timer")
    root.geometry("700x700")
    root.configure(bg="#37474f")

    # Center the window on the screen
    window_width = 700
    window_height = 700
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_left = int(screen_width / 2 - window_width / 2)
    root.geometry(f'{window_width}x{window_height}+{position_left}+{position_top}')

    # Frame for form fields
    frame = tk.Frame(root, bg="#263238", padx=20, pady=20, relief=tk.GROOVE, borderwidth=3)
    frame.place(relx=0.5, rely=0.4, anchor="center")

    # Title label
    title_label = tk.Label(root, text="OTP Verification", font=("Arial", 20, "bold"), bg="#37474f", fg="#64b5f6")
    title_label.place(relx=0.5, rely=0.1, anchor="center")

    # OTP entry field
    otp_label = tk.Label(frame, text="Enter OTP:", font=("Arial", 12, "bold"), bg="#263238", fg="#81c784")
    otp_label.grid(row=0, column=0, sticky="w", pady=10, padx=10)

    otp_entry = tk.Entry(frame, show="*", state='normal', font=("Arial", 12), relief=tk.SUNKEN, borderwidth=2)
    otp_entry.grid(row=0, column=1, pady=10, padx=10)

    # Generate and display the QR code
    qr_code_image = generate_qr_code()

    # Save QR code to a buffer and load it into ImageTk
    qr_buffer = BytesIO()
    qr_code_image.save(qr_buffer, format="PNG")
    qr_buffer.seek(0)

    # Create an ImageTk.PhotoImage object
    qr_image = ImageTk.PhotoImage(Image.open(qr_buffer).resize((150, 150)))

    # Store the image reference in the root (this will prevent garbage collection)
    root.qr_image = qr_image

    # Create a Label widget to display the QR code
    qr_label = tk.Label(frame, image=qr_image, bg="#263238")
    qr_label.grid(row=2, column=0, columnspan=2, pady=20)


    # Timer label
    timer_label = tk.Label(root, text="Time Left: 30s", font=("Arial", 14), bg="#263238", fg="#81c784", relief=tk.SUNKEN)
    timer_label.place(relx=0.5, rely=0.65, anchor="center")

    # Cancel button action
    def cancel_action():
        root.destroy()
        log_in()

    # Buttons at the bottom
    button_frame = tk.Frame(root, bg="#37474f")
    button_frame.place(relx=0.5, rely=0.9, anchor="center")

    cancel_button = tk.Button(button_frame, text="Cancel", font=("Arial", 12, "bold"), bg="#d32f2f", fg="white", command=cancel_action)
    cancel_button.grid(row=0, column=0, padx=10, ipadx=20, ipady=5)

    submit_button = tk.Button(button_frame, text="Submit OTP", font=("Arial", 12, "bold"), bg="#43a047", fg="white", command=submit_otp)
    submit_button.grid(row=0, column=1, padx=10, ipadx=20, ipady=5)
    
    # Start the timer countdown
    root.after(1000, countdown, 30)  # Start with a 30-second countdown
    
    # Run the Tkinter event loop
    root.mainloop()
    return submit_button


def admin():
    def insertOffice():
        id = entry_office_id.get()
        name = entry_office_name.get()
        DB = database()
        DB.insertOffice(id , name)



    def create_logistics_office():
        office_id = entry_office_id.get()
        office_name = entry_office_name.get()

        if not office_id or not office_name:
            messagebox.showwarning("Incomplete Data", "Please fill in all fields!")
        else:
            central_database.append({"Office ID": office_id, "Office Name": office_name})
            messagebox.showinfo("Success", "Logistics office added successfully!")

    def logout():
        admin_root.destroy()
        sign_up()

    def backup_database():
        if not central_database:
            messagebox.showwarning("No Data", "No data to backup!")
            return

        try:
            with open("database_backup.csv", "w", newline="") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=["Office ID", "Office Name"])
                writer.writeheader()
                writer.writerows(central_database)
            messagebox.showinfo("Success", "Backup completed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to backup data: {str(e)}")

    # Create admin application window
    admin_root = tk.Tk()
    admin_root.title("Admin Page")
    admin_root.geometry("700x500")
    admin_root.configure(bg="#37474f")

    # Center window on screen
    window_width = 700
    window_height = 500
    screen_width = admin_root.winfo_screenwidth()
    screen_height = admin_root.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_left = int(screen_width / 2 - window_width / 2)
    admin_root.geometry(f'{window_width}x{window_height}+{position_left}+{position_top}')

    # Frame for form fields
    frame = tk.Frame(admin_root, bg="#263238", padx=20, pady=20, relief=tk.GROOVE, borderwidth=3)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Form Title
    title_label = tk.Label(admin_root, text="Admin Panel", font=("Arial", 20, "bold"), bg="#37474f", fg="#64b5f6")
    title_label.place(relx=0.5, rely=0.1, anchor="center")

    # Logistics Office ID
    tk.Label(frame, text="Office ID:", font=("Arial", 12, "bold"), bg="#263238", fg="#81c784").grid(row=0, column=0, sticky="w", pady=10, padx=10)
    entry_office_id = tk.Entry(frame, font=("Arial", 12), relief=tk.SUNKEN, borderwidth=2)
    entry_office_id.grid(row=0, column=1, pady=10, padx=10)

    # Logistics Office Name
    tk.Label(frame, text="Office Name:", font=("Arial", 12, "bold"), bg="#263238", fg="#81c784").grid(row=1, column=0, sticky="w", pady=10, padx=10)
    entry_office_name = tk.Entry(frame, font=("Arial", 12), relief=tk.SUNKEN, borderwidth=2)
    entry_office_name.grid(row=1, column=1, pady=10, padx=10)

    # Buttons
    button_frame = tk.Frame(admin_root, bg="#37474f")
    button_frame.place(relx=0.5, rely=0.85, anchor="center")

    create_button = tk.Button(button_frame, text="Create", font=("Arial", 12, "bold"), bg="#43a047", fg="white", command=insertOffice)
    create_button.grid(row=0, column=0, padx=10, ipadx=20, ipady=5)

    logout_button = tk.Button(button_frame, text="Logout", font=("Arial", 12, "bold"), bg="#0288d1", fg="white", command=logout)
    logout_button.grid(row=0, column=1, padx=10, ipadx=20, ipady=5)

    backup_button = tk.Button(button_frame, text="Backup", font=("Arial", 12, "bold"), bg="#ffa000", fg="white", command=backup_database)
    backup_button.grid(row=0, column=2, padx=10, ipadx=20, ipady=5)

    # Run the Tkinter event loop
    admin_root.mainloop()
 
    
#log_in()
import tkinter as tk
from tkinter import messagebox
import random
import time
from tkinter import ttk

# Mock function to simulate the database connection and transaction logging
def log_transaction(user_id, receiver_id, package_details, logistics_office_id):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open("transaction_log.txt", "a") as log_file:
        log_file.write(f"{timestamp} - Sender: {user_id}, Receiver: {receiver_id}, Package: {package_details}, Logistics Office: {logistics_office_id}\n")

# Mock function to simulate package tracking
def retrieve_user_packages(user_id):
    # In a real-world scenario, this would fetch data from a central database
    return [
        {"tracking_number": "1234567890123456", "status": "Shipped", "location": "Warehouse A"},
        {"tracking_number": "2345678901234567", "status": "In Transit", "location": "Logistics Office B"},
    ]

# Function to generate a random tracking number
def generate_tracking_number():
    return ''.join([str(random.randint(0, 9)) for _ in range(16)])

# User Window
import tkinter as tk
from tkinter import messagebox
import random
import time
from tkinter import ttk

# Mock function to simulate the database connection and transaction logging
def log_transaction(user_id, receiver_id, package_details, logistics_office_id):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open("transaction_log.txt", "a") as log_file:
        log_file.write(f"{timestamp} - Sender: {user_id}, Receiver: {receiver_id}, Package: {package_details}, Logistics Office: {logistics_office_id}\n")

# Mock function to simulate package tracking
def retrieve_user_packages(user_id):
    # In a real-world scenario, this would fetch data from a central database
    return [
        {"tracking_number": "1234567890123456", "status": "Shipped", "location": "Warehouse A"},
        {"tracking_number": "2345678901234567", "status": "In Transit", "location": "Logistics Office B"},
    ]

# Function to generate a random tracking number
def generate_tracking_number():
    return ''.join([str(random.randint(0, 9)) for _ in range(16)])

# User Window
import logging
logging.basicConfig(filename='transaction.log',
filemode='a',
format='%(asctime)s - %(levelname)s - %(message)s',
level=logging.DEBUG)
def user_window():
    def add_package():
        DB = database()  
        tracking_number = ""
        for i in range(16):
            tracking_number += str(random.randint(0,9))
            
        dimension = entry_length.get()+"X"+entry_width.get()+"X"+entry_height.get()
        weight = entry_weight.get()
        office_name = logistics_office_var.get()
        receiver_id = entry_receiver_user_id.get()
        dictionOffice = DB.retrieveOffices()    

        DB.insertPackage(tracking_number , dictionOffice[office_name] , receiver_id ,  user_id , dimension , weight , "pending")
        logging.info(f"package added: tracking number: {tracking_number} , office ID: {dictionOffice[office_name]} , office name: {office_name} ,sender ID: {user_id} , receiver ID: {receiver_id} , dimension: {dimension} , Weight: {weight} , Status: pending")
        
    def logout():
        root.destroy()
        sign_up()  # Assuming you want to call the sign-up function again on logout

    def drop_package():
        # Get values from the entry fields and drop the package
        logistics_office = logistics_office_var.get()
        dimensions = (entry_length.get(), entry_width.get(), entry_height.get())
        weight = entry_weight.get()
        receiver_user_id = entry_receiver_user_id.get()

        if not all([logistics_office, *dimensions, weight, receiver_user_id]):
            messagebox.showwarning("Incomplete Data", "Please fill in all fields!")
        else:
            tracking_number = generate_tracking_number()
            log_transaction(user_id="User123", receiver_id=receiver_user_id, package_details=(dimensions, weight), logistics_office_id=logistics_office)
            messagebox.showinfo("Success", f"Package Dropped! Tracking Number: {tracking_number}")

    def view_packages():
        DB = database()
        package_list.delete( 0 , tk.END )
        user_packages = DB.retrievePackages()
        global user_id
        main_lst = [] # TN , OfficeID , senderID , dimension , weight , status
        for i in user_packages:
            if user_id == i[2]:
                current_list = []
                current_list.append(i[0])
                current_list.append(i[1])
                current_list.append(i[3])
                current_list.append(i[4])
                current_list.append(i[5])
                current_list.append(i[6])
                main_lst.append(current_list)
                
         # Clear existing list
        
        for package in main_lst:
            package_list.insert(tk.END, f"Traking Number: {package[0]} , Office ID: {package[1]} , Sender ID: {package[2]} , dimensions: {package[3]} , Weight: {package[4]}KG , Status: {package[5]} ")
    
    def view_sending_packages():
        DB = database()
        package_sending_list.delete( 0 , tk.END )
        user_packages = DB.retrievePackages()
        global user_id
        main_lst = [] # TN , OfficeID , senderID , dimension , weight , status
        for i in user_packages:
            if user_id == i[3]:
                current_list = []
                current_list.append(i[0])
                current_list.append(i[1])
                current_list.append(i[2])
                current_list.append(i[4])
                current_list.append(i[5])
                current_list.append(i[6])
                main_lst.append(current_list)
                
         # Clear existing list
        
        for package in main_lst:
            package_sending_list.insert(tk.END, f"Traking Number: {package[0]} , Office ID: {package[1]} , Recievier: {package[2]} , dimensions: {package[3]} , Weight: {package[4]}KG , Status: {package[5]} ")


    # Create main application window
    root = tk.Tk()
    root.title("User Window")
    root.geometry("700x700")
    root.configure(bg="#37474f")

    # Center window on screen
    window_width = 800
    window_height = 800
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_left = int(screen_width / 2 - window_width / 2)
    root.geometry(f'{window_width}x{window_height}+{position_left}+{position_top}')

    # Create notebook (tabbed interface)
    notebook = ttk.Notebook(root)
    notebook.pack(pady=20)

    # Tab 1 - Drop a Package
    drop_package_frame = tk.Frame(notebook, bg="#263238")
    notebook.add(drop_package_frame, text="Drop a Package")

    DB = database()
    flag = False  
    logistics_offices = list(DB.retrieveOffices().keys()) # { NAME -> ID }

    logistics_office_var = tk.StringVar()
    if not logistics_offices:
        logistics_offices = ["no offices"]
        flag = True
    logistics_office_var.set(logistics_offices[0])    

            # Default selection

    # Logistics Office Dropdown
    tk.Label(drop_package_frame, text="Select Logistics Office:", font=("Arial", 12, "bold"), bg="#263238", fg="#81c784").grid(row=0, column=0, sticky="w", pady=10, padx=10)
    logistics_office_dropdown = tk.OptionMenu(drop_package_frame, logistics_office_var, *logistics_offices)
    logistics_office_dropdown.grid(row=0, column=1, pady=10, padx=10)

    # Package Dimensions (Length, Width, Height)
    tk.Label(drop_package_frame, text="Package Dimensions (L x W x H):", font=("Arial", 12, "bold"), bg="#263238", fg="#81c784").grid(row=1, column=0, sticky="w", pady=10, padx=10)
    
    # Adjusted Entry Size for smaller width (for dimensions)
    entry_width_size = 4  # Adjusted to be smaller

    entry_length = tk.Entry(drop_package_frame, font=("Arial", 12), relief=tk.SUNKEN, borderwidth=2, width=entry_width_size)
    entry_length.grid(row=1, column=1, pady=10, padx=5  ,sticky='w')
    tk.Label(drop_package_frame, text="Length", font=("Arial", 10), bg="#263238", fg="#81c784").grid(row=2, column=1, pady=1 ,padx=2,sticky='w')

    entry_width = tk.Entry(drop_package_frame, font=("Arial", 12), relief=tk.SUNKEN, borderwidth=2, width=entry_width_size)
    entry_width.grid(row=1, column=1, pady=10, padx=5  )
    tk.Label(drop_package_frame, text="Width", font=("Arial", 10), bg="#263238", fg="#81c784").grid(row=2, column=1, pady=5 )

    entry_height = tk.Entry(drop_package_frame, font=("Arial", 12), relief=tk.SUNKEN, borderwidth=2, width=entry_width_size)
    entry_height.grid(row=1, column=1, pady=10, padx=5 ,sticky='e') 
    tk.Label(drop_package_frame, text="Height", font=("Arial", 10), bg="#263238", fg="#81c784").grid(row=2, column=1, pady=5 , sticky='e')

    # Package Weight
    tk.Label(drop_package_frame, text="Package Weight (kg):", font=("Arial", 12, "bold"), bg="#263238", fg="#81c784").grid(row=3, column=0, sticky="w", pady=10, padx=10)
    entry_weight = tk.Entry(drop_package_frame, font=("Arial", 12), relief=tk.SUNKEN, borderwidth=2)
    entry_weight.grid(row=3, column=1, pady=10, padx=10)

    # Receiver User ID
    tk.Label(drop_package_frame, text="Receiver User ID:", font=("Arial", 12, "bold"), bg="#263238", fg="#81c784").grid(row=4, column=0, sticky="w", pady=10, padx=10)
    entry_receiver_user_id = tk.Entry(drop_package_frame, font=("Arial", 12), relief=tk.SUNKEN, borderwidth=2)
    entry_receiver_user_id.grid(row=4, column=1, pady=10, padx=10)

    # Buttons: Logout and Confirm (with logout to the left of Confirm)
    button_frame = tk.Frame(drop_package_frame, bg="#263238")
    button_frame.grid(row=5, column=0, columnspan=4, pady=20)

    logout_button = tk.Button(button_frame, text="Logout", font=("Arial", 12, "bold"), bg="#d32f2f", fg="white", command=logout)
    logout_button.grid(row=0, column=0, padx=10, ipadx=20, ipady=5)

    confirm_button = tk.Button(button_frame, text="Confirm", font=("Arial", 12, "bold"), bg="#43a047", fg="white", command=add_package)
    confirm_button.grid(row=0, column=1, padx=10, ipadx=20, ipady=5)

    # Tab 2 - View my Packages
    view_packages_frame = tk.Frame(notebook, bg="#263238")
    notebook.add(view_packages_frame, text="View my Packages")

    # View Packages Button
    view_button = tk.Button(view_packages_frame, text="Show my Packages", font=("Arial", 12, "bold"), bg="#43a047", fg="white", command=view_packages)
    view_button.grid(row=0, column=0, pady=20)

    # Package Listbox with no white frame
    package_list = tk.Listbox(view_packages_frame, font=("Arial", 12), bg="#37474f", fg="#ffffff", width=60, height=15, bd=0)
    package_list.grid(row=1, column=0, pady=10)

    # Logout Button for View Packages Tab
    logout_button = tk.Button(view_packages_frame, text="Logout", font=("Arial", 12, "bold"), bg="#d32f2f", fg="white", command=logout)
    logout_button.grid(row=2, column=0, pady=10)
    
    # Tab 3 - View sending Packages
    view_sending_packages_frame = tk.Frame(notebook, bg="#263238")
    notebook.add(view_sending_packages_frame, text="View sending Packages")

    # View Packages Button
    view_button = tk.Button(view_sending_packages_frame, text="Show sending Packages", font=("Arial", 12, "bold"), bg="#43a047", fg="white", command=view_sending_packages)
    view_button.grid(row=0, column=0, pady=20)

    # Package Listbox with no white frame
    package_sending_list = tk.Listbox(view_sending_packages_frame, font=("Arial", 12), bg="#37474f", fg="#ffffff", width=60, height=15, bd=0)
    package_sending_list.grid(row=1, column=0, pady=10)

    # Logout Button for View Packages Tab
    logout_button = tk.Button(view_sending_packages_frame, text="Logout", font=("Arial", 12, "bold"), bg="#d32f2f", fg="white", command=logout)
    logout_button.grid(row=2, column=0, pady=10)

 
    # Run the Tkinter event loop
    root.mainloop() # main
    


def courier_window():

    def accept():
        sender = entry_sender_user_id.get()
        tracking_number = entry_tracking_number.get()  # 0 , 3
        DB = database()
        packages = DB.retrievePackages()
        for i in packages:
            if i[0] == tracking_number and i[3] == sender and i[6] == "pending":
                DB = database()
                DB.update_status("Accepted" , tracking_number)
                break
        print("Error")   

    def deliver():
        sender = entry_deliver_sender_user_id.get()
        tracking_number = entry_deliver_tracking_number.get()
        DB = database()
        packages = DB.retrievePackages()
        for i in packages:
            if i[0] == tracking_number and i[3] == sender and i[6] == "Accepted":
                DB = database()
                DB.update_status("Delivered" , tracking_number)
                break
        print("Error")   

    def accept_package():
        DB = database()
        sender_user_id = entry_sender_user_id.get()
        tracking_number = entry_tracking_number.get()

        # Check if both fields are filled
        if not sender_user_id or not tracking_number:
            messagebox.showwarning("Incomplete Data", "Please fill in all fields!")
            return
        
        # Simulate the acceptance of the package into the logistics system
        if DB.acceptPackage(sender_user_id, tracking_number):
            messagebox.showinfo("Success", f"Package {tracking_number} accepted!")
        else:
            messagebox.showerror("Error", "Failed to accept the package. Please check the information.")

    def deliver_package():
        DB = database()
        sender_user_id = entry_sender_user_id.get()
        tracking_number = entry_tracking_number.get()

        # Check if both fields are filled
        if not sender_user_id or not tracking_number:
            messagebox.showwarning("Incomplete Data", "Please fill in all fields!")
            return
        
        # Simulate the delivery of the package
        if DB.deliverPackage(sender_user_id, tracking_number):
            messagebox.showinfo("Success", f"Package {tracking_number} delivered!")
        else:
            messagebox.showerror("Error", "Failed to deliver the package. Please check the information.")

    def logout():
        root.destroy()
        sign_up()  # Assuming sign_up() brings back the sign up window

    # Create main application window
    root = tk.Tk()
    root.title("Courier Window")
    root.geometry("800x800")  # Slightly smaller window size
    root.configure(bg="#37474f")

    # Center window on screen
    window_width = 800
    window_height = 800
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_left = int(screen_width / 2 - window_width / 2)
    root.geometry(f'{window_width}x{window_height}+{position_left}+{position_top}')

    # Create notebook (tabbed interface)
    notebook = ttk.Notebook(root)
    notebook.pack(pady=40)  # Add extra padding to move the entire notebook a bit down

    # Tab 1 - Accept a Package
    accept_package_frame = tk.Frame(notebook, bg="#263238")
    notebook.add(accept_package_frame, text="Accept a Package")

    # Title for the tab
    title_label = tk.Label(accept_package_frame, text="Accept Package", font=("Arial", 18, "bold"), bg="#263238", fg="#81c784")
    title_label.grid(row=0, column=0, columnspan=2, pady=20)

    # Sender User ID
    tk.Label(accept_package_frame, text="Sender User ID:", font=("Arial", 14, "bold"), bg="#263238", fg="#81c784").grid(row=1, column=0, sticky="w", pady=12, padx=15)
    entry_sender_user_id = tk.Entry(accept_package_frame, font=("Arial", 14), relief=tk.SUNKEN, borderwidth=3, width=25)
    entry_sender_user_id.grid(row=1, column=1, pady=12, padx=15)

    # Tracking Number
    tk.Label(accept_package_frame, text="Tracking Number:", font=("Arial", 14, "bold"), bg="#263238", fg="#81c784").grid(row=2, column=0, sticky="w", pady=12, padx=15)
    entry_tracking_number = tk.Entry(accept_package_frame, font=("Arial", 14), relief=tk.SUNKEN, borderwidth=3, width=25)
    entry_tracking_number.grid(row=2, column=1, pady=12, padx=15)

    # Accept Button
    accept_button = tk.Button(accept_package_frame, text="Accept Package", font=("Arial", 14, "bold"), bg="#43a047", fg="white", command=accept, width=18, height=2)
    accept_button.grid(row=3, column=0, columnspan=2, pady=25)

    # Logout Button
    logout_button = tk.Button(accept_package_frame, text="Logout", font=("Arial", 14, "bold"), bg="#d32f2f", fg="white", command=logout, width=18, height=2)
    logout_button.grid(row=4, column=0, columnspan=2, pady=15)

    # Tab 2 - Deliver a Package
    deliver_package_frame = tk.Frame(notebook, bg="#263238")
    notebook.add(deliver_package_frame, text="Deliver a Package")

    # Title for the tab
    title_label = tk.Label(deliver_package_frame, text="Deliver Package", font=("Arial", 18, "bold"), bg="#263238", fg="#81c784")
    title_label.grid(row=0, column=0, columnspan=2, pady=20)

    # Sender User ID
    tk.Label(deliver_package_frame, text="Sender User ID:", font=("Arial", 14, "bold"), bg="#263238", fg="#81c784").grid(row=1, column=0, sticky="w", pady=12, padx=15)
    entry_deliver_sender_user_id = tk.Entry(deliver_package_frame, font=("Arial", 14), relief=tk.SUNKEN, borderwidth=3, width=25)
    entry_deliver_sender_user_id.grid(row=1, column=1, pady=12, padx=15)

    # Tracking Number
    tk.Label(deliver_package_frame, text="Tracking Number:", font=("Arial", 14, "bold"), bg="#263238", fg="#81c784").grid(row=2, column=0, sticky="w", pady=12, padx=15)
    entry_deliver_tracking_number = tk.Entry(deliver_package_frame, font=("Arial", 14), relief=tk.SUNKEN, borderwidth=3, width=25)
    entry_deliver_tracking_number.grid(row=2, column=1, pady=12, padx=15)

    # Deliver Button
    deliver_button = tk.Button(deliver_package_frame, text="Deliver Package", font=("Arial", 14, "bold"), bg="#43a047", fg="white", command=deliver, width=18, height=2)
    deliver_button.grid(row=3, column=0, columnspan=2, pady=25)

    # Logout Button
    logout_button = tk.Button(deliver_package_frame, text="Logout", font=("Arial", 14, "bold"), bg="#d32f2f", fg="white", command=logout, width=18, height=2)
    logout_button.grid(row=4, column=0, columnspan=2, pady=15)

    # Run the Tkinter event loop
    root.mainloop()



log_in()



