###########################################################
# Imports
###########################################################
import add_food                                 # Import add_food to move to it if add food button is clicked
import home_screen                              # Import home_screen to make screen
import intro                                    # Import intro to pull up first
import tkinter as tk                            # Library for making GUIs



###########################################################
# Main Class
###########################################################
class main():                                   # Main class for application
    intro.WelcomePage()

    # Function that clears screen to allow new variables to be used
    #def clear_screen(self):
    #    for widget in self.winfo_children():    # Calls on all window children variables
    #        widget.destroy()                    # Destroys all window children variables



###########################################################
# Main to keep application working
###########################################################
if __name__ == "__main__":
    app = main()
    app.mainloop()
