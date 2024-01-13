# import subprocess

# # Function to make the computer speak
# def say_text(text):
#     subprocess.call(['say', text])

# # Call the function with the desired text
# say_text("Hello, Lara")
# python
import subprocess

def say_hello_lara():
    applescript_command = 'say "Hello, Lara"'
    subprocess.run(["osascript", "-e", applescript_command])

print("HDFHSDFH")
say_hello_lara()