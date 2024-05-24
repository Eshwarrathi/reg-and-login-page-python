import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np


class UserSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("User System")

        self.bg_color = "#f4f4f4"
        
        self.create_registration_form()

    def create_registration_form(self):
        registration_frame = tk.Frame(self.root, bg=self.bg_color)
        registration_frame.pack(pady=20)

        title = tk.Label(registration_frame, text="Registration Form", font=("Helvetica", 16, "bold"), bg=self.bg_color, fg="#333")
        title.pack(fill=tk.X, pady=10)

        self.reg_name_var = tk.StringVar()
        self.reg_email_var = tk.StringVar()
        self.reg_password_var = tk.StringVar()

        lbl_name = tk.Label(registration_frame, text="Name:", font=("Helvetica", 12), bg=self.bg_color, fg="#555")
        lbl_name.pack(pady=5)
        txt_name = tk.Entry(registration_frame, textvariable=self.reg_name_var, font=("Helvetica", 12), bd=5, relief=tk.GROOVE)
        txt_name.pack()

        lbl_email = tk.Label(registration_frame, text="Email:", font=("Helvetica", 12), bg=self.bg_color, fg="#555")
        lbl_email.pack(pady=5)
        txt_email = tk.Entry(registration_frame, textvariable=self.reg_email_var, font=("Helvetica", 12), bd=5, relief=tk.GROOVE)
        txt_email.pack()

        lbl_password = tk.Label(registration_frame, text="Password:", font=("Helvetica", 12), bg=self.bg_color, fg="#555")
        lbl_password.pack(pady=5)
        txt_password = tk.Entry(registration_frame, textvariable=self.reg_password_var, font=("Helvetica", 12), bd=5, relief=tk.GROOVE, show="*")
        txt_password.pack()

        btn_submit = tk.Button(registration_frame, text="Submit", font=("Helvetica", 12, "bold"), bg="#074463", fg="white", bd=5, relief=tk.RAISED, command=self.submit_registration)
        btn_submit.pack(fill=tk.X, pady=5)
        btn_login = tk.Button(registration_frame, text="Login", font=("Helvetica", 12, "bold"), bg="#555", fg="white", bd=5, relief=tk.RAISED, command=self.open_login_page)
        btn_login.pack(fill=tk.X, pady=5)

    def submit_registration(self):
        name = self.reg_name_var.get()
        email = self.reg_email_var.get()
        password = self.reg_password_var.get()

        # Perform registration logic and validation here
        
        message = f"Registration Successful!\nName: {name}\nEmail: {email}\nPassword: {password}"
        messagebox.showinfo("Registration", message)
        
        self.clear_registration_form()

    def clear_registration_form(self):
        self.reg_name_var.set("")
        self.reg_email_var.set("")
        self.reg_password_var.set("")

    def open_login_page(self):
        self.root.destroy()  # Close the registration page
        
        login_root = tk.Tk()
        login_app = LoginSystem(login_root)
        login_root.mainloop()


class LoginSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Login Form")

        self.bg_color = "#f4f4f4"
        
        self.create_login_form()

    def create_login_form(self):
        login_frame = tk.Frame(self.root, bg=self.bg_color)
        login_frame.pack(pady=20)

        title = tk.Label(login_frame, text="Login Form", font=("Helvetica", 16, "bold"), bg=self.bg_color, fg="#333")
        title.pack(fill=tk.X, pady=10)

        self.login_email_var = tk.StringVar()
        self.login_password_var = tk.StringVar()

        lbl_email = tk.Label(login_frame, text="Email:", font=("Helvetica", 12), bg=self.bg_color, fg="#555")
        lbl_email.pack(pady=5)
        txt_email = tk.Entry(login_frame, textvariable=self.login_email_var, font=("Helvetica", 12), bd=5, relief=tk.GROOVE)
        txt_email.pack()

        lbl_password = tk.Label(login_frame, text="Password:", font=("Helvetica", 12), bg=self.bg_color, fg="#555")
        lbl_password.pack(pady=5)
        txt_password = tk.Entry(login_frame, textvariable=self.login_password_var, font=("Helvetica", 12), bd=5, relief=tk.GROOVE, show="*")
        txt_password.pack()

        btn_login = tk.Button(login_frame, text="Login", font=("Helvetica", 12, "bold"), bg="#074463", fg="white", bd=5, relief=tk.RAISED, command=self.login)
        btn_login.pack(fill=tk.X, pady=10)

    def login(self):
        email = self.login_email_var.get()
        password = self.login_password_var.get()

        # Perform login logic and validation here
        
        message = f"Login Successful!\nEmail: {email}\nPassword: {password}"
        messagebox.showinfo("Login", message)
        
        self.root.destroy()
        
        self.show_slope_viz()

    def show_slope_viz(self):
        self.slope_viz()

    def slope_viz(self, m=1):
        x = np.linspace(-1, 10, 100)
        y = m * x
        x_values = np.linspace(-1, 10, 100)

        plt.scatter(x, y)
        plt.plot(x_values, m * x_values, lw=3, color='black')

        plt.ylim(-1.2, 12.2)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Slope Visualization')
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    root = tk.Tk()
    app = UserSystem(root)
    root.mainloop()
