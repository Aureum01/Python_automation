import tkinter as tk
from tkinter import filedialog
import pandas as pd

# Create the root window
root = tk.Tk()

# Create a function to open a file dialog and select a CSV file
def open_csv_file():
    # Open the file dialog and get the selected file
    file = filedialog.askopenfilename(title="Select a CSV file", filetypes=[("CSV files", "*.csv")])

    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file)

    # Open the file dialog and get the file to save the Excel file to
    file = filedialog.asksaveasfilename(title="Save Excel file", defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])

    # Save the DataFrame as an Excel file
    df.to_excel(file, index=False)

# Create a button to open the CSV file
button = tk.Button(root, text="Open CSV file", command=open_csv_file)
button.pack()

# Run the main loop
root.mainloop()
