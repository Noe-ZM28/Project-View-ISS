from requests import get
from requests.models import Response
from requests.exceptions import RequestException
from datetime import datetime

from utils.coords import validate_coords

  

class API_reponse:
    def construc_url(self, **kwars)->str: ...

    def get_response_api(self, url:str, to_JSON:bool= True) -> Response | dict | None:
        try:
            print(url)
            response = get(url)
            response.raise_for_status()

            return response.json() if to_JSON else response

        except RequestException as e:
            print(e)
            print("Error en la petición.")
            return None


class WeatherData(API_reponse):
    def __init__(self, API_KEY:str)->None:
        self.API_KEY = API_KEY

    def construc_url(self, lat:float|int, lon:float|int, units:str= "metric") -> Response | dict | None:

        url_api_weather = f"https://api.openweathermap.org/data/3.0/weather?appid={self.API_KEY}&units={units}&lat={lat}&lon={lon}"

        return url_api_weather if validate_coords(lat=lat, lon=lon) else None

    def get_response_api_weather_icon(self, name_icon:str) -> str:

        path_icon = f"https://openweathermap.org/img/wn/{name_icon}@2x.png"
        return path_icon

class GeoDataLocation(API_reponse):
    def __init__(self, API_KEY:str)->None:
        self.API_KEY = API_KEY

    def construc_url(self, lat:float|int, lon:float|int, limit:int= 1) -> Response | dict | None:
        url_api_geodata = f"http://api.positionstack.com/v1/reverse?access_key={self.API_KEY}&query={lat},{lon}&limit={limit}"

        return url_api_geodata if validate_coords(lat=lat, lon=lon) else None

class GeoDataCountry(API_reponse):

    def construc_url(self, code_country:str) -> Response | dict | None:
        url_api_geodata_other = f"https://restcountries.com/v3.1/alpha/{code_country}"

        return url_api_geodata_other if code_country is not None else None

class ISSData(API_reponse):
    def __init__(self) -> None:
        self.url= "http://api.open-notify.org/iss-now.json"
        self.response_api = self.get_response_api(self.url)

    def get_ISS_position(self) -> tuple | None:

        if self.response_api is None:
            return None

        lon = self.response_api["iss_position"]["longitude"]
        lat = self.response_api["iss_position"]["latitude"]

        date = datetime.fromtimestamp(self.response_api["timestamp"]).strftime("%Y-%m-%d %H:%M:%S")

        return lon, lat, date


from pprint import pprint
from os import getenv
from dotenv import load_dotenv
load_dotenv()

API_KEY_OPENWEATHER = getenv('API_KEY_OPENWEATHER')
API_KEY_POSITIONSTACK = getenv('API_KEY_POSITIONSTACK')

lat = 19.599083
lon = -99.261550



print("Latitud: ", lat)
print("Longitud: ", lon)
print("\n\n")

data_1 = WeatherData(API_KEY_OPENWEATHER)

pprint(data_1.get_response_api(data_1.construc_url(lat,lon)))
print("\n\n")

data_2 = GeoDataLocation(API_KEY_POSITIONSTACK)
pprint(data_2.get_response_api(data_2.construc_url(lat,lon)))
#country_code = data_2.get_response_api(data_2.construc_url(lat,lon))["data"][0]["country_code"]

print("\n\n")
print()


data_4 = ISSData()
pprint(data_4.get_ISS_position())
print("\n\n")
