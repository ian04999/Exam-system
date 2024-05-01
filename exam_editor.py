import tkinter as tk
from tkinter import messagebox
import re

# Function to handle button click event for calculation
def calculate():
    # Get the input from the entry widget
    user_input = entry.get()
    data = is_equation(user_input)
    # Update the output text widget
    if data is not None:
        output_text.delete(1.0, tk.END)  # Clear previous content
        output_text.insert(tk.END, f"{data[1]}\n")

# Function to handle button click event for saving
def save():
    # Get the input from the entry widget
    question = entry.get()
    answer = output_text.get(1.0, tk.END).strip()
    if question and answer:
        data = f"Q: {question}\nA: {answer}\n"
        with open("data.txt", "a") as file:  # Append mode to add to existing data
            file.write(data)
        messagebox.showinfo("Saved", "Data saved successfully.")
    else:
        messagebox.showerror("Error", "Both question and answer must be provided.")
    entry.delete(0, tk.END)

def is_equation(user_input):
    # Check if the input is an equation using regular expressions
    if re.match(r'^\s*([-+]?[0-9]+(\.[0-9]+)?([-+\/*]([-+]?[0-9]+(\.[0-9]+)?))*)\s*$', user_input):
        try:
            # Evaluate the equation
            result = eval(user_input)
            return [user_input, result]
        except Exception as e:
            messagebox.showerror("Error", f"Error evaluating expression: {e}")
            return None  # Return None if an error occurs during evaluation
    else:
        messagebox.showerror("Error", "This is not an equation")
        return None  # Return None if the input is not an equation

# Create the main application window
root = tk.Tk()
root.title("Exam Editor")

# Text Label 1 and Input Bar
label1 = tk.Label(root, text="Question: ")
label1.pack(anchor="w")

entry = tk.Entry(root)
entry.pack(anchor="w")

# Button for calculation
calc_button = tk.Button(root, text="Calculate", command=calculate)
calc_button.pack()

# Text Label 2 and Output Area
label2 = tk.Label(root, text="Answer: ")
label2.pack(anchor="w")

output_text = tk.Text(root, height=5, width=30)
output_text.pack()

# Button for saving
save_button = tk.Button(root, text="Save", command=save)
save_button.pack()

# Start the main loop
root.mainloop()
