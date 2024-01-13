import requests
import geocoder
from openai import OpenAI
client = OpenAI()
import openai
location_coords = geocoder.ip('me').latlng

def call_openai_api(prompt):
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": "You are a helpful assistant summarizing the weather."},
            {"role": "user", "content": prompt},
        ]
    )
    return response

def get_current_weather(api_key, location):
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        'key': api_key,
        'q': location,
        'aqi': 'no'  # Air Quality Index (optional, set to 'no' for this example)
    }

    # Make the API request
    response = requests.get(base_url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        # Print an error message if the request was unsuccessful
        print(f"Error: Unable to retrieve weather data. Status code: {response.status_code}")
        return None

def main():
    api_key = '5f8609babd8f4d2eb9b220636241301'
    location_str = str(location_coords[0]) + "," + str(location_coords[1])

    # Get and print the current weather
    weather_data = get_current_weather(api_key, location_str)

    weather_prompt = "Here is weather data for where I am. Please concisely summarize important takeaways in two sentences:" + str(weather_data)

    response = call_openai_api(weather_prompt)

    response = response.choices[0].message.content
    print(response)
