###########################################################
# Imports
###########################################################
import add_food                                 # Import add_food to move to it if add food button is clicked
import tkinter as tk                            # Library for making GUIs
import graph_display                            #



###########################################################
# NutritionTracker Class
###########################################################
class NutritionTracker(tk.Tk):                  # Main class for application
    def __init__(self):                         # Defining application basics
        super().__init__()
        self.geometry('1050x500')               # Defining dimensions of self

        self.title("Nutrition Tracker")         # Assign name to application

        self.configure(background="gray")       # Assign gray to window background

        self.create_widgets()                   # Call on create_widgets def

    def create_widgets(self):                   # Creating widgets for application
        home_screen_label = tk.Label(self, text="Home", font=("Arial", 20))    # Food name section
        home_screen_label.pack(pady=(10, 20))   # Add some padding

        add_food_button = tk.Button(self, text="Add Food", command=self.to_adding_food)   # Button to add food
        add_food_button.pack(pady=(10,20))      # Add some padding

        add_food_button = tk.Button(self, text="Show Progress", command=self.to_show_progress)   # Button to add food
        add_food_button.pack(pady=(10,20))      # Add some padding

    # Function that clears screen to allow new variables to be used
    #def clear_screen(self):
    #    for widget in self.winfo_children():    # Calls on all window children variables
    #        widget.destroy()                    # Destroys all window children variables

    def to_adding_food(self):                   # Def to delete screen and start add_food screen
        #self.clear_screen()
        #self = AddingFood.self
        self.destroy()                          # Delete current screen
        main_window = add_food.AddingFood()     # Starts add_food
        main_window.mainloop()                  # Starts loop for window

    def to_show_progress(self):                 # Def to delete screen and start  screen
        #self.clear_screen()
        #self = AddingFood.self
        self.destroy()                          # Delete current screen
        main_window = graph_display.GraphDisplay()# 
        main_window.mainloop()                  # Starts loop for window



###########################################################
# Main to initialize and run the application
###########################################################
if __name__ == "__main__":
    app = NutritionTracker()
    app.mainloop()