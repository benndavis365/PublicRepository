import requests
import json
# OpenWeather API key
api_key = "4c89e57d7d1b6faa69d6ee45fb047810"


def get_weather_data(location):
  # Base URL for the OpenWeather API
  base_url = "https://api.openweathermap.org/data/2.5/weather"

  try:
    # Send a GET request to the API
    url = f"{base_url}?q={location}&units=imperial&APPID={api_key}"
    response = requests.get(url)
    data = response.json()
    #print(data)
    if response.status_code == 200:

      temperature = data["main"]["temp"]
      temperature_max = data["main"]["temp_max"]
      print("\nAPI Connection was successful...")
      print()
      print(f"The current temperature in {location} is {temperature}°F.")
      print(f"The current max temperature in {location} is {temperature_max}°F.")
    else:
      print("\nAn Error Occurred. Please Try again")
  except Exception:
    print("\nAn Error Occurred. Please Try again")
    return None


def main():
  while True:
    location = input("\nEnter a city name or zip code (or press 'q' to quit): ")

    if location == 'q':
      break
    else:
      get_weather_data(location)


main()
