import openai
import os
from openai import OpenAI
client = OpenAI()

openai.api_key = os.environ["OPENAI_API_KEY"]

def call_openai_api(prompt):
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": "You are a helpful assistant who is writing text messages."},
            {"role": "user", "content": prompt},
        ]
    )
    return response

def main(content_input):
    prompt = "The user entered a message to be sent to a person. If you think that this message should be sent verbatim, leave it as it is, or if you think the user intended for you to rewrite or write the message based on this input, do so. Here is in the input: " + content_input
    response = call_openai_api(prompt)
    response = response.choices[0].message.content
    return response