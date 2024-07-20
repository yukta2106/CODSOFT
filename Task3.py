import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    if length < 1:
        return "Invalid length. Please enter a positive integer."

    all_characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def generate_password_button():
    try:
        length = int(entry_length.get())
        password = generate_password(length)
        result_var.set(f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid integer.")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")
root.configure(bg="#e0f7fa")

label_length = tk.Label(root, text="Enter desired length of the password:", bg="#e0f7fa")
label_length.pack(pady=10)
entry_length = tk.Entry(root)
entry_length.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password_button, bg="#00796b", fg="white")
generate_button.pack(pady=10)

result_var = tk.StringVar(root)
result_label = tk.Label(root, textvariable=result_var, bg="#e0f7fa")
result_label.pack(pady=20)

root.mainloop()
