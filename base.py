import subprocess
import functions

def runAppleScript(script: str, parameters: list):    
    # Write the AppleScript to a temporary file
    script_path = "temp.applescript"
    with open(script_path, "w") as script_file:
        script_file.write(script)

    try:
        # Run the AppleScript using osascript
        subprocess.run(["osascript", script_path, *parameters], check=True)
    finally:
        # Clean up the temporary script file
        subprocess.run(["rm", script_path])

runAppleScript(functions.closeApplication, ["Safari"])