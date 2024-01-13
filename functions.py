functions = {"openApplication": """
    tell application "{arg1}"
            activate
    end tell
""", 

"closeApplication": """
    tell application "{arg1}"
        quit
    end tell
""", 

"speak": """
    say "{arg1}"
""",

"sendMessage": """
  tell application "Messages"
    set targetBuddy to "{arg1}"
    set targetService to id of 1st account whose service type = iMessage
    set theBuddy to participant targetBuddy of account id targetService
    send {arg2} to buddy 
  end tell
""",
	    
"searchFiles": """
	tell application "Finder"
    activate
  end tell

  tell application "System Events"
    keystroke "f" using command down
    delay 0.5
    keystroke "name:" & "{arg1}"
    keystroke return
  end tell
""",

"takeScreenshot": """
    do shell script "screencapture ~/Desktop/screenshot.png"
"""
}