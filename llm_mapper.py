import openai
import os
from openai import OpenAI
client = OpenAI()
import simple_llm_command
import call_routine
import pandas as pd
import define_routine

openai.api_key = os.environ["OPENAI_API_KEY"]

def call_openai_api(prompt):
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": "You are a helpful assistant who is mapping user inputs to specific functions to be called."},
            {"role": "user", "content": prompt},
        ]
    )
    return response

def main(user_input):
    # user_input = input("Enter your input: ")
    try:
        routines = pd.read_csv("routines.csv")
        if user_input in routines["routineName"].values:
            response = call_routine.main(user_input)
            return
    except:
        routines = pd.DataFrame()

    prompt = f"""The user entered command is this: {user_input}. Here is a list of the ways you can classify this command: 1) the user wants to run a simple command: "simpleCommand" such as opening/closing files, sending messages, weather, screenshots, speaking, or searching files. 2) the user wants to define a routine: "defineRoutine." Please output what kind of command the user inputted. For example, if the user says to open an application like Safari or Slack, please output a single string simpleCommand. Or if they say whenever I say work mode, open slack and close messages, then output defineCommand"""
    response = call_openai_api(prompt)
    response = response.choices[0].message.content

    if 'simple' in response:
        response = simple_llm_command.main(user_input)
        return response
    elif "define" in response:
        define_routine.main(user_input)
    else:
        print("Command not recognized. Please try again.")

# main()