from dotenv import load_dotenv
from os import getenv

load_dotenv()

OPENWEATHER_API_KEY = getenv("API_KEY_OPENWEATHER")
POSITIONSTACK_API_KEY = getenv("API_KEY_POSITIONSTACK")
