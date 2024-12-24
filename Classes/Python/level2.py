import tkinter as tk
from tkinter import * 
from tkinter import messagebox

import csv


#Load the dataset
def load_destinations(file_path):
    destinations= []
    try:
        with open(file_path,mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                #Parse numeric fields
                row["popularity"] = float(row["popularity"])
                row["price"] = float(row["price"])
                for key in row:
                    if row[key] in {'0','1'}:
                        row[key]=int(row[key])        
                destinations.append(row)
        return destinations
    except FileNotFoundError:
        messagebox.showerror("Error!", f"file '{file_path}' not found.")
        return []
    except Exception as e:
        messagebox.showerror("Error!", f"Error loading file: {e}")
        return []


def filter_destinations():
    # Get the current values of preferences
    preference_values = {key : var.get() for key, var in preferences.items()}

    # Filter destinations
    filtered_destinations = []
    for destination in destinations:
        match = True
        for key, value in preference_values.items():
            if value == 1 and destination[key] != 1:
                match = False
                break
        
        if match:
            filter_destinations.append(destination)
            # Display results
    results_text.delete('1.0', tk.END)
    if not filter_destinations:
        results_text.insert(tk.END, 'No matches found for your preferences.\n')
        results_text.insert(tk.END, 'Here are the top popular destinations:\n\n')
        sorted_destinations = sorted(destinations, key = lambda x: x['popularity'], reverse = True)[:5]

    else:
        results_text.insert(tk,END, 'Top picks based on your preferences:\n\n')
        sorted_destinations = sorted(filter_destinations, key = lambda x: x['popularity'],reverse = True)

    for i, destination in enumerate(sorted_destinations, start = 1):
        results_text.insert(
            tk.END,
            f'{i}, Destination: {destination['competitorname']}\n'
            f'  Popularity: {destination['popularity']}\n'
            f'  Price: ${destination['price']}\n\n0'
        )

def clear_preferences():
    for var in preferences.values():
        var.set(0)
    results_text.delete("1.0",tk.END)

# Let's initialize the GUI
root=tk.Tk()
root.title("Travel Destination Finder")
root.geometry("500x600")
#Checkbox Variables should be stored in the preferences dictionary.
preferences={
    "tropical":tk.IntVar(),
    "cold":tk.IntVar(),
    "adventure":tk.IntVar(),
    "relaxation":tk.IntVar(),
    "cultural":tk.IntVar(),
    "nature":tk.IntVar(),
    "shopping":tk.IntVar(),
    "modern":tk.IntVar(),
    "historic":tk.IntVar()
    }

#Layout
tk.Label(root,text="Select Your Travel Preferences: ",font=("Consolas",16)).pack(pady=10)
for (key,var) in preferences.items():
    tk.Checkbutton(root,text=key.capitalize(),variable=var).pack(anchor='w',padx=20)

#Buttons
tk.Button(root,text="Find Destinations",command=filter_destinations, font=("Consolas",12)).pack(pady=5)
tk.Button(root,text="Clear Preferences",command=clear_preferences, font=("Consolas",12)).pack(pady=10)

#Result
tk.Label(root,text="Results: ",font=("Consolas",14)).pack(pady=10)
results_text=tk.Text(root,wrap="word",height=20,width=50,font=("Consolas",12))
results_text.pack(pady=5)

# Load travel destination data
FILE_PATH = 'travel_destinations.csv'
destinations = load_destinations(FILE_PATH)

# Display results
results_text.delete('1.0', tk.END)
if not filter_destinations:
    results_text.insert(tk.END, 'No matches found for your preferences.\n')
    results_text.insert(tk.END, 'Here are the top popular destinations:\n\n')
    sorted_destinations = sorted(destinations, key = lambda x: x['popularity'], reverse = True)[:5]

else:
    results_text.insert(tk,END, 'Top picks based on your preferences:\n\n')
    sorted_destinations = sorted(filter_destinations, key = lambda x: x['popularity'],reverse = True)

for i, destination in enumerate(sorted_destinations, start = 1):
    results_text.insert(
        tk.END,
        f'{i}, Destination: {destination['competitorname']}\n'
        f'  Popularity: {destination['popularity']}\n'
        f'  Price: ${destination['price']}\n\n0'
    )


root.mainloop()