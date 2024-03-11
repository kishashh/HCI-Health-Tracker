###########################################################
# Imports
###########################################################
from add_food import AddingFood                 # Import add_food to move to it if add food button is clicked
from home_screen import NutritionTracker        # Import home_screen to make screen
from intro import WelcomePage                   # Import intro to pull up first
import tkinter as tk                            # Library for making GUIs



###########################################################
# Main Class
###########################################################
class main():                                   # Main class for application
    def __init__(self):                         # Defining application basics
        super().__init__()
        self.geometry('1050x500')               # Defining dimensions of self

        self.title("Nutrition Tracker")         # Assign name to application

        self.create_widgets()                   # Call on create_widgets def

    def create_widgets(self):                   # Creating widgets for application
        WelcomePage()

    # Function that clears screen to allow new variables to be used
    #def clear_screen(self):
    #    for widget in self.winfo_children():    # Calls on all window children variables
    #        widget.destroy()                    # Destroys all window children variables

    def to_adding_food(self):
        #self.clear_screen()
        #self = AddingFood.self
        self.destroy()
        main_window = AddingFood()
        main_window.mainloop()



###########################################################
# Main to keep application working
###########################################################
if __name__ == "__main__":
    app = main()
    app.mainloop()
