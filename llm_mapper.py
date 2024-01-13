import openai
import os
from openai import OpenAI
client = OpenAI()
import json
import base
import functions
import simple_llm_command

openai.api_key = os.environ["OPENAI_API_KEY"]

def call_openai_api(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        # response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": "You are a helpful assistant who is mapping user inputs to specific functions to be called."},
            {"role": "user", "content": prompt},
        ]
    )
    return response

def main():
    user_input = input("Enter your input: ")

    # list of routines to check 

    # if LLM thinks it's a simple command:

    prompt = f"""The user entered command is this: {user_input}. Here is a list of the ways you can classify this command: 1) the user wants to run a simple command: "simpleCommand", 2) the user wants to define a routine: "defineRoutine." Please output what kind of command the user inputted. For example, if the user says to open an application like Safari or Slack, please output a single string simpleCommand."""
    response = call_openai_api(prompt)
    response = response.choices[0].message.content


    if 'simple' in response:
        simple_llm_command.main(user_input)
    # else user is defining a routine
    else:
        return

if __name__ == "__main__":
    main()