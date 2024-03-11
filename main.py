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
class Controller(tk.Tk):                        # Main class for application
    def __init__(self):
        super().__init__()                      # Call the constructor of the Tk class
        self.destroy()                          # Destroy extra window (will throw error for now)
        intro.WelcomePage()                     # Call on intro file to start file
        
    def run(self):
        self.root.mainloop()                    # Start the main event loop

    # Function that clears screen to allow new variables to be used
    #def clear_screen(self):
    #    for widget in self.winfo_children():    # Calls on all window children variables
    #        widget.destroy()                    # Destroys all window children variables



###########################################################
# Main to keep application working
###########################################################
if __name__ == "__main__":
    app = Controller()
    app.mainloop()
