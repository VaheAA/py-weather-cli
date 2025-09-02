import os
from dotenv import load_dotenv

load_dotenv()
OPEN_WEATHER_API_KEY = os.environ.get('OPEN_WEATHER_API_KEY')
OPEN_WEATHER_API_URL = os.environ.get('OPEN_WEATHER_API_URL')
GITHUB_USER_NAME = os.environ.get('GITHUB_USER_NAME')
