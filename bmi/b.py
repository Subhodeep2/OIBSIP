# Import necessary libraries
import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Create a DataFrame to store user data
user_data = pd.DataFrame(columns=["Name", "Weight (kg)", "Height (m)", "BMI"])

# Function to calculate BMI
def calculate_bmi():
    try:
        # Get weight and height from user input
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        # Calculate BMI
        bmi = weight / (height ** 2)
        return round(bmi, 2)
    except ValueError:
        # Handle errors if the input is not a number
        return None

# Function to categorize BMI
def categorize_bmi(bmi):
    if bmi is not None:
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        elif 30 <= bmi < 34.9:
            return "Obese Class 1"
        elif 35 <= bmi < 39.9:
            return "Obese Class 2"
        else:
            return "Obese Class 3"
    else:
        return "N/A"

# Function to update and display BMI
def update_bmi():
    bmi = calculate_bmi()
    category = categorize_bmi(bmi)
    if bmi is not None:
        # Update the result label with calculated BMI and category
        label_result.config(text=f"BMI: {bmi} ({category})", fg="black")
        # Change text color based on the BMI category
        if category == "Underweight":
            label_result.config(fg="yellow")
        elif category == "Normal":
            label_result.config(fg="green")
        elif category == "Overweight" or category.startswith("Obese"):
            label_result.config(fg="red")
    else:
        # Display "N/A" if BMI cannot be calculated
        label_result.config(text="BMI: N/A", fg="black")

# Function to save user data
def save_data():
    global user_data
    name = entry_name.get()
    weight = entry_weight.get()
    height = entry_height.get()
    bmi = calculate_bmi()
    
    if bmi is not None:
        data = {"Name": [name], "Weight (kg)": [weight], "Height (m)": [height], "BMI": [bmi]}
        new_entry = pd.DataFrame(data)
    
        if not user_data.empty:
            user_data = user_data.append(new_entry, ignore_index=True)
        else:
            user_data = new_entry
            
        user_data.to_csv("user_data.csv", index=False)
        messagebox.showinfo("Success", "Data saved successfully!")
    else:
        messagebox.showerror("Error", "Please enter valid weight and height.")

# Function to display BMI history
def show_history():
    history_window = tk.Toplevel(root)
    history_window.title("BMI History")
    
    # Create a Treeview to display user data
    tree = ttk.Treeview(history_window, columns=("Name", "Weight (kg)", "Height (m)", "BMI"))
    tree.heading("#1", text="Name")
    tree.heading("#2", text="Weight (kg)")
    tree.heading("#3", text="Height (m)")
    tree.heading("#4", text="BMI")
    
    for index, row in user_data.iterrows():
        # Insert user data into the Treeview
        tree.insert("", "end", values=(row["Name"], row["Weight (kg)"], row["Height (m)"], f"{row['BMI']} ({categorize_bmi(row['BMI'])})"))
    
    tree.pack()

    # Function to visualize data
    def show_data_visualization():
        fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
        ax.set_title("BMI Distribution")
        
        # Categorize BMI and plot a bar graph
        categories = user_data["BMI"].apply(categorize_bmi)
        categories.value_counts().plot(kind="bar", ax=ax)       
        ax.set_xlabel("BMI Categories")
        ax.set_ylabel("Count")
        
        # Embed the Matplotlib figure into the Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=history_window)
        canvas.get_tk_widget().pack()
        canvas.draw()
    
    button_visualize = tk.Button(history_window, text="Visualize Data", command=show_data_visualization, font=font_style)
    button_visualize.pack(pady=10)

# GUI setup
root = tk.Tk()
root.title("BMI Calculator")

font_style = ("Helvetica", 14)
bg_color = "#F3EFEF"

root.configure(bg=bg_color)

label_name = tk.Label(root, text="Name:", font=font_style, bg=bg_color)
entry_name = tk.Entry(root, font=font_style)
label_weight = tk.Label(root, text="Weight (kg):", font=font_style, bg=bg_color)
entry_weight = tk.Entry(root, font=font_style)
label_height = tk.Label(root, text="Height (m):", font=font_style, bg=bg_color)
entry_height = tk.Entry(root, font=font_style)
button_calculate = tk.Button(root, text="Calculate BMI", command=update_bmi, font=font_style)
label_result = tk.Label(root, text="BMI: N/A", font=font_style, bg=bg_color, fg="black")
button_save = tk.Button(root, text="Save Data", command=save_data, font=font_style)
button_history = tk.Button(root, text="View History", command=show_history, font=font_style)

label_name.pack(pady=10)
entry_name.pack(pady=5)
label_weight.pack(pady=10)
entry_weight.pack(pady=5)
label_height.pack(pady=10)
entry_height.pack(pady=5)
button_calculate.pack(pady=10)
label_result.pack(pady=5)
button_save.pack(pady=10)
button_history.pack(pady=10)

# Start the GUI application
root.mainloop()
