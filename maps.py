import geocoder
from datetime import datetime
import requests

def get_current_location():
    # Get the current location using the Google Maps API
    location = geocoder.ip('me')

    # Print the latitude and longitude
    return (location.latlng[0], location.latlng[1])



def get_travel_time(origin, destination, transport_type="cycling"):
    mapbox_access_token = "pk.eyJ1IjoiZWR3YXJkb3N1bm55IiwiYSI6ImNscmNtdTk0bTEyOW4ydWxlZ2wzemU2M2QifQ.Z_a9btW04SSKWxUdi9sI-A"
    request_url = f"https://api.mapbox.com/directions/v5/mapbox/{transport_type}/-84.518641,39.134270;-84.512023,39.102779?geometries=geojson&access_token=pk.eyJ1IjoiZWR3YXJkb3N1bm55IiwiYSI6ImNscmNtdTk0bTEyOW4ydWxlZ2wzemU2M2QifQ.Z_a9btW04SSKWxUdi9sI-A" 
    print(request_url)
    # Set query parameters
    
    # Make the API request
    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()

        # Extract and print the travel duration
        duration = data["routes"][0]["duration"]
        print(f"Travel duration from {origin} to {destination} is {duration} seconds.")
    else:
        print(f"Failed to retrieve travel duration. Status code: {response.status_code}")


origin = get_current_location()  # San Francisco, CA
destination = [34.0549, 118.2426]  # Los Angeles, CA

get_travel_time(origin, destination)