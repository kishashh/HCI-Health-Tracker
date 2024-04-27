###########################################################
# Imports
###########################################################
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
import os
from datetime import datetime



from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure



###########################################################
# Nutrition Tracker Class
###########################################################
class NutritionTracker(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Nutrition Tracker")
        self.geometry("1050x500")
        # Image for intro and login background
        self.intro_login_bg_image = PhotoImage(file='intro_login_background.png')
        self.configure(background="gray")
        self.create_widgets_intro()
        self.food_entries = []  # Initialize the food_entries list
        self.current_user = None  # Initialize a variable to hold the username persistently

        



    #######################################################
    # Making Intro
    #######################################################
    def create_widgets_intro(self):
        # Clear screen for new screen contents, does not do anything when first turning on
        self.clear_screen()

        # Add label for adding background image
        background_label = tk.Label(self, image=self.intro_login_bg_image)
        background_label.place(relwidth=1.0, relheight=1.0)

        # Add label at the top of the intro screen
        welcome_label = tk.Label(self, text="Welcome!", font=("Arial", 24))
        welcome_label.place(relx=0.5, rely=0.1, anchor="center")

        # Add label for adding name
        name_label = tk.Label(self, text="Name:", font=("Arial", 14))
        name_label.place(relx=0.35, rely=0.25, anchor="center")

        # Add entry for name
        self.name_entry = tk.Entry(self, font=("Arial", 14))
        self.name_entry.place(relx=0.35, rely=0.3125, anchor="center")

        # Add label for age
        age_label = tk.Label(self, text="Age", font=("Arial", 14))
        age_label.place(relx=0.35, rely=0.375, anchor="center")

        # Add entry for age
        self.age_entry = tk.Entry(self, font=("Arial", 14))
        self.age_entry.place(relx=0.35, rely=0.4375, anchor="center")

        # Add label for weight
        weight_label = tk.Label(self, text="Weight:", font=("Arial", 14))
        weight_label.place(relx=0.35, rely=0.5, anchor="center")

        # Add entry for weight
        self.weight_entry = tk.Entry(self, font=("Arial", 14))
        self.weight_entry.place(relx=0.35, rely=0.5625, anchor="center")

        # Add label for sex with options for sex
        sex_label = tk.Label(self, text="Sex:", font=("Arial", 14))
        sex_label.place(relx=0.35, rely=0.625, anchor="center")
        gender_options = ["Male", "Female"]

        # Add combo box for selecting sex
        self.sex_combobox = ttk.Combobox(self, values=gender_options, state="readonly", font=("Arial", 14))
        self.sex_combobox.set("Select a Sex")
        self.sex_combobox.place(relx=0.35, rely=0.6875, anchor="center")

        # Add label for height
        height_label = tk.Label(self, text="Height (in):", font=("Arial", 14))
        height_label.place(relx=0.65, rely=0.3125, anchor="center")

        # Add entry for height
        self.height_entry = tk.Entry(self, font=("Arial", 14))
        self.height_entry.place(relx=0.65, rely=0.375, anchor="center")

        # Add label for activity
        activity_label = tk.Label(self, text="Activity:", font=("Arial", 14))
        activity_label.place(relx=0.65, rely=0.4375, anchor="center")

        # Add combo box options and combo box for activity
        activity_options = ["None", "Light (1-3 days)", "Moderate (3-5 days)", "Hard (6-7 days)"]
        self.activity_combobox = ttk.Combobox(self, values=activity_options, state="readonly", font=("Arial", 14))
        self.activity_combobox.set("Select an Activity Level")
        self.activity_combobox.place(relx=0.65, rely=0.5, anchor="center")

        # Add label for plan option
        plan_label = tk.Label(self, text="Plan:", font=("Arial", 14))
        plan_label.place(relx=0.65, rely=0.5625, anchor="center")

        # Add combo box options and combo box for selecting plan
        plan_options = ["Gain Weight", "Maintain Weight", "Lose Weight"]
        self.plan_combobox = ttk.Combobox(self, values=plan_options, state="readonly", font=("Arial", 14))
        self.plan_combobox.set("Select a Plan")
        self.plan_combobox.place(relx=0.65, rely=0.625, anchor="center")

        # Add continue button
        continue_button = tk.Button(self, text="Continue", command=self.save_data_and_continue, font=("Arial", 14))
        continue_button.place(relx=0.35, rely=0.85, anchor="center")

        # Add login button
        login_button = tk.Button(self, text="Log in Already", command=self.create_widgets_login, font=("Arial", 14))
        login_button.place(relx=0.65, rely=0.85, anchor="center")

    def save_data_and_continue(self):
        # Gather user data
        user_name = self.name_entry.get()
        # calorie_goal = self.calculate_calorie_goal()
        # Get the current date
        current_date = datetime.now().strftime("%m/%d/%Y")
        
        # Ensure that the name field is not empty
        if not user_name.strip():
            messagebox.showerror("Error", "Please enter your name.")
            return
        
        # Calculate the calorie goal
        calorie_goal = self.calculate_calorie_goal()
        
        # Save data to file named after the user in the "Accounts" folder
        results_folder = "Accounts"
        os.makedirs(results_folder, exist_ok=True)  # Ensure the directory exists
        filename = os.path.join(results_folder, f"{user_name}.txt")
        
        results_folder = "Results"
        os.makedirs(results_folder, exist_ok=True)  # Ensure the directory exists
        filename2 = os.path.join(results_folder, f"{user_name}.txt")
        
        with open(filename, 'w') as file:
            # Write the name and calorie goal to the file in the specified format
            file.write(f"{user_name}, {calorie_goal}, {current_date}\n")
        
        with open(filename2, 'w') as file:
            file.write("")

        self.current_user = user_name
        
        # Now proceed to the home screen
        self.create_widgets_home_screen(user_name, calorie_goal)


    
    def calculate_calorie_goal(self):
        # Assuming all entries have been validated and converted to the appropriate data types.
        age = int(self.age_entry.get())
        weight_pounds = float(self.weight_entry.get())
        height_inches = float(self.height_entry.get())
        sex = self.sex_combobox.get()
        activity_level = self.activity_combobox.get()
        plan = self.plan_combobox.get()

        # Define activity level factors
        activity_factors = {
            "None": 1.2,
            "Light (1-3 days)": 1.375,
            "Moderate (3-5 days)": 1.55,
            "Hard (6-7 days)": 1.9
        }

        # Define weight goal factors
        weight_goal_factors = {
            "Lose Weight": -500,
            "Maintain Weight": 0,
            "Gain Weight": 500
        }

        # Calculate BMR (Basal Metabolic Rate)
        if sex == "Female":
            bmr = 655 + (4.35 * weight_pounds) + (4.7 * height_inches) - (4.7 * age)
        else:  # Male
            bmr = 66 + (6.23 * weight_pounds) + (12.7 * height_inches) - (6.8 * age)

        # Calculate total daily calorie needs
        daily_calories = bmr * activity_factors[activity_level]

        # Adjust based on weight goal
        calorie_goal = daily_calories + weight_goal_factors[plan]

        return int(calorie_goal)


    #######################################################
    # Making Home Screen
    #######################################################
    def create_widgets_home_screen(self, user_name, calorie_goal):
        self.clear_screen()

        # # Ensure calorie goal is an integer if it's not already handled in the calculation
        # if isinstance(calorie_goal, float):
        #     calorie_goal = int(calorie_goal)

        # Add sentence about calorie goal for specific day
        greeting_label = tk.Label(self, text=f"Hello {user_name}, your calorie goal is {calorie_goal}", font=("Arial", 14))
        greeting_label.place(relx=0.5, rely=0.2, anchor="center")

        # Add label for home
        home_screen_label = tk.Label(self, text="Home", font=("Arial", 24))
        home_screen_label.place(relx=0.5, rely=0.1, anchor="center")

        # Add button to go to add food
        add_food_button = tk.Button(self, text="Add Food", command=lambda: self.create_widgets_add_food(user_name, calorie_goal), font=("Arial", 14))
        add_food_button.place(relx=0.35, rely=0.5, anchor="center")

        # Add button to go to progress page
        show_progress = tk.Button(self, text="Show Progress", command=lambda: self.create_widgets_progress(user_name, calorie_goal), font=("Arial", 14))

        show_progress.place(relx=0.65, rely=0.5, anchor="center")

        # Add logout button
        logout_button = tk.Button(self, text="Logout", background = "red", command=self.create_widgets_intro, font=("Arial", 14))
        logout_button.place(relx=1.0, anchor="ne")


    #######################################################
    # Making Add Food Screen
    #######################################################
    def create_widgets_add_food(self, user_name, calorie_goal):          # Creating widgets for application
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

        # Add back button
        back_button = tk.Button(self, text="Back", command=lambda: self.create_widgets_home_screen(user_name, calorie_goal), font=("Arial", 14))
        back_button.place(relx=0.5, rely=0.85, anchor="center")

        # Add logout button
        logout_button = tk.Button(self, text="Logout", background = "red", command=self.create_widgets_intro, font=("Arial", 14))
        logout_button.place(relx=1.0, anchor="ne")

    def add_food(self):                         # Def related to adding food button
        food = self.food_entry.get()            # Calls for food name input
        calories = self.calories_entry.get()    # Calls for calories input
        protein = self.protein_entry.get()      # Calls for protein input
        fat = self.fat_entry.get()              # Calls for fat input
        carbs = self.carbs_entry.get()          # Calls for carbs input

        if food and calories and protein and fat and carbs:                 # If all entries have input, append then add them to food_listbox
            self.food_entries.append((food, calories, protein, fat, carbs))
            self.food_listbox.insert(tk.END, f"{food} - Calories: {calories}, Protein: {protein}, Fat: {fat}, Carbs: {carbs}")
            self.save_food_entry(calories, protein, carbs, fat)
            self.clear_entries()                # Empties boxes for new food item
        else:
            messagebox.showerror("Error", "Please fill in all fields.")  # Error if there is an empty field

    def save_food_entry(self, calories, protein, carbs, fat):
        if self.current_user is None:
            messagebox.showerror("Error", "No user logged in.")
            return
        current_date = datetime.now().strftime("%m/%d/%Y")
        results_folder = "Results"
        os.makedirs(results_folder, exist_ok=True)
        filename = os.path.join(results_folder, f"{self.current_user}.txt")

        with open(filename, 'a') as file:
            file.write(f"{current_date}, {calories}, {protein}, {carbs}, {fat}\n")

    def clear_entries(self):                    # Empties contents of all entries for new entries to be added
        self.food_entry.delete(0, tk.END)       # Clears food entry
        self.calories_entry.delete(0, tk.END)   # Clears calories entry
        self.protein_entry.delete(0, tk.END)    # Clears protein entry
        self.fat_entry.delete(0, tk.END)        # Clears fat entry
        self.carbs_entry.delete(0, tk.END)      # Clears carbs entry

    

    #######################################################
    # Making Progress Screen
    #######################################################
    def create_widgets_progress(self, user_name, calorie_goal):
        # TODO: get the food data from add_food for the information below

        # "Your Progress!" text at the top middle
        self.clear_screen()

        welcome_label = tk.Label(self, text=f"{user_name}'s progress!", font=("Arial", 20))
        welcome_label.pack(pady=(10, 20))       # Add some padding

        frameChartsLT = tk.Frame(self)          # Corrected to use self
        frameChartsLT.pack() 

        barcat = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
        barvalue = [1,2,3,4,5,6,7]
        calavg = sum(barvalue)/7

        bar_fig = Figure(figsize=(5, 5), dpi=100, facecolor='gray')
        bar_ax = bar_fig.add_subplot(111)  # Adjust the subplot position for the bar chart
        bar_ax.bar(barcat, barvalue, color='skyblue')
        bar_ax.set_title('Average Calories this week: ' + str(calavg))
        bar_ax.set_xlabel('Day of the Week')
        bar_ax.set_ylabel('Days Calorie Intake')
        bar_ax.axhline(y=calavg, color='blue', linestyle=':', linewidth=1.5) # dashed line for average 

        chart1 = FigureCanvasTkAgg(bar_fig, frameChartsLT)
        chart1.get_tk_widget().pack(side=tk.LEFT)
        
        piecat = ['Protien', 'Fat', 'Carbs']
        pievalue = [10, 25, 40]    # TODO: make these variables i.e.[protien, fat, carbs] use date like stated above   

        fig = Figure(facecolor='gray')                # create a figure object
        ax = fig.add_subplot(111)               # add an Axes to the figure
        ax.set_title('Calories Left: ')
        ax.pie(pievalue, radius=1, labels=piecat, autopct='%0.2f%%', shadow=False)

        chart1 = FigureCanvasTkAgg(fig, frameChartsLT)
        chart1.get_tk_widget().pack()

        # Add back button
        back_button = tk.Button(self, text="Back", command=lambda: self.create_widgets_home_screen(user_name, calorie_goal), font=("Arial", 14))
        back_button.place(relx=0.5, rely=0.85, anchor="center")

        # Add logout button
        logout_button = tk.Button(self, text="Logout", background = "red", command=self.create_widgets_intro, font=("Arial", 14))
        logout_button.place(relx=1.0, anchor="ne")

    

    #######################################################
    # Making Login Screen
    #######################################################
    def create_widgets_login(self):
        # Clear screen for new screen contents
        self.clear_screen()

        # Add label for adding background image
        background_label = tk.Label(self, image=self.intro_login_bg_image)
        background_label.place(relwidth=1.0, relheight=1.0)

        # Add label for username
        username_label = tk.Label(self, text="Enter your name:", font=("Arial", 14))
        username_label.place(relx=0.5, rely=0.4, anchor="center")

        # Add entry for username
        self.username_entry = tk.Entry(self, font=("Arial", 14))
        self.username_entry.place(relx=0.5, rely=0.5, anchor="center")

        # Set focus to username entry
        self.username_entry.focus_set()

        # Add login Button
        login_button = tk.Button(self, text="Log In", command=self.login_user, font=("Arial", 14))
        login_button.place(relx=0.5, rely=0.6, anchor="center")

        # Add back button
        back_button = tk.Button(self, text="Back", command=self.create_widgets_intro, font=("Arial", 14))
        back_button.place(relx=0.5, rely=0.85, anchor="center")

    def login_user(self):
        # Get the username from the entry
        username = self.username_entry.get()
        results_folder = "Accounts"
        filename = os.path.join(results_folder, f"{username}.txt")
        self.current_user = self.username_entry.get()  # Store the username after a successful login

        
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                # Assuming the last line contains the calorie goal
                calorie_goal = lines[-1].strip().split(", ")[1]

                
            self.create_widgets_home_screen(username, calorie_goal)
        except FileNotFoundError:
            messagebox.showerror("Login Failed", "Account does not exist. Please check your username or register.")


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