import tkinter as tk
from tkinter import messagebox
import random

def play_game(user_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    
    result = determine_winner(user_choice, computer_choice)
    
    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def exit_game():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Create buttons for user choices
rock_button = tk.Button(root, text="Rock", width=15, command=lambda: play_game('rock'))
paper_button = tk.Button(root, text="Paper", width=15, command=lambda: play_game('paper'))
scissors_button = tk.Button(root, text="Scissors", width=15, command=lambda: play_game('scissors'))

rock_button.pack(pady=10)
paper_button.pack(pady=10)
scissors_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=20)

# Exit button
exit_button = tk.Button(root, text="Exit", width=15, command=exit_game)
exit_button.pack(pady=10)

# Run the application
root.mainloop()
