import subprocess
import weather
import functions

def runAppleScript(scriptTemplate: str, **kwargs):
    try:
        if scriptTemplate == "weather":
            weather.main()
            return
        command = scriptTemplate.format(**kwargs)
    except Exception as e:
        print(f"Error: {e}")
        return None

    try:
        subprocess.run(["osascript", "-e", command])
    except Exception as e:
        print(f"Error: {e}")
        return None