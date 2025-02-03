import tkinter as tk
import pandas as pd

##### FUNCTIONS ####

def import_upc_data():  # Imports CSV file and creates global UPC dictionary
    global upc_mapping
    cell_code = []
    # Generate cell barcode codes
    for shelf in range(3):
        for row in range(5):
            for col in range(3):
                cell_code.append(f"{shelf}{row}{col}")
    try:
        # Hardcoded file path
        file_path = "/Users/karanvirsingh/Downloads/SampleData.csv"

        # Read the Excel file
        data = pd.read_csv(file_path, header=None, names=["Data"], on_bad_lines='skip', dtype=str)

        upc_mapping = {}  # Create dictionary for UPCs
        current_cell = None

        for value in data["Data"]:
            if value in cell_code:
                current_cell = value.strip()  # Set the current cell code
                upc_mapping[current_cell] = []  # Initialize an empty list for its UPCs
            elif current_cell is not None:  # If it's a UPC and a cell is non-zero
                upc_mapping[current_cell].append(str(value).strip())  # Add the UPC to the cell's list

        if not upc_mapping:
            print("No UPC data was loaded")
        else:
            print(upc_mapping)

    except Exception as e:
        print(f"Error while importing UPC data: {e}")

def reset_highlights(cell_references):
    for cell in cell_references.values():
        cell.configure(bg="white")  # Reset to white or the original background color

def search_upc(cell_references):
    # Clear previous highlights
    reset_highlights(cell_references)

    # Get the user's input
    upc_suffix = search_entry.get().strip() 
    found_cells = []  # List to store all cells containing the partial UPC

    # Ensure the input is a number
    if not upc_suffix.isdigit():
        print("Please enter a valid numeric suffix.")
        return

    # Search for the UPC suffix in the dictionary
    for cell_code, upcs in upc_mapping.items():
        for upc in upcs:
            # Check if the last digits of the UPC match the user input
            if upc.endswith(upc_suffix):
                found_cells.append(cell_code)
                break  # Avoid duplicate entries for the same cell

    if found_cells:
        print(f"The UPCs ending with '{upc_suffix}' are located in cells: {', '.join(found_cells)}")

        for found_cell in found_cells:
            # Split the `cell_code` into separate integers
            a, b, c = int(found_cell[0]), int(found_cell[1]), int(found_cell[2])

            # Change the background color of the corresponding cell
            if (a, b, c) in cell_references:
                cell_references[(a, b, c)].configure(bg="yellow")
            else:
                print(f"Error: Cell {found_cell} does not exist in the GUI layout.")
    else:
        print(f"No UPCs ending with '{upc_suffix}' were found.")

############ CREATE GUI VISUAL ###############
# Create main application window
Root = tk.Tk()
Root.title("Laptop Warehouse Location")
Root.geometry("500x500")
shelf_dict = {0: "A", 1: "B", 2: "C"}

# Create a container frame for the shelves
shelf_frame = tk.Frame(Root, padx=10, pady=10)
shelf_frame.pack(fill="both", expand=True)

# Dictionary to store references to each cell for later manipulation
cell_references = {}

# Create a container for 3 shelves
for shelf_number in range(3):
    shelf = tk.Frame(shelf_frame, bg="lightgrey", padx=5, pady=5)
    shelf.pack(side="left", fill="both", pady=5, expand=True)

    # Add a grid of cells to each shelf
    for row in range(5):  # 5 rows
        for col in range(3):  # 3 columns
            cell = tk.Frame(
                shelf,
                bg="white",
                highlightbackground="black",
                highlightthickness=1,
            )
            cell.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")  # Make cells expand to fill space
            # Label each cell in the grid
            label = tk.Label(cell, text=f"{shelf_dict[shelf_number]}{row}{col}", bg="lightgray", font=("Arial", 10))
            label.pack(expand=True)  # Use expand=True to center the label

            # Store a reference to each cell in the dictionary
            cell_references[(shelf_number, row, col)] = cell

    # Configure shelf's grid to make cells expand within the shelf
    for row in range(5):
        shelf.grid_rowconfigure(row, weight=1)  # Allow each row inside the shelf to expand
    for col in range(3):
        shelf.grid_columnconfigure(col, weight=1)  # Allow each column inside the shelf to expand

# Create a search bar and a search button
search_label = tk.Label(Root, text="Enter UPC to search:")
search_label.pack(pady=10)

search_entry = tk.Entry(Root, width=40)  # Entry widget for user input
search_entry.pack(pady=5)

import_upc_data()

search_button = tk.Button(Root, text="Search", command=lambda: search_upc(cell_references))
search_button.pack(pady=10)

Root.mainloop()
