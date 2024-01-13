import subprocess
import weather
import writeMessage

def runAppleScript(scriptTemplate: str, **kwargs):
    try:
        if scriptTemplate == "weather":
            response = weather.main(kwargs['arg1'])
            return response
        elif 'Message' in scriptTemplate:
            message = writeMessage.main(kwargs['arg2'])
            kwargs['arg2'] = message
        command = scriptTemplate.format(**kwargs)
    except Exception as e:
        print(f"Error: {e}")
        return None

    try:
        subprocess.run(["osascript", "-e", command])
    except Exception as e:
        print(f"Error: {e}")
        return None