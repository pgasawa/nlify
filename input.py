import tkinter as tk
import llm_mapper

FONTSIZE = 30

WRAP_LENGTH = 600
BACKGROUND_COLOR = "lightblue"

def get_user_input():
    user_input = entry.get()
    response = llm_mapper.main(user_input)
    entry.delete(0, tk.END)  # Clear the entry box after getting input
    # Show the "Done with" label followed by user input when the task is completed
    # done_label.config(text=f"Your task \"{user_input}\" has finished.")
    print("response", response)
    if response: 
        print(response)
        done_label.config(text=response)
    done_label.pack()

# Create the main window
root = tk.Tk()
root.title("NLIFY")  # Set the title to "NLIFY"

# Set the background color for the main window
root.configure(bg=BACKGROUND_COLOR)

# Create a label with a different font and background color
label = tk.Label(root, text="Input:", font=("Arial", FONTSIZE), bg=BACKGROUND_COLOR)
label.pack(pady=10)

# Create an entry widget for user input with a background color
entry = tk.Entry(root, bg="white")  # Change "white" to the desired background color
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
