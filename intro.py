import tkinter as tk
from tkinter import ttk
import home_screen
from login import LoginPage  # Import the LoginPage from login.py

class WelcomePage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Welcome Page")
        self.geometry("1050x500")
        self.configure(background="gray")
        self.create_widgets()

    def create_widgets(self):
        welcome_label = tk.Label(self, text="Welcome!", font=("Arial", 20))
        welcome_label.pack(pady=(10, 20))

        name_label = tk.Label(self, text="Name:")
        name_label.pack()

        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        weight_label = tk.Label(self, text="Weight:")
        weight_label.pack()

        self.weight_entry = tk.Entry(self)
        self.weight_entry.pack()

        plan_label = tk.Label(self, text="Plan:")
        plan_label.pack()

        plan_options = ["Gain Weight", "Maintain Weight", "Lose Weight"]
        self.plan_combobox = ttk.Combobox(self, values=plan_options, state="readonly")
        self.plan_combobox.set("Select a Plan")
        self.plan_combobox.pack()

        continue_button = tk.Button(self, text="Continue", command=self.save_and_continue)
        continue_button.pack()

        login_button = tk.Button(self, text="Log in Already", command=self.open_login)
        login_button.pack()

    def save_and_continue(self):
        name = self.name_entry.get()
        weight = self.weight_entry.get()
        plan = self.plan_combobox.get()
        accounts_folder = "Accounts"
        if not os.path.exists(accounts_folder):
            os.makedirs(accounts_folder)
        with open(f"{accounts_folder}/{name}.txt", "w") as file:
            file.write(f"Name: {name}\nWeight: {weight}\nPlan: {plan}\n")
        self.destroy()
        main_window = home_screen.NutritionTracker()
        main_window.mainloop()

    def open_login(self):
        login_window = LoginPage()
        login_window.mainloop()

if __name__ == "__main__":
    app = WelcomePage()
    app.mainloop()
