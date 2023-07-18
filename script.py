# Script created by hackrish at Virtual Cybertrons 
import subprocess
import sys

# List of required packages
required_packages = ["pandas", "numpy", "openpyxl"]

# Check if the required packages are installed
missing_packages = [pkg for pkg in required_packages if pkg not in sys.modules]

# Install missing packages using pip if any are not found
if missing_packages:
    print("Installing missing packages...")

    for package in missing_packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

    print("Packages installed successfully.")

# Import the required modules
import pandas as pd
import numpy as np
import json
import tkinter as tk
from tkinter import filedialog, messagebox

def process_excel():
    # Prompt for the Excel file using a file dialog
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if not file_path:
        return

    try:
        # Read the Excel file into a DataFrame
        df = pd.read_excel(file_path)

        # Get the column names from the first row
        columns = list(df.columns)

        # Create the main Tkinter window for column selection
        column_window = tk.Toplevel()
        column_window.title("Select Key and Value Columns")

        # Create variables to store the selected columns
        key_column_var = tk.StringVar()
        value_column_var = tk.StringVar()

        # Function to save the selected columns and process the Excel file
        def save_and_process():
            key_column = key_column_var.get()
            value_column = value_column_var.get()

            if key_column and value_column:
                # Replace NaN values in the value column with the corresponding key
                df[value_column] = df[value_column].fillna(df[key_column])

                # Convert NaN values to "NaN" string
                df[value_column] = df[value_column].apply(lambda x: "NaN" if pd.isna(x) else x)

                # Create a dictionary from the key and value columns
                data = df[[key_column, value_column]].set_index(key_column).to_dict()[value_column]

                # Save the dictionary as a nicely formatted JSON file
                save_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
                if save_path:
                    with open(save_path, "w", encoding="utf-8") as outfile:
                        json.dump(data, outfile, ensure_ascii=False, indent=4)
                    messagebox.showinfo("Success", "JSON data has been saved.")

            column_window.destroy()

        # Create checkboxes for column selection
        for i, column in enumerate(columns):
            key_checkbox = tk.Radiobutton(column_window, text=column, variable=key_column_var, value=column)
            key_checkbox.grid(row=i, column=0, sticky="w")

            value_checkbox = tk.Radiobutton(column_window, text=column, variable=value_column_var, value=column)
            value_checkbox.grid(row=i, column=1, sticky="w")

        # Create a button to save and process the selected columns
        process_button = tk.Button(column_window, text="Process Excel", command=save_and_process)
        process_button.grid(row=len(columns), columnspan=2, pady=10)

        # Run the Tkinter event loop for the column selection window
        column_window.mainloop()

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main Tkinter window
root = tk.Tk()
root.title("Excel to JSON Converter")

# Create a button to trigger the Excel processing
process_button = tk.Button(root, text="Select Excel File", command=process_excel)
process_button.pack(pady=20)

# Run the Tkinter event loop for the main window
root.mainloop()
