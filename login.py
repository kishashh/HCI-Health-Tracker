import tkinter as tk
import os
import home_screen

class LoginPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login Page")
        self.geometry("400x200")
        self.configure(background="light blue")
        self.create_widgets()

    def create_widgets(self):
        # Username Entry
        username_label = tk.Label(self, text="Enter your name:", font=("Arial", 14))
        username_label.pack(pady=(20, 10))

        self.username_entry = tk.Entry(self, font=("Arial", 14))
        self.username_entry.pack()

        # Login Button
        login_button = tk.Button(self, text="Log In", command=self.login_user, font=("Arial", 14))
        login_button.pack(pady=(10, 20))

    def login_user(self):
        username = self.username_entry.get()
        account_path = f"Accounts/{username}.txt"
        if os.path.exists(account_path):
            self.destroy()
            main_window = home_screen.NutritionTracker()
            main_window.mainloop()
        else:
            error_label = tk.Label(self, text="Account not found, please try again or register.", foreground="red")
            error_label.pack()
