import subprocess
import functions

def runAppleScript(scriptTemplate: str, **kwargs):
    try:
        command = scriptTemplate.format(**kwargs)
    except Exception as e:
        print(f"Error: {e}")
        return None

    try:
        subprocess.run(["osascript", "-e", command])
    except Exception as e:
        print(f"Error: {e}")
        return None
    
runAppleScript(functions.functions["accessFiles"], arg1="TreeHacks")