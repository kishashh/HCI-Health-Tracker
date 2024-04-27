###########################################################
# Imports
###########################################################
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime, timedelta
from collections import defaultdict
from tkinter import PhotoImage
import os


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
        self.add_food_bg_image = PhotoImage(file='add_food_background.png')
        self.home_bg_image = PhotoImage(file='home_background.png')
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
        welcome_label = tk.Label(self, text="Welcome!", fg="black", highlightthickness=0, font=("Arial", 24))
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

        # Add label for height
        height_label = tk.Label(self, text="Height (in):", font=("Arial", 14))
        height_label.place(relx=0.35, rely=0.625, anchor="center")

        # Add entry for height
        self.height_entry = tk.Entry(self, font=("Arial", 14))
        self.height_entry.place(relx=0.35, rely=0.6875, anchor="center")

        # Add label for sex with options for sex
        sex_label = tk.Label(self, text="Sex:", font=("Arial", 14))
        sex_label.place(relx=0.65, rely=0.3125, anchor="center")
        gender_options = ["Male", "Female"]

        # Add combo box for selecting sex
        self.sex_combobox = ttk.Combobox(self, values=gender_options, state="readonly", font=("Arial", 14))
        self.sex_combobox.set("Select a Sex")
        self.sex_combobox.place(relx=0.65, rely=0.375, anchor="center")

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

        # Add login button
        login_button = tk.Button(self, text="Log in Already", command=self.create_widgets_login, font=("Arial", 14))
        login_button.place(relx=0.35, rely=0.85, anchor="center")

        # Add continue button
        continue_button = tk.Button(self, text="Continue", command=self.save_data_and_continue, font=("Arial", 14))
        continue_button.place(relx=0.65, rely=0.85, anchor="center")

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
        # Clear screen for new screen contents
        self.clear_screen()

        # Add label for adding background image
        background_label = tk.Label(self, image=self.home_bg_image)
        background_label.place(relwidth=1.0, relheight=1.0)

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

        # Add label for adding background image
        background_label = tk.Label(self, image=self.add_food_bg_image)
        background_label.place(relwidth=1.0, relheight=1.0)

        # Add label for food name
        tk.Label(self, text="Food:", font=("Arial", 14), bg="white").place(relx=0.2, rely=0.2, anchor="center")

        # Add label for calories
        tk.Label(self, text="Calories:", font=("Arial", 14), bg="white").place(relx=0.35, rely=0.2, anchor="center")

        # Add label for protein
        tk.Label(self, text="Protein (g):", font=("Arial", 14), bg="white").place(relx=0.5, rely=0.2, anchor="center")

        # Add label for fat
        tk.Label(self, text="Fat (g):", font=("Arial", 14), bg="white").place(relx=0.65, rely=0.2, anchor="center")

        # Add label for carbs
        tk.Label(self, text="Carbs (g):", font=("Arial", 14), bg="white").place(relx=0.8, rely=0.2, anchor="center")

        self.food_entry = tk.Entry(self)                            # Adds widget food name information to self object
        self.food_entry.place(relx=0.2, rely=0.3, anchor="center")       # Assign input box below food label

        self.calories_entry = tk.Entry(self)                        # Adds widget calories information to self object
        self.calories_entry.place(relx=0.35, rely=0.3, anchor="center")   # Assign input box below calories label

        self.protein_entry = tk.Entry(self)                         # Adds widget protein information to self object
        self.protein_entry.place(relx=0.5, rely=0.3, anchor="center")    # Assign input box below protein label

        self.fat_entry = tk.Entry(self)                             # Adds widget fat information to self object
        self.fat_entry.place(relx=0.65, rely=0.3, anchor="center")        # Assign input box below fat label

        self.carbs_entry = tk.Entry(self)                           # Adds widget carbs information to self object
        self.carbs_entry.place(relx=0.8, rely=0.3, anchor="center")      # Assign input box below carbs label

        self.add_button = tk.Button(self, text="Add Food", command=self.add_food, font=("Arial", 14))   # Button to add food
        self.add_button.place(relx=0.5, rely=0.4, anchor="center")                # Placement of the button

        self.food_listbox = tk.Listbox(self, width=50)                              # Creation of the listbox
        self.food_listbox.place(relx=0.5, rely=0.65, anchor="center")       # Placemtn of the listbox

        # Add back button
        back_button = tk.Button(self, text="Back", command=lambda: self.create_widgets_home_screen(user_name, calorie_goal), font=("Arial", 14))
        back_button.place(relx=0.5, rely=0.9, anchor="center")

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
        # Clear screen for new screen contents
        self.clear_screen()

        # Add label for adding background image
        background_label = tk.Label(self, image=self.add_food_bg_image)
        background_label.place(relwidth=1.0, relheight=1.0)

        # Get the current date and format it
        current_date = datetime.now()
        today = current_date.strftime("%A")

        # "{Name}'s Progress!" text at the top middle
        welcome_label = tk.Label(self, text=f"{user_name}'s Progress!", bg="white", font=("Arial", 20))
        welcome_label.pack(pady=(10, 20))           # Add some padding

        frameChartsLT = tk.Frame(self)              # Corrected to use self
        frameChartsLT.pack()

        #######################################################
        # Bar Chart
        #######################################################

        seven_days_ago = ((current_date - timedelta(days=7)).date()).strftime("%m/%d/%Y")

        # Open the user's file and check for matches with dates 7 days ago or earlier
        with open(f'Accounts\{user_name}.txt', 'r') as file:
            for line in file:
                items = line.strip().split(',')
                date_item = items[2].strip()

                date1 = datetime.strptime(date_item, "%m/%d/%Y")
                date2 = datetime.strptime(seven_days_ago, "%m/%d/%Y")

                difference = date1 - date2
                seven_days = timedelta(days=0)

                if difference <= seven_days:
                    # Match found for a date 7 days ago or earlier, do something here
                    # Format DOW
                    if today == "Sunday":
                        barcat = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
                    elif today == "Monday":
                        barcat = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
                    elif today == "Tuesday":
                        barcat = ['Tue','Wed','Thu','Fri','Sat','Sun','Mon']
                    elif today == "Wednesday":
                        barcat = ['Wed','Thu','Fri','Sat','Sun','Mon','Tue']
                    elif today == "Thursday":
                        barcat = ['Thu','Fri','Sat','Sun','Mon','Tue','Wed']
                    elif today == "Friday":
                        barcat = ['Fri','Sat','Sun','Mon','Tue','Wed','Thu']
                    elif today == "Saturday":
                        barcat = ['Sat','Sun','Mon','Tue','Wed','Thu','Fri']
                    else: # THIS CANT EXIST AHHH
                        continue

                    barvalue_temp = defaultdict(int)  # Initialize a dictionary to store sums of values for each unique first item

                    with open(f'Results\{user_name}.txt', 'r') as file:
                        for line in file:
                            calcalc = line.strip().split(',')
                            first_item = calcalc[0].strip()
                            second_item = calcalc[1].strip()

                            # Update the sum of values for the current first item
                            barvalue_temp[first_item] += int(second_item)

                    # Convert the dictionary to a list
                    barvalue_a = [value for key, value in barvalue_temp.items()]
                    barvalue_a.reverse()

                    barvalue = [0,0,0,0,0,0,0]

                    for i in range(7):
                        barvalue[i] = barvalue_a[i+1]

                    calavg = sum(barvalue)/7

                    seven_days_ago = current_date - timedelta(days=7) 
                    bar_fig = Figure(figsize=(3.8, 3.8), dpi=100)
                    bar_ax = bar_fig.add_subplot(111)  # Adjust the subplot position for the bar chart
                    bar_ax.bar(barcat, barvalue, color='skyblue')
                    bar_ax.set_title('Average Calories Past 7 Days: ' + str(calavg)[:6])
                    bar_ax.set_xlabel('Day of the Week')
                    bar_ax.set_ylabel('Calorie Intake')
                    bar_ax.axhline(y=calavg, color='blue', linestyle=':', linewidth=1.5) # dashed line for average 

                    chart1 = FigureCanvasTkAgg(bar_fig, frameChartsLT)
                    chart1.get_tk_widget().pack(side=tk.LEFT)
                else:
                    # No match found, move to the next line
                    continue

        #######################################################
        # Pie Chart
        #######################################################

        # Initialize variables to store the summed values
        calories_total = 0
        protein_total = 0
        fat_total = 0
        carbs_total = 0

        # Open the user's file and check for matches with today's date
        with open(f'Results\{user_name}.txt', 'r') as file:
            for line in file:
                # Check if the current line matches today's date
                items = line.strip().split(',')
                date_item = items[0].strip()

                # Convert the date string to a datetime object
                date_item = datetime.strptime(date_item, "%m/%d/%Y")

                if date_item.date() == current_date.date():
                    # Match found for today's date, sum the values for each nutrient
                    calories_total += int(items[1])     # sums Calories
                    protein_total += int(items[2])      # sums Protein
                    fat_total += int(items[3])          # sums Fat
                    carbs_total += int(items[4])        # sums Carbs
                else:
                    # Stop processing once we've passed today's date
                    continue
        piecat = ['Protien', 'Fat', 'Carbs']
        pievalue = [protein_total, fat_total, carbs_total] 


        fig = Figure(figsize=(3.8, 3.8))                  # create a figure object

        ax = fig.add_subplot(111)                       # add an Axes to the figure
        cal_left =  int(calorie_goal) - calories_total  # calculate how many calories are left in the day
        ax.set_title(f'Calories Left: {cal_left}')      # print out calories left
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