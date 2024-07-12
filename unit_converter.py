import tkinter as tk
from tkinter import ttk

# Function to convert units
def convert_units():
    value = float(entry.get())
    from_unit = from_unit_combobox.get()
    to_unit = to_unit_combobox.get()
    result = 0

    # Conversion logic
    if from_unit == "cm" and to_unit == "m":
        result = value / 100
    elif from_unit == "m" and to_unit == "cm":
        result = value * 100
    elif from_unit == "grams" and to_unit == "kg":
        result = value / 1000
    elif from_unit == "kg" and to_unit == "grams":
        result = value * 1000
    else:
        result_label.config(text="Invalid conversion.")
        return

    result_label.config(text=f"Result: {result}")

# Create main application window
root = tk.Tk()
root.title("Unit Converter")

# Create and place widgets
entry_label = tk.Label(root, text="Enter value:")
entry_label.grid(column=0, row=0, padx=10, pady=10)
entry = tk.Entry(root)
entry.grid(column=1, row=0, padx=10, pady=10)

from_unit_label = tk.Label(root, text="From unit:")
from_unit_label.grid(column=0, row=1, padx=10, pady=10)
from_unit_combobox = ttk.Combobox(root, values=["cm", "m", "grams", "kg"])
from_unit_combobox.grid(column=1, row=1, padx=10, pady=10)
from_unit_combobox.current(0)

to_unit_label = tk.Label(root, text="To unit:")
to_unit_label.grid(column=0, row=2, padx=10, pady=10)
to_unit_combobox = ttk.Combobox(root, values=["cm", "m", "grams", "kg"])
to_unit_combobox.grid(column=1, row=2, padx=10, pady=10)
to_unit_combobox.current(1)

convert_button = tk.Button(root, text="Convert", command=convert_units)
convert_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()

