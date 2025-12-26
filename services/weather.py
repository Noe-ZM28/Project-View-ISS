from utils.coords import Coords
from config.keys import get_openweather_key
from utils.responseAPI import API_reponse

class WeatherData():
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    ICON_URL = "https://openweathermap.org/img/wn"

    def __init__(self)->None:
        self._API_KEY = get_openweather_key()
        self._client = API_reponse()

    def construct_url(
        self,
        lat:float|int,
        lon:float|int,
        units:str= "metric"
    ) -> str | None:
        if not Coords.validate_coords(lat=lat, lon=lon):
            return None

        return (
            f"{self.BASE_URL}"
            f"?appid={self._API_KEY}"
            f"&units={units}"
            f"&lat={lat}"
            f"&lon={lon}"
        )

    def get_weather_icon(self, response_data:dict) -> str:
        return f"{self.ICON_URL}/{response_data["weather"][0]["icon"]}@2x.png"

    def get_weather(self, lat: float | int, lon: float | int) -> dict | None:
        url = self.construct_url(lat, lon)
        if not url:
            return None
        return self._client.get_response_api(url)
