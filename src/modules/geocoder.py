import requests
import geocoder
from modules.settings.settings import OPEN_WEATHER_API_KEY, OPEN_WEATHER_API_URL

g = geocoder.ip('me')

def get_my_location():
    return g.latlng, g.city, g.country

def get_custom_location(input):
    g = geocoder.osm(input)

    return g

def get_weather(lat,lon):
    r = requests.get(f"{OPEN_WEATHER_API_URL}?lat={lat}&lon={lon}&appid={OPEN_WEATHER_API_KEY}&units=metric&exclude=hourly,daily,minutely")

    return r.json()


def format_weather(weather, location):
    weather_str = ""
    current_weather = weather
    weather_str += f"Location: {location[0]}, {location[1]}\n"
    weather_str += f"Current weather: {current_weather['weather'][0]['description']}\n"
    weather_str += f"Temperature: {current_weather['temp']}°C\n"
    weather_str += f"Humidity: {current_weather['humidity']}%\n"
    weather_str += f"Wind speed: {current_weather['wind_speed']} m/s\n"

    return weather_str
