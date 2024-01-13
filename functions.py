openApplication = """
    tell application "{appName}"
            activate
    end tell
"""

closeApplication = """
    tell application "{appName}"
        quit
    end tell
"""

speak = """
    say "{text}"
"""