import tkinter as tk
import llm_mapper

FONTSIZE = 30

WRAP_LENGTH = 600

def get_user_input():
    user_input = entry.get()
    response = llm_mapper.main(user_input)
    entry.delete(0, tk.END)  # Clear the entry box after getting input
    # Show the "Done with" label followed by user input when the task is completed
    done_label.config(text=f"Your task \"{user_input}\" has finished.")
    if response: 
        done_label.config(text=response)
    done_label.pack()

# Create the main window
root = tk.Tk()
root.title("NLIFY")  # Set the title to "NLIFY"

# Create a label with a different font
label = tk.Label(root, text="Input:", font=("Arial", FONTSIZE))  # Change the font to Arial and font size to 14
label.pack(pady=10)

# Create an entry widget for user input
entry = tk.Entry(root)
entry.pack(pady=10)

# Create a button to trigger the user input function
button = tk.Button(root, text="Submit", command=get_user_input)
button.pack(pady=10)

# Create a label to display "Done" with text wrapping
done_label = tk.Label(root, text="", font=("Arial", FONTSIZE), wraplength=WRAP_LENGTH)
done_label.pack()
done_label.pack_forget()  # Hide the "Done" label initially

# Start the main loop
root.mainloop()
