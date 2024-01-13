# from openai import OpenAI
# client = OpenAI()
# import base

# def call_openai_api():
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": "Who won the world series in 2020?"},
#             {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
#             {"role": "user", "content": "Where was it played?"}
#         ]
#     )
#     return response

# def main():
#     user_input = input("Enter your input: ")
#     response = call_openai_api()
#     prompt = """The user entered command is this: {user_input}. Here is a list of the functions that are available to you: openApplication takes in one parameter, the name of the application to open. closeApplication takes in one parameter, the name of the application to close. speak takes in one parameter, the text to be spoken. Please output in a JSON format the name of the function that should be called and the parameters. For example, if the user says to open safari, please output {"Function": openApplication, "Argument1": Safari}."""

#     runAppleScript(functions.openApplication, arg1="Safari", arg2="")

# if __name__ == "__main__":
#     main()