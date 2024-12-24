import tkinter as tk
from tkinter import ttk, messagebox

def show_message():
    messagebox.showinfo("Message", "Button clicked!")

root = tk.Tk()
root.title("Tkinter Widgets Example")
root.geometry("400x300")

# Label
label = tk.Label(root, text="Welcome to Tkinter!", font=("Arial", 16))
label.pack(pady=10)

# Entry
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Button
button = tk.Button(root, text="Click Me", command=show_message)
button.pack(pady=10)

# Combobox
combobox = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
combobox.set("Choose an option")
combobox.pack(pady=10)

# Progressbar
progress = ttk.Progressbar(root, length=200, mode="indeterminate")
progress.pack(pady=10)
progress.start(10)

root.mainloop()
