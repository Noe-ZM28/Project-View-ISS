from utils.coords import Coords
from config.keys import get_openweather_key
from utils.responseAPI import API_reponse

class WeatherData():
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    def __init__(self)->None:
        self.__API_KEY__ = get_openweather_key()
        self._client = API_reponse()

    def construct_url(
        self,
        lat:float|int,
        lon:float|int,
        units:str= "metric"
    ) -> dict | None:
        if not Coords.validate_coords(lat=lat, lon=lon):
            return None

        return (
            f"{self.BASE_URL}"
            f"?appid={self.__API_KEY__}"
            f"&units={units}"
            f"&lat={lat}"
            f"&lon={lon}"
        )

    def get_response_api_weather_icon(self, name_icon:str) -> str:
        path_icon = f"https://openweathermap.org/img/wn/{name_icon}@2x.png"
        return path_icon

    def get_weather(self, lat:float|int, lon:float|int) -> str | None:
        url = self.construct_url(lat, lon)
        if not url:
            return None
        return API_reponse().get_response_api(url)