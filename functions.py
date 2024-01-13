openApplication = """
    on run argv
        set appName to item 1 of argv
        tell application appName
            activate
        end tell
    end run
    """

closeApplication = """
    on run argv
        set appName to item 1 of argv
        tell application appName
            quit
        end tell
    end run
    """