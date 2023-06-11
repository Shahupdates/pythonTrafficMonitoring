import tkinter as tk
from recommendation_system import recommend_handler

# Create a Tkinter window
window = tk.Tk()
window.title("Recommendation System")
window.geometry("400x250")

# Create GUI elements
age_label = tk.Label(window, text="Age:")
age_label.pack()
age_entry = tk.Entry(window)
age_entry.pack()

gender_label = tk.Label(window, text="Gender:")
gender_label.pack()
gender_var = tk.StringVar()
gender_radio_male = tk.Radiobutton(window, text="Male", variable=gender_var, value=1)
gender_radio_male.pack()
gender_radio_female = tk.Radiobutton(window, text="Female", variable=gender_var, value=0)
gender_radio_female.pack()

product_label = tk.Label(window, text="Product Interest:")
product_label.pack()
product_entry = tk.Entry(window)
product_entry.pack()

recommend_button = tk.Button(window, text="Recommend", command=recommend_handler)
recommend_button.pack()

result_label = tk.Label(window, text="Recommendations will appear here")
result_label.pack()

window.mainloop()
