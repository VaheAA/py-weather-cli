import requests
import geocoder
from modules.settings.settings import OPEN_WEATHER_API_KEY, OPEN_WEATHER_API_URL

g = geocoder.ip('me')

def get_location():

    return g.latlng


def get_weather(lat,lon):
    r = requests.get(f"{OPEN_WEATHER_API_URL}?lat={lat}&lon={lon}&appid={OPEN_WEATHER_API_KEY}&units=metric&exclude=hourly,daily,minutely")

    return r.json()
