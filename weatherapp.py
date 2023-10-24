import requests
import pytz
from datetime import datetime

def get_weather(city, api_key, timezone):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # You can change units to 'imperial' for Fahrenheit
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data["cod"] == 200:
        main_data = data["main"]
        weather_data = data["weather"][0]

        temperature = main_data["temp"]
        description = weather_data["description"]

        current_time = datetime.now(pytz.timezone(timezone))

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description.capitalize()}")
        print(f"Current Time: {current_time.strftime('%Y-%m-%d %H:%M:%S')} ({timezone})")
    else:
        print(f"Could not fetch weather data for {city}. Error code: {data['cod']}")

while True:
    if __name__ == "__main__":
        api_key = "3301007ff78e08c345eeba4bc785d345"  # Replace with your OpenWeatherMap API key
        continent = input("Enter a Continent: ")
        city = input("Enter a city: ")
        timezone = str(continent + "/" + city)
        get_weather(city, api_key, timezone)
