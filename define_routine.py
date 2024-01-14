import openai
import os
from openai import OpenAI
client = OpenAI()
import pandas as pd
import json
import base
import functions

openai.api_key = os.environ["OPENAI_API_KEY"]

def call_openai_api(prompt):
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": "You are a helpful assistant who is mapping user routines to specific functions to be called."},
            {"role": "user", "content": prompt},
        ]
    )
    return response

def main(user_input):
    # user_input = input("Enter your input: ")
    prompt = f"""The user entered this input to define a routine of functions: {user_input}. Here is a list of the functions that are available to you: openApplication takes in one parameter, the name of the single application to open and optionally a second search parameter. closeApplication takes in one parameter, the name of the single application to close. speak takes in one parameter, the text to be spoken. sendMessage takes in two parameters, the phone number and message. takeScreenshot takes no parameters. weather optionally takes one parameters. Please output in JSON format the name of the routine and the LIST of functions that should be called with their parameters, using one function per application. For example, if the user says that whenever they say work mode to open slack and close their messages, please output {{"RoutineName": "work mode", "functions": [("openApplication", Slack), (closeApplication, Messages)]}}. Or if they said wake up mode should open safari and close messages, then output {{"RoutineName": "wake up mode", "functions": [("openApplication", Safari), (closeApplication, Messages)]}}."""
    response = call_openai_api(prompt)
    response = response.choices[0].message.content

    try:
        data_dict = json.loads(response)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    
    routineName = data_dict["RoutineName"]
    rowToAdd = {"routineName": routineName, "functions": data_dict["functions"]}

    try:
        routines = pd.read_csv("routines.csv")
    except:
        routines = pd.DataFrame()
    routines = routines._append(rowToAdd, ignore_index=True)
    routines.to_csv("routines.csv", index=False)