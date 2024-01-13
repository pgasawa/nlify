import requests
import llm_mapper

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

api_key = '5f8609babd8f4d2eb9b220636241301'
location = 'green bay'

# Get and print the current weather
weather_data = get_current_weather(api_key, location)

if weather_data:
    print("Current Weather in", location)
    print(weather_data)
else:
    print("Unable to retrieve current weather data.")

weather_prompt = "Here is weather data for where I am. Can you give me 5 tips as I prepare for the morning?" + str(weather_data)

response = llm_mapper.call_openai_api(weather_prompt)

print(response)
