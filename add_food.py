###########################################################
# Imports
###########################################################
import home_screen                              # Import main to move to it if back button is clicked
import main
import tkinter as tk                            # Library for making GUIs



###########################################################
# AddingFood Class
###########################################################
class AddingFood(tk.Tk):                        # Adding food class for application
    def __init__(self):                         # Defining application basics
        super().__init__()
        self.title("Nutrition Tracker: Adding Food")    # Assign name to application

        self.geometry('1050x500')               # Defining dimensions of self

        self.configure(background="gray")       # Assign gray to window background

        self.food_entries = []                  # Make array for food entries

        self.create_widgets()                   # Call on create_widgets def

    def create_widgets(self):                   # Creating widgets for application
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

    def back_to_home(self):
        self.destroy()
        main_window = home_screen.NutritionTracker()
        main_window.mainloop()


###########################################################
# Main to keep application working
###########################################################
if __name__ == "__main__":
    app = AddingFood()
    app.mainloop()