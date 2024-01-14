import openai
import os
from openai import OpenAI
client = OpenAI()
import json
import base
import functions

openai.api_key = os.environ["OPENAI_API_KEY"]

def call_openai_api(prompt):
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": "You are a helpful assistant who is mapping user inputs to specific functions to be called."},
            {"role": "user", "content": prompt},
        ]
    )
    return response

def main(user_input):
    # user_input = input("Enter your input: ")
    prompt = f"""The user entered command is this: {user_input}. Here is a list of the functions that are available to you: openApplication takes in one parameter, the name of the application to open, and optionally a second search parameter. closeApplication takes in one parameter, the name of the application to close. speak takes in one parameter, the text to be spoken. sendMessage takes in two parameters, the phone number and message. Please output in a JSON format the name of the function that should be called and the parameters, takeScreenshot takes no parameters. weather optionally takes one parameter. For example, if the user says to open safari, please output {{"Function": openApplication, "Argument1": Safari}}. If they said to open News about finance, please output {{"Function": openApplication, "Argument1": News, "Argument2": finance}}"""
    response = call_openai_api(prompt)
    response = response.choices[0].message.content

    print(response)

    try:
        # Try to parse the text as JSON
        data_dict = json.loads(response)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    
    function = data_dict["Function"]
    arg1 = data_dict.get("Argument1", "")
    arg2 = data_dict.get("Argument2", "")
    arg3 = data_dict.get("Argument3", "")

    response = base.runAppleScript(functions.functions[function], arg1=arg1, arg2=arg2, arg3=arg3)
    return response