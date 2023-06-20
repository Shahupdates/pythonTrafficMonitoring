import tkinter as tk
from tkinter import messagebox
from recommendation_system import recommend_handler

class RecommendationApp:
    def __init__(self, root):
        self.window = root
        self.window.title("Recommendation System")
        self.window.geometry("400x400")

        self.age_var = tk.StringVar()
        self.gender_var = tk.StringVar()
        self.product_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Age Input
        age_frame = tk.Frame(self.window)
        age_frame.pack(fill='x', padx=20, pady=10)
        tk.Label(age_frame, text="Age:").pack(side='left')
        tk.Entry(age_frame, textvariable=self.age_var).pack(fill='x', expand=True)

        # Gender Input
        gender_frame = tk.Frame(self.window)
        gender_frame.pack(fill='x', padx=20, pady=10)
        tk.Label(gender_frame, text="Gender:").pack(side='left')
        tk.Radiobutton(gender_frame, text="Male", variable=self.gender_var, value='male').pack(side='left')
        tk.Radiobutton(gender_frame, text="Female", variable=self.gender_var, value='female').pack(side='left')

        # Product Input
        product_frame = tk.Frame(self.window)
        product_frame.pack(fill='x', padx=20, pady=10)
        tk.Label(product_frame, text="Product Interest:").pack(side='left')
        tk.Entry(product_frame, textvariable=self.product_var).pack(fill='x', expand=True)

        # Recommendation button
        tk.Button(self.window, text="Recommend", command=self.recommend).pack(pady=10)

        # Results display
        self.result_label = tk.Label(self.window, text="Recommendations will appear here")
        self.result_label.pack(padx=20, pady=10)

    def recommend(self):
        age = self.age_var.get().strip()
        gender = self.gender_var.get()
        product = self.product_var.get().strip()

        # Basic input validation
        if not age.isdigit():
            messagebox.showerror('Input Error', 'Please enter a valid age.')
            return
        if gender not in ['male', 'female']:
            messagebox.showerror('Input Error', 'Please select a gender.')
            return
        if not product:
            messagebox.showerror('Input Error', 'Please enter a product of interest.')
            return

        recommendations = recommend_handler(age, gender, product)
        self.result_label.config(text=f"Recommendations: {', '.join(recommendations)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RecommendationApp(root)
    root.mainloop()
