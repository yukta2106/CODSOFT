import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is undefined."
    return x / y

def perform_calculation(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        if operation == "Add":
            result = add(num1, num2)
        elif operation == "Subtract":
            result = subtract(num1, num2)
        elif operation == "Multiply":
            result = multiply(num1, num2)
        elif operation == "Divide":
            result = divide(num1, num2)

        result_var.set(f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter numeric values.")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x300")
root.configure(bg="#e0f7fa")

label_num1 = tk.Label(root, text="Enter first number:", bg="#e0f7fa")
label_num1.pack(pady=5)
entry_num1 = tk.Entry(root)
entry_num1.pack(pady=5)

label_num2 = tk.Label(root, text="Enter second number:", bg="#e0f7fa")
label_num2.pack(pady=5)
entry_num2 = tk.Entry(root)
entry_num2.pack(pady=5)

button_frame = tk.Frame(root, bg="#e0f7fa")
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add", command=lambda: perform_calculation("Add"), bg="#00796b", fg="white", padx=10, pady=5)
add_button.grid(row=0, column=0, padx=5)

subtract_button = tk.Button(button_frame, text="Subtract", command=lambda: perform_calculation("Subtract"), bg="#00796b", fg="white", padx=10, pady=5)
subtract_button.grid(row=0, column=1, padx=5)

multiply_button = tk.Button(button_frame, text="Multiply", command=lambda: perform_calculation("Multiply"), bg="#00796b", fg="white", padx=10, pady=5)
multiply_button.grid(row=0, column=2, padx=5)

divide_button = tk.Button(button_frame, text="Divide", command=lambda: perform_calculation("Divide"), bg="#00796b", fg="white", padx=10, pady=5)
divide_button.grid(row=0, column=3, padx=5)

result_var = tk.StringVar(root)
result_label = tk.Label(root, textvariable=result_var, bg="#e0f7fa")
result_label.pack(pady=20)

root.mainloop()
