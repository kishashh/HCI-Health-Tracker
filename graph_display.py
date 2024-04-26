###########################################################
# Imports
###########################################################
import tkinter as tk                            # Library for making GUIs
from tkinter import ttk                         # Import ttk module for Combobox
import home_screen                              # Import main to move to it if continue button is clicked


from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


###########################################################
# GraphDisplay Class
###########################################################


class GraphDisplay(tk.Tk):                      # Main class for the application
    def __init__(self):
        super().__init__()                      # Initialize the superclass (tk.Tk)
        self.title("Progress Graph")            # Set the window title

        self.geometry("1050x500")               # Set the window size

        self.configure(background="gray")       # Assign gray to window background

        self.create_widgets()                   # Call method to create widgets

    def create_widgets(self):
        # "Your Progress!" text at the top middle

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


    def open_main(self):
        self.destroy()                          # Optionally, hide the main window
        main_window = home_screen.NutritionTracker()
        main_window.mainloop()                  # Optional: makes the second window modal



###########################################################
# Main to initialize and run the application
###########################################################
if __name__ == "__main__":
    app = GraphDisplay()
    app.mainloop()
