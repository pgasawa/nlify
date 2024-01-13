import tkinter as tk
import llm_mapper

def get_user_input():
    user_input = entry.get()
    # label_result.config(text=f"You entered: {user_input}")
    llm_mapper.main(user_input)
    entry.delete(0, tk.END)  # Clear the entry box after getting input

# Create the main window
root = tk.Tk()
root.title("User Input Example")

# Create a label
label = tk.Label(root, text="Input:")
label.pack(pady=10)

# Create an entry widget for user input
entry = tk.Entry(root)
entry.pack(pady=10)

# Create a button to trigger the user input function
button = tk.Button(root, text="Submit", command=get_user_input)
button.pack(pady=10)

# Create a label to display the result
# label_result = tk.Label(root, text="")
# label_result.pack(pady=10)

# Start the main loop
root.mainloop()