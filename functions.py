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

"switchWorkspaceRight": """
tell application "System Events"
	key code 124 using control down
end tell
""",

"switchWorkspaceLeft": """
tell application "System Events"
	key code 123 using control down
end tell""",

"sendMessage": """
  tell application "Messages"
    set targetBuddy to "{arg1}"
    set targetService to id of 1st account whose service type = iMessage
    set theBuddy to participant targetBuddy of account id targetService
    send {arg2} to buddy 
  end tell
"""}