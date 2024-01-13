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

"sendMessage": """tell application "Messages"
    set targetBuddy to "{arg1}"
    set targetService to id of 1st service whose service type = iMessage
    set theBuddy to buddy targetBuddy of service id targetService
    send "{arg2}" to theBuddy
end tell""",
	    
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
""",

"weather": """weather""",

"searchNotes": """

tell application "Notes"
    quit
end tell

tell application "Notes"
  delay 0.5
	activate
end tell

tell application "System Events"
	keystroke "f" using {{command down, option down}}
	delay 0.5
	keystroke "{arg1}"
	keystroke return
end tell
"""
}
