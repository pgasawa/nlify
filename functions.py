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
"""}