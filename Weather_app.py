import requests

API_KEY = "1ba7cabac02fd264622cf9af4a26583d"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"  # Celsius
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()

    city_name = data["name"]
    country = data["sys"]["country"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    print(f"\nWeather in {city_name}, {country}")
    print(f"Temperature : {temperature}°C")
    print(f"Humidity    : {humidity}%")
    print(f"Condition   : {weather.title()}")
    print(f"Wind Speed  : {wind_speed} m/s")

else:
    print("City not found or invalid API key.")  