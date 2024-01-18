#CODSOFT Task - Simple Calculator
import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                raise ValueError("Math Error!! Cannot divide by zero")
            result = num1 / num2
        else:
            raise ValueError("Invalid operation!")

        result_label.config(text=f"Result: {result}")

    except ValueError as e:
        messagebox.showerror("Error!", str(e))

# Creating the Main Window
guiWindow = tk.Tk()
guiWindow.geometry('400x300')
guiWindow.title("Simple Calculator - CODSOFT")
guiWindow.config(bg = '#2b2d30')

# Creating input fields and labels
label_num1 = tk.Label(guiWindow, text="Enter First Number:", font=("georgia", 12, "bold"),  bg = '#2b2d30', fg='#ffffff')
label_num1.grid(row=0, column=0, padx=10, pady=10)
entry_num1 = tk.Entry(guiWindow)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

label_num2 = tk.Label(guiWindow, text="Enter Second Number:", font=("georgia", 12, "bold"),  bg = '#2b2d30', fg='#ffffff')
label_num2.grid(row=1, column=0, padx=10, pady=10)
entry_num2 = tk.Entry(guiWindow)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

# Creating the operation choices
label_operation = tk.Label(guiWindow, text="Choose Operation:", font=("georgia", 12, "bold"),  bg = '#2b2d30', fg='#ffffff')
label_operation.grid(row=2, column=0, padx=10, pady=10)
operations = ["+", "-", "*", "/"]
operation_var = tk.StringVar(guiWindow)
operation_var.set("+")
operation_menu = tk.OptionMenu(guiWindow, operation_var, *operations)
operation_menu.grid(row=2, column=1, padx=0, pady=10)

# Creating the calculate button
calculate_button = tk.Button(guiWindow, text="Calculate", font='Georgia 10 bold',bg='red', fg="white",command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Creating result label
result_label = tk.Label(guiWindow, text="Result: ",font='Georgia 10 bold',bg='green', fg="white")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Running the main loop
guiWindow.mainloop()
