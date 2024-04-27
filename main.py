###########################################################
# Imports
###########################################################
import tkinter as tk
from tkinter import ttk
import os
from tkinter import messagebox


from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure



###########################################################
# Nutrition Tracker Class
###########################################################
class NutritionTracker(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Welcome Page")
        self.geometry("1050x500")
        self.configure(background="gray")
        self.create_widgets_intro()



    #######################################################
    # Making Intro
    #######################################################
    def create_widgets_intro(self):
        self.clear_screen()
        welcome_label = tk.Label(self, text="Welcome!", font=("Arial", 20))
        welcome_label.pack(pady=(10, 20))

        name_label = tk.Label(self, text="Name:")
        name_label.pack()

        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        age_label = tk.Label(self, text="Age")
        age_label.pack()

        self.age_entry = tk.Entry(self)
        self.age_entry.pack()

        weight_label = tk.Label(self, text="Weight:")
        weight_label.pack()

        self.weight_entry = tk.Entry(self)
        self.weight_entry.pack()

        sex_label = tk.Label(self, text="Sex:")
        sex_label.pack()
        gender_options = ["Male", "Female"]

        self.sex_combobox = ttk.Combobox(self, values=gender_options, state="readonly")
        self.sex_combobox.set("Select a Sex")
        self.sex_combobox.pack()

        height_label = tk.Label(self, text="Height (in):")
        height_label.pack()

        self.height_entry = tk.Entry(self)
        self.height_entry.pack()

        activity_label = tk.Label(self, text="Activity:")
        activity_label.pack()
        activity_options = ["None", "Light (1-3 days)", "Moderate (3-5 days)", "Hard (6-7 days)"]
        self.activity_combobox = ttk.Combobox(self, values=activity_options, state="readonly")
        self.activity_combobox.set("Select an Activity Level")
        self.activity_combobox.pack()

        plan_label = tk.Label(self, text="Plan:")
        plan_label.pack()

        plan_options = ["Gain Weight", "Maintain Weight", "Lose Weight"]
        self.plan_combobox = ttk.Combobox(self, values=plan_options, state="readonly")
        self.plan_combobox.set("Select a Plan")
        self.plan_combobox.pack()

        continue_button = tk.Button(self, text="Continue", command=self.save_data_and_continue)
        continue_button.pack()

        login_button = tk.Button(self, text="Log in Already", command=self.create_widgets_login)
        login_button.pack()
    def save_data_and_continue(self):
        # Gather user data
        user_data = {
            "name": self.name_entry.get(),
            "age": self.age_entry.get(),
            "weight": self.weight_entry.get(),
            "sex": self.sex_combobox.get(),
            "height": self.height_entry.get(),
            "activity": self.activity_combobox.get(),
            "plan": self.plan_combobox.get()
        }

        # Save data to file named after the user in the "Accounts" folder
        accounts_folder = "Accounts"
        os.makedirs(accounts_folder, exist_ok=True)  # Ensure the directory exists
        filename = os.path.join(accounts_folder, f"{user_data['name']}.txt")
        with open(filename, 'w') as file:
            for key, value in user_data.items():
                file.write(f"{key}: {value}\n")

        # Now proceed to the home screen
        self.create_widgets_home_screen()
    

    #######################################################
    # Making Home Screen
    #######################################################
    def create_widgets_home_screen(self):       # Creating widgets for application
        self.clear_screen()
        home_screen_label = tk.Label(self, text="Home", font=("Arial", 20))    # Food name section
        home_screen_label.pack(pady=(10, 20))   # Add some padding

        add_food_button = tk.Button(self, text="Add Food", command=self.create_widgets_add_food)   # Button to add food
        add_food_button.pack(pady=(10,20))      # Add some padding

        add_food_button = tk.Button(self, text="Show Progress", command=self.create_widgets_progress_graph)   # Button to add food
        add_food_button.pack(pady=(10,20))      # Add some padding



    #######################################################
    # Making Add Food Screen
    #######################################################
    def create_widgets_add_food(self):          # Creating widgets for application
        self.clear_screen()
        tk.Label(self, text="Food:").grid(row=0, column=0, padx=5, pady=5)          # Food name section
        tk.Label(self, text="Calories:").grid(row=0, column=1, padx=5, pady=5)      # Calories section
        tk.Label(self, text="Protein (g):").grid(row=0, column=2, padx=5, pady=5)   # Protein section
        tk.Label(self, text="Fat (g):").grid(row=0, column=3, padx=5, pady=5)       # Fat section
        tk.Label(self, text="Carbs (g):").grid(row=0, column=4, padx=5, pady=5)     # Carbs section

        self.food_entry = tk.Entry(self)                            # Adds widget food name information to self object
        self.food_entry.grid(row=1, column=0, padx=5, pady=5)       # Assign input box below food label

        self.calories_entry = tk.Entry(self)                        # Adds widget calories information to self object
        self.calories_entry.grid(row=1, column=1, padx=5, pady=5)   # Assign input box below calories label

        self.protein_entry = tk.Entry(self)                         # Adds widget protein information to self object
        self.protein_entry.grid(row=1, column=2, padx=5, pady=5)    # Assign input box below protein label

        self.fat_entry = tk.Entry(self)                             # Adds widget fat information to self object
        self.fat_entry.grid(row=1, column=3, padx=5, pady=5)        # Assign input box below fat label

        self.carbs_entry = tk.Entry(self)                           # Adds widget carbs information to self object
        self.carbs_entry.grid(row=1, column=4, padx=5, pady=5)      # Assign input box below carbs label

        self.add_button = tk.Button(self, text="Add Food", command=self.add_food)   # Button to add food
        self.add_button.grid(row=2, column=0, columnspan=5, pady=10)                # Placement of the button

        self.food_listbox = tk.Listbox(self, width=50)                              # Creation of the listbox
        self.food_listbox.grid(row=3, column=0, columnspan=5, padx=5, pady=5)       # Placemtn of the listbox

        self.add_button = tk.Button(self, text="Back to Home", command=self.back_to_home)  # Button to go back to home screen
        self.add_button.grid(row=4, column=0, columnspan=5, pady=10)                # Placemtn of the listbox

    def add_food(self):                         # Def related to adding food button
        food = self.food_entry.get()            # Calls for food name input
        calories = self.calories_entry.get()    # Calls for calories input
        protein = self.protein_entry.get()      # Calls for protein input
        fat = self.fat_entry.get()              # Calls for fat input
        carbs = self.carbs_entry.get()          # Calls for carbs input

        if food and calories and protein and fat and carbs:                 # If all entries have input, append then add them to food_listbox
            self.food_entries.append((food, calories, protein, fat, carbs))
            self.food_listbox.insert(tk.END, f"{food} - Calories: {calories}, Protein: {protein}, Fat: {fat}, Carbs: {carbs}")
            self.clear_entries()                # Empties boxes for new food item
        else:
            tk.messagebox.showerror("Error", "Please fill in all fields.")  # Error if there is an empty field

    def clear_entries(self):                    # Empties contents of all entries for new entries to be added
        self.food_entry.delete(0, tk.END)       # Clears food entry
        self.calories_entry.delete(0, tk.END)   # Clears calories entry
        self.protein_entry.delete(0, tk.END)    # Clears protein entry
        self.fat_entry.delete(0, tk.END)        # Clears fat entry
        self.carbs_entry.delete(0, tk.END)      # Clears carbs entry

    

    #######################################################
    # Making Progress Screen
    #######################################################
    def create_widgets_progress(self):
        # "Your Progress!" text at the top middle
        self.clear_screen()

        welcome_label = tk.Label(self, text="Your progress!", font=("Arial", 20))
        welcome_label.pack(pady=(10, 20))       # Add some padding

        frameChartsLT = tk.Frame(self)          # Corrected to use self
        frameChartsLT.pack()

        # TODO: add bar chart to the left of the pie chart for weekly progress

        # TODO: get the food data from add_food for the information below
        stockListExp = ['Protien', 'Fat', 'Carbs']
        stockSplitExp = [10, 25, 40]    # TODO: make these variables i.e.[protien, fat, carbs] use date like stated above    

        fig = Figure(facecolor='gray')                          # create a figure object
        ax = fig.add_subplot(111)               # add an Axes to the figure
        ax.pie(stockSplitExp, radius=1, labels=stockListExp, autopct='%0.2f%%', shadow=False)

        chart1 = FigureCanvasTkAgg(fig, frameChartsLT)
        chart1.get_tk_widget().pack()

        continue_button = tk.Button(self, text="Continue", command=self.open_main)
        continue_button.pack()

    

    #######################################################
    # Making Login Screen
    #######################################################
    def create_widgets_login(self):
        self.clear_screen()
        # Username Entry
        username_label = tk.Label(self, text="Enter your name:", font=("Arial", 14))
        username_label.pack(pady=(20, 10))

        self.username_entry = tk.Entry(self, font=("Arial", 14))
        self.username_entry.pack()

            # Set focus to username entry
        self.username_entry.focus_set()

        # Login Button
        login_button = tk.Button(self, text="Log In", command=self.login_user, font=("Arial", 14))
        login_button.pack(pady=(10, 20))
    def login_user(self):
            # Get the username from the entry
        username = self.username_entry.get()

        # Check if the account file exists
        account_file_path = os.path.join("Accounts", f"{username}.txt")
        if os.path.exists(account_file_path):
            # File exists, log in successful, proceed to home screen
            self.create_widgets_home_screen()
        else:
            # File does not exist, show an error or prompt to create an account
            error_label = tk.Label(self, text="Account not found, please try again or register.", foreground="red")
            error_label.pack()


    #######################################################
    # Clears Screen for New Content
    #######################################################
    # Function that clears screen to allow new variables to be used
    def clear_screen(self):
        for widget in self.winfo_children():    # Calls on all window children variables
            widget.destroy()                    # Destroys all window children variables



###########################################################
# Main to initialize and run the application
###########################################################
if __name__ == "__main__":
    app = NutritionTracker()
    app.mainloop()