import tkinter as tk
from tkinter import messagebox

def string_to_digit(string):
    try:
        # Convert the string to an integer
        string_as_int = int(string)
        # Compare the integer value with the number
        return string_as_int
    except ValueError:
        # If the string cannot be converted to an integer, return False
        return False

# Function to handle Enter key press event
def on_enter_pressed(event):
    # Simulate button click event
    on_button_click()

# Define a function to handle button clicks
def on_button_click():
    global current_question
    global user_answer
    global current_score
    
    # Get the input from the entry widget
    user_input = answer.get()
    user_answer.append(user_input)
    #print(user_answer)

    # Update the label with the input
    current_question += 1
    if current_question < num_question:
        label1.config(text=f"Question {current_question+1}: \n{data[current_question][0]}")
        answer.delete(0, tk.END)
    else:
        # End of questions
        for i in range(len(data)):
            #print(data[i][1], string_to_digit(user_answer[i]))
            if data[i][1] == user_answer[i]:
                current_score += 1 
        # print(current_score, fullscore)
        messagebox.showinfo("Information", f"You got {current_score}/{fullscore} marks")
        label1.config(text=f"End of questions!! Your score is {(current_score/fullscore)*100}%")
        answer.delete(0, tk.END)
        # Hide the button
        button.pack_forget()
        restart_button.pack()

# Function to restart the exam
def restart_exam():
    global current_question
    global user_answer
    global current_score

    # Reset current question index
    current_question = 0
    current_score = 0
    # Clear user's answers
    user_answer.clear()

    # Display the first question
    label1.config(text=f"Question 1: \n{data[0][0]}")
    answer.delete(0, tk.END)

def read_data(filename):
    question_answer_pairs = []
    with open(filename, "r") as file:
        question = None
        answer = None
        for line in file:
            if line.startswith("Q: "):
                question = line[len("Q: "):].strip()
            elif line.startswith("A: "):
                answer = line[len("A: "):].strip()
                if question and answer:
                    question_answer_pairs.append([question, answer])
                    question = None
                    answer = None
    return question_answer_pairs

filename = "data.txt"
data = read_data(filename)
num_question = len(data)
current_question = 0

fullscore = len(data)
current_score = 0
user_answer = []

# Create the main application window
root = tk.Tk()
root.title("Exam")

# Set the window size to 400x300 pixels
root.geometry("500x500")

font_style = ("Arial", 12, "bold")

# Text Label 2 and Output Area
label1 = tk.Label(root, text=f"Question {current_question+1}: \n{data[current_question][0]}", font=font_style)
label1.pack(anchor="w")

label2 = tk.Label(root, text=f"Answer = ")
label2.pack(anchor="w")

answer = tk.Entry(root)
answer.pack(anchor="w")

# Create a button that triggers the on_button_click function
button = tk.Button(root, text="Next Question", command=on_button_click)
button.pack()

restart_button = tk.Button(root, text="Restart Exam", command=restart_exam)
restart_button.pack_forget()

# Bind the Enter key press event to the button
root.bind("<Return>", on_enter_pressed)

# Start the main loop
root.mainloop()
