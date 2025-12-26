from services.geo import GeoDataLocation
from services.weather import WeatherData
from services.iss import ISSData

from pprint import pprint

lat = 19.599083
lon = -99.261550


print("Latitud: ", lat)
print("Longitud: ", lon)
print("\n\n")

data_1 = WeatherData()
response_data = data_1.get_weather(lat=lat, lon=lon)
pprint(response_data)
print("\n")
print(data_1.get_weather_icon(response_data))
print("\n\n")

data_2 = GeoDataLocation()
pprint(data_2.get_location(lat,lon))
print("\n\n")

data_4 = ISSData()
pprint(data_4.get_ISS_position())
print("\n\n")
