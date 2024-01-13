import subprocess
import tkinter as tk
from tkinter import simpledialog

def run_applescript(script):
    subprocess.run(["osascript", "-e", script])

def open_slack():
    run_applescript('tell application "Slack" to activate')

def close_calculator():
    run_applescript('tell application "Calculator" to quit')

def start_morning_routine():
    open_slack()
    close_calculator()

def on_start_routine():
    command = simpledialog.askstring("Input", "Type your command",
                                     parent=root)
    if command == "start morning routine":
       start_morning_routine()

# Set up the basic window
root = tk.Tk()
root.title("Command Runner")

# Add a button to start the routine
start_button = tk.Button(root, text="Start Command", command=on_start_routine)
start_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()



   