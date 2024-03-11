import tkinter as tk

class NutritionTracker(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Nutrition Tracker")

        self.food_entries = []

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Food:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self, text="Calories:").grid(row=0, column=1, padx=5, pady=5)
        tk.Label(self, text="Protein (g):").grid(row=0, column=2, padx=5, pady=5)
        tk.Label(self, text="Fat (g):").grid(row=0, column=3, padx=5, pady=5)
        tk.Label(self, text="Carbs (g):").grid(row=0, column=4, padx=5, pady=5)

        self.food_entry = tk.Entry(self)
        self.food_entry.grid(row=1, column=0, padx=5, pady=5)

        self.calories_entry = tk.Entry(self)
        self.calories_entry.grid(row=1, column=1, padx=5, pady=5)

        self.protein_entry = tk.Entry(self)
        self.protein_entry.grid(row=1, column=2, padx=5, pady=5)

        self.fat_entry = tk.Entry(self)
        self.fat_entry.grid(row=1, column=3, padx=5, pady=5)

        self.carbs_entry = tk.Entry(self)
        self.carbs_entry.grid(row=1, column=4, padx=5, pady=5)

        self.add_button = tk.Button(self, text="Add Food", command=self.add_food)
        self.add_button.grid(row=2, column=0, columnspan=5, pady=10)

        self.food_listbox = tk.Listbox(self, width=50)
        self.food_listbox.grid(row=3, column=0, columnspan=5, padx=5, pady=5)

    def add_food(self):
        food = self.food_entry.get()
        calories = self.calories_entry.get()
        protein = self.protein_entry.get()
        fat = self.fat_entry.get()
        carbs = self.carbs_entry.get()

        if food and calories and protein and fat and carbs:
            self.food_entries.append((food, calories, protein, fat, carbs))
            self.food_listbox.insert(tk.END, f"{food} - Calories: {calories}, Protein: {protein}, Fat: {fat}, Carbs: {carbs}")
            self.clear_entries()
        else:
            tk.messagebox.showerror("Error", "Please fill in all fields.")

    def clear_entries(self):
        self.food_entry.delete(0, tk.END)
        self.calories_entry.delete(0, tk.END)
        self.protein_entry.delete(0, tk.END)
        self.fat_entry.delete(0, tk.END)
        self.carbs_entry.delete(0, tk.END)

if __name__ == "__main__":
    app = NutritionTracker()
    app.mainloop()
