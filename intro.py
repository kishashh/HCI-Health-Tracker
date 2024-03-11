###########################################################
# Imports
###########################################################
import tkinter as tk                            # Library for making GUIs
from tkinter import ttk                         # Import ttk module for Combobox
import home_screen                              # Import main to move to it if continue button is clicked



###########################################################
# WelcomePage Class
###########################################################
class WelcomePage(tk.Tk):                       # Main class for the application
    def __init__(self):
        super().__init__()                      # Initialize the superclass (tk.Tk)
        self.title("Welcome Page")              # Set the window title

        self.geometry("1050x500")               # Set the window size

        self.configure(background="gray")       # Assign gray to window background

        self.create_widgets()                   # Call method to create widgets

    def create_widgets(self):
        # "Welcome!" text at the top middle
        welcome_label = tk.Label(self, text="Welcome!", font=("Arial", 20))
        welcome_label.pack(pady=(10, 20))       # Add some padding

        name_label = tk.Label(self, text="Name:")
        name_label.pack()

        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        # Weight Entry
        weight_label = tk.Label(self, text="Weight:")
        weight_label.pack()

        self.weight_entry = tk.Entry(self)      # Make it an instance attribute if needed elsewhere
        self.weight_entry.pack()

        # Plan Dropdown (Combobox)
        plan_label = tk.Label(self, text="Plan:")
        plan_label.pack()

        # Define the options for the plan
        plan_options = ["Gain Weight", "Maintain Weight", "Lose Weight"]
        self.plan_combobox = ttk.Combobox(self, values=plan_options, state="readonly")
        self.plan_combobox.set("Select a Plan") # Default placeholder text
        self.plan_combobox.pack()

        continue_button = tk.Button(self, text = "Continue",command=self.open_main)
        continue_button.pack()


        # Add more widgets or functionality as needed

    def open_main(self):
        self.destroy()                          # Optionally, hide the main window
        main_window = home_screen.NutritionTracker()
        main_window.mainloop()                  # Optional: makes the second window modal



###########################################################
# Main to initialize and run the application
###########################################################
if __name__ == "__main__":
    app = WelcomePage()
    app.mainloop()
