import tkinter as tk
from tkinter import ttk
import llm_mapper

def get_user_input():
    user_input = entry.get()
    llm_mapper.main(user_input)
    entry.delete(0, tk.END)  # Clear the entry box after getting input

# Create the main window
root = tk.Tk()
root.title("User Input Example")

# Configure a style for ttk elements with a nice color scheme
style = ttk.Style()
style.configure("TFrame", background="#EAEAEA")
style.configure("TLabel", background="#EAEAEA", font=("Arial", 12))
style.configure("TButton", background="#4CAF50", foreground="white", font=("Arial", 12))

# Create and configure a frame with the defined style
frame = ttk.Frame(root, padding=(20, 20))
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create a label with the defined style
label = ttk.Label(frame, text="Input:")
label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

# Create an entry widget for user input
entry = ttk.Entry(frame)
entry.grid(row=0, column=1, padx=10, pady=5, sticky=(tk.W, tk.E))

# Create a button with the defined style to trigger the user input function
button = ttk.But
