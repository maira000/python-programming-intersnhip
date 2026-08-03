import tkinter as tk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Cannot divide by zero"
        else:
            result = "Invalid operation"

        entry_result.delete(0, tk.END)
        entry_result.insert(0, result)
    except ValueError:
        entry_result.delete(0, tk.END)
        entry_result.insert(0, "Invalid input")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create and place UI components
label_num1 = tk.Label(root, text="Enter number 1:")
label_num1.grid(row=0, column=0, padx=10, pady=10)

entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

label_num2 = tk.Label(root, text="Enter number 2:")
label_num2.grid(row=1, column=0, padx=10, pady=10)

entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

label_operation = tk.Label(root, text="Select operation:")
label_operation.grid(row=2, column=0, padx=10, pady=10)

operations = ["Addition", "Subtraction", "Multiplication", "Division"]
operation_var = tk.StringVar(root)
operation_var.set(operations[0])

dropdown_operation = tk.OptionMenu(root, operation_var, *operations)
dropdown_operation.grid(row=2, column=1, padx=10, pady=10)

button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.grid(row=3, column=0, columnspan=2, pady=10)

label_result = tk.Label(root, text="Result:")
label_result.grid(row=4, column=0, padx=10, pady=10)

entry_result = tk.Entry(root)
entry_result.grid(row=4, column=1, padx=10, pady=10)

# Run the application
root.mainloop()
