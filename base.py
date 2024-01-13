import subprocess
import functions

def open_application_with_parameter(application_name):
    script = functions.openApplication
    
    # Save the AppleScript to a temporary file
    script_path = "openApplication.applescript"
    with open(script_path, "w") as script_file:
        script_file.write(script)

    try:
        # Run the AppleScript using osascript
        subprocess.run(["osascript", script_path, application_name], check=True)
    finally:
        # Clean up the temporary script file
        subprocess.run(["rm", script_path])
open_application_with_parameter("Safari")