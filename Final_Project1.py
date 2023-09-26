import requests
import json
# OpenWeather API key (replace with your own API key)
api_key = "4c89e57d7d1b6faa69d6ee45fb047810"

def get_weather_data(location):
    # Base URL for the OpenWeather API
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    # Parameters for the API request (you can use either 'q' for city name or 'zip' for zip code)
    params = {
        "q": location,  # City name or zip code
        "appid": api_key,  # Your API key
        
    }

    while True:
        # Send a GET request to the API
        url = f"{base_url}?q={location}&units=imperial&APPID={api_key}"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            # Extract temperature data from the API response
            temperature = data["main"]["temp"]
            return temperature
        else:
            print("Error: Unable to fetch weather data. Please check your input.")
            return None
      
def main():
    location = input("Enter a city name or zip code: ")

    temperature = get_weather_data(location)

    if temperature is not None:
        print(f"The current temperature in {location} is {temperature}°F.")

main()