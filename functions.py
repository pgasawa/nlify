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
end tell
"""}