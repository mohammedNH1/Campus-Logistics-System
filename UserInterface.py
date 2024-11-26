import tkinter as tk
from tkinter import ttk, messagebox
from User import user
import re

# Submit button action
def sign_up():
    
    def submit():
        first_name = entry_first_name.get()
        last_name = entry_last_name.get()
        user_id = entry_id.get()
        user_type = user_type_var.get()
        password = entry_password.get()
        email = entry_email.get()
        phone_number = entry_phone_number.get()

        if not all([first_name, last_name, user_id, user_type, password, email, phone_number]):
            messagebox.showwarning("Incomplete Data", "Please fill in all fields!")
        else:
            messagebox.showinfo("Success", "Form Submitted Successfully!")

    # Login button action
    def login():
        messagebox.showinfo("Login", "Redirecting to login page...")

    # Toggle switch style update
    def toggle_switch():
        selected = user_type_var.get()

        # Check and update the appearance of the toggles based on selection
        if selected == "User":
            toggle_user.config(bg="#43a047", fg="white", relief="solid")
            toggle_faculty.config(bg="#263238", fg="white", relief="solid")
            toggle_employee.config(bg="#263238", fg="white", relief="solid")
        elif selected == "Faculty":
            toggle_faculty.config(bg="#43a047", fg="white", relief="solid")
            toggle_user.config(bg="#263238", fg="white", relief="solid")
            toggle_employee.config(bg="#263238", fg="white", relief="solid")
        elif selected == "Employee":
            toggle_employee.config(bg="#43a047", fg="white", relief="solid")
            toggle_user.config(bg="#263238", fg="white", relief="solid")
            toggle_faculty.config(bg="#263238", fg="white", relief="solid")

    # Create main application window
    root = tk.Tk()
    root.title("Sign Up")  # Changed to "Sign Up"
    root.geometry("700x700")  # Set window size
    root.configure(bg="#37474f")  # Set a masculine background color

    # Center window on screen
    window_width = 700
    window_height = 700
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    position_top = int(screen_height / 2 - window_height / 2)
    position_left = int(screen_width / 2 - window_width / 2)

    root.geometry(f'{window_width}x{window_height}+{position_left}+{position_top}')

    # Create a frame for form fields with bold, masculine colors
    frame = tk.Frame(root, bg="#263238", padx=20, pady=20, relief=tk.GROOVE, borderwidth=3)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Form Title
    title_label = tk.Label(root, text="Sign Up", font=("Arial", 20, "bold"), bg="#37474f", fg="#64b5f6")
    title_label.place(relx=0.5, rely=0.1, anchor="center")

    # First Name
    tk.Label(frame, text="First Name:", font=("Arial", 12, "bold"), bg="#263238", fg="#81c784").grid(row=0, column=0, sticky="w", pady=10, padx=10)
    entry_first_name = tk.Entry(frame, font=("Arial", 12), relief=tk.SUNKEN, borderwidth=2)
    entry_first_name.grid(row=0, column=1, pady=10, padx=10)

    # Last Name
    tk.Label(frame, text="Last Name:", font=("Arial", 12, "bold"), bg="#263238", fg="#81c784").grid(row=1, column=0, sticky="w", pady=10, padx=10)
    entry_last_name = tk.Entry(frame, font=("Arial", 12), relief=tk.SUNKEN, borderwidth=2)
    entry_last_name.grid(row=1, column=1, pady=10, padx=10)

    # ID
    tk.Label(frame, text="ID:", font=("Arial", 12, "bold"), bg="#263238", fg="#81c784").grid(row=2, column=0, sticky="w", pady=10, padx=10)
    entry_id = tk.Entry(frame, font=("Arial", 12), relief=tk.SUNKEN, borderwidth=2)
    entry_id.grid(row=2, column=1, pady=10, padx=10)

    # Type (Toggle buttons placed next to each other)
    tk.Label(frame, text="Type:", font=("Arial", 12, "bold"), bg="#263238", fg="#81c784").grid(row=3, column=0, sticky="w", pady=10, padx=10)
    user_type_var = tk.StringVar(value="User")  # Default to "User"

    # Create a frame to hold the toggle switches
    toggle_frame = tk.Frame(frame, bg="#263238")
    toggle_frame.grid(row=3, column=1, pady=10, padx=10)

    # Create the toggle buttons with black borders
    toggle_user = tk.Button(toggle_frame, text="User", font=("Arial", 12), width=12, bg="#43a047", fg="white", relief="solid", borderwidth=2, command=lambda: user_type_var.set("User"))
    toggle_faculty = tk.Button(toggle_frame, text="Faculty", font=("Arial", 12), width=12, bg="#263238", fg="white", relief="solid", borderwidth=2, command=lambda: user_type_var.set("Faculty"))
    toggle_employee = tk.Button(toggle_frame, text="Employee", font=("Arial", 12), width=12, bg="#263238", fg="white", relief="solid", borderwidth=2, command=lambda: user_type_var.set("Employee"))

    # Position the toggle buttons horizontally
    toggle_user.grid(row=0, column=0, padx=10)
    toggle_faculty.grid(row=0, column=1, padx=10)
    toggle_employee.grid(row=0, column=2, padx=10)

    # Password
    tk.Label(frame, text="Password:", font=("Arial", 12, "bold"), bg="#263238", fg="#81c784").grid(row=4, column=0, sticky="w", pady=10, padx=10)
    entry_password = tk.Entry(frame, font=("Arial", 12), show="*", relief=tk.SUNKEN, borderwidth=2)
    entry_password.grid(row=4, column=1, pady=10, padx=10)

    # Email
    tk.Label(frame, text="Email:", font=("Arial", 12, "bold"), bg="#263238", fg="#81c784").grid(row=5, column=0, sticky="w", pady=10, padx=10)
    entry_email = tk.Entry(frame, font=("Arial", 12), relief=tk.SUNKEN, borderwidth=2)
    entry_email.grid(row=5, column=1, pady=10, padx=10)

    # Phone Number
    tk.Label(frame, text="Phone Number:", font=("Arial", 12, "bold"), bg="#263238", fg="#81c784").grid(row=6, column=0, sticky="w", pady=10, padx=10)
    entry_phone_number = tk.Entry(frame, font=("Arial", 12), relief=tk.SUNKEN, borderwidth=2)
    entry_phone_number.grid(row=6, column=1, pady=10, padx=10)

    # Buttons
    def func():
        root.destroy()
        log_in()
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
             print("invalid phone number 05")
        elif not valid_ID:
             if type == "student":
                 
             print("invalid digits ID")
        elif not valid_pass:
             print("invalid password wrong ")
        elif not valid_email:
             print("invalid email")
        else:
            print("insert worked")
            myUser = user(id , Fname , Lname , type, email , number , password)
    button_frame = tk.Frame(root, bg="#37474f")
    button_frame.place(relx=0.5, rely=0.85, anchor="center")  # Adjusted position slightly
    submit_button = tk.Button(button_frame, text="Submit", font=("Arial", 12, "bold"), bg="#43a047", fg="white", command=input_valid)
    submit_button.grid(row=0, column=1, padx=10, ipadx=20, ipady=5)

    login_button = tk.Button(button_frame, text="Login", font=("Arial", 12, "bold"), bg="#0288d1", fg="white", command= func)
    login_button.grid(row=0, column=0, padx=10, ipadx=20, ipady=5)

    # Update toggle appearance on selection
    user_type_var.trace_add("write", lambda *args: toggle_switch())
    
                 
        

    # Run the Tkinter event loop
    root.mainloop()

import tkinter as tk
from tkinter import messagebox

# Login button action
def login():
    user_id = entry_id.get()
    password = entry_password.get()
    user_type = user_type_var.get()

    if not all([user_id, password, user_type]):
        messagebox.showwarning("Incomplete Data", "Please fill in all fields!")
    else:
        messagebox.showinfo("Success", f"Welcome, {user_type}!")

# Toggle switch style update
import tkinter as tk
from tkinter import messagebox

def login():
    user_id = entry_id.get()
    password = entry_password.get()

    if not all([user_id, password]):
        messagebox.showwarning("Incomplete Data", "Please fill in all fields!")
    else:
        messagebox.showinfo("Success", f"Welcome, {user_id}!")

# Create main application window
def log_in():
    # Create main application window
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

    

    login_button = tk.Button(button_frame, text="Login", font=("Arial", 12, "bold"), bg="#0288d1", fg="white", command=login)
    login_button.grid(row=0, column=1, padx=10, ipadx=20, ipady=5)


    
    # Run the Tkinter event loop
    root.mainloop()

<<<<<<< HEAD
# Call the login function to start the application
log_in()



=======
def input_valid(Fname ,Lname , Type , password, email ,  number,  id  ):
        valid_phone_number = re.search("^(05)" ,number)
        valid_ID = len(id) == 10
        valid_pass = len(password) >= 6
        valid_email = re.search("(@ksu.edu.sa)$", email)
        if not valid_phone_number:
             # error on GUI
             pass
        if not valid_ID:
             pass
        if not valid_pass:
             pass
        if not valid_email:
             pass
        mohammed = User(id , Fname , Lname , Type, email , number , password)

def admin():
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

    create_button = tk.Button(button_frame, text="Create", font=("Arial", 12, "bold"), bg="#43a047", fg="white", command=create_logistics_office)
    create_button.grid(row=0, column=0, padx=10, ipadx=20, ipady=5)

    logout_button = tk.Button(button_frame, text="Logout", font=("Arial", 12, "bold"), bg="#0288d1", fg="white", command=logout)
    logout_button.grid(row=0, column=1, padx=10, ipadx=20, ipady=5)

    backup_button = tk.Button(button_frame, text="Backup", font=("Arial", 12, "bold"), bg="#ffa000", fg="white", command=backup_database)
    backup_button.grid(row=0, column=2, padx=10, ipadx=20, ipady=5)

    # Run the Tkinter event loop
    admin_root.mainloop()

# Run the admin function for testing purposes
admin()    
    

log_in()    
>>>>>>> 57eaeb70f422733608cee428d63c29b6ac0adf41
