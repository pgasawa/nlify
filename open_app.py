
import subprocess

def open_application(app_name):
    # Replace spaces with backslashes and spaces for AppleScript
    app_name_escaped = app_name.replace(" ", r"\ ")
    
    # AppleScript command to tell the application to open
    applescript_command = f'tell application "{app_name_escaped}" to activate'
    
    # Run the AppleScript command using osascript
    subprocess.run(["osascript", "-e", applescript_command])

# Replace 'Calculator' with the name of the application you want to open
# open_application("Calculator")

try:
    open_application("Calculator")
except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e}")